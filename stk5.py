def push(stk,val):
    stk.append(val)
    print("item pushed successfully!!!")

def pop(stk):
    val=stk.pop()
    print("poped item:",val)

def peek(stk):
    index=len(stk)-1
    print("toppest item:",stk[index])

def display(stk):
    top=len(stk)-1
    print(stk[top],"<--Top")
    for i in range(top-1,-1,-1):
        print(stk[i])

#main

stk = []

top=None

while True:
    print("1.push")
    print("2.pop")
    print("3.peek")
    print("4.display")
    print("5.exit")
    ch=int(input("enter your choice(1-5):"))
    if ch==1:
        val=int(input("enter number to be pushed:"))
        push(stk,val)
    elif ch==2:
        if len(stk)==0:
            print("empty stack!!")
        else:
            pop(stk)
    elif ch==3:
        if len(stk)==0:
            print("empty stack!!")
        else:
            peek(stk)
    elif ch==4:
        if len(stk)==0:
            print("empty stack!!")
        else:
            display(stk)
    elif ch==5:
        print("thank you!!")
        break
    else:
        print("invalid choice!!")
    
