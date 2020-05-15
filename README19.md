# 第19课
```python
L=["life","answer",42,0]
for thing in L:
    if thing==0:
        L[thing]="universe"
    elif thing==42:
        L[1]="everything"

print(L)
```
## 结果：
## ['universe', 'everything', 42, 0]
### 第一次：['life', 'answer', 42, 0]
### 第二次：['life', 'answer', 42, 0]
### 第三次：['life', 'everything', 42, 0]
### 第四次：['universe', 'everything', 42, 0]
