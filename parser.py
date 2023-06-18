import queue

expression = "and(eq(f(a,b),a),dis(f(f(a,b),b),a))"
#f(f(f(a)))=a and f(f(f(f(f(a)))))=a and f(a)!=a
form = "and(eq(f(f(f(a))),a),and(eq(f(f(f(f(f(a))))),a),dis(f(a),a)))"
# f(f(f(a)))=f(a) and f(f(a))=a and f(a)!=a
f = "and(eq(f(f(f(a))),f(a)),and(eq(f(f(a)),a),dis(f(a),a)))"

ciao = "imply(eq(x,g(y,z)),eq(f(x),f(g(y,z))))"
dnf_ciao ="and(eq(x,g(y,z)),dis(f(x),f(g(y,z))))" 

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

ops = ["and","eq","dis"]
pars = []

def printer(fun,parameters):
    global pars
    if fun == 'and' or fun == 'or':
        print(f'{parameters[0]} {fun} {parameters[1]}')
    elif fun == 'eq':
        pars.append(f'{parameters[0]}={parameters[1]}')
        print(f'{parameters[0]}={parameters[1]}')
    elif fun == 'dis':
        pars.append(f'{parameters[0]}!={parameters[1]}')
        print(f'{parameters[0]}!={parameters[1]}')

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

def getFirstFun(expression):
    opened_parenthesis_position, closed_parenthesis_position = getParenthesisPosition(expression)
    return expression[:opened_parenthesis_position[0]]


getParams(f)
final_formula = ''
for i,p in enumerate(pars):
    if i != len(pars)-1:
        final_formula += p + ' ' + getFirstFun(form) + ' '
    else:
        final_formula += p
# final_formula = pars[0]+' ' +getFirstFun(form)+' '+pars[1]
print(final_formula)


