def recursive_primes(n, current=2, result=None):
    if result is None:
        result = []
    
    def is_prime(num, i=2):
        if num <= 2:
            return num == 2
        if num % i == 0:
            return False
        if i * i > num:
            return True
        return is_prime(num, i + 1)
    
    if current > n:
        return result
    
    if is_prime(current):
        result.append(current)
    
    return recursive_primes(n, current + 1, result)

def linear_primes(n):
    primes = []
    
    def is_prime_linear(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    
    for num in range(2, n + 1):
        if is_prime_linear(num):
            primes.append(num)
    
    return primes

def main():
    while True:
        try:
            user_input = input("Digite um número N >= 1 para calcular os primos ate o numero: ")

            n = int(user_input)
            if n < 1:
                print("Erro: N deve ser maior ou igual a 1.")
                continue
            
            print(f"Primos recursivo : {recursive_primes(n)}")
            print(f"Primos linear : {linear_primes(n)}")
        
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()