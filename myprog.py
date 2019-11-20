import string
def num ():
    print("---  "*3)
    for x in range (1,10):
        mX = "| ".join(str(x))
        for i in range(0, 3):
            print("|",end = "")
            break
        if mX == str(3)  or  mX == str(6) :
            print(mX+"|")
            print("---  " * 3)
        else:
            print(mX, end="|  ")
if __name__ == '__main__':
    num()
