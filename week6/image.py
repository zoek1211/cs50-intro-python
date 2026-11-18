from PIL import Image
from PIL import ImageFilter

def main():
   # better to use context manager to automatically close the file
#    img = Image.open("in.jpeg")
#    img.close()
   with Image.open("in.jpeg") as img:
      print(img.size)
      print(img.format)
      img = img.rotate(180)
      img = img.filter(ImageFilter.BLUR)
      img.save("out.jpeg")
      

main()
