
from sys import stdin

data = iter(stdin.read().split())
q = int(next(data))

seq:list[int] = [1, 2, 7]
while True:
    next_val = (3*seq[-1] + seq[-2] - seq[-3]) % 67
    seq.append(next_val)

    if seq[-3] == 1 and seq[-2] == 2 and seq[-1] == 7:
        _ = seq.pop()
        _ = seq.pop()
        _ = seq.pop()
        break

cycle_len = len(seq)

for _ in range(q):
    t = int(next(data))
    print( seq[(t - 1) % cycle_len])

