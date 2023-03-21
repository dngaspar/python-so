import subprocess
import threading


cp = subprocess.run(["py", "./test.py"])
print(cp)

