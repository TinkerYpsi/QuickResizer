# QuickResizer
QuickResizer is an image resizer that shrinks .jpg and .png images to a specified dimension and maintains aspect ratios if requested. IMPORTANT: This script will overwrite the target files, so if you want to also keep the full sized images, make a copy of them in a new folder before running the script.

### Installation
First, download [Python][python-download]. Make sure to click the **add Python 3.6.4 to PATH** checkbox at the bottom. Then, run Command Prompt as an Administrator, or the Terminal if on Mac, and type `pip install argparse python-resize-image` to install necessary packages.  

Next, [download a ZIP file][zip-file] of this script, and extract the `resize-image.py` file
into a location you will remember.

### Running the Script
To run the script in the command prompt, open the start menu, type cmd, click Command Prompt,
and type `python C:\Users\YourUserName\QuickResizer\resize-image.py --help`. If
you're prompted with an error message indicating that "python is not recognized
as an internal or external command,"
follow the instructions on [this page][addToPathPage] or [re-download Python][python-download] and be sure to click the **add Python 3.6.4 to PATH** checkbox this time.

Upon typing the above command, you will be prompted with:
```
usage: resize_image.py [-h] [-p [PATH]] [-a [{x,y}]] [-x [X]] [-y [Y]]

Shrink some .jpg and .png images

optional arguments:
  -h, --help            show this help message and exit
  -p [PATH], --path [PATH]
                        desired directory in which to operate (default is
                        current directory)
  -a [{x,y}], --aspect [{x,y}]
                        [x or y] If specified and -x and -y values would
                        result in a change in aspect ratio, maintain the
                        aspect ratio with the specified axis as the driving
                        parameter.
  -x [X]                If -y is not specified, resize using this value and
                        current aspect ratio.
  -y [Y]                If -x is not specified, resize using this value and
                        current aspect ratio.
```

### Examples
`python C:\Users\YourUserName\QuickResizer\resize-image.py -p C:\Users\YourUserName\Desktop\Images -x 100 -y 100`

This will shrink all the images at the given directory to exactly 100x100 pixels without preserving aspect ratios.

`python C:\Users\YourUserName\QuickResizer\resize-image.py -p C:\Users\YourUserName\Desktop\Images -a y -x 400 -y 720`

This will shrink all the images at the given directory to a height of 720 pixels and, if their aspect ratios allow it, to a width of 400 pixels, otherwise the width will be larger according to the aspect ratio. For example, a 1920x1080 picture will shrink to 1280x720, a 3400x2448 picture will shrink to 1000x720 and a 2000x2000 picture will shrink to 720x720. Regardless of the width, the height will always be 720 for any picture.

`python C:\Users\YourUserName\QuickResizer\resize-image.py -p C:\Users\YourUserName\Desktop\Images -y 720`

This does the exact same thing as the previous example above.

`python C:\Users\YourUserName\QuickResizer\resize-image.py -y 720`

This has the same functionality of the last two examples but executes the script in the directory where the script is located.



[python-download]: "https://www.python.org/downloads/"
[zip-file]: "https://github.com/TinkerYpsi/QuickResizer/archive/master.zip"
[addToPathPage]: "https://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/"
