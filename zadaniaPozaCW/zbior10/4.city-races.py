"""
Zadanie 4. (wyścigi) Król Bitocji postanowił zorganizować serię 
wyścigów samochodowych. Wyścigi mają się odbywać po trasach 
zamkniętych, składających się z odcinków autostrady łączących 
miasta Bitocji. Król chce, żeby każde miasto było 
zaangażowane w dokładnie jeden wyścig. W tym celu należy 
sprawdzić, czy da się wynająć odpowiednie odcinki autostad. 
Należy jednak pamiętać o następujących ograniczeniach: 
1. w Bitocji wszystkie autostrady są jednokierunkowe, 
2. z każdego miasta wychodzą co najwyżej dwa odcinki autostrady, 
którymi można dojechać do innych miast, 
3. do każdego miasta dochodzą co najwyżej dwa odcinki autostrady, 
którymi można przyjechać z innych miast, 
Proszę zaproponować algorytm, który mając na wejściu opis sieci 
autostrad Bitocji sprawdza czy da się zorganizować serię wyścigów 
tak, żeby przez każde miasto przebiegała trasa dokładnie jednego. 
Utrudnienie: Każdy odcinek autostrady ma przedział dopuszczalnych 
cen i należy wybrać wspólną cenę dla wszystkich wynajętych odcinków.
"""


def can_race(edges:list[tuple[int,int,int,int]], n:int) -> bool:
    prices:set[int] = set()
    for _, _, a, _ in edges:
        prices.add(a)

    def possible(price:int) -> int:
        adj:list[list[int]] = [[] for _ in range(n)]
        for u, v, a, b in edges:
            if a <= price <= b:
                adj[u].append(v)
        recieved = [-1] * n
        
        def dfs(vert:int, vis:list[bool]) -> bool:
            for child in adj[vert]:
                if not vis[child]:
                    vis[child] = True
                    if recieved[child] == -1 or dfs(recieved[child], vis):
                        recieved[child] = vert
                        return True
            return False
        
        matched = 0
        for i in range(n):
            vis = [False] * n
            if dfs(i, vis):
                matched += 1
            else: break
        return matched
    
    for price in prices:
        if possible(price) == n:
            return True
    return False
            




def solution():
    # TODO: Implement algorithm logic here
    pass

if __name__ == "__main__":
    solution()
