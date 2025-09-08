#lists in python
marks = [67.87,88.89,65.65,99.00,99.96]#here it is written in square brackets and the number are seperated with comma
print(marks)
print(type(marks))
print(len(marks))
print(marks[3])
marks[3] = 100
print(marks)
marks.sort()
marks.append(78)
marks.sort(reverse=True)
marks.reverse()
