max=101  #maxを１０１に変えたからmidに１００以上が現れるようになった,切り捨てでmid=100が出せる
min=0
mid=50

while mid!=min:  #０歳対策で「０歳以上ですか？」の質問を無くした
    print("あなたは"+str(int(mid))+"歳以上ですか？　yes or no")
    re=input()
    if re=="yes":
        min=mid
        mid=(max+min)/2 
        mid=int(mid)  
    elif re=="no":
        max=mid
        mid=(max+min)/2
        mid=int(mid)
    else:
        print("write yes or no")
    print(max,mid,min)

print("your age is "+str(int(mid)))    
