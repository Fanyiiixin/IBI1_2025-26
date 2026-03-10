a = 5.08
b = 5.33
c = 5.55
d = b-a
e = c-b
if d > e:
  print("d is larger than e")
elif e > d:
  print("e is larger than d")
else:
  print("d and e are equal")

# The population growth is decelerating
X = True
Y = False
W = X or Y
# | X     | Y     | W     |
# |-------|-------|-------|
# | True  | True  | True  |
# | True  | False | True  |
# | False | True  | True  |
# | False | False | False |
