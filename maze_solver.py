from sys import argv
def find_path(row, column, maze,health,health_list,list_path):
    combine = []
    combinations = [[row, column - 1], [row, column + 1], [row + 1, column], [row - 1, column]]
    for x, y in combinations:
        if not [x, y] in list_path:
            if not (x < 0 or y < 0 or x > len(maze) - 1 or y > len(maze[0]) - 1):
                combine += [[x, y]]
    if health > 0 :
        for x, y in combine:
                if maze[x][y] == "P" or maze[x][y] == "H" :
                    health -= 1
                    if maze[x][y] == "H" :
                        health = int(argv[3])
                    health_list.append(health)
                    list_path.append([x, y])
                    return find_path(x, y, maze,health,health_list,list_path)
                elif maze[x][y] == "F":
                    return True
    maze[list_path[-1][0]][list_path[-1][1]] = "W"
    list_path.pop()
    health_list.pop()
    health = health_list[-1]
    return find_path(list_path[-1][0], list_path[-1][1], maze,health,health_list,list_path)
def solution(arguman,health = 99999999) :
    health = int(health)
    health_list = list([health])
    with open(arguman , "r", encoding = "utf-8") as h_maze :
        maze = [[row for row in column if row != "\n"] for column in h_maze.readlines()]
        list_path = [[maze.index(i), i.index('S')] for i in maze if 'S' in i]
        row , column = list_path[0][0] , list_path[0][1]
    try :
        find_path(row,column,maze,health,health_list,list_path)
        for i in maze:
            for j in i:
                if [maze.index(i), i.index(j)] in list_path :
                    maze[maze.index(i)][i.index(j)] = "1" if j != "S" else "S"
                elif j == "W" or j == "P" or j == "H":
                    maze[maze.index(i)][i.index(j)] = "0"
            output.writelines(", ".join(i) + "\n")
        output.write("\n")
    except:
        output.write("There is no path to survive" + "\n")
with open(argv[4], "w" , encoding = "utf-8") as output :
    solution(argv[1])
    solution(argv[2],argv[3])