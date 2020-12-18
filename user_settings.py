from pathlib import Path
import json

def set_config_default():
    """ Creates and returns a dictionary with default settings
    """

    def_dict = dict()

    def_dict["script version"] = "1.0.0"
    def_dict["source folder"] = "/home/user/display_reader/images"
    def_dict["dest folder"] = "/home/user/display_reader/images"

    return def_dict

def read_config_file(config_filename="default_settings.txt", path_to_use=False):
    """ Reads a json/xml file from disk
    """

    new_settings = set_config_default()

    if not path_to_use:
        #path_to_use = os.path.dirname(__file__)
        path_to_use = Path(__file__).parent
        print(f"Using default config path {path_to_use} from {__file__}")
    else:
        print(f"Using supplied config path {path_to_use} from {__file__}")

    #config_fullname = os.path.join(path_to_use, config_filename)
    config_fullname = path_to_use / config_filename
    print(f"Attempting to read config from: {config_fullname}")

    test_path = Path(config_fullname)
    #if not os.path.exists(config_fullname): # Need to create config file with defaultsd
    if not test_path.exists(): # Need to create config file with defaults
        print(f"Creating new default configuration file: {config_fullname}")
        write_config_file(set_config_default(), config_filename, path_to_use)
    else:
        print(f"Config file exists at: {config_fullname}")

    with open(config_fullname, "r") as config_fp:
        new_settings = json.load(config_fp)

    return new_settings

def write_config_file(config_dict, config_file_name="default_settings.txt", path_to_use=False, ):
    """ Writes the supplied configration dictionary to a file
    """

    if not path_to_use:
        path_to_use = Path(__file__).parent

    #config_fullname = os.path.join(path_to_use, config_file_name)
    config_fullname = path_to_use / config_file_name

    with open(config_fullname, "w") as config_fp:
        json.dump(config_dict, config_fp)
    print(f"Wrote config file to: [{config_fullname}]")

    return True


if __name__ == "__main__":
    print(f"Imported: {__file__}")
