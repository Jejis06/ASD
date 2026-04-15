
#Graph

#      4
#     /  \
#    1    5 _
#     \  /    \
#     2 - 3 - 6

# Vert-list
G_v = [(1, 2), (2, 3), (3, 6), (5, 6), (5, 3) ,(5, 4), (1, 4)]

# Conn-matrix 
n = 6
G_c = [[0 for _ in range(n)] for _ in range(n)]

G_c[1][2] = True
G_c[2][3] = True
G_c[3][6] = True
G_c[5][6] = True
G_c[5][3] = True
G_c[5][4] = True
G_c[1][4] = True

# Nei-list
G_n:list[list[int]] = [[] for _ in range(n)]

G_n[1].append(2)
G_n[2].append(3)
G_n[3].append(6)
G_n[5].append(6)
G_n[5].append(3)
G_n[5].append(4)
G_n[1].append(4)

