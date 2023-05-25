class Node:
    def __init__(self,id: int,fn: str, args: list, find: int, ccpar: list):
        self.id = id
        self.fn = fn
        self.args = args
        self.find = find
        self.ccpar = ccpar

    def __str__(self):
        return "Node: id = {}, fn = {}, args = {}, find = {}, ccpar = {}".format(self.id,self.fn,self.args,self.find,self.ccpar)
    
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
    
    def setCcpar(self,ccpar):
        self.ccpar = ccpar

    def setFind(self,find):
        self.find = find

    
