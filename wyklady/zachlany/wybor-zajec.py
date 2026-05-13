'''

[ O(nlogn) ]
'''
def pick_classes(terms:list[tuple[int,int]]) -> list[tuple[int, int]]:
    terms = sorted(terms, key = lambda x: x[1])
    n = len(terms)

    picks:list[tuple[int,int]] = [terms[0]]
    curr_end:int = terms[0][1]

    for i in range(1, n):
        if terms[i][0] >= curr_end:
            picks.append(terms[i])
            curr_end = terms[i][1]

    return picks 


