"""
 Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right

There are three solutions given below, one for whether we can find a path, one which gives us a path with recursive method, another with tabular method for number of paths.
"""

def canTravel_robot_in_a_gridRecursive(grid, blocked, hashmap = {}):
    # print('exploring from grid: ', grid)
    # given the grid dimensions, you need to get to origin, can only go up or left.

    if grid in hashmap:
        return hashmap[grid]
    if grid == (0,0):
        return True

    # print(grid)
    if (grid[0] < 0) or (grid[1] < 0):
        return False

    for direction in ["left","up"]:
        if direction == "left":
            next_pos = (grid[0], grid[1] - 1)
            # print('left, next pos is :',next_pos)
            if next_pos not in blocked:
                result = canTravel_robot_in_a_gridRecursive(next_pos, blocked)
                hashmap[grid] = result
                return result            
        else:
            next_pos = (grid[0] - 1, grid[1])
            # print('up, next pos is :',next_pos)
            if next_pos not in blocked:
                result = canTravel_robot_in_a_gridRecursive(next_pos, blocked)
                hashmap[grid] = result
                return result

    return False


def getPath_robot_in_a_gridRecursive(grid, blocked):
    # print('exploring from grid: ', grid)
    # given the grid dimensions, you need to get to origin, can only go up or left.

    if grid == (0,0):
        return []

    # print(grid)
    if (grid[0] < 0) or (grid[1] < 0):
        return None

    for direction in ["left","up"]:
        # print('direction is ', direction)
        if direction == "left":
            next_pos = (grid[0], grid[1] - 1)
            # print('left, next pos is :',next_pos)
            if next_pos not in blocked:
                result = getPath_robot_in_a_gridRecursive(next_pos, blocked)
                # print('top result', result)
                if result != None:
                    result.append(grid)
                return result            
        else:
            next_pos = (grid[0] - 1, grid[1])
            # print('up, next pos is :',next_pos)
            if next_pos not in blocked:
                
                result = getPath_robot_in_a_gridRecursive(next_pos, blocked)
                # print('bot result', result)
                if result != None:
                    result.append(grid)
                return result

    return None
import copy
def countPath_robot_in_a_gridTabluar(grid, blocked):
    # print('exploring from grid: ', grid)
    # given the grid dimensions, you need to get to origin, can only go up or left.
    table = []

    for i in range(grid[0]+1):
        table.append([])
        for j in range(grid[1]+1):
            table[i].append(0)
    
    table[grid[0]][grid[1]] = 1
    print(table)
    
    for row in range(grid[0],-1,-1):
        for column in range(grid[1],-1,-1):
            if row-1 >= 0:
                print('in first')
                if (row-1, column) not in blocked:
                    
                    table[row-1][column] += table[row][column]
            
            if column-1 >= 0:
                print('in second')
                if (row, column-1) not in blocked:
                    
                    table[row][column-1] += table[row][column]
    return table

def getPath_robot_in_a_gridTabluar(grid, blocked):
    # print('exploring from grid: ', grid)
    # given the grid dimensions, you need to get to origin, can only go up or left.
    table = []

    for i in range(grid[0]+1):
        table.append([])
        for j in range(grid[1]+1):
            table[i].append(0)
    
    table[grid[0]][grid[1]] = 1
    print(table)
    path = []
    for row in range(grid[0],-1,-1):
        for column in range(grid[1],-1,-1):
            if row-1 >= 0:
                print('in first')
                if (row-1, column) not in blocked:
                    
                    table[row-1][column] += table[row][column]

            if column-1 >= 0:
                print('in second')
                if (row, column-1) not in blocked:
                    
                    table[row][column-1] += table[row][column]
    print(table)

grid = (3,3)
# grid = (2,4)
blocked = [(0,3),(2,2),(3,1),(3,2)]

# print(canTravel_robot_in_a_gridRecursive(grid, blocked))
# print(getPath_robot_in_a_gridRecursive(grid, blocked))
print(countPath_robot_in_a_gridTabluar(grid, blocked))