def transformSentence(sentence):
    _list = sentence.split()
    trans=''
    for word in _list:
        trans += word[0]
        prev = word[0]
        for ltr in word[1:]:
            if prev.lower() < ltr.lower():
                trans += ltr.upper()
            elif prev.lower() > ltr.lower():
                trans += ltr.lower()
            else:
                trans += ltr
            prev = ltr
        trans+= ' '
    return trans

print(transformSentence("do you like cheese"))