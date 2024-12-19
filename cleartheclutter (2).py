'''
Write a program to clear the clutter inside a folder on your computer
you should use os module to rename all the png images from 1.png
all the way till n.png where n is the number of png files in that 
folder. Do the same for other file formats
'''
import os 

 

files = os.listdir ("C:/Users/ACER/OneDrive/Documents/python/Clutterfolder/clutterfolder2")
i= 1
for file in files:
    if file.endswith(".png"):
      os.rename (f"C:/Users/ACER/OneDrive/Documents/python/Clutterfolder/clutterfolder2/{file}",f"C:/Users/ACER/OneDrive/Documents/python/Clutterfolder/clutterfolder2/{i}.png")
      print(file)