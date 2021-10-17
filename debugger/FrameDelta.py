from . import FrameDelta, RFrame


class FrameDelta():
    def __init__(self, adds, upds, dels):
        self.additions = adds
        self.updates = upds
        self.deletions = dels

    @classmethod
    def from_frames(cls, pf, af):
        additions = {}
        updates = {}
        deletions = {}
        pf = pf.f_locals    
        af = af.f_locals

        for a in af:
            if a not in pf:
                additions[a] = af[a]
                continue
            if pf[a] != af[a]:
                updates[a] = pf[a],af[a]
                for p in pf:
                    if p not in af:
                        deletions[p] = pf[p]

        return FrameDelta(additions, updates, deletions)

    def apply_f(self, frame):
        nframe = RFrame.from_frame(frame)
        for a in self.additions:
            nframe.f_locals[a] = self.additions[a]
        for u in self.updates:
            nframe.f_locals[u] = self.updates[u][1]

        for d in self.deletions:
            if d in nframe.f_locals:
                del nframe.f_locals[d]

        return nframe
    def apply_b(self, frame):
        nframe = RFrame.from_frame(frame)
        for d in self.deletions:
            nframe.f_locals[d] = self.deletions[d]
        for u in self.updates:
            nframe.f_locals[u] = self.updates[u][0]
        for a in self.additions:
            if a in nframe.f_locals:
                del nframe.f_locals[a]
        return nframe
    def __str__(self):
        return "{’+’: %s, ’-’: %s, ’delta’: %s}" % (self.additions, self.deletions, self.updates)
