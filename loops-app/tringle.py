num = int(input("Eneter the number :"))
for i in range(1,num+1):
    print(" " * (num-i) , end="")
     
    for j in range(1,2*i):
        print(j,end="")
    print()   
