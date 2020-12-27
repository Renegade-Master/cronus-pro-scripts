last_seed = 32767

# a = 16807;
# m = 2147483647;
# seed = (a * seed) mod m;
# random = seed / m;

# num = (rand() % (upper - lower + 1)) + lower;

def prandom3(mult=16807, mod=(2**31) - 1):
    global last_seed

    last_seed = (mult * last_seed) % mod

    return last_seed / mod

def pdist(low=0, high=10, seed=123456789):
    return ((prandom3() * 100) % (high - low + 1)) + low


print("0 - 10")
[print(f"Random: {pdist()}") for x in range(10)]
print()
print("0 - 75")
[print(f"Random: {pdist(low=0, high=75)}") for x in range(10)]
print()
print("-75 - 75")
[print(f"Random: {pdist(low=-75, high=75)}") for x in range(10)]
