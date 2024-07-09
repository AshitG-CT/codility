import operator
d = {1:20, 3:4, 5:6, 7:24, 8:3}
print("Original dictionary: ", d)

sorted_a = dict(sorted(d.items(), key = operator.itemgetter(1), reverse=True))
print("Dictionary in ascending order by value: ", sorted_a)

sorted_d = dict(sorted(d.items(), key = operator.itemgetter(1)))
print("Dictionary in decending order by value: ", sorted_d)