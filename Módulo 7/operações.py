def soma(*args):
    return sum(args)

def multiplicacao(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

def media(*args):
    if args:
        return sum(args) / len(args)
    return 0

def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n - 1)