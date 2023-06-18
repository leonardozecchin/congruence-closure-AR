formula = "x=g(y,x)=>f(x)=f(g(y,z))"
# and(eq(f(a,b),a),dis(f(f(a,b),b),a)) -> f(a,b)=a and f(f(a,b),b)!=a
F = "imply(eq(x,g(y,x)),eq(f(x),f(g(y,z)))"
# Turn the formula into a dnf formula
subformulas = formula.split("=>")

def apply_demorgans_laws(formula):
    
    # implication case
    if "=>" in formula:
        subformulas = formula.split("=>")
        f1 = apply_demorgans_laws(subformulas[0])
        formula = f1 + " or " + subformulas[1]
        formula = apply_demorgans_laws(formula)
    
        return formula

    if "!" not in formula:
        if "=" in formula and "!=" not in formula and "=>" not in formula:
            formula = formula.replace("=","!=")
        return formula
    else:
        if "and" in formula:
            formula = formula.replace("and","or")
        elif "or" in formula:
            formula = formula.replace("or","and")
        if "!" in formula:
            formula = formula.replace("!","")  
        return formula
    

def negation(formula):
    if "and" in formula:
        formula = formula.replace("and","or")
    elif "or" in formula:
        formula = formula.replace("or","and")
    elif '!=' in formula:
        formula = formula.replace('!=','=')
    elif '=' in formula:
        formula = formula.replace('=','!=')
    return formula

def generic_deMorgan(formula):
    if "=>" in formula:
        subformulas = formula.split("=>")
        f1 = negation(subformulas[0])
        formula = f1 + " or " + subformulas[1]

    return formula

f3 = generic_deMorgan(formula)
print(f3)
