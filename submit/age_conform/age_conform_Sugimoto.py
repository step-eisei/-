import def_age_guess
miss=0

for i in range(0,151):
    age_min=def_age_guess.age_guess(i)
    if i!=age_min:
        miss+=1
    if i==150:
        print(str(miss)+"回年齢当てを失敗しました")
