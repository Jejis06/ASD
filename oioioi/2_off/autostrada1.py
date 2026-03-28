from sys import stdin

l_type = list[tuple[int,int]]

def mergesort(A):
    n = len(A)
    B = [None] * n
    width = 1
    src, dst = A, B
    while width < n:
        for i in range(0, n, 2*width):
            l = i
            r = min(i + width, n)
            r_end = min(i + 2*width, n)
            l_end = r
            k = i
            while l < l_end and r < r_end:
                if src[l] <= src[r]:
                    dst[k] = src[l]
                    l += 1
                else:
                    dst[k] = src[r]
                    r += 1
                k += 1
            while l < l_end:
                dst[k] = src[l]
                l += 1
                k += 1
            while r < r_end:
                dst[k] = src[r]
                r += 1
                k += 1
        src, dst = dst, src
        width *= 2
    if src is not A:
        A[:] = src[:]


def solution() -> None:
    inp = iter([ int(i) for i in stdin.read().split()])
    n = next(inp)
    T = next(inp)

    events:list[tuple[int, int]] = []
    for i in range(n):
        a = next(inp); b = next(inp)
        events.append((a, 1))
        events.append((b+1, -1))
    #events.sort()
    mergesort(events)
    max_val = 0
    max_ind = -1

    curr_val = 0
    for i in range(2 * n - 1):
        curr_val += events[i][1]
        if events[i+1][0] != events[i][0]:
            if curr_val > max_val:
                max_val = curr_val
                max_ind = events[i][0]
    curr_val += events[2*n - 1][1]
    if curr_val > max_val:
        max_val = curr_val
        max_ind = events[2*n - 1][0]
    print(max_val, max_ind)



if __name__ == "__main__":
    solution()

