import numpy as np
class Board:
    def __init__(self,y,x):
        self.map = [ ['o'] * x for i in range(y) ]
        self.map = np.array(self.map)
        print(map)
    def update_position(self, old_position, amount, direction, character):
        if old_position == new_position:
            y = old_position[0]
            x = old_position[1]
            self.map[y,x] = character.tag
            return True
        if not self.collision(old_position, amount, direction):
            y = old_position[0]
            x = old_position[1]
            self.map[y,x] = 'o'
            y = new_position[0]
            x = new_position[1]
            self.map[y,x] = character.tag
            return True
        return False
    def collision(self, old, amount, direction):
        print('old')
        print(old)
        print('new')
        print(new)
        # only one dir at a time

        y = new[0] - old[0]
        x = new[1] - old[1]

        path = self.map[old[0]:new[0]+1, old[1]:new[1]+1]
        path = np.array(path)
        path = path.flatten()
        unique = set(path)
        print(unique)
        print(unique == {'o'})

        if unique == {'o'}:
            return False

        return True


# board = [
#         ['o','o','o','o'],
#         ['o','o','o','o'],
#         ['o','o','o','o'],
#         ['o','o','o','o']
#       ]
