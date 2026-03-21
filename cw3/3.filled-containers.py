"""
3. Pojemniki z woda:
    - duzo rozneg rozmiaru 2d prosokatow w ukladzie wspolrzednych
    - wszystkie pojemniki polaczone rurami (wiec napelnione tak ze jak jest podany poziom to tak jakby w 2d 
                                            tam gdzie linia poziomu to ponizej kazdy istniejacy pojemnik napelniony do danego pojemnika)
    - nalalismy k litrow wody i interesuje nas ile pojemnikow bedzie w pelni napelnione
"""

from random import randint

class Bucket:
    def __init__(self, x0:int=0, y0:int=0, x1:int=0, y1:int=0):
        self.x0:int = x0
        self.y0:int = y0
        self.x1:int = x1
        self.y1:int = y1

# ------------- Brut n^2 ----------------

def check_level(buckets:list[Bucket], level:int) -> tuple[int, int]:
    buckets_filled = 0
    liters_used = 0

    for bucket in buckets:
        if bucket.y0 <= level:
            w = abs(bucket.x1 - bucket.x0)
            min_y = 0
            if bucket.y1 <= level:
                buckets_filled += 1
                min_y = bucket.y1
            else: min_y = level

            h = abs(min_y - bucket.y0)
            liters_used += w * h
    return (buckets_filled, liters_used)

def partition(A:list[int], low:int, high:int) -> int:
    pivot = A[high]
    
    i = low - 1
    for j in range(low, high + 1):
        if A[j] <= pivot:
            i += 1
            A[j], A[i] = A[i], A[j]
    return i

def qsort(A:list[int], low:int, high:int) -> None:
    while low < high:
        pivot = partition(A, low, high)
        qsort(A, low, pivot - 1)
        low = pivot + 1

def solution(buckets:list[Bucket], availlt:int):
    events:list[int] = [b.y0 for b in buckets]
    events.extend([b.y1 for b in buckets])

    n = len(events)

    qsort(events,0, n-1)

    curr_filled = 0
    for event in events:
        b_filled, l_used = check_level(buckets, event)
        if l_used < availlt: curr_filled = b_filled
        else: break

    return curr_filled 

# ------------- Ultrafast O(nlogn) ----------------



# ------------- Testing and generators ----------------

def random_bucket(minx, maxx, miny, maxy) -> Bucket:
    x0 = randint(minx, maxx-1)
    x1 = randint(x0+1, maxx)

    y0 = randint(miny, maxy-1)
    y1 = randint(y0+1, maxy)
    
    return Bucket(x0, y0, x1, y1)

def gen_buckets(num:int) -> list[Bucket]:
    minx = miny = randint(0, 200)
    maxx = maxy = randint(0, 200)

    return [random_bucket(minx, maxx, miny, maxy) for _ in range(num)]




if __name__ == "__main__":
    n = randint(5, 10)
    buckets = gen_buckets(n)

    for liters in range(25, 1000):
        res = solution(buckets, liters)
        print(res)
