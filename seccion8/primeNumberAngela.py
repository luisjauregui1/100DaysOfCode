def prime_number(number):
    is_prime = True
    for i in range(2, number):
        print(f'Estado de is_prime={is_prime}')
        if number % i == 0:
            print(f'Estado de is_prime={is_prime}')
            is_prime = False
            
    if is_prime:
        print(f'Estodo de is_prime={is_prime} i={i} number={number}')
        print("It's a prime number.")
    else:
        print(f'Estodo de is_prime={is_prime} i={i} number={number}')
        print("It's not a prime number.")
    
    
n = int(input(":"))
prime_number(number=n)