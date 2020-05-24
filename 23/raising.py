def getratios(L1,L2):
    ratios=[]
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) # nan=not a number
        except:
            raise ValueError('getratios called with bad arg')
    return ratios
print(getratios([1.0,2.0,7.0,8.0],[1.0,2.0,0.0,3.0]))
print(getratios([],[]))
print(getratios([1.0,2.0],[3.0]))