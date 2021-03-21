import sys
import subprocess
import os
import time
def resource_path(relative_path):
    try: 
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
    
filePath = resource_path(os.path.dirname(os.path.abspath(__file__))) + "\\cat.jpg"
subprocess.Popen(filePath,shell=True)
while True:
    print("I hacked you")
    time.sleep(0.5)
   
