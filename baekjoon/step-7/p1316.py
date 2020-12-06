# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.

# 97 ~ 122

N = int(input())

group_words_count = 0
for n in range(N):
    alphabet = [0 for i in range(27)]
    word = str(input())
    checkFlag = 0
    for i in range(len(word) - 1):
        if word[i] != word[i+1]:
            if alphabet[ord(word[i+1])-97] > 0:
                checkFlag += 1
                break
            else:
                alphabet[ord(word[i])-97] += 1
    if checkFlag == 0:
        group_words_count += 1

print(group_words_count)
