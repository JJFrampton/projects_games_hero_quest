from Characters.Players.Player import Player
class Elf(Player):
    def __init__(self, name, position, board):
        self.stats_attack = 2
        self.stats_defend = 2
        self.stats_body = 6
        self.stats_mind = 4
        self.stats_move = 2
        self.stats_weapon = "shortsword"
        self.stats_armour = None
        self.stats_name = name
        self.tag = name[:1]
        self.position = position
        self.board = board
        self.board.update_position(position, position, self)
        # board.update_position(position, [1,2], self)
        print("initialized")

