import argparse
import os


class Folder:
    def __init__(self, path):
        self.size = 0
        self.children = []
        self.path = path
        self.parent = None
        #self.file_size = 0
#     def update_size(self):
#         for c in self.children:
#             self.size += self.children.size
            
    def largest_child(self):
        max_size = -1
        for c in self.children:
            if c.size > max_size:
                max_child = c
                max_size = c.size
        return max_child

def size_transform(size):
    G = 1000000000
    M = 1000000
    K = 1000
    if size > G:
        return str(round(size / G , 3)) + " GB"
    elif size > M:
        return str(round(size / M , 3)) + " MB"
    elif size > K:
        return str(round(size / K , 3)) + " KB"
    else:
        return str(size) + "B"


def file_parser(init_path):
    
    try:
        flist = os.listdir(init_path)
        root_folder = Folder(path= init_path)
        for f in flist:

            fpath = os.path.join(init_path, f)
            if os.path.isdir(fpath):
                child_folder = file_parser(fpath)
                child_folder.parent = root_folder
                root_folder.children.append(child_folder)
                root_folder.size += child_folder.size
            elif os.path.isfile(fpath):
                #file_path = os.path.join(root, f)
                file_size = os.path.getsize(fpath)
                root_folder.size += file_size
    except:
        return None
            
    return root_folder
def show_folder_and_size(root):
    for child in root.children:
        print("size {}   {}".format(size_transform(child.size), child.path))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", help= "Directory Path")
    args = parser.parse_args()
    root = file_parser(args.p)
    
    
    while 1:
        print("Current Path: ", root.path)
        option = input("1. Get max folder.\n2. Show all folder size.\n3. Check folder.\n4. Quit\nWhat do you want to do: ")
        #next_folder = input("Which folder do you want to check : ")
        
        if option == '1':
            max_child = root.largest_child()
            print('Max Folder: ', max_child.path)
        elif option == '2':
            show_folder_and_size(root)
        elif option == '3':
            f = input("Which folder do you want to check :")
            #try & except
            next_folder = os.path.join(root.path, f)
            for c in root.children:
                if c.path == next_folder:
                    root = c
                    break

        elif option == '4':
            exit()
        else:
            print("Input Error!")
        print("===================================")
