
# import OS module
import os
 
# Get the list of all files and directories
path = "C:\\Users\\path\\to\\folder\\"
linpath = "c:/Users/path/to/folder/"
files = os.listdir(path)
 

# importing the module
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()
import os
# im = Image.open("c:/Users/ragha/Desktop/JPGCONVERT/IMG/IMG_8223.heic")
for file in files: 
# importing the image 
    im = Image.open(linpath+file)
    os.remove(linpath+file)
    rgb_im = im.convert("RGB")
    rgb_im.save(linpath+file.split('.')[0]+'.jpg')

