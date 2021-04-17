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

# 강사님 코드
def solution(n, words):
    words_spoken = set()
    for i, w in enumerate(zip(words, words[1:])):
        words_spoken.add(w[0])
        if w[1] in words_spoken or w[0][-1] != w[1][0]:
            return [(i+1)%n + 1, (i+1)//n + 1]
    return [0, 0]
