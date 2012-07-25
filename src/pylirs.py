import collections

class LirsCache(object):

    def __init__(self, s_capacity, q_capacity):
        self.s_capacity = s_capacity
        self.q_capacity = q_capacity
        self.cache = dict()
        self.s = collections.OrderedDict()
        self.q = collections.OrderedDict()

    def get(self, key, loader):
        if key not in self.cache:
            if len(self.s) < self.s_capacity:
                self.s[key] = key
                self.cache[key] = loader(key)
            elif key not in self.s:
                x = self.q.popitem(False)[0]
                self.cache.pop(x)
                self.s[key] = key
                self.q[key] = key
                self.cache[key] = key
            elif key in self.s:
                x = self.q.popitem(False)[0]
                self.cache.pop(x)
                self.s[key] = key
                y = self.s.popitem(False)[0]
                self.q[y] = y
                self.prune()
            else:
                assert False
        else:
            if key in self.s and key not in self.q:
                if self.s.iterkeys().next() == key:
                    do_prune = True
                x = self.s.pop(key)
                self.s[key] = key
                if do_prune:
                    self.prune()
            elif key in self.s and key in self.q:
                x = self.s.pop(key)
                self.s[key] = key
                self.q.pop(key)
                x = self.s.popitem(False)[0]
                self.q[x] = x
                self.prune()
            elif key not in self.s and key in self.q:
                self.s[key] = key
                self.q.pop(key)
                self.q[key] = key
            else:
                assert False

    def prune(self):
        #TODO(barracel)
        pass

