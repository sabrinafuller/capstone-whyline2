import FrameDelta
import RFrame
class FrameStep():
    def __init__(self, delta_dict, lineno):
        self.deltas = delta_dict
        self.lineno = lineno
    def update(self, delta_dict):
        self.deltas.update(delta_dict)
    def __getitem__(self, key):
        return self.deltas.get(key, FrameDelta({},{},{}))
    def __setitem__(self, key, value):
        self.deltas[key] = value

    def apply_f(self, frames):
        new_frames = {}
        
        for k in frames:
            new_frames[k] = self[k].apply_f(frames[k])
        for k in self.deltas:
            if k not in frames:
                new_frames[k] = self[k].apply_f(RFrame.new(k))
        return new_frames

    def apply_b(self, frames):
        new_frames = {}
        for k in frames:
            new_frames[k] = self[k].apply_b(frames[k])
        return new_frames


    def __str__(self):
        dstr = "{"
        for k in self.deltas:
            dstr += "%d: %s\n" % (k, str(self.deltas[k]))
        return dstr + "}"