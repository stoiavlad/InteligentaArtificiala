print(type(10))
print(10 + 3)
print(10 * 2)

text = "Hello"

print(text[0])
print(text[1:4])
print(text[::-1])

print("Hi " + "there")
print("*" * 5)

print(len("Python"))
print(" hello ".strip())
print("hello".upper())
print("HELLO".lower())

print(bool(True))
print(bool(False))

print(bool(0))
print(bool(10))
print(bool(""))

my_list = [1, 2, 3]

print(my_list[0])
print(my_list[1:])

my_list.append(4)
print(my_list)

my_list.pop()
print(my_list)

person = {
    "name": "John",
    "age": 25
}

print(person["name"])
print(person.keys())

person["age"] = 26
print(person)

my_tuple = ("apple", "banana", "mango")

print(my_tuple[0])
print(len(my_tuple))
print(my_tuple.count("banana"))

my_set = {1,2,3}

my_set.add(4)
print(my_set)

print(2 in my_set)

set2 = {3,4,5}
print(my_set.union(set2))


#ex
a = 10
b = 3

print(a + b)
print(a * b)
print(a % b)

name = "Andrei"

print(name[0])
print(name[::-1])
print("Hello " + name)

numbers = [1, 2, 3]

numbers.append(4)

print(numbers)

print(numbers[1])