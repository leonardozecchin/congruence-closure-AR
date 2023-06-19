import queue
import time
import sys
#
sys.path.insert(0, './code')
from cca import start_program

f = "imply(eq(x,g(y,z)),eq(f(x),f(g(y,z))))"

ops = ["and", "or", "eq", "dis", "imply"]

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

def getValue(matching_pairs,value):
    for t in matching_pairs:
        if value in t:
            return t[1]
        
def getCommaIndexes(term : str) -> list:
    comma_indexes = list()
    for i in range(len(term)):
        if term[i] == ',':
            comma_indexes.append(i)
    return comma_indexes

def getFunctionParameters(term : str,matching_par: list) -> list:
    parameters = []
    if matching_par[0] is None:
        return None
    string_parameterters = term[matching_par[-1][0]+1:matching_par[-1][1]]
    commaIndex = getCommaPosition(string_parameterters)
    if commaIndex is None:
        return [string_parameterters]
    string_parameterters = string_parameterters[:commaIndex] + '@' + string_parameterters[commaIndex + 1:]
    parameters = string_parameterters.split('@')
    
    return parameters

def getCommaPosition(term: str,) -> int:
    opened_parenthesis_position, closed_parenthesis_position = getParenthesisPosition(term)
    comma_indexes = getCommaIndexes(term)
    match = find_matching_pairs(opened_parenthesis_position, closed_parenthesis_position)
    if opened_parenthesis_position is None or closed_parenthesis_position is None:
        return None
    elif len(opened_parenthesis_position) == 0:
        return comma_indexes[0]
    values = [False for i in range(len(comma_indexes))]
    for c in comma_indexes:
        for m in match:
            if c > m[0] and c < m[1]:
                values[comma_indexes.index(c)] = False
                break
            else:
                values[comma_indexes.index(c)] = True
    
    return comma_indexes[values.index(True)]



def printer(fun,parameters):
    global pars
    if fun == 'eq':
        pars.append(f'{parameters[0]}={parameters[1]}')
        # print(f'{parameters[0]}={parameters[1]}')
    elif fun == 'dis':
        pars.append(f'{parameters[0]}!={parameters[1]}')
        # print(f'{parameters[0]}!={parameters[1]}')

def getFirstFun(expression):
    opened_parenthesis_position, _ = getParenthesisPosition(expression)
    return expression[:opened_parenthesis_position[0]]

deMorganLaws = {
    'imply': 'or',
    'or': 'and',
    'and': 'or',
    'eq': 'dis',
    'dis': 'eq'
}

def parser(expression):
    global ops,pars
    if expression is None or expression == '' or len(expression) == 1:
        return None
    opened_parenthesis_position, closed_parenthesis_position = getParenthesisPosition(expression)
    first_function = getFirstFun(expression)
    if first_function not in ops:
        return None
    matching_pairs = find_matching_pairs(opened_parenthesis_position, closed_parenthesis_position)
    parametri_fun_princ = getFunctionParameters(expression,matching_pairs)
    # print(parametri_fun_princ)

    if parametri_fun_princ is None:
        return None
    # deMorganLaws(first_function,parametri_fun_princ)
    
    # while first_function != 'and':

    if first_function == 'imply':
        formula = ""
        ff = getFirstFun(parametri_fun_princ[0])
        ff_p = deMorganLaws[ff]
        parametri_fun_princ[0] = parametri_fun_princ[0].replace(ff,ff_p)
        formula = 'or(' + parametri_fun_princ[0] + ',' + parametri_fun_princ[1] + ')'
        # print(formula)
        return formula
    
    if first_function == 'or':
        formula = ""
        ff = getFirstFun(parametri_fun_princ[0])
        ff_p = deMorganLaws[ff]
        parametri_fun_princ[0] = parametri_fun_princ[0].replace(ff,ff_p)
        ff = getFirstFun(parametri_fun_princ[1])
        ff_p = deMorganLaws[ff]
        parametri_fun_princ[1] = parametri_fun_princ[1].replace(ff,ff_p)
        formula = 'and(' + parametri_fun_princ[0] + ',' + parametri_fun_princ[1] + ')'
        # print(formula)
        return formula
    
def getParams(expression):
    global ops,pars
    if expression is None or expression == '' or len(expression) == 1:
        return None
    opened_parenthesis_position, closed_parenthesis_position = getParenthesisPosition(expression)
    first_function = expression[:opened_parenthesis_position[0]]
    if first_function not in ops:
        return None
    matching_pairs = find_matching_pairs(opened_parenthesis_position, closed_parenthesis_position)
    parametri_fun_princ = getFunctionParameters(expression,matching_pairs)
    printer(first_function,parametri_fun_princ)

    if parametri_fun_princ is None:
        return None
    # expression = parametri_fun_princ[0]
    for p in parametri_fun_princ:
        getParams(p)


if __name__ == "__main__":

    filename = "input/inputToParser.txt"
    file = open(filename, "r")
    fout = open("output/outputParser.txt", "w")
    lines = file.readlines()

    for i,line in enumerate(lines):

        pars = []
        f = line.strip()
        print("\n*********************")
        print(f"Formula {i+1}: {f}")
        while getFirstFun(f) != 'and':
            f = parser(f)

        getParams(f)
        final_formula = ''
        for i,p in enumerate(pars):
            if i != len(pars)-1:
                final_formula += p + ' ' + getFirstFun(f) + ' '
            else:
                final_formula += p

        print("The final formula is:", final_formula)


        start_time = time.time()
        satisfiability = start_program(final_formula.strip())
        if satisfiability:
            print(f"{line.strip()} --> SATISFIABLE. Time: {time.time()-start_time}", file=fout)
        else:
            print(f"{line.strip()} --> UNSATISFIABLE. Time: {time.time() - start_time}", file=fout)