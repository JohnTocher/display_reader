""" This script periodically saves images using the raspberry Pi camera

	It was intended to use as ameans of grabbing images to use with
	testing another project, but might be usefel on it's own to a limited
	degree.

	Tested on an Raspberry pi 2 using a recent version of Raspberry Pi OS
	November 2020

	GRAB_DELAY is the time before the first shot is taken
	GRAB_PERIOD is the time (in seconds) between images
	NUMBER_OF_IMAGES is the total number of images to grab

	Written by John Tocher
	November 2020
	jmtocher@gmail.com

"""


import time
import picamera

OUTPUT_PATH = "/home/pi/display_reader/images"
GRAB_PERIOD = 2	# Time in seconds between frames
GRAB_DELAY = 3	# Inital preview wait period in seconds
NUMBER_OF_IMAGES = 5

# Some arbitrary resolutions for capturing
RES_FULLHD = (1920, 1080)
RES_XGA = (1024, 768)
RES_LOW = (640, 480)

with picamera.PiCamera() as camera:
	img_res = RES_LOW
	camera.resolution = img_res
	camera.start_preview()
	time.sleep(GRAB_DELAY)
	img_res = RES_LOW
	for pic_num in range(1, NUMBER_OF_IMAGES + 1):
		res_text = f"{img_res[0]}x{img_res[1]}"
		output_filename = f"{OUTPUT_PATH}/cam_grab_{res_text}_{pic_num:02}.jpg"
		print(f"Capturing image to: {output_filename} in {GRAB_PERIOD} S")
		time.sleep(GRAB_PERIOD)
		camera.capture(output_filename)

