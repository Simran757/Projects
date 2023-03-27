# preparing a result.....
name = input("enter your name = ")
print(f"your name is {name}.")
print(f"{name}, Now enter your subjects.")
sub1 = int(input("enter your hindi marks ="))
sub2 = int(input("enter your english marks ="))
sub3 = int(input("enter your maths marks ="))
sub4 = int(input("enter your science marks ="))
sub5 = int(input("enter your arts marks ="))
results = (sub1+sub2+sub3+sub4+sub5)/5
if results>100:
    raise ValueError("dont enter more then 100")
print(f"{name} you have got {results}%")

if results>90 :
    print(f"{name} you have got first division ..")
elif results<90 and results>60:
    print(f"{name} you have got second division ..")
elif results<60 and results>40:
    print(f"{name} you have got third division ..")
else:
    print(f"{name} you have got no division and you are failed ..")
