t=('one','for','one')
a_set=set(t)
print(a_set)

q={1,2,3,4}
p={4,5,6,7}
my_set=q.union(p)
print(my_set)

print(q.intersection(p))
print(q.difference(p))
print(p.difference(q))

for i in q:
    print(i)

q.add("adhu")
print(q)

def first_non_repeating_char(string):
    for char in string:
        if string.count(char) ==1:
            return char
    return None
print(first_non_repeating_char('Adhu'))
print(first_non_repeating_char('aa'))
