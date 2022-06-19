import os
from os import listdir
from os.path import isfile, join

# Get all files in directory
path = "assets"
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

# TODO: delete any .png and .mp4 files for the assets direcotry
# before generating the symlinks

# Temporarily use one asset for symlink purposes
base_png = "../hard_assets/K_Parcel.png"
base_mp4 = "../hard_assets/K_Parcel.mp4"

print("******Generating symlinks for {} files***********".format(len(onlyfiles)))
for file_name in onlyfiles:
    prefix = "assets/" + file_name.split(".")[0]
    os.symlink(base_png, prefix + ".png")
    os.symlink(base_mp4, prefix + ".mp4")