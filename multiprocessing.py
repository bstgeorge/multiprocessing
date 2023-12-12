#!/usr/bin/env python3
import subprocess
from multiprocessing import Pool 
import os
import shutil
src = "./data/prod/"
dest = "./data/prod_backup/"
subprocess.call(["rsync", "-arq", src, dest])
for root, dirs, files in os.walk(src):
  for name in files:
    shutil.copyfile(os.path.join(root, name), os.path.join(dest, name))
    print (os.path.join(root, name))
#  for name in dirs:
#    print (os.path.join(root, name))

# #!/usr/bin/env python3
# from multiprocessing import Pool
# def run(task):
#  # Do something with task here
#    print("Handling {}".format(task))
