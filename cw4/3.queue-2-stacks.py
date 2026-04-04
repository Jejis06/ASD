"""
3. Kolejka na 2 stosach

"""

class Stos:
    def __init__(self):
        self.vals:list[int] = [0]
        self.size:int = 0
    def push(self, val:int) -> bool:
        if self.size > len(self.vals) - 1:
            temp = [0 for _ in range(self.size+1)]
            self.vals.extend(temp)
        self.vals[self.size] = val
        self.size += 1

        return True 
    def pop(self) -> int:
        if self.size <= 0:
            raise Exception("stack is empty")
        self.size -= 1
        return self.vals[self.size]
    def __str__(self):
        return f"Stack:{self.vals}, size:{self.size}"

class queue_s1:
    def __init__(self):
        self.s1: Stos = Stos()
        self.s2: Stos = Stos()

    def size(self) -> int:
        return self.s1.size + self.s2.size

    def push(self, val:int):
        _ = self.s1.push(val)

    def pop(self) -> int:
        if self.s2.size == 0:
            while self.s1.size > 0:
                x = self.s1.pop()
                _ = self.s2.push(x) 
        if self.s2.size == 0:
            raise Exception("Queue is empty")
        return self.s2.pop()

    def __str__(self):
        return f"S1 (in) {self.s1}\n S2 (out) {self.s2}"



def solution():
    kolejka = queue_s1()
    for i in range(10):
        kolejka.push(i)
    print(kolejka)
    print(kolejka.size())
    for i in range(10):
        x = kolejka.pop()
        print(x)

    print(kolejka)
    print(kolejka.size())
    y = kolejka.pop()

if __name__ == "__main__":
    solution()
        
