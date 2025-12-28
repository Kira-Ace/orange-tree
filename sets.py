# create a new set
s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(3)
s.add(4)
s.add(5)

s.remove(4)
print(s)

print(f"The sets have a number of {len(s)} elements")