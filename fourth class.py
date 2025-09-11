#dictionary
info = {
    "name" : "MRITYUNJAY THAKUR",
    "age" : 20,
    "subject" : ["python","physics","maths"],
    "hometown" : "MADHUBANI"
}
info["name"] = "sonu"
print(info)
print(info["name"])
nulldict = {}
print(nulldict)
student = {
    "name" : "MRITYUNJAY THAKUR",
    "score" : {
        "phy" : 98,
        "chem" : 89,
        "maths" : 90
    }
}
print(student)
print(student["score"]["chem"])
print(student.keys())
print(list(student.keys()))
print(len(list(student.keys())))
print(student.values())
print(student.items())
print(student.get("score"))
student.update({"city" : "Madhubani"})
print(student)
#if i write "name :"rahul" then the new value will be output
#sets in python
collection = {2,3,4,5,3,4,5}
print(type(collection))
print(collection) #here the output will have only one 3 as set will ignore repititive value.
print(len(collection))
set = set()#empty set
print(type(set))
set.add(1)
set.add(2)
set.add(3)
collection.remove(4)
print(set)
print(collection)
set.add("hello")
set.add((2,5,3))
print(set)
#but if i add a dictionary in the set the output will be error as the elements of a set are immutable eventhoug set itself is mutable.
set1 = {2,3,4,5,8,"hi"}
set2 = {2,7,0,5,"hello"}
print(set1.union(set2))
print(set1.intersection(set2))
print(set.pop())
print(set.clear())