mencari sub string yang urut secara alphabet

s = 'azcbobobegghakl'
jwb=''
jwbl=[]
for i in range(len(s)):
    if i < len(s)-1:
        a=s[i]
        b=s[i+1]
        if (ord(a)<=ord(b)):
            jwb+=a
        else:
            jwb+=a
            jwbl.append(jwb)
            jwb=''
temp=0
res=""
for i in jwbl:
    if (len(i)>temp):
        temp=len(i)
        res=i
print(res)
#output beggh
