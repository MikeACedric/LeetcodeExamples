# 1266. Minimum Time Visiting All Points
# Difficulty: Easy

# On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

arr = [[1,1],[3,4],[-1,0]]

# def manhattan_distance(p1, p2):
#     return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def minTimeToVisitAllPoints(points):
    time = 0
    current_point = points[0]
    for i in range(1, len(points)):
        x_diff = abs(points[i][0] - current_point[0])
        y_diff = abs(points[i][1] - current_point[1])
        time += max(x_diff, y_diff)
        current_point = points[i]
    return time

print("Minimum time to visit all points:", minTimeToVisitAllPoints(arr)) #7