from math import sqrt, pow


def EuclideanDistance(start_position, target_position):
    distance_x = target_position[0]-start_position[0]
    distance_y = target_position[1]-start_position[1]
    return sqrt(pow((distance_x), 2)+pow((distance_y), 2))


def ManhattanDistance(start_position, target_position):
    distance_x = target_position[0]-start_position[0]
    distance_y = target_position[1]-start_position[1]
    return abs(distance_x/24)+abs(distance_y/24)
