# hrs = input("Enter Hours:")
# rte = input("Enter Rate:")

hrs = 45
rte = 10.50

h = float(hrs)
r = float(rte)

if h <= 40 :
    h = h * r
else :
    h = h - 40
    h = h * (r * 1.5) + (40 * r)
print(h)
