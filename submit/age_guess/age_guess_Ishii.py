a=0
b=100
c=(a+b)//2
for i in range(1,10+1):
    ans=input("あなたの年齢は"+str(c)+"歳以上ですか？yes or no:")
    if ans == "yes":
        a=c
        c=(a+b)//2
    elif ans == "no":
        b=c
        c=(a+b)//2
    elif a == b:
        break
print("あなたの年齢は"+str(c)+"歳です")
