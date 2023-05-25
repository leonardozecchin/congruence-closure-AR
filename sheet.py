import re

s = 'f(f(a,b),f(b,c))'
parameters = list()

def getFuntionParameters(term : str, parPos:list) -> list:
    global parameters
    if len(parPos) == 0:
        return parameters
    f = term[parPos[0]+1:parPos[-1]]
    parameters.append(f)
    getFuntionParameters(term,parPos[1:-1])
    return parameters

def getParenthesisPosition(term : str) -> list:
    parenthesis_position = list()
    for i in range(len(term)):
        if term[i] == '(':
            parenthesis_position.append(i)
        elif term[i] == ')':
            parenthesis_position.append(i)
    return parenthesis_position

parPos = getParenthesisPosition(s)

parameters = list()


parameters = getFuntionParameters(s, parPos)



print(parameters)
print(parPos)