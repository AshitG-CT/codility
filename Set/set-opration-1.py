seta = {1,2,3,4,5}
setb = {4,5,6,7,8}

print(seta | setb)
# {1, 2, 3, 4, 5, 6, 7, 8}
print(seta & setb )
# {4, 5}
print(seta.intersection(setb))
# {4, 5}

print(seta - setb )
# {1, 2, 3}
print(seta.difference(setb))
# {1, 2, 3}
print(seta ^ setb)
# {1, 2, 3, 6, 7, 8}
print(seta.symmetric_difference(setb))
# {1, 2, 3, 6, 7, 8}

seta.add(10)
print(seta)
# {1, 2, 3, 4, 5, 10}
seta.remove(1)
print(seta)
# {2, 3, 4, 5, 10}
seta.discard(10)
print(seta)
# {2, 3, 4, 5}
b = setb.pop()
print(b)
# 2
seta.clear()