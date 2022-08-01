class Solution:
    def isPathCrossing(self, path: str):
        path_list = [[0, 0]]
        x = 0
        y = 0
        for vector in path:
                if vector == 'N':
                    y += 1
                    z = path_list.append([x, y])
                elif vector == 'S':
                    y -= 1
                    z = path_list.append([x, y])
                elif vector == 'E':
                    x += 1
                    z = path_list.append([x, y])
                else:
                    x -= 1
                    z = path_list.append([x, y])
        path_list = list(map(str, path_list))
        path_list_1 = set(path_list)
        print(path_list)
        print(path_list_1)
        if len(path_list) != len(path_list_1):
            return True
        else:
            return False