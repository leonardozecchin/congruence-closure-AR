class Node:
    def __init__(self,id: int,fn: str, args: list, find: int, ccpar: list, fl=[]):
        self.id = id
        self.fn = fn
        self.args = args
        self.find = find
        self.ccpar = ccpar
        self.fl = fl

    def __str__(self):
        return "Node: id = {}, fn = {}, args = {}, find = {}, ccpar = {}, fl = {}".format(self.id,self.fn,self.args,self.find,self.ccpar,self.fl)
    
    def getId(self):
        return self.id
    
    def getFn(self):
        return self.fn
    
    def getArgs(self):
        return self.args
    
    def getFind(self):
        return self.find
    
    def getCcpar(self):
        return self.ccpar
    
    def getFl(self):
        return self.fl
    
    def setCcpar(self,ccpar):
        self.ccpar = ccpar

    def setFind(self,find):
        self.find = find