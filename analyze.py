import os
import sys

def folder(path):
     total = 0
     py_count = 0
     txt_count = 0
     
     for _,_, files in os.walk(path):
          total+=len(files)
          for f in files:
               if f.endswith(".py"):
                    py_count+=1
               elif f.endswith(".txt"):
                    txt_count+=1
                    
     print("Total files :",total)
     print(".py files : ",py_count)
     print(".txt files : ",txt_count)
     
if __name__ == "__main__":
     if len(sys.argv) < 2 :
          print("Usage: python analyze.py<folder_pth")
          sys.exit(1)
     
     folder(sys.argv[1])          
     