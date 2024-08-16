# sets
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#####################
# Exercise: Level 1
#####################

# 1. Find the length of the set it_companies
print(len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(["Nvida", "AMD"])
print(it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove("Twitter")
print(it_companies)

# 5. What is the difference between remove and discard
print("discard doesn't throw error if item doesn't exist")


#####################
# Exercise: Level 2
#####################

# 6. Join A and B
A.update(B)
print(A)

# 7. Find A intersection B
print(A.intersection(B))

# 8. Is A subset of B
print(A.issubset(B))

# 9. Are A and B disjoint sets
print(A.isdisjoint(B))

# 10. Join A with B and B with A
C = A.union(B)
D = B.union(A)

# 11. What is the symmetric difference between A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.symmetric_difference(B))

# 12. Delete the sets completely
del A
del B

#####################
# Exercise: Level 3
#####################

# 13. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(len(age))
print(len(age_set))
print(max(len(age), len(age_set)))

# 14. Explain the difference between the following data types: string, list, tuple and set
print("String: list of characters")
print(
    "List: is a collection which is ordered and changeable(modifiable). Allows duplicate members."
)
print(
    "Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members."
)
print(
    "Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed."
)

# 15. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
print(len(set("I am a teacher and I love to inspire and teach people".split(" "))))
