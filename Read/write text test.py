def thing():
    with open('Pass.txt','r') as g:
        l = g.read()
        l = l.split(',')
        print(l)
    with open('Pass.txt','w') as g:
        l.append(input("You cool? "))
        g.write(','.join(l))
    return l