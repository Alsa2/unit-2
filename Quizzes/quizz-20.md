# Quizz 20

## Part 1

```python
def get_truth():
    truth = []
    print("| A | B | C |")
    for i in range(8):
        truth.append([i//4, (i//2)%2, i%2])
        print("|", truth[i][0], "|", truth[i][1], "|", truth[i][2], "|")
get_truth()
```
![](../Images/quizz20-proof.png)
**Fig. 1** Proof

## Part 2

![](../Images/quizz19-logiccircuit.png)
**Fig. 2** Logic circuit for AB+(B+C(notA))A