from heapq import heappop, heappush

def dijkstra(A, s):
    dist, anterior = {}, {}
    for v in A:
        dist[v] = float("inf")
        anterior[v] = None

    dist[s] = 0

    D = [(0, s)]

    while D:
        dist_atual, v_atual = heappop(D)

        if dist_atual > dist[v_atual]:
            continue

        for viz in A[v_atual]:
            nova_dist = dist_atual + 1

            if nova_dist < dist[viz]:
                dist[viz] = nova_dist
                anterior[viz] = v_atual
                heappush(D, (nova_dist, viz))
    return [dist, anterior]
