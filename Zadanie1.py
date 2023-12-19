import turtle as t

N = 4          #размер поля
SIZE = 200      #размер клетки
SIZEq = 200     #размер ферзя



#### Класс расчета расположения ферзей ####

class Queen:
    def __init__(self, N): # конструктор класса
        self.N = N
        self.board =[[0 for i in range(N)] for j in range(N)]
        self.find(0)

    def check(self, i, j): # функция проверки правильности расстановки
        for x in range(i):
            if self.board[x][j] == 1:
                return False
        for x,y in zip(range(i, -1, -1), range(j, -1, -1)):
            if self.board[x][y] == 1:
                return False
        for x,y in zip(range(i, -1, -1), range(j, self.N, 1)):
            if self.board[x][y] == 1:
                return False
        return True

    def find(self, col):   # функция поиска решений
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

    def read_board(self):  # чтение поля
        return self.board

############################################



####           Генерация поля           ####

def pole(x, y, SIZEp, SIZEk): # функция отрисовки поля
    t.penup()
    t.goto(x, y)
    t.pendown()

    if SIZEp % 2 == 0:
        t.fillcolor('gray')
    else:
        t.fillcolor('black')
    t.begin_fill()
    for i in range(4):
        t.forward(SIZEk)
        t.left(90)
    t.end_fill()

t.tracer(0)                   # отрисовка поля
for i in range(N):
    for j in range(N):
        pole((i - N/2)*SIZE, (j - N/2)*SIZE, i + j, SIZE)

############################################



####           Генерация ферзя          ####

def queen(x,y, SIZEf):         # функция отрисовки ферзя
    circle = SIZEf / 20
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor('orange')
    t.begin_fill()

    for i in range(0, 2):      # отриовка основания ферзя
        t.forward(SIZEf)
        t.right(90)
        t.forward(SIZEf / 4)
        t.right(90)
    t.left(90)
    t.forward(SIZEf)

    lenght = ((SIZEf / 2) ** 2 + (SIZEf / 4) ** 2) ** (1 / 2)  # длинна 'шипа' короны ферзя
    angle = 63.5                                               # угол 'шипа' короны ферзя

    # отрисовка короны ферзя

    t.circle(circle)
    t.right(angle + 90)
    count = 1
    for i in range(0,4):
        t.forward(lenght)
        if count % 2 == 0:
            t.circle(circle)
            t.right(angle * 2)
            count += 1
        else:
            t.left(angle * 2)
            count += 1
    t.right((angle*6) + 5.5)
    t.forward(SIZEf)
    t.end_fill()

############################################




board = Queen(N)
queens = board.read_board()
for i in range(N):
    for j in range(N):
        if queens[i][j]>0:
            queen((i - N/2)*SIZE + 0.25 * SIZE, (j - N/2)*SIZE + 0.2*SIZE, 0.5*SIZE)
            t.setheading(0)
t.update()
t.mainloop()
