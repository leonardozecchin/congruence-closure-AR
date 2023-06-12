
from dd import autoref as _bdd

def convert_to_dbf(formula):
    bdd = _bdd.BDD()

    # Define the variables
    variables = set(formula.replace("(", "").replace(")", "").replace("and", "").replace("or", "").replace("not", "").replace(" ", ""))
    bdd.declare(*variables)

    # Parse the formula into a binary decision diagram
    root = parse_formula(formula, bdd)

    return bdd, root

def parse_formula(formula, bdd):
    if formula.startswith("not"):
        subformula = parse_formula(formula[3:], bdd)
        return bdd.apply('not', subformula)
    elif formula.startswith("("):
        # Find the matching closing parenthesis
        closing_index = find_closing_parenthesis(formula)

        # Split the formula into the left and right subformulas
        left_subformula = formula[1:closing_index]
        right_subformula = formula[closing_index + 1:]

        if right_subformula.startswith("and"):
            op = 'and'
            right_subformula = right_subformula[3:]
        elif right_subformula.startswith("or"):
            op = 'or'
            right_subformula = right_subformula[2:]

        left = parse_formula(left_subformula, bdd)
        right = parse_formula(right_subformula, bdd)

        return bdd.apply(op, left, right)
    else:
        # Variable case
        return bdd.var(formula)

def find_closing_parenthesis(formula):
    open_count = 0
    for i, char in enumerate(formula):
        if char == '(':
            open_count += 1
        elif char == ')':
            open_count -= 1
        if open_count == 0:
            return i

    return -1


formula = "(A and B) or (C and D)"
bdd, root = convert_to_dbf(formula)

print(bdd.to_expr(root))

