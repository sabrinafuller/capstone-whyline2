import bdb
from inspect import currentframe
from .RFrame import RFrame
from .FrameDelta import FrameDelta
from .FrameStep import FrameStep



class rdb(bdb.Bdb):

    def __init__(self):
        bdb.Bdb.__init__(self)
        
        self.frame_steps = []
        self.last_frame_dict = {}
        self.master_frame_dict = {}
        self.last_line_no = 0
        self.call_stack_linenos = [] 
        self.call_master_list = []  
        self.botframe = None

    def make_deltas_and_update(self, frame):
        #print("make deltas and update")
       
        cur_id = id(frame)
        self.botframe = None
        frame_step = FrameStep({}, self.last_line_no)
       # print( "stack here")
        # We need to avoid getting the main.py program call stack info
        x =  self.get_stack(frame, None)[0][3:]

        for f, lineno in x:

          #  print(f, lineno, "f line no")
            if f.f_locals.get("self", None) == currentframe().f_locals["self"]:  
                continue
            fid = id(f)
            # print(fid == cur_id)
            if fid == cur_id:
                self.last_line_no = lineno
           # print(fid== cur_id)
            frame_copy = RFrame.from_frame(f)
            frame_step[fid] = FrameDelta.from_frames(self.last_frame_dict.get(fid,RFrame.new(fid)),frame_copy)                                                               
            self.last_frame_dict[fid] = frame_copy
            return cur_id, frame_step
      


    def user_call(self, frame, args):
        
        name = frame.f_code.co_name or "<unknown>"
       # print(dir(name), "name")
        fid = id(frame)
        return_to_lineno = self.get_stack(frame, None)[0][-2][1]
        self.call_stack_linenos.append(return_to_lineno)
        self.master_frame_dict[fid] = RFrame.from_frame(frame)
        
        self.last_line_no = return_to_lineno
        


    def user_line(self, frame):
        self.frame_steps.append(self.make_deltas_and_update(frame))

    def user_return(self, frame, val):
        self.frame_steps.append(self.make_deltas_and_update(frame))
        try:
            
            self.last_line_no = self.call_stack_linenos.pop(-1)
            
            self.call_master_list.append(self.last_line_no)
            
        except:
            
            pass 