ef Hey_siri():
    word=input()
    if word=="こんにちは" or word=="こんにちわ":
        print("こんにちは")
    elif word=="おはよう" or word=="おはようございます":
        print("おはよう")
    elif word=="こんばんは" or word=="こんばんわ":
        print("こんばんは")
    elif word=="名前は？":
        print("siriです")
    else:
        print("すみません。よくわかりません。")

Hey_siri()
