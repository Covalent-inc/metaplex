import os
from os import listdir
from os.path import isfile, join
import json
import glob

# Get all files in directory
destination = "assets/"
def force_symlink(src, dest):
    try:
        os.symlink(src, dest)
    except OSError as e:
        os.remove(dest)
        os.symlink(src, dest)


def remove_files(ext):
    """Remove any existing assets"""
    to_delete = glob.glob(destination + "*." + ext)
    for f in to_delete:
        try:
            if ext in f:
                os.remove(f)
        except OSError as e:
            pass

if __name__ == "__main__":
    remove_files("png")
    remove_files("mp4")
    onlyfiles = [f for f in listdir(destination) if isfile(join(destination, f))]
    print("******Generating symlinks for {} files***********".format(len(onlyfiles)))
    for file_name in onlyfiles:
        with open(destination+file_name, "rb") as f:
            json_content = json.load(f)
        asset_name = json_content['attributes'][0]['value'].replace(" ", "_")
        prefix = destination + file_name.split(".")[0]
        png = prefix + ".png"
        mp4 = prefix + ".mp4"
        force_symlink("../hard_assets/"+asset_name+".png", png)
        force_symlink("../hard_assets/"+asset_name+".mp4", mp4)


