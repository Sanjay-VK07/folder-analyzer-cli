import os
import sys
import os 
import json
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
                    
     return {
          "Total_files" : total,
            "py_files" : py_count,
             "txt_files" : txt_count
     }
if __name__ == "__main__":
     if len(sys.argv) < 2 :
          print("Usage: python analyze.py<folder_pth [-json]")
          sys.exit(1)
     
     path = sys.argv[1]
     use_json = "-json" in sys.argv
     
     result = folder(path)
     
     if use_json:
          print(json.dumps(result, indent=2))
     else :
          print("Total files : ", result["total_files"])          
          print(".py files : ", result["py_files"])
          print(".txt files : ", result["txt_files"])