from itertools import permutations 
  

perm = list(permutations([x for x in range(1,4)]))
def isprime(n):
    if n==2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def cek(lp):
    cp=[]
    for i in range(len(lp)):
        if i==len(lp)-1:
            break
        a=i
        b=i+1
        c=lp[a]+lp[b]
        if isprime(c)==False:
            cp.append(1)
            break
        else:
            cp.append(0)
    if sum(cp)==0:
        return True
    else:
        return False
# Print the obtained permutations 
#print(perm)
it=0
for i in perm:
    if (cek(i)):
        print(i)
        it+=1
print(it)

#output
#(1, 2, 3)                                                                                                                       
#(3, 2, 1) 
#2
