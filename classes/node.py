class Node:
    def __init__(self, id: int, fn: str, args: list, find: int, ccpar: set):
        self.id = id
        self. fn = fn
        self.args = list
        self.find = find
        self.ccpar = ccpar

    @property
    def id(self):
        return self._id

    @property
    def fn(self):
        return self._fn

    @property
    def args(self):
        return self._args

    @property
    def find(self):
        return self._find

    @find.setter
    def find(self, value):
        self._find = value

    @property
    def ccpar(self):
        return self._ccpar

    def add_ccpar(self, ccpar_id):
        self._ccpar.add(ccpar_id)

    def remove_ccpar(self, ccpar_id):
        self._ccpar.remove(ccpar_id)
