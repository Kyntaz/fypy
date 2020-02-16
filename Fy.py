class Fy:
    def __init__(self):
        self.fs = []
    
    def __or__(self, other):
        if callable(other):
            self.fs.append(other)
        else:
            raise TypeError()
        return self

    def __call__(self, *args):
        r = args
        for f in self.fs:
            try: tr = f(*r)
            except TypeError: tr = f(r)
            if tr != None: r = tr
        return r