import os
if __name__ == '__main__':
    while True:
            x=input("enter what you want to say : ")
            if x=="q":
                break
            else:
                
                command=f"say {x}"
                os.system(command)
