class Node:
    _next_id = 0
    def __init__(self, label=''):
        self.id = _next_id
        # self.count += 1
        # pass

    def __str__(self):
        raise NotImplementedError
    
    def __hash__(self):
        raise NotImplementedError
n1 = Node()
n2 = Node()
