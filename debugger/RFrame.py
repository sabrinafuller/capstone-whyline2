

from . RObject import copy_object

class RFrame():

    def __init__(self, fid, f_locals, f_back):
        #super().__init__(self)
        self.id = fid
        self.f_locals = copy_object(f_locals.copy()).o
        self.f_back = f_back

    def __getitem__(self, key):
      return self.f_locals[key]

    def __contains__(self, key):
      return key in self.f_locals

    @classmethod
    def from_frame(cls, f):
        fid = id(f)
        f_locals = copy_object(f.f_locals.copy()).o
        if isinstance(f, RFrame):
            f_back = f.f_back
        else:
            f_back = id(f.f_back)
        return RFrame(fid, f_locals, f_back)


    @classmethod
    def new(cls, fid, f_back=None):
        return RFrame(fid, {}, f_back)

    def copy(self):
        return RFrame.from_frame(self)
    def __str__(self):
        return str(self.f_locals)