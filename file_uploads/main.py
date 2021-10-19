
import dis
import csv
import rdb
import test
import debug
import RObject
import FrameStep
import sys
import RFrame
import ast
import inspect


def trace_lines(frame, event, arg):
    print(frame.f_lineno)

def read_ast():
    tree = None
    with open("test2.py","r") as f: 
        tree = ast.parse(f.read())
    r = RObject.RObject(tree)
    f.close
    return r
frame_list = []
def make_frame_step(frame, delta_dict):
    if(delta_dict == None):
        f_step = FrameStep.FrameStep({},frame.f_lineno) 
    return f_step

#trace the call stack and store the frames in a dictionary
def trace_calls(frame, event, arg):
    for i in inspect.stack():
        frame_dict.update({id(i.frame): i.frame})
  
#create the global frame dictionary
global frame_dict  
frame_dict = dict()
## this function creates a dictionary of frames from the target program
def get_target_program_frames(target_program_name):
    prog_name= target_program_name
    # set the trace on the program
    sys.settrace(trace_calls)
    #run the program
    test.main()
    #get the list of frames
    frame_list = list(frame_dict.items())
    debug_dict = dict()
    # for each frame in the frame list
    # check to see if its in the target program and add it to the dictionary

    for i in frame_list:
        x = inspect.getmodule(i[1])
        if(x.__name__ == prog_name):
            debug_dict.update({i[0]:i[1]})
    return debug_dict


    
def main_two():
    
    
    # get the list of frame from the target dictionary
    my_dict = get_target_program_frames("test")
    obj_list = list(my_dict.items())   
    # create the python debugger 
    psi = rdb.rdb()
    #psi.user_call(first_frame, None)
    
    for i in obj_list:
        psi.user_call(i[1], None)
        psi.user_line(i[1])
        psi.user_return(i[1], None)
      
    
  

    
   
def main():
    d = debug.debug("test")
    d.run()
    
main()
