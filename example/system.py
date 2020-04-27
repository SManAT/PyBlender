import sys
sys.exec_prefix
import os
rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__)))
libPath = os.path.join(rootPath, "test.py")
#add libPath to SystemPath
sys.path.insert(0, libPath)

print sys.path
