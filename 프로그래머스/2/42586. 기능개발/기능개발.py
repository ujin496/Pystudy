def solution(progresses, speeds):
    n = len(progresses)
    finished = [False] * n    # 각 기능이 '개발완료' 상태인지 표시
    pending = set()           # 완료됐지만 아직 배포되지 않은 인덱스들(대기목록)
    next_deploy = 0           # 다음 배포 대기 중인 가장 앞 인덱스
    answer = []

    # progresses는 하루가 지날 때마다 업데이트
    # next_deploy가 끝까지 가면 모든 배포가 끝난 것
    while next_deploy < n:
        # 1) 하루 진행
        for i in range(n):
            if not finished[i]:
                progresses[i] += speeds[i]
                if progresses[i] >= 100:
                    finished[i] = True
                    pending.add(i)

        # 2) 맨 앞(next_deploy) 기능이 완료됐다면, 연속으로 완료된 것들을 한 번에 배포
        if finished[next_deploy]:
            cnt = 0
            while next_deploy < n and finished[next_deploy]:
                cnt += 1
                # 대기목록에 있었다면 제거(정리용)
                if next_deploy in pending:
                    pending.remove(next_deploy)
                next_deploy += 1
            answer.append(cnt)

    return answer
