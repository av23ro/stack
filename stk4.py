def push(arr,val):
    arr.append(val)
    print("data pushed successfully!!")

def display(arr):
    for i in range(0,len(arr),1):
        if arr[i]%5==0:
            print("displaying item divisable by 5:",arr[i])
        elif arr[i]%5!=0:
            print(arr[i],"is not divisable by 5!!!!!!!!!!")

arr=[]

top=None

while True:
    print("1.push")
    print("2.display item divisable by 5")
    print("3.exit")
    ch=int(input("enter your choice(1-3):"))
    if ch==1:
        val=int(input("enter the number to be pushed:"))
        push(arr,val)
    elif ch==2:
        if len(arr)==0:
            print("empty stack!!")
        else:
            display(arr)
    elif ch==3:
        print("thank you!!!")
        break
    else:
        print("invalide choice")
