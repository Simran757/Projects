diction = {
    "variable":"container for vales",
"variables declaration":"to assign a value to a variable",
"interpreter":"decodes the code",
"python":"object oriented language",
"syntax":"correct way to write code",
}




print("your options are : ")
print(list(diction.keys()))

a = input("enter the word you want to search = ")

print(diction.get(a))
