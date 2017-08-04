from sys import argv

base = int(argv[1])
mod = int(argv[2])
exp = int(argv[3])


# recursive repeated squaring
def exp_mod(x, n, m):
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = exp_mod(x, (n/2), m)
        return (y * y) % m
    else:
        return (x * exp_mod(x, (n-1), m)) % m


print(str(base) + "^" + str(exp) + " mod " + str(mod) +
      "= " + str(exp_mod(base, exp, mod)))
