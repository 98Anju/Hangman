import random

print(""" __________
|          |                   
| {}    {} |
|    ()    |
 ----------
----| |----
\\\\--| |---//
------------
     |
     |
     |
    /|\\
   / | \\
  /     \\
 /       \\""")
a=["true","play","request","want","space"]
b=["t__e","p_a_","r__u__t","w__t","s_a_e"]
d=[["r","u"],["l","y"],["e","q","e","s"],["a","n"],["p","c"]]
print(a)
r1 = random.randint(0, 4)
print(b[r1])
c=3
for i in range(len(d[r1])):
    # print("you have only ",c+1,"chance to give answer ")
    option=input("enter any answer ")
    if option==d[r1][i]:
        print("correct yes")
    else:
        print("you have only ",c,"chance to give answer ")
        print("increct ansser")
        while c>0:
            c-=1
            option = input("enter any answer ")
            if option==d[r1][i]:
                print("correct yes")
                break
            else:
                print("you have only ",c,"chance to give answer ")
                print("sorry increct")
        if c==0:
            print("you lost match")
            break
if c>0:
    print("congrets")
                






