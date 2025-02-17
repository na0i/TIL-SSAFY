# 테스트 케이스가 10개
for tc in range(10):
    # 테스트 케이스 1개별로 정수 1개와 리스트 입력
    T = int(input())
    arr = []
    # 100개의 행으로 이루어진 리스트 입력받기
    for i in range(100):
        arr.append(list(map(int, input().split())))

    # 행의 sum
    # 행의 sum을 담을 빈 리스트 생성
    sum_rows = []
    for i in range(100):
        # total 생성
        # total을 j 바로 위에 작성해야 매번 0으로 초기화 됨
        rows_total = 0
        for j in range(100):
            # i 행의 j를 차례로 더하기
            rows_total += arr[i][j]
        # i행의 j 합을 sum_rows 리스트에 추가
        sum_rows.append(rows_total)

    # 열의 sum
    # 열의 sum을 담을 빈 리스트 생성
    sum_columns = []
    for i in range(100):
        # total 생성
        # total을 j 바로 위에 작성해야 매번 0으로 초기화 됨
        columns_total = 0
        for j in range(100):
            # i 열을 고정하고 j 행을 차례로 더하기
            columns_total += arr[j][i]
        # i 열의 j 행 합을 sum_columns 리스트에 추가
        sum_columns.append(columns_total)

    # 대각선 sum(좌상>우하)
    # 대각선 sum을 담을 빈 리스트 생성
    sum_diagonal_1 = []
    diagonal_1_total = 0
    for i in range(100):
        # 좌상우하 대각선은 행,열의 인덱스가 동일
        # total에 값 추가
        diagonal_1_total += arr[i][i]
    # total 값을 리스트에 담기
    sum_diagonal_1.append(diagonal_1_total)

    # 대각선 sum(우상>좌하)
    # 대각선 sum을 담을 빈 리스트 생성
    sum_diagonal_2 = []
    diagonal_2_total = 0
    for i in range(100):
        # 우상좌하 대각선은 행, 열 인덱스 두값의 합 = 가로세로 길이 -1
        diagonal_2_total += arr[i][100 - i - 1]
    # total 값을 리스트에 담기
    sum_diagonal_2.append(diagonal_2_total)

    # 모든 합을 담을 entire 리스트 생성
    # 리스트끼리 더하는 것이므로 []로 감싸줄 필요가 없었다
    entire_sum = sum_rows + sum_columns + sum_diagonal_1 + sum_diagonal_2

    # entire_sum의 최댓값 구하기
    max_s = entire_sum[0]
    for i in range(len(entire_sum)):
        if entire_sum[i] > max_s:
            max_s = entire_sum[i]

    # 테스트 케이스를 순회하며 '테스트케이스 번호, 최댓값' 출력
    print('#{} {}'.format(T, max_s))
