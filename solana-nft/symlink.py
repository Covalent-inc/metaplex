import os
from os import listdir
from os.path import isfile, join

# Get all files in directory
path = "assets"
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

# Temporarily use one asset for symlink purposes
base_png = "../hard_assets/K_Parcel.png"
base_mp4 = "../hard_assets/K_Parcel.mp4"

def force_symlink(src, dest):
    try:
        os.symlink(src, dest)
    except OSError as e:
        os.remove(dest)
        os.symlink(src, dest)

print("******Generating symlinks for {} files***********".format(len(onlyfiles)))
for file_name in onlyfiles:
    prefix = "assets/" + file_name.split(".")[0]
    png = prefix + ".png"
    mp4 = prefix + ".mp4"
    force_symlink(base_png, png)
    force_symlink(base_mp4, mp4)