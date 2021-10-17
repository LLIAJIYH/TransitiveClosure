# Python 3.9.7


def transitiveСlosure(graph):
    result = [[graph[i][j] for j in range(len(graph))] for i in range(len(graph))]

    # фиксация k строки и столбца, где k = from 1 to n, где n=|graph|
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                # result[i][j] = max(result[i,j], result[i,k]*result[k,j])
                result[i][j] = result[i][j] or (result[i][k] and result[k][j])
    return result


graph = [
[0,1,0,0,1,0,0,0,0,0,0,0],
[1,0,1,0,0,1,0,0,0,0,0,0],
[0,1,0,1,0,0,1,0,0,0,0,0],
[0,0,1,0,0,0,0,1,0,0,0,0],
[1,0,0,0,0,1,0,0,1,0,0,0],
[0,1,0,0,1,0,1,0,0,1,0,0],
[0,0,1,0,0,1,0,1,0,0,1,0],
[0,0,0,1,0,0,1,0,0,0,0,1],
[0,0,0,0,1,0,0,0,0,1,0,0],
[0,0,0,0,0,1,0,0,1,0,1,0],
[0,0,0,0,0,0,1,0,0,1,0,1],
[0,0,0,0,0,0,0,1,0,0,1,0],
]

result = transitiveСlosure(graph)
for i in result:
    for j in i:
        print(j, end=" ")
    print("")
