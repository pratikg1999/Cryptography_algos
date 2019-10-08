from random import randrange, getrandbits

def is_prime(n, k=1024):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True


def generate_prime_candidate(length):
    p = getrandbits(length)
    p |= (1 << length - 1) | 1
    return p


def generate_prime_number(length=1024):
    p = 4
    while not is_prime(p, 1024):
        p = generate_prime_candidate(length)
    return p

length_bits = 300
print("Number of Bits of N and G: {}bits\n".format(length_bits))
n = generate_prime_number(length_bits)
g = generate_prime_number(length_bits)

print('n: {}\ng: {}'.format(n,g))

def modulo_power(bas, exp,N): 
    if (exp == 0): 
        return 1; 
    if (exp == 1): 
        return bas % N; 
      
    t = modulo_power(bas, int(exp / 2),N); 
    t = (t * t) % N; 
    if (exp % 2 == 0): 
        return t;     
    else: 
        return ((bas % N) * t) % N;


def genA(length = 64):
    x = generate_prime_number(length)
    A = modulo_power(g,x,n)
    return x,A


x,A = genA(100)
y,B = genA(100)
print('\nx: {}, A: {}\ny: {}, B: {}'.format(x,A,y,B))
K1 = modulo_power(B,x,n)
K2 = modulo_power(A,y,n)

print("\n\nKey1: {}\nKey2: {}".format(K1,K2))
print("Are Both Keys Equal?: ",K1==K2)


