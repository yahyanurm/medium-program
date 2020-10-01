import random
file=open('wordlist.txt','r')
isi=file.read()

word=''
isi=isi.split(" ")
while len(word)<3:
    rint=random.randrange(len(isi))
    word=str(isi[rint])
wordans=[str(0) for x in range(len(word))]
print("kata yang harus ditebak ada {} huruf".format(len(word)))

tebakan=[]
kesempatan=9
n=1
c=1
while True:
    if c>=kesempatan:
        print("answer",word,"you lose")
        break
    print("\n ================================================= \nTebakan ke ", n,"\n ada %s kesempatan" % (kesempatan-c))
    if len(tebakan)>0:
        a=""
        a=a.join(tebakan)
        print("huruf yang sudah diinput \n{}".format(a))
    print("Masukkan huruf yang mungkin ada di kata misteri")
    inp=input()
    try:
        if len(inp)>1:
            print("masukkan satu huruf saja")
            continue
    except exception as e:
        print(e)
    if str(inp) in word:

        jmlhuruf=word.count(inp)
        a=word.find(inp)
        jh=word.count(inp)
        ch=0
        while ch<jh:
            wordans[a]=inp
            a=word[a+1:].find(inp)+(a+1)
            ch+=1
        strwa=""
        strwa=strwa.join(wordans)
        print(strwa)
        if "0" not in wordans:
            print("you win")
            break
    elif inp in tebakan:
        n+=1
        continue
    else:
        if inp not in tebakan:
            tebakan.append(inp)
            print("%s tidak ada" % inp)
        c+=1
    n+=1
            