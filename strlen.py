i=0
a='silver oak university'

while i < len(a):
    if a[i]=='e'or a[i]=='s':
        i+=1
        continue

    print('current letter:',a[i])
    i+=1

