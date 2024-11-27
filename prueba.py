contador = 0

def increment():
    global contador
    contador+= 1
    return contador
    

print(increment())