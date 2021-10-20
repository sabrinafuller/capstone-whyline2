# Class debug: 

`__init__(self, program_name)` 
    `program_name` ensures that all the frames are the program frames and not the caller debugger info

`make_frame_steps(self, frame, delta_dict)`
    returns the frame steps given frame and delta dict 

`trace_calls(self, frame, event,arg)`
`frame` only needed argument, grabs the frames from the stack and adds it to dictionary, `self.frame_dict` 

`get_target_program_frames(self, target_program_name)`
Get the sets a `sys.settrace()` 
And gets all the frames of the program. Filters the program based on the routine name (filter for program_name) and create a list, store the frames in `self.debug_dict` 

`run(self)`
Combines all the procedures for the object. Creates a debugger object from `rdb()` 
And retures the framesteps of the program