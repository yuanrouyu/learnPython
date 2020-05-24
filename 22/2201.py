def mult_iter(a,b):
    result=0
    while b>0:
        result+=a
        b-=1  
    return result
q=mult_iter(2,5)
print(q)

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(4))


def mult(a,b):
    if b==1:
        return a
    else:
        return a+mult(a,b-1)

print(mult(3,4))

def printmove(fr,to):
    print('move from'+str(fr)+'to'+str(to))

def towers(n,fr,to,spare):
    if n==1:
        printmove(fr,to)
    else:
        towers(n-1,fr,spare,to)
        towers(1,fr,to,spare)
        towers(n-1,spare,to,fr)

print(towers(3,2,1,3))


def fib(x):
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

print(fib(5))

def ispa(s):
    def tocha(s):
        s=s.lower()
        ans=''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans =ans+c
        return ans
    def ispal(s):
        if len(s)<1:
            return True
        else:
            return s[0]==s[-1]and ispal(s[1:-1])
    return ispal(tocha(s))

grades={'anna':'B','john':'A+','den':'A','kat':'A'}
grades.keys()
grades.values()



def ly(ly):
    mydict={}
    for word in ly:
        if word in mydict:
            mydict[word]+=1
        else:
            mydict[word]=1
    return mydict

she=['yuan','ruo','yu','xu','ling','xiao','xu','yuan','ling','de','de','de','huai','huai','de','yao','si','zhen','shi','tai','huai','le']
print(ly(she))

def most_common_words(freqs):
    values=freqs.values()
    best=max(values)
    words=[]
    for k in freqs:
        if freqs[k]==best:
            words.append(k)
    return(words,best)

she={'yuan': 2, 'ruo': 1, 'yu': 1, 'xu': 2, 'ling': 2, 'xiao': 1, 'de': 4, 'huai': 3, 'yao': 1, 'si': 1, 'zhen': 1, 'shi': 1, 'tai': 1, 'le': 1}
print(most_common_words(she))

def words_often(freqs,mintimes):
    result=[]
    done =False
    while not done:
        temp = most_common_words(freqs)
        if temp[1]>=mintimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done=True
    return result

print(words_often(she,2))
 

def fib_eff(n,d):
    if n in d:
        return d[n]
    else:
        ans=fib_eff(n-1,d)+fib_eff(n-2,d)
        d[n]=ans
        return ans
d={1:1,2:2}
print(fib_eff(6,d))