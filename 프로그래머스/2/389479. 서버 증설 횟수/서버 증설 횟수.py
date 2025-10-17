def solution(players, m, k):
    # 해당 시간에 증설 필요한 지 어떻게 확인하지?
    # 0~m-1이면 증설 0, m~2m-1이면 증설 1, 2m~3m-1이면 증설 2
    # 해당 시간 인원 // m 랑 그 시간의 서버 개수 비교해서
    answer = 0
    list = [0] * len(players)
    for time in range(len(players)):
        if players[time] // m > list[time]:
            add = players[time]//m - list[time]
            answer += add
            if time+k < len(players):
                for i in range(time, time+k):
                    list[i] += add
            else:
                 for i in range(time, len(players)):
                        list[i] += add
                
    print(list)
    return answer