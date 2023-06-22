from classes.node import Node

class Dag:
    def __init__(self,nodes):
        self.nodes = nodes

    def __str__(self) -> str:
        return "Dag: nodes = {}".format(self.nodes)
    
    def forbidList(self, id: int) -> list:
        return self.NODE(self.FIND(id)).getFl()

    def checkArgs(self, args1: list, args2: list) -> bool:
        if len(args1) != len(args2):
            return False
        for i in range(len(args1)):
            if self.FIND(args1[i]) != self.FIND(args2[i]):
                return False
        return True

    def NODE(self, id: int) -> Node:
        for n in self.nodes:
            if n.getId() == id:
                return n
        return None
    
    def FIND(self, id: int) -> int:
        n = self.NODE(id)
        if n.getFind() == id:
            return id
        else:
            return self.FIND(n.getFind())
        
    def UNION(self, id1: int, id2: int) -> None:
        print(f"UNION {id1} {id2}")
        n1 = self.NODE(id1)
        n2 = self.NODE(id2)
        n1_ccpar = self.CCPAR(id1)
        n2_ccpar = self.CCPAR(id2)
        # n1.setFind(id2)
        # n1.find = n2.find
        if self.FIND(n1.find) != n1.id:
            self.NODE(self.FIND(n1.find)).find = n2.find
        else:
            n1.find = n2.find
        # n2.setCcpar(n2.getCcpar() + n1.getCcpar())
        n2.ccpar = n2_ccpar+ n1_ccpar
        # n2.setCcpar(self.CCPAR(id2) + self.CCPAR(id1))
        # n1.setCcpar([])
        n1.ccpar = []

    def CCPAR(self,id: int) -> list:
        return self.NODE(self.FIND(id)).getCcpar()
    

    def CONGRUENT(self, id1: int, id2: int) -> bool:
        n1 = self.NODE(id1)
        n2 = self.NODE(id2)
        if n1.getFn() == n2.getFn() and len(n1.getArgs()) == len(n2.getArgs()) and self.checkArgs(n1.getArgs(),n2.getArgs()):
            return True
        else:
            return False
        
    def MERGE(self, id1: int, id2: int) -> None:
        b = True
        print(f"MERGE {id1} {id2}")
        if self.FIND(id1) != self.FIND(id2):
            Pi1 = self.CCPAR(id1)
            Pi2 = self.CCPAR(id2)
            self.UNION(id1,id2)
            for i in Pi1:
                for j in Pi2:
                    if j in self.forbidList(i):
                        return False
                    if self.FIND(i) != self.FIND(j) and self.CONGRUENT(i,j) :
                        b = self.MERGE(i,j)
                        return b 