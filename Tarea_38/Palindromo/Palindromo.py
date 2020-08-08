# Inicializo variables
N = 31
M = N

def primo(M):
    if M < 1:
        return False
    elif M == 2:
        return True
    else:
        for i in range(2,M):
            if M % i == 0:
                primo = False
                return False
            else:
                primo = True
    return True

def palindromo(M):
    string = str(M)

    if string == string[::-1]:
        return True
    else:
        return False

while M >= N:
    comprobacion_primo = primo(M)
    comprobacion_palindromo = palindromo(M) 
    if comprobacion_primo and comprobacion_palindromo:
        print(M)
        break
    else:
        M = M+1