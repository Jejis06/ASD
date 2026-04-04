import sys
from array import array
import random

def solve():
    def get_ints():
        for line in sys.stdin:
            yield int(line)
            
    iterator = get_ints()
    
    try:
        n = next(iterator)
        T = array('i', (next(iterator) for _ in range(n)))
        
        q_count = next(iterator)
        queries = [next(iterator) for _ in range(q_count)]
    except StopIteration:
        return

    target_indices = [n - q for q in queries]
    unique_targets = list(set(target_indices))

    stack = [(0, n - 1, unique_targets)]

    while stack:
        left, right, targets = stack.pop()

        if left >= right or not targets:
            continue

        pivot_idx = random.randint(left, right)
        pivot_val = T[pivot_idx]

        lt = left
        gt = right
        i = left

        while i <= gt:
            if T[i] < pivot_val:
                T[i], T[lt] = T[lt], T[i]
                lt += 1
                i += 1
            elif T[i] > pivot_val:
                T[i], T[gt] = T[gt], T[i]
                gt -= 1
            else:
                i += 1

        left_targets = []
        right_targets = []
        
        for t in targets:
            if t < lt:
                left_targets.append(t)
            elif t > gt:
                right_targets.append(t)

        if left_targets:
            stack.append((left, lt - 1, left_targets))
        if right_targets:
            stack.append((gt + 1, right, right_targets))

    for target_idx in target_indices:
        print(T[target_idx])

if __name__ == '__main__':
    solve()
