# import subprocess
import os
from failure_tc import tc_list

# subprocess.run(["pip3", "install", "bs4"])
    
for tc in tc_list:
    os.system(f"python3 -m subunit.run {tc}")
    
# print(tc_list)
