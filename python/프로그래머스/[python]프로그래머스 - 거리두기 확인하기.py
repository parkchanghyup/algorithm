def solution(places):

    answer = []

    for p in places:

        # 거리두기가 지켜지지 않으면 바로 return 하기 위한 변수
        key = False
        arr = []

        for x in p:
            arr.append(list(x))

        # 이중 for문을 이용해 확인

        for i in range(5):

            if key:
                break

            for j in range(5):
                if key:
                    break

                # 응시자가 앉아있다면
                if arr[i][j] == 'P':

                    if i+1 < 5:
                        # 아래 확인

                        if arr[i+1][j] == 'P':
                            key = True
                            break

                        # 바로 아래는 빈테이블 이고 그 다음에 응시자가 있다면
                        if arr[i+1][j] == 'O':

                            if i+2 < 5:

                                if arr[i+2][j] == 'P':
                                    key = True
                                    break

                    # 오른쪽
                    if j + 1 < 5:
                        if arr[i][j+1] == 'P':
                            key = True
                            break

                        if arr[i][j+1] == 'O':
                            if j+2 < 5:
                                if arr[i][j+2] == 'P':

                                    key = True
                                    break

                    # 우측아래
                    if i+1 < 5 and j + 1 < 5:
                        if arr[i+1][j+1] == 'P' and (arr[i+1][j] == 'O' or arr[i][j+1] == 'O'):
                            key = True
                            break
                    # 좌측아래
                    if j-1 >= 0 and i + 1 < 5:
                        if arr[i+1][j-1] == 'P' and (arr[i+1][j] == 'O' or arr[i][j-1] == 'O'):
                            key = True
                            break

        if key:
            answer.append(0)
        else:
            answer.append(1)

    return answer
