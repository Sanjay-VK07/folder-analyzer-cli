import os
import sys

def folder(path):
     count = 0
     for _,_,files in os.walk(path):
          count+=len(files)
     print("Total files : ", count)
     
if __name__ == "__main__":
     if len(sys.argv) < 2 :
        print(" Usage : python analyze.py <folder_path>")
        sys.exit(1)
        
     folder(sys.argv[1])