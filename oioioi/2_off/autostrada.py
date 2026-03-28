from sys import stdin

def counting_sort_radix(arr:list[tuple[int,int]], pad:int):
    n = len(arr)
    B:list[tuple[int,int]] = [0] * n

    cnts = [0] * 256
    for i in range(n):
        ind = (arr[i][0] >> 8 * pad) & 255
        cnts[ind] += 1
    for i in range(1, 256):
        cnts[i] += cnts[i-1]
    #print(cnts)
    for i in range(n-1, -1, -1):
        ind = (arr[i][0] >> 8 * pad) & 255
        cnts[ind] -= 1
        B[cnts[ind]] = arr[i]

    arr[0:n] = B[0:n]


def radix_sort(arr:list[tuple[int, int]], passes:int) -> None:
    for i in range(passes):
        counting_sort_radix(arr, i)

def solution() -> None:
    inp = iter([ int(i) for i in stdin.read().split()])
    n = next(inp)
    T = next(inp)

    events:list[tuple[int, int]] = []
    for i in range(n):
        a = next(inp); b = next(inp)
        events.append((a, 1))
        events.append((b+1, -1))

    '''
    T_c = T
    max_passes = 0
    while T_c > 0:
        max_passes += 1
        T_c >>= 8
    if max_passes == 0: max_passes = 1
    '''

    events.sort()
    #radix_sort(events, max_passes)
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

