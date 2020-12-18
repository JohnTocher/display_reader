""" Version 01 - Updated by John Tocher 08/11/2020 for initial tests

    Used to matach pixel values to nearby colours
    Designed for basic, low speed interpretation of simple
    LCD, LED or other displays
"""

from pathlib import Path
import user_settings
import time
from PIL import Image

# from datetime import datetime
from jmt_utils import d_print, reverse_str

TOOL_NAME = "display_reader"
VERSION = "1.0.0"

def get_next_image(usr_settings, last_image=False):
    """ Returns the next image as a PIL image

        This might be creted from a file or read from a camera device
    """
    image_dict = dict()
    image_file_list = ["pi_link_led_640x480_off.jpg", "pi_link_led_640x480_on.jpg"]

    image_file_list = ["remote_640x480_fan_0.jpg", "remote_640x480_fan_1.jpg", "remote_640x480_fan_2.jpg", "remote_640x480_fan_3.jpg", "remote_640x480_off.jpg"]

    return_dict = dict()

    return_dict["OK"] = False

    img_index = 0
    for each_file in image_file_list:
        image_dict[each_file] = img_index
        img_index += 1


    if last_image in image_file_list:
        old_index = image_dict[last_image]
        new_index = (old_index + 1) % len(image_file_list)
    else:
        new_index = 0
    
    new_image = image_file_list[new_index]

    return_dict["Filename"] = new_image
    img_fullpath = f"{usr_settings['source folder']}/{new_image}"
    image_object = Image.open(img_fullpath)
    return_dict["Image"] = image_object
    return_dict["OK"] = True
    d_print(f"New image is {new_index:02} : {new_image} ({return_dict['OK']})", 100)

    return return_dict


def closest_colour_match(usr_settings, rgb_values):
    """ Returns the user colour with the closest colour match

        This is an e\inefficient way to store the standard values
        but it is simple and self contained and wont matter much in
        terms of efficiency in the scope this was built for
    """

    colour_map = dict()

    colour_map["Green_on"] = (240, 240, 240)
    colour_map["Green_off"] = (240, 200, 100)
    colour_map["LCD bar on"] = (20, 50, 110)
    colour_map["LCD bar_off"] = (0, 120, 250)
    
    colour_name = "Unknown"
    dist_min = 65535

    for colour_name, colour_rgb in colour_map.items():
        dist_sum = 0
        for col_index in range(0, 3):
            #d_print(f"Colour index {col_index}: {rgb_values[col_index]},{colour_rgb[col_index]}", 10)
            this_dist = (rgb_values[col_index] - colour_rgb[col_index]) ** 2
            dist_sum += this_dist
        if dist_sum < dist_min:
            dist_min = dist_sum
            dist_name = colour_name

    return dist_name


def test_pixel_reading(usr_settings):
    """ repetitively reads pixels from an image and reports matches to text
    """

    this_file = ""
    test_count = 0

    while test_count < 5:
        image_parms = get_next_image(usr_settings, this_file)
        this_file = image_parms["Filename"]
        #d_print(f"Image is {this_file}", 100)
        test_count += 1
        time.sleep(1)
        if image_parms["OK"]:
            this_image = image_parms["Image"].load()
            #pixel_rgb_vals = this_image[463, 182]   # Pi link LED
            pixel_rgb_vals = this_image[280, 166]   # remote Fan Middle bar
            best_match = closest_colour_match(usr_settings, pixel_rgb_vals)
            d_print(f"Pixels A: {pixel_rgb_vals} <> {this_file} match:{best_match}" , 100)

            #d_print(f"Pixels B: {this_image[182, 453]}", 100)




def basic_test(usr_settings):
    """ Runs basic  test
    """
    source_folder = usr_settings["source folder"]
    d_print(f"Source folder:\n{source_folder}", 1000)
    d_print("All done", 1000)



if __name__ == "__main__":
    SETTINGS_FILENAME = f"{TOOL_NAME}_settings.txt"
    ALL_SETTINGS = user_settings.read_config_file(SETTINGS_FILENAME)
    basic_test(ALL_SETTINGS)
    test_pixel_reading(ALL_SETTINGS)

