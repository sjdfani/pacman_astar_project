from queue import PriorityQueue
from heuristic import ManhattanDistance

path_list = []


def traverse_back(came_from, end_index, start_position):
    if came_from[end_index] != start_position:
        path_list.append(came_from[end_index])
        traverse_back(came_from, came_from[end_index], start_position)
    else:
        return path_list.reverse()


def aStar(graph, start_index, end_index, x_y_start, x_y_end) -> dict:
    queue = PriorityQueue()
    queue.put((0, start_index))
    cost_so_far = {}
    came_from = {}
    cost_so_far[start_index] = 0

    while not queue.empty():
        current = queue.get()[1]

        if current == end_index:
            break

        for next in graph[current]:
            x_y_current = (current // 10, current % 10)
            x_y_neighbor = (next // 10, next % 10)
            new_cost = (
                cost_so_far[current] +
                ManhattanDistance(x_y_current, x_y_neighbor)
            )

            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + ManhattanDistance(x_y_neighbor, x_y_end)

                queue.put((priority, next))
                came_from[next] = current

    return came_from
