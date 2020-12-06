# 입력
# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어는 2글자~15글자로 이루어져 있다.

# 출력
# 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.

word = str(input()).upper()

dial = [0 for i in range(65, 91)]

for w in word:
    dial[ord(w)-65] += 1

result = [0 for i in range(10)]

for i in range(len(dial)):
    if i <= 2:
        result[2] += dial[i]
    elif i <= 5:
        result[3] += dial[i]
    elif i <= 8:
        result[4] += dial[i]
    elif i <= 11:
        result[5] += dial[i]
    elif i <= 14:
        result[6] += dial[i]
    elif i <= 18:
        result[7] += dial[i]
    elif i <= 21:
        result[8] += dial[i]
    elif i <= 25:
        result[9] += dial[i]

sum_of_time = 0

for j in range(2, 10):
    sum_of_time += (3 + (j - 2)) * result[j]

print(sum_of_time)
