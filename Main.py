text = 'NotWord7 7NotWord! 777'
res = dict()
text = text.replace(".", "")
text = text.replace(",", "")
text = text.split()
print(text)

for word in text:
    if not any([i.isdigit() for i in word]):
        if word not in res:
            res[word] = 1
        else:
            res[word] += 1

print(res)
