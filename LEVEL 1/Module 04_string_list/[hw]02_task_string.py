text = "мама босс раму мыла балкон"
test = text.split(" ")
print(test)
check = False

for word in test:
    if word.startswith("б"):
        print(word)
        check = True
        break
if check == False:
    print("слов на Б нету")