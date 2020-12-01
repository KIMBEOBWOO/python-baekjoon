# 첫째 줄에 테스트 케이스의 개수가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.

# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 각 테스트 케이스마다 점수를 출력한다.

N = int(input())
scores = []

for i in range(N):
    scores.append(str(input()))

for pIndex in range(N):
    eachTotalScore = 0
    tempCount = 1
    if scores[pIndex][0] == 'O':
        eachTotalScore += 1
    for eachIndex in range(1, len(scores[pIndex])):
        if scores[pIndex][eachIndex] == 'O':
            # O 일 경우
            if(scores[pIndex][eachIndex-1]) == 'O':
                # 연속된 O 일 경우
                tempCount += 1
                eachTotalScore += tempCount
            else:
                # 처음 O 일 경우
                eachTotalScore += tempCount
        else:
            # X 일 경우
            eachTotalScore += 0
            tempCount = 1
    print(eachTotalScore)
