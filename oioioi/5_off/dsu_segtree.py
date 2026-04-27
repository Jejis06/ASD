import sys
import bisect

def solve():
    data = sys.stdin.read().split()
    iterator = iter(data)

    n = int(next(iterator))
    m = int(next(iterator))
    q = int(next(iterator))
    d = int(next(iterator))

    edges = []
    unique_w_set = set()
    for _ in range(m):
        a = int(next(iterator))
        b = int(next(iterator))
        c = int(next(iterator))
        edges.append((a, b, c))
        unique_w_set.add(c)

    queries = []
    for i in range(q):
        u = int(next(iterator))
        v = int(next(iterator))
        queries.append((u, v, i))

    unique_w = sorted(list(unique_w_set))
    T = len(unique_w)

    if T == 0:
        for _ in range(q):
            print("NIE")
        return

    size = 1
    while size < T:
        size *= 2

    tree = [[] for _ in range(2 * size)]

    for u, v, w in edges:
        start_t = bisect.bisect_left(unique_w, w - d)
        end_t = bisect.bisect_right(unique_w, w) - 1
        
        if start_t <= end_t:
            ql = start_t + size
            qr = end_t + size
            while ql <= qr:
                if ql % 2 == 1:
                    tree[ql].append((u, v))
                    ql += 1
                if qr % 2 == 0:
                    tree[qr].append((u, v))
                    qr -= 1
                ql //= 2
                qr //= 2

    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    history = []

    def find(x: int) -> int:
        while x != parent[x]:
            x = parent[x]
        return x

    def onion(x: int, y: int):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return
        if rank[rx] > rank[ry]:
            rx, ry = ry, rx
            
        history.append((rx, ry, rank[ry]))
        parent[rx] = ry
        if rank[rx] == rank[ry]:
            rank[ry] += 1

    def rollback(target_size: int):
        while len(history) > target_size:
            rx, ry, old_rank_ry = history.pop()
            parent[rx] = rx
            rank[ry] = old_rank_ry

    ans = ["NIE"] * q
    active_queries = set(range(q))

    def dfs(node: int):
        if not active_queries:
            return

        history_size = len(history)
        
        for u, v in tree[node]:
            onion(u, v)

        if node >= size:
            t = node - size
            if t < T:
                to_remove = []
                for q_idx in active_queries:
                    qu, qv, _ = queries[q_idx]
                    if find(qu) == find(qv):
                        ans[q_idx] = "TAK"
                        to_remove.append(q_idx)
                for q_idx in to_remove:
                    active_queries.remove(q_idx)
        else:
            dfs(2 * node)
            dfs(2 * node + 1)

        rollback(history_size)

    dfs(1)

    for res in ans:
        print(res)

if __name__ == '__main__':
    solve()
