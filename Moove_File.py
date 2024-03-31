import os
import shutil

from_dir = "C:/Users/jainn/OneDrive/Pictures"
to_dir = "C:/Users/jainn/OneDrive/Documents"

list_of_files = os.listdir(from_dir)
print("List of files in the source directory:", list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print("File:", name, "Extension:", extension)

    if extension == "":
        continue
    if extension in [ '.txt', '.doc', '.docx', '.pdf']:
                         
    
     path1 = from_dir + '/' + file_name
     path2 = to_dir + '/' + "Image_Files"
     path3 = to_dir + '/' + "Image_Files" + '/' + file_name
     print("Path 1:", path1)
     print("Path 3:", path3)


     if os.path.exists(path2):
        print("Moving"+ file_name + "....")
        shutil.move(path1, path3)
     else:
    
       os.makedirs(path2)
       print("Moving", file_name + "....")
       shutil.move(path1, path3)

    
