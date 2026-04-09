s = {1,2,2,2,2,2,33,33,33,33}
print(s)

# add eelement to the set
s.add(4)
print(s)

# remove element from the set
s.remove(2)
print(s)

# clear the set
s.clear()
print(s)

# pop element from the set
# remove any random element from the set and return it
s = {1,2,3,4,5}
popped_element = s.pop()
print("Popped element:", popped_element)
print("Set after popping:", s)

# union of sets
s1 = {1,2,3}
s2 = {3,4,5}
union_set = s1.union(s2)
print("Union of s1 and s2:", union_set)

# intersection of sets
intersection_set = s1.intersection(s2)
print("Intersection of s1 and s2:", intersection_set)