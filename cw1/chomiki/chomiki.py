from math import ceil
'''
Zad 6 ______________ [bin search po wyniku]

Chomiki

[a1, b1], [a2, b2], ... , [an, bn]
a1 < b1 < a2 < b2 ..... < an < bn

Vi ai, bi nal do N
k chomikow
'''




def check(holes:list[tuple[int, int]], dist:int, hamsters:int) -> bool:
    if dist == 0: return True
    placed = 0
    curr_pos = -float('inf')

    for a, b in holes:
        next_pos = max(curr_pos + dist, a)
        if next_pos <= b:
            count = (b - next_pos) // dist + 1
            placed += count

            if placed >= hamsters: return True
            curr_pos = next_pos + (count - 1) * dist

    return placed >= hamsters


def solve(holes:list[tuple[int,int]], hamsters:int, l:int, r:int) -> int:
    while l <= r:
        mid = (l + r) // 2
        if check(holes, mid, hamsters):
            l = mid + 1
        else: 
            r = mid - 1
    return l - 1



def main() -> None:

    holes = []

    n, k = map(int, input().split())

    for _ in range(n):
        a, b = map(int, input().split())

        holes.append((a, b))

    max_pos = holes[n-1][1]
    min_pos = holes[0][0]
    r:int = ceil((max_pos - min_pos))

    print(solve(holes, k, 0, r))


    return None

if __name__ == "__main__":
    main()

