#strings
str = ("hello!\nhow are you")
print(str)
#concatenation
str1 = 'mrityunjay'
str2 = 'thakur' 
print(str1 + str2)
#length of string
print(len(str1))
#indexing
print(str1[2])
print(str2[3])
#slicing
string = 'Apnacollege'
print(string[:len(string)])
print(str1[3:7])
#negative indexing
str5 = 'state'
print(str5[-3:-1])
#string function
str6 = "i am Iron Man"
print(str6.endswith("an"))
print(str6.capitalize())
print(str6.replace("a","o"))
print(str6.replace("Man","Woman"))
print(str6.find("Iron"))
print(str6.count("a"))
#conditional statements
light = "pink"
if(light == "red"):
    print("stop")
elif(light == 'green' ):
    print(go)
else:
    print("mat jao be")
#nesting
age = 34
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")    