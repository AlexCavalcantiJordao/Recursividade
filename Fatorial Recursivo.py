# Recursividade


# Formula geral para o fatorial:
# Fatorial(num) = 1, se num = 0 ou se num = 1 'Caso-Base'....
# Fatorial(num) = num * fatorial(num -1), para num > 1 'Caso Recursivo'......
# 4! -> 4 * Fatorial(3) = 4 * 3 * Fatorial(2) = 4 * 3 * 2 * Fartorial(1)......

def fatorial(numero):
    if(numero == 0 or numero == 1):
        return 1
    else:
        return numero * fatorial(numero - 1)
        if __name__ == "__main__":
            x = int(input("Digite um número inteiro positivo para calcular seu fatorial: "))
        try:
            res = fatorial(x)
        except RecursionError:
            print(f"O número fornecido é muito grande ou negativo.")
        else:
            print(f"O fatorial de {x} é {res}.")