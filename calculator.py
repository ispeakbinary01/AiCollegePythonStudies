# import operator as op

# ops = {
#     "+": op.add,
#     "-": op.sub,
#     "/": op.truediv,
#     "//": op.floordiv,
#     "*": op.mul,
#     "**": op.pow,
#     "%": op.mod
# }

__operators = ('+', '-', '/', '//', '*', '**', '%')

def calculator():
    x = input()
    operator = input()
    y = input()

    rezultat = 0
    # print(str(x) + operator + str(y))
    if operator in __operators:
        rezultat = eval(x + operator + y)
    else:
        return "Operator not in __operators"    

    return rezultat    


print(calculator())