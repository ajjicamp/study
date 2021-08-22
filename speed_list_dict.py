import random
import time
def create_data(n):
    # key 값 생성
    keys = [i for i in range(n)]
    # key 값 섞기 (중복없는 랜덤)
    random.shuffle(keys)
    # value값 생성
    # random.randrange(시작, 끝) -> 범위 내 랜덤 출력
    values = [random.randrange(0, 100) for i in range(n)]

    # 두가지 데이터로 [key, value] array를 생성
    data = [[keys[i], values[i]] for i in range(n)]
    # print(data)
    return data


def create_dict(li):
    d = {}
    KEY = 0
    VALUE = 1
    # 랜덤값을 딕셔너리에 대입

    for i in li:
        d[i[KEY]] = i[VALUE]
    # print(d)
    return d


def find_list(key, li):
    start = time.time()
    for i in li:
        if i[0] == key:      # 리스트 값 중 첫번째 값, 즉 dict의 key값에 상응하는 값
            t = (time.time() - start) * 1000  # ms
            return {'key': i[0], 'value': i[1], 'time': t}
    return -1


def find_dict(key, d):
    start = time.time()
    try:
        value = d[key]
        t = (time.time() - start) * 1000  # ms
        return {'key': key, 'value': value, 'time': t}
    except:
        return -1


def time_test(n, key):
    # 리스트 생성
    NUM_DATA = n  # n개의 데이터
    KEY = key  # 찾으려는 Key 값
    li = create_data(NUM_DATA)

    # 딕셔너리 생성
    d = create_dict(li)
    # 시간 측정(리스트)
    t_li = find_list(KEY, li)
    # 시간 측정(딕셔너리)
    t_d = find_dict(KEY, d)

    return {'list': t_li, 'dict': t_d, 'list_value': li}


if __name__ == '__main__':
    print('[100개 탐색 시]')
    r = time_test(1000, 1)
    print(f'리스트 탐색: {r["list"]}')
    print(f'딕셔너리 탐색: {r["dict"]}')
    print(f'{r["list"]["time"] / (r["dict"]["time"]+0.00001)}배 차이\n')
    print('list마지막값:', r['list_value'])

    print('[10^3개 탐색 시]')
    r = time_test(10000, 1)
    print(f'리스트 탐색: {r["list"]}')
    print(f'딕셔너리 탐색: {r["dict"]}')
    print(f'{r["list"]["time"] / (r["dict"]["time"]+0.00001)}배 차이\n')

    print('[10^4개 탐색 시]')
    r = time_test(100000, 1)
    print(f'리스트 탐색: {r["list"]}')
    print(f'딕셔너리 탐색: {r["dict"]}')
    print(f'{r["list"]["time"] / (r["dict"]["time"]+0.00001)}배 차이\n')

    print('[10^6개 탐색 시')
    r = time_test(1000000, 1)
    print(f'리스트 탐색: {r["list"]}')
    print(f'딕셔너리 탐색: {r["dict"]}')
    print(f'{r["list"]["time"] / (r["dict"]["time"]+0.00001)}배 차이\n')
