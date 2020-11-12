from tabulate import tabulate

counter = 0
def updateCounter():
    global counter
    counter += 1


def create_table(n,c):
    table = []
    row = []
    for i in range(0,n + 1):
        for x in range(0,c + 1):
           row.append(-1)
        table.append(row)
        row = []
    for i in range(0,n + 1):
        table[i][0] = 0
    for i in  range(0,c + 1):
        table[0][i] = 0
    return table

def print_table(table):
    print(tabulate(table, headers=["c=" + str(x) for x in range(0,len(table[0]))], tablefmt='orgtbl'))


table = []

def main():
    global table
    global counter
    v = [5,12,8,2,7,9,1,6]
    w = [4,10,5,4,1,2,7,2]
    n = len(v)
    c = 10
    ndc = 0
    dc = 0
    table = create_table(n,c)
    # print_table(table)
    ksp(n,c,v,w)
    print("Non-Dynamic Operations: " + str(counter))
    ndc = counter
    counter = 0
    dyn = ksp_dp(n,c, v, w)
    print("Dynamic Operations: " + str(counter))
    dc = counter
    print(" ")
    print_table(table)
    bestItems = findBestItems(table,w,v)
    print(" ")
    print("Items that maximize value: " + str(bestItems) + ". Providing a value of " + str(dyn) + ".")
    print(f"The Dynamic Programming implementation performed {str(round(ndc/dc, 2))}x faster in this instance.")
    # print(counter)

def ksp(n,c, v, w):
    # print(1)
    updateCounter()
    if n == 0 or c == 0:
        return 0
    if w[n-1] > c:
        return ksp(n-1, c, v, w)
    else:
        return max(v[n-1] + ksp(n-1, c-w[n-1], v,w), ksp(n-1,c,v,w))

def findBestItems(table, weights):
    n = len(table) - 1
    c = len((table[0])) - 1
    bestItems = []
    while c > 0 and n > 0:
        # print("n=" + str(n))
        # print(c)
        if table[n][c] == table[n-1][c]:
            # print("here")
            n -= 1
        else:
            bestItems.append(n)
            n -= 1
            c -= weights[n]
    return bestItems


def ksp_dp(n,c,v,w):
    updateCounter()
    if n == 0 or c == 0:
        return 0
    if table[n][c] != -1:
        return table[n][c]
    if w[n-1] > c:
        result = ksp_dp(n-1, c, v, w)
    else:
        result = max(v[n-1] + ksp_dp(n-1, c-w[n-1], v,w), ksp_dp(n-1,c,v,w))
    table[n][c] = result
    return table[n][c]


main()
