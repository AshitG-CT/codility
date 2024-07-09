'''How to count number of instances of a class in Python?'''
class geeks:
    counter = 0

    def __init__(self) -> None:
        geeks.counter += 1


g1 = geeks()
g1 = geeks()
g1 = geeks()
g1 = geeks()

print(geeks.counter)

# Output: 3