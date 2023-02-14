class OrderedStream(object):
    
    def __init__(self, n):
        self.seen = {}
        self.ptr = 1

    def insert(self, id, value):
        seen, ptr = self.seen, self.ptr
        
        seen[id] = value
        result = []
        
        while ptr in seen:
            result.append(seen[ptr])
            del seen[ptr]
            ptr += 1
        
        self.ptr = ptr
        return result
