# 第20课
# List Operations
```python
L1=['re']
L2=['mi']
L3=['do']
L4=L1+L2
L3.extend(L4)
L3.sort()
del(L3[0])
L3.append(['fa','la'])
print(L3)
```
## 结果
## ['mi', 're', ['fa', 'la']]

 L4==['re','mi']
 L3==['do','re','mi']
 L3==['do','mi','re']
 L3==['mi','re']
 L3==['mi', 're', ['fa', 'la']]
 