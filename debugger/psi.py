
import os
import traceback
import sys
from . import FrameDelta, FrameStep, RFrame, RObject, rdb, test1

import traceback
import subprocess
from test1 import main
import ast
from inspect import currentframe, getframeinfo, walktree
def main():
    tree = ast.parse("test_1.py")
    robj = RObject(tree)
    #print(traceback.extract_stack())
    #with open("test_1.py","r") as f: 
     #   my_string = f.read()
    

    
    
    fout, error_out = None, None
    args = ['python3',  "test1.py" ]
    #x = subprocess.call(args, shell = "-m pdb",  stdout = fout , stderr = error_out)
    #print(sys._current_frames())
    #print(x, fout, error_out)
    
    
  
    
    
   
        
        

       
    
    

if __name__ == "__main__":
    main()
   

 
