def age_guess(age):

    age_min=0
    age_max=150
    i=0

    while age_max!=age_min:
        med=(age_min+age_max)//2+1

        if age>=med:
            age_min=med
            i+=1
        else:
            age_max=med-1
            i+=1
    print(str(i)+"回の質問をしました")
    print("あなたは"+str(age_min)+"歳です")
    print("実際は"+str(age)+"歳です")
    if age==age_min:
        print("年齢当て成功")
    else:
        print("年齢当て失敗")
    return(age_min)
