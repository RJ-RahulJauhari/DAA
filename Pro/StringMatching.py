def StringMatch(sub,sen):

    sub_len = len(sub)
    sen_len = len(sen)

    for i in range(0,sen_len - sub_len):
        if sen[i:i+sub_len] == sub:
            print("Match Found at ",i)
            return True