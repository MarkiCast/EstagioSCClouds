def recursive_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def linear_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a,b = b, a+b
    return a

def main():
    while True:
        try:
            user_input = input("Digite um número N >= 0 para calcular Fibonacci: ")

            n = int(user_input)
            if n < 0:
                print("Erro: N deve ser maior ou igual a 0.")
                continue
            
            print(f"Fibonacci Recursivo : {recursive_fibonacci(n)}")
            print(f"Fibonacci Linear : {linear_fibonacci(n)}")
        
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()