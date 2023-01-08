# Quizz 29
## Part 1
```python
def wordcouter(dic, word):
    for i in word:
        if i in dic:
            dic[i] += 1
    return dic

dic = {"w":0, "l":0, "c":0}
word = "hello world"

print(wordcouter(dic, word))
```
![](../Images/quizz29-proof.png)

**Fig. 1** Proof


## Part 2
How many colors can we represent in a 6 bit computer?
2^6 = 64