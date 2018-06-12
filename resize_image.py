import os
from PIL import Image
from resizeimage import resizeimage
import argparse

parser = argparse.ArgumentParser(description='Shrink some .jpg and .png images')
parser.add_argument('-p', '--path', nargs='?', default='path', type=str, help='desired directory in which to operate (default is current directory)')
parser.add_argument('-a', '--aspect', nargs='?', default='z', type=str, choices=['x', 'y'], help='[x or y] If specified and -x and -y values would result in a change in aspect ratio, maintain the aspect ratio with the specified axis as the driving parameter.')
parser.add_argument('-x', nargs='?', default=-100, type=int, help='If -y is not specified, resize using this value and current aspect ratio.')
parser.add_argument('-y', nargs='?', default=-100, type=int, help='If -x is not specified, resize using this value and current aspect ratio.')
args = parser.parse_args()



if args.path == 'path':
    # set path to current directory
    path = os.getcwd()
    outPath = path
else:
    # set path to user destination
    path = args.path
    outPath = path

# iterate through the names of contents of the folder
for image_path in os.listdir(path):

    # create the full input path and read the file
    input_path = os.path.join(path, image_path)
    file_extension = input_path[-3:]
    if file_extension == 'jpg' or file_extension == 'png':
        img_to_shrink = Image.open(input_path)
        img_width, img_height = img_to_shrink.size

        aspect_ratio = img_width / img_height

        # if user set aspect ratio preference
        if args.aspect != 'z' or args.x == -100 or args.y == -100:
            if args.aspect == 'x' or args.y == -100:
                new_y = args.x / aspect_ratio
                new_x = args.x
            else:
                new_x = args.y * aspect_ratio
                new_y = args.y
        else:
            new_y = args.y
            new_x = args.x

        # skip image resizing on images that would be enlarged
        if new_y < img_height and new_x < img_width:
            # shrink the image
            shrunk = resizeimage.resize_cover(img_to_shrink, [new_x, new_y])

            # overwrite image path with shrunken image
            fullpath = os.path.join(outPath, image_path)
            shrunk.save(fullpath)
            shrunk.close()

        img_to_shrink.close()
