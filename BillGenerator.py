
print("\t\t\t\tThe Grocery Store\t\t\t\t")
print("WELCOME TO OUR STORE \U0001F60D")
CousName=input("Enter your name : ")
dict={"chocolate":10,"biscuit":15,"flour":70,"paste":100,"soap":25,"brush":20}
print("ITEMS WE HAVE : ")
print(dict)
print("PRESS q TO QUIT ")
sum=0
while(True):
    userInput=input("Enter the price \U0001F5100:  ")
    if(userInput!="q"):
        sum+=int(userInput)
    else:
        print(f"{CousName}, YOUR TOTAL BILL IS = {sum}\n\t\t\tTHANKS  FOR SHOPPING \U0001F60D")
        break 
