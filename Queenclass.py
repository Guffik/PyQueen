class Queen:
    def __init__(self, N): #конструктор класса
        self.N = N
        self.board =[[0 for i in range(N)] for j in range(N)]
        self.find(0)

    def check(self, i, j):
        for x in range(i):
            if self.board[x][j] == 1:
                return False
        for x,y in zip(range(i, -1, -1), range(j, -1, -1)):
            if self.board[x][y] == 1:
                return False
        for x,y in zip(range(i, -1, -1), range(j, self.N, -1)):
            if self.board[x][y] == 1:
                return False
        return True


    def find(self, col):
        if col >= self.N:
            for q in self.board:
                print(q)
            print()
            return True
        for i in range(self.N):
            if self.check(col, i):
                self.board[col][i] = 1
                if self.find(col + 1):
                    return True
                self.board[col][i] = 0
            return False


    def read_board(self):
        return self.board