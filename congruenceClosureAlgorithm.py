from classes.node import Node
import re

# Create the DAG using Node class
"""def createDAG(sf : set) -> list:
    dag = []
    for i in range(len(sf)+1):
        dag.append(Node(i+1,sf[0],))
    """


def createSubtermSet(formula : str) -> set:

    subterm_set = set()
    for i in formula.split("and"):
        i = i.replace(" ", "")
        if "!" in i:
            for j in i.split("!="):
                subterm_set.add(j)
        else:
            for j in i.split("="):
                subterm_set.add(j)

    function_symbols = set()
    variables = set()
    for term in subterm_set:
        function_symbols.update(re.findall(r'\b[a-zA-Z]+\b(?=\()', term))
        variables.update(re.findall(r'[a-zA-Z]', term))
    for s in function_symbols:
        variables.remove(s)
    
    subterm_set.update(variables)

    return subterm_set

print("CONGRUENCE CLOSURE ALGORITHM with DAG")
print("Menù (how to type formulas):")
print("\t* AND --> and\n\t* OR --> or\n\t* NOT EQUAL --> !=\n\t* f TO THE POWER OF n --> f^n")
print("Example:\n\t- f(a,b)=a and f(f(a,b),b)!=a\n\t- f^2(a)=a")

F = input("Enter the formula: ")
print("The formula is: ", F)
#F = "f(a,b)=a and f(f(a,b),b)!=a"
#Sf = createSubtermSet("f(f(f(a))=a and f(f(f(f(f(a)))))=a and f(a)!=a")
Sf = createSubtermSet(F)
Sf = sorted(Sf,key=len,reverse=True)
#The Initial Partition
P = []

for s in Sf:
    P.append({s})

print("The subterm set is: ", Sf)
print("The initial partition is: ", P)

#dag = createDAG(Sf)