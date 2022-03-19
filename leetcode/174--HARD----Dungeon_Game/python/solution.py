# ---------------------------------------------------------------------------------------
#
#  Title:       Dungeon Game
#
#  Link:        https://leetcode.com/problems/dungeon-game/
#
#  Difficulty:  Hard
#
#  Language:    Python
#
# ---------------------------------------------------------------------------------------

class Dungeon(object):
    def __init__(self):
        self.best_hp = 8000000001

    def calculateMinimumHP(self, dungeon):
        self.process(dungeon, 0, 0, 0, 0)
        return self.best_hp+1

    def process(self, dungeon, r, c, hp, abs):
        hp = hp + dungeon[r][c]
        if hp < abs:
            abs = hp
        if c < len(dungeon[0]) - 1:
            self.process(dungeon, r, c+1, hp, abs)
        if r < len(dungeon) - 1:
            self.process(dungeon, r+1, c, hp, abs)
        if c==len(dungeon[0])-1 and r==len(dungeon)-1:
            if abs < 0:
                abs = abs * -1
            if abs < self.best_hp:
                self.best_hp = abs


z = Dungeon()
print( z.calculateMinimumHP([[-2,-3,3,2],[-5,-10,1,5],[10,30,-5,-1]]) )
