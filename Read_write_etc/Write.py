def Write_file(write):
    with open('Pass.txt','r') as Opened:
        Readfile = Opened.read()
        Writefile = Readfile.split(',')
        print(Writefile)
    with open('Pass.txt','w') as g:
        Writefile.append(write)
        g.write(','.join(Writefile))
    return Writefile

