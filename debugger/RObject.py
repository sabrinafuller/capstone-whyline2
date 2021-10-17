
class RObject():
    def __init__(self, obj):
        self.o = obj
        self.id = id(obj)

def copy_object(obj):
    primitive = (int, float, bool, str)
    if obj is None or callable(obj) or type(obj) in primitive:
        return RObject(obj)
    collection = (tuple, set, list)
    if type(obj) in collection:
        return RObject(type(obj)([copy_object(i) for i in obj]))
    if type(obj) == dict:
        d = {k: copy_object(obj[k]) for k in obj}
        return RObject(d)
    return RObject(obj)