def columnar_cipher_e(text, key):
    text = text.replace(" ", "")

    ls = {}
    index = 0
    for i in range(len(text)):
        try:
            ls[key[index]] += text[i]
        except:
            ls[key[index]] = text[i]

        index += 1
        if index == len(key):
            index = 0
    
    key = "".join(sorted(key))
    result = ""
    largest = len(text)//len(key)
    for i in key:
        if len(ls[i]) == largest:
            result += ls[i] +"_"
        else:
            result += ls[i]

    print(result)
    return result

def columnar_cipher_d(text, key):
    ls = {}
    sortedKey = "".join(sorted(key))
    largest = len(text)//len(key)
    index = 0
    track = 1
    for i in range(len(text)):
        try: 
            ls[sortedKey[index]] += text[i]
        except:
            ls[sortedKey[index]] = text[i]
        track += 1
        if track == largest + 1:
            index += 1 
            track = 1
    
    result = ""
    for j in range(largest):
        for i in key:
            result += ls[i][j]
    print(result)
