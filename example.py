import time
import sys
from doctest import testmod


def trib(n):
    if n < 3:
        return 1
    tribs = [1, 1, 1]
    for i in range(3, n + 1):
        tribs.append(tribs[-1] + tribs[-2] + tribs[-3])
    return tribs[n]


# 単純に起動した場合にテストをする
if __name__ == "__main__":
    print("ロジックのテストを行います、出力が無ければOKです")
    results = testmod()
    print("テストが完了しました")
    if results.failed > 0:
        print("テストに失敗しているため、処理を中断します")
        sys.exit(1)
    if results.failed == 0:
        print("0〜99までのトリボナッチ数列を表示します")
        start_time = time.time()
        for i in range(100):
            print(f"{i}: {trib(i)}")
            if time.time() - start_time > 1:
                print("処理時間が1秒を超えたため、強制的に終了します")
                break
