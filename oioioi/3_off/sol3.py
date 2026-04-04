import sys
from array import array

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

    T_out = array('i', [0] * n)
    
    count = [0] * 65536
    for val in T:
        count[val & 0xFFFF] += 1
        
    for i in range(1, 65536):
        count[i] += count[i-1]
        
    for i in range(n - 1, -1, -1):
        val = T[i]
        idx = val & 0xFFFF
        count[idx] -= 1
        T_out[count[idx]] = val
        
    count = [0] * 65536
    for val in T_out:
        count[(val >> 16) & 0xFFFF] += 1
        
    for i in range(1, 65536):
        count[i] += count[i-1]
        
    for i in range(n - 1, -1, -1):
        val = T_out[i]
        idx = (val >> 16) & 0xFFFF
        count[idx] -= 1
        T[count[idx]] = val

    for q in queries:
        print(T[n - q])

if __name__ == '__main__':
    solve()
