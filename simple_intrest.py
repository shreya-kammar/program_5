

import sys

def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(sys.argv[1])
r = float(sys.argv[2])
t = float(sys.argv[3])

si = simple_interest(p, r, t)

print("Principal amount:", p)
print("Rate of interest:", r)
print("Time:", t, "years")
print("Simple Interest:", si)

