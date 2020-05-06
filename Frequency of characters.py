def character_freqency(str1):
    dict = {}
    for x in str1:
        keys = dict.keys()
        if x in keys:
         dict[x] += 1
        else:
         dict[x] = 1
    return dict

string = input("Enter your word or phrase: ")
print(character_freqency(string))
