from collections import deque
import time

def add_orcs_area(x, y, c, area):
    for i in range(n):
        for j in range(m):
            if abs(x-i) + abs(y-j) < c + 1:
                area[i, j] = [c, 0, '']
    return area

def erase_area(area):
    add_empty_area()
    for i in orcs:
        area = add_orcs_area(i[0], i[1], i[2], area)


def add_empty_area():
    for i in range(n):
        for j in range(m):
            area[i, j] = [0, 0, '']

def search(area, curr):
    frontier = deque()
    explored = []
    frontier.append(curr)
    if(len(fellows) == len(fellows_target)):
        if len(fellows) == 0 and len(fellows_target) == 0:
            target = 3
        else:
            target = 1
    else:
        target = 2

    if check_goal(curr, target):
        return curr
    
    while(True):
        curr = frontier.popleft()
        explored.append(curr)
        temp = 0
        left = [curr[0], curr[1] - 1]
        if left[1] >= 0:
            if not left in explored and not left in frontier:
                if area[left[0], left[1]][0] != 0:
                    area[left[0], left[1]][1] = area[curr[0], curr[1]][1] + 1
                if area[left[0], left[1]][0] >= area[left[0], left[1]][1]:
                    frontier.append(left)
                    area[left[0], left[1]][2] = area[curr[0], curr[1]][2] + "L"
                if check_goal(left, target):
                    return left
        right = [curr[0], curr[1] + 1]
        if right[1] < m:
            if not right in explored and not right in frontier:
                if area[right[0], right[1]][0] != 0:
                    area[right[0], right[1]][1] = area[curr[0], curr[1]][1] + 1
                if area[right[0], right[1]][0] >= area[right[0], right[1]][1] :
                    frontier.append(right)
                    area[right[0], right[1]][2] = area[curr[0], curr[1]][2] + "R"
                if check_goal(right, target):
                    return right
        up = [curr[0] - 1, curr[1]]
        if up[0] >= 0:
            if not up in explored and not up in frontier:
                if area[up[0], up[1]][0] != 0:
                    area[up[0], up[1]][1] = area[curr[0], curr[1]][1] + 1
                if area[up[0], up[1]][0] >= area[up[0], up[1]][1]:
                    frontier.append(up)
                    area[up[0], up[1]][2] = area[curr[0], curr[1]][2] + "U"
                if check_goal(up, target):
                    return up
        down = [curr[0] + 1, curr[1]]
        if down[0] < n:
            if not down in explored and not down in frontier:
                if area[down[0], down[1]][0] != 0:
                    area[down[0], down[1]][1] = area[curr[0], curr[1]][1] + 1
                if area[down[0], down[1]][0] >= area[down[0], down[1]][1]:
                    frontier.append(down)
                    area[down[0], down[1]][2] = area[curr[0], curr[1]][2] + "D"
                if check_goal(down, target):
                    return down
        temp += len(explored)
def check_goal(curr, target):
    if target == 1:
        if curr in fellows:
            ind = fellows.index(curr)
            target_fellow.append(fellows_target[ind])
            del fellows[ind]
            return True
    elif target == 2:
        if [curr[0], curr[1]] == target_fellow[0]:
            ind = fellows_target.index(curr)
            target_fellow.clear()
            del fellows_target[ind]
            return True
    elif target == 3:
        if [curr[0], curr[1]] == end:
            return True

n, m = map(int, input().split())

area = [[0 for item in range(m)] for item in range(n)]

start = [int(item) for item in input().split()]

end = [int(item) for item in input().split()]

k, l = map(int, input().split())

area = {}

orcs = []

path = ''

add_empty_area()

for i in range(k):
    x, y, c = map(int, input().split())
    orcs.append([x, y, c])
    area = add_orcs_area(x, y, c, area)


fellows = [[int(item) for item in input().split()] for item in range(l)]

fellows_target = [[int(item) for item in input().split()] for item in range(l)]
target_fellow = []

curr = start

start_t = time.time()
while(curr != end):
    curr = search(area, curr)
    path += str(area[curr[0], curr[1]][2])
    erase_area(area)
end_t = time.time()
print(path)
print(len(path))
print(end_t - start_t)

