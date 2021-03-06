import random
import math

'''Construction of a separate Chameleon Hash Function based on RSA'''

'''Random e'''
def random_e(p, q, l):
    # Carmichael's totient function
    # lcm = phi_n // math.gcd(p - 1, q - 1)
    e = random.getrandbits(l)
    phi_n = (p - 1) * (q - 1)

    # check_relatively_primes_to_e
    # plus math.gcd(e, lcm) != 1 if using Carmichael's totient function
    while math.gcd(e, phi_n) != 1:
        e = random.getrandbits(l)

    return e


'''Random j'''
def random_j(n):
    j = random.randint(1, n)
    return j


'''Random r'''
def random_r(l):
    r = random.getrandbits(l)
    return r


''' CHF Public Key '''
def public_key(n, e, j):
    pub_key = str(n) + str(e) + str(j)
    return pub_key


'''Function Trapdoor'''
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y


def modular_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def value_d(p, q, e):
    phi_n = (p - 1) * (q - 1)
    d = modular_inverse(e, phi_n)
    if (e * d) % phi_n == 1 % phi_n:
        return d


def chameleon_hash_function(m, r, j, e, n):
    a = pow(j, m, n)
    b = pow(r, e, n)
    ch = (a * b) % n

    return ch
