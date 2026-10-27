
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

p = 1000
r = 5
t = 2

si = simple_interest(p, r, t)

print("Principal amount:", p)
print("Rate of interest:", r)
print("Time:", t, "years")
print("Simple Interest:", si)
