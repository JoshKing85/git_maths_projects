def implies(a, b):

    if a and not b:
        return False
    else:
        return True
    

a = True
b = False

print(implies(a, not b))