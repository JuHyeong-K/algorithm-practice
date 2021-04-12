# algorithm-practice

## 프로그래머스 문제 풀이
https://programmers.co.kr/learn/courses/30/lessons/12981

### solution.py
```python
def solution(n, words):
    answer = []

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    word_chain = []
    for word in words:
        word_chain.append(word)                 
        if len(word_chain) == 1:
            continue
        if word in word_chain[:-1]:
            if len(word_chain) % n == 0:
                answer.append(len(word_chain) // n)
                answer.append(n)
                return answer
            else:
                answer.append(len(word_chain) // n + 1)
                answer.append(len(word_chain) % n)
                return answer
        elif word_chain[-2][-1] != word[0]:
            if len(word_chain) % n == 0:
                answer.append(len(word_chain) // n)
                answer.append(n)
                return answer
            else:
                answer.append(len(word_chain) % n)
                answer.append(len(word_chain) // n + 1)
                return answer
        print(word_chain[-2][-1], word[0])

    return [0, 0]
```

https://programmers.co.kr/learn/courses/30/lessons/12913
### solution2.py
```python
def solution(land):
    answer = 0
    before_index = None;
    for i in range(3):
        if i > 0:
            before_index = land[i-1].index(max(land[i-1]))
        if before_index != None and before_index == land[i].index(max(land[i])):
            land[i].pop(before_index)
            answer += max(land[i])
        else:
            answer += max(land[i])
    return answer
```
