This is a simple python script to generate HTML tags (but can be used to generate repetitive lines for anything really) that contain information on each file in a given folder. the original purpose of this script was to create img tags for each image in a gallery folder of images. As there was over 100 images in this folder this would have been tedious to go and put in each image filename into the src of the image tag so I wrote this simple script to do it.

The user can either go through step by step defining:
* the location of the folder to generate the tags for
* the symbol to use to represent each image in the line of code
* if it is just the filename or the filename with the file extention they want in the code
* the output name of the file the lines of code will be wrote to for the user to then simply copy paste into there own code base


```bash
python3 folder_tag_generator.py
``` 

Or the user can pass the argument of true which will use the default folder location of the current location the folder_tag_generator is in, use the ^ symbol to be used to represent filenames, include filename extentions and have the output wrote to an output.txt file.

```bash
python3 folder_tag_generator.py true
``` 
In both cases the user will still have to provide the line of code that they want repetitively generated with the symbol in place for where the filename would be in the line of code. For example if the user provided the argument true for the express version the symbol is ^ so the use of generating lines of img tags would be

```bash
<img src="^" width="200px" height="140px" />
```