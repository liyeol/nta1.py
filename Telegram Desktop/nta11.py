import time
import math
from functools import reduce


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def trial_division(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def pollard_rho(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def f(x):
        return (x ** 2 + 1) % n

    factors = []
    x = 2
    y = 2
    d = 1

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    if d != n:
        factors.append(d)
        factors.extend(pollard_rho(n // d))

    return factors


def brilhart_morrison(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def f(x):
        return (x ** 2 + 2) % n

    factors = []
    x = 2
    y = 2
    d = 1

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    if d != n:
        factors.append(d)
        factors.extend(brilhart_morrison(n // d))

    return factors


def find_canonical_factorization(n):
    print("Пошук канонічного розкладу числа:", n)
    start_time = time.time()

    if is_prime(n):
        print("Число", n, "є простим. Канонічний розклад:", n)
        print("Час виконання:", time.time() - start_time, "секунд")
        return

    factors = []
    factors.extend(trial_division(n))

    return factors

def find_canonical_factorization(n):
        print("Пошук канонічного розкладу числа:", n)
        start_time = time.time()

        if is_prime(n):
            print("Число", n, "є простим. Канонічний розклад:", n)
            print("Час виконання:", time.time() - start_time, "секунд")
            return

        factors = []
        factors.extend(trial_division(n))
        if factors:
            print("Метод пробних ділень знайшов наступні дільники:", factors)
            print("Використаний метод: Метод пробних ділень")
            print("Час виконання:", time.time() - start_time, "секунд")
            n //= reduce(lambda x, y: x * y, factors)

        factors.extend(pollard_rho(n))
        if factors:
            print("ρ-метод Полларда знайшов наступні дільники:", factors)
            print("Використаний метод: ρ-метод Полларда")
            print("Час виконання:", time.time() - start_time, "секунд")
            n //= reduce(lambda x, y: x * y, factors)

        factors.extend(brilhart_morrison(n))
        if factors:
            print("Метод Брілхарта-Моррісона знайшов наступні дільники:", factors)
            print("Використаний метод: Метод Брілхарта-Моррісона")
            print("Час виконання:", time.time() - start_time, "секунд")
            n //= reduce(lambda x, y: x * y, factors)

        if is_prime(n):
            factors.append(n)
            print("Число", n, "є простим. Канонічний розклад:", factors)
            print("Використаний метод: Перевірка на простоту")
            print("Час виконання:", time.time() - start_time, "секунд")
        else:
            print("Не вдалося знайти канонічний розклад числа :(")


n = int(input("Введіть число для перевірки: "))
find_canonical_factorization(n)