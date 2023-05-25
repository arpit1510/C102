import os
import shutil

from_dir = "C:/Users/DELL/Desktop/102"
to_dir = "D:/document_file"

list_of_file = os.listdir(from_dir)
print(list_of_file)

for file_name in list_of_file:
    name,extension = os.path.splitext(file_name)
    
for file_name in list_of_file:
    name,extension = os.path.splitext(file_name)
    #print(name, extension)
    
    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1 =  from_dir + '/' + file_name  
        path2 = to_dir + '/' + "Document_file" 
        path3 = to_dir + '/' + "Documents_file" + '/' + file_name
        
        if os.path.exists(path2):
            print("Moving " + file_name + "...")
            
            shutil.move(path1, path3)
            
        else:
            os.akedirs(path2)
            print("Making " + file_name + "...")
            shutil.move(path1, path3)
            
        

    