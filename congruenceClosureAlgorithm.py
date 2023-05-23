from classes.node import Node
import re

#Create the subterm set
#function that takes a formula and returns a set of subterms
def createSubtermSet(formula : str) -> list:
    splitted_formula = formula.split("and")
    function_char = ['f','g']
    subterm_set = set()
    for term in splitted_formula:
        variables = re.findall(r'\b\w+\b', term)
        subterm_set.update(variables)

        for c in function_char:
            if c in subterm_set:
                subterm_set.remove(c)

        

    

    return subterm_set







print("CONGRUENCE CLOSURE ALGORITHM with DAG")
print("Menù (how to type formulas):")
print("\t* AND --> and\n\t* OR --> or\n\t* NOT EQUAL --> !=\n\t* f TO THE POWER OF n --> f^n")
print("Example:\n\t- f(a,b)=a and f(f(a,b),b)!=a\n\t- f^2(a)=a")

#F = input("Enter the formula: ")
#print("The formula is: ", F)

Sf = createSubtermSet("f(a,b)=a and f(f(a,b),b)!=a")

print(Sf)

