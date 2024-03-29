from classes.node import Node
from classes.dag import Dag
import re
import queue
import time


# Count the number of parenthesis of a formula
def countParenthesis(formula : str) -> int:
    count = 0
    for i in formula:
        if i == "(" or i == ")":
            count += 1
    return count

#Function that returns the position of the parenthesis, one list for the opened parenthesis and one list for the closed parenthesis
def getParenthesisPosition(term):
    opened_parenthesis_position = list()
    closed_parenthesis_position = list()
    if len(term) == 1:
        return None,None

    for i in range(len(term)):
        if term[i] == '(':
            opened_parenthesis_position.append(i)
        elif term[i] == ')':
            closed_parenthesis_position.append(i)
    
    return opened_parenthesis_position, closed_parenthesis_position

def getCommaIndexes(term : str) -> list:
    comma_indexes = list()
    for i in range(len(term)):
        if term[i] == ',':
            comma_indexes.append(i)
    return comma_indexes

# Get the position of the comma not between parenthesis
def getCommaPosition(term: str,) -> int:
    opened_parenthesis_position, closed_parenthesis_position = getParenthesisPosition(term)
    comma_indexes = getCommaIndexes(term)
    match = find_matching_pairs(opened_parenthesis_position, closed_parenthesis_position)
    if opened_parenthesis_position is None or closed_parenthesis_position is None:
        return None
    elif len(opened_parenthesis_position) == 0:
        return comma_indexes[0]
        
    for m in match:
        for c in comma_indexes:
            if c > m[0] and c < m[1]:
                continue
            else:
                return c


# Get the parameters of a function
def getFunctionParameters(term : str,matching_par: list) -> list:
    parameters = []
    if len(matching_par) == 0:
        return None
    elif matching_par[0] is None:
        return None
    string_parameterters = term[matching_par[-1][0]+1:matching_par[-1][1]]
    commaIndex = getCommaPosition(string_parameterters)
    if commaIndex is None:
        return [string_parameterters]
    string_parameterters = string_parameterters[:commaIndex] + '@' + string_parameterters[commaIndex + 1:]
    parameters = string_parameterters.split('@')
    
    
    return parameters

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



def find_matching_pairs(open_indexes, close_indexes):
    matching_pairs = []
    lifo = queue.LifoQueue()
    if open_indexes is None or close_indexes is None:
        matching_pairs.append(None)
        return matching_pairs
    
    sorted_list = sorted(open_indexes + close_indexes)
    for v in sorted_list:
        if v in open_indexes:
            lifo.put(v)
        else:
            matching_pairs.append((lifo.get(), v))

    return matching_pairs


def recursiveGetFunctionParameters(term : str, parametri: list) -> list:
    parameters = []
    if term is None:
        return None
    opened_par, closed_par = getParenthesisPosition(term) 
    matching_par = find_matching_pairs(opened_par, closed_par)
    if len(matching_par)==0:
        return None
    elif matching_par[0] is None:
        return None
    string_parameterters = term[matching_par[-1][0]+1:matching_par[-1][1]]
    if string_parameterters in parametri:
        return None
    commaIndex = getCommaPosition(string_parameterters)
    if commaIndex is None:
        if string_parameterters not in parametri:
            parametri.append(string_parameterters)
            recursiveGetFunctionParameters(string_parameterters,parametri)
        return None
    string_parameterters = string_parameterters[:commaIndex] + '@' + string_parameterters[commaIndex + 1:]
    parameters = string_parameterters.split('@')
    for x in parameters:
        if x not in parametri:
            parametri.append(x)
        if len(x) > 1:
            recursiveGetFunctionParameters(x,parametri)

def getParents(i,relations):
    parents = []
    for idx, r in enumerate(relations):
        if i in r:
            parents.append(idx)
    return parents

def createDAG(Sf: list, relations: list) -> list:
    DAG = []
    for i, term in enumerate(Sf):
       parents = getParents(i,relations)
       node = Node(id= i,fn = term[0], args= relations[i],find = i, ccpar=parents)
       DAG.append(node)
    
    return DAG


print("CONGRUENCE CLOSURE ALGORITHM with DAG")
# print("Menù (how to type formulas):")
# print("\t* AND --> and\n\t* OR --> or\n\t* NOT EQUAL --> !=\n\t* f TO THE POWER OF n --> f^n")
# print("Example:\n\t- f(a,b)=a and f(f(a,b),b)!=a\n\t- f(f(f(a)))=a and f(f(f(f(f(a)))))=a and f(a)!=a")

# F = input("Enter the formula: ")

def getIndex(f,Sf):
    if "!" not in f:
        formula = f.split("=")
    else:
        formula = f.split("!=")
    return Sf.index(formula[0]), Sf.index(formula[1])


def congruenceClosureAlgorithm(F_plus, F_minus,Sf,new_dag):
    for f in F_plus:
        #Step 1
        idx1,idx2 = getIndex(f,Sf)
        new_dag.MERGE(idx1,idx2)
    #Step 2
    for f in F_minus:
        idx1,idx2 = getIndex(f,Sf)
        if new_dag.FIND(idx1) == new_dag.FIND(idx2):
            return False
        else:
            return True


def start_program(F):
    global parametri
    # print("The formula is: ", F)
    start_time = time.time()

    Sf = createSubtermSet(F)
    Sf = sorted(Sf,key=len,reverse=False)

    print("The initial subterm set is: ", Sf)

    parametri = list()
    for x in Sf:
        if len(x) == 1:
            if x not in parametri:
                parametri.append(x)
            continue
        parametri.append(x)
        recursiveGetFunctionParameters(x,parametri)

    Sf = sorted(parametri,key=len)

    #The Initial Partition
    P = []

    for s in Sf:
        P.append({s})


    opened_parenthesis_position = list()
    closed_parenthesis_position = list()
    for t in Sf:
        indexes_par = getParenthesisPosition(t)
        opened_parenthesis_position.append(indexes_par[0])
        closed_parenthesis_position.append(indexes_par[1])

    list_of_matching = list()
    for i in range(len(opened_parenthesis_position)):
        list_of_matching.append(find_matching_pairs(opened_parenthesis_position[i],  closed_parenthesis_position[i]))

    parameters_functions = list()
    for i,f in enumerate(Sf):
        parameters_functions.append(getFunctionParameters(f,list_of_matching[i]))

    # print("The parameters of the functions are: ", parameters_functions)

    # print("The new subterm set is: ", Sf)
    # print("The initial partition is: ", P)

    relations = [[]for _ in range(len(Sf))]
    for i,p in enumerate(parameters_functions):
        if p is not None:
            for x in p:
                relations[i].append(Sf.index(x))

    # print("The relations are: ", relations)

    dag = createDAG(Sf,relations)
    print("The DAG is: ")
    for node in dag:
        print(node)

    new_dag = Dag(dag)

    # node = new_dag.NODE(0)
    # print("The node is: ", node)

    # Applicate Congruence Closure Algorithm
    formula = F.strip().replace(" ", "").split("and")
    # print("The formula is: ", formula)
    F_plus = [f for f in formula if "!=" not in f]
    F_minus = [f for f in formula if "!=" in f] 
    # print("F_plus: ", F_plus)
    # print("F_minus: ", F_minus)
    print("The algorithm steps are:")
    if congruenceClosureAlgorithm(F_plus, F_minus,Sf,new_dag):
        print("The formula is SATISFIABLE")
        return True
    else:
        print("The formula is UNSATISFIABLE")
        return False

    