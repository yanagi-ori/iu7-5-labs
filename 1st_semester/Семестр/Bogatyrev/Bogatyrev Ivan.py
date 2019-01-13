# Богатырев Иван
# Нумерация пути

# Важно! Вводные данные считываются из файла input.txt!
with open('input.txt', 'r') as f:
    numbers = [int(i) for i in f.read().split()]

cities = []
while len(numbers) > 0:
    pairs = []
    max_point = -1
    for i in range(numbers.pop(0)):
        j = numbers.pop(0)
        k = numbers.pop(0)
        max_point = max(j, k, max_point)
        pairs.append((j, k))
    cities.append({
        'points': max_point + 1,
        'pairs': pairs
    })

for index, city in enumerate(cities):
    n = city['points']
    graph = [set() for i in range(n)]
    for i, j in city['pairs']:
        graph[i].add(j)
    matrix = [[0] * n for i in range(n)]
    for start in range(n):
        queue = [{
            'node': start,
            'prev': None
        }]

        while queue:
            v_from = queue.pop(0)
            if matrix[start][v_from['node']] == -1:
                continue
            p = v_from['prev']
            while p is not None:
                if matrix[start][p['node']] == -1 or p['node'] == v_from['node']:
                    matrix[start][v_from['node']] = -1
                    break
                p = p['prev']
            for v_to in graph[v_from['node']]:
                if matrix[start][v_to] != -1:
                    matrix[start][v_to] += 1
                queue.append({
                    'node': v_to,
                    'prev': v_from
                })

    print('matrix for city', index)
    for row in matrix:
        print(*row)
