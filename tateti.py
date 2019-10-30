class TaTeTi():

    def __init__(self, board=None):
        self.board = board
        if self.board is None:
            self.board = [' ' for _ in range(9)]

    def full(self):
        for x in range(9):
            if ' ' in self.board[x]:
                return False
        return True

    def validate(self, position):
        if self.board[position - 1] == ' ':
            return True
        else:
            return False

    def assign(self, position, piece):
        if self.validate(position) is False:
            raise Exception
        else:
            self.board[position - 1] = piece

    def draw_board(self):
        Draw = '\n '
        for i in range(9):
            if self.board[i] == ' ':
                Draw += str(i + 1)
            else:
                Draw += self.board[i]
            if i != 8:
                if (i + 1) % 3 == 0:
                    Draw += ' \n---+---+---\n '
                else:
                    Draw += ' | '
        Draw += ' \n'
        return Draw

    def check_row(self):
        if self.board[0] == 'x' and self.board[1] == 'x' and self.board[2] == 'x':
            return True
        if self.board[3] == 'x' and self.board[4] == 'x' and self.board[5] == 'x':
            return True
        if self.board[6] == 'x' and self.board[7] == 'x' and self.board[8] == 'x':
            return True
        if self.board[0] == 'o' and self.board[1] == 'o' and self.board[2] == 'o':
            return True
        if self.board[3] == 'o' and self.board[4] == 'o' and self.board[5] == 'o':
            return True
        if self.board[6] == 'o' and self.board[7] == 'o' and self.board[8] == 'o':
            return True
        else:
            return False

    def check_diag(self):
        if self.board[0] == 'x' and self.board[4] == 'x' and self.board[8] == 'x':
            return True
        if self.board[0] == 'o' and self.board[4] == 'o' and self.board[8] == 'o':
            return True
        if self.board[2] == 'x' and self.board[4] == 'x' and self.board[6] == 'x':
            return True
        if self.board[2] == 'o' and self.board[4] == 'o' and self.board[6] == 'o':
            return True
        else:
            return False

    def check_column(self):
        if self.board[0] == 'x' and self.board[3] == 'x' and self.board[6] == 'x':
            return True
        if self.board[0] == 'o' and self.board[3] == 'o' and self.board[6] == 'o':
            return True
        if self.board[1] == 'x' and self.board[4] == 'x' and self.board[7] == 'x':
            return True
        if self.board[1] == 'o' and self.board[4] == 'o' and self.board[7] == 'o':
            return True
        if self.board[2] == 'x' and self.board[5] == 'x' and self.board[8] == 'x':
            return True
        if self.board[2] == 'o' and self.board[5] == 'o' and self.board[8] == 'o':
            return True
        else:
            return False

    def win(self):
        if self.check_row() or self.check_column() or self.check_diag():
            return True
        else:
            return False
