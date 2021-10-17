from RFrame import RFrame
import pdb
import sys
import RObject
import RFrame


class Debug(pdb.Pdb):
    def __init__(self, *args, **kwargs):
        super(Debug, self).__init__(*args, **kwargs)
        self.prompt = "[Time Traveling Debugger] "


def stop():
    debugger = Debug()
    first_frame =sys._getframe().f_back
    debugger.set_trace(sys._getframe().f_back)
    
    