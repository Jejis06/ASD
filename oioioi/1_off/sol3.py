import sys
def solution(words):
    if not words:
        return 0

    uniq = sorted(set(words))
    vals = dict(zip(uniq, range(1, len(uniq)+1)))

    max_val = len(uniq)
    tree = [0] * (max_val + 1)
    max_cnt = 0

    for word in words:
        curr_val = vals[word]

        ind = curr_val - 1
        cnt = 0
        while ind > 0:
            cnt += tree[ind]
            ind -= ind & (-ind)
        if cnt > max_cnt:
            max_cnt = cnt

        ind = curr_val
        while ind <= max_val:
            tree[ind] += 1
            ind += ind & (-ind)
    return max_cnt



if __name__ == "__main__":
    dane = sys.stdin.read().split()
    if dane:
        words = dane[1:]
        print(solution(words))

