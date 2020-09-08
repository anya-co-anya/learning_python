#  Как поняла, нужно было сделать картинку доски, чтоб кликом мышки ставить коня. Но я не знаю как ((

from PyQt5 import QtWidgets
from design import Ui_MainWindow
import sys


class Board:
    BOARD = (('a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'),
             ('a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'),
             ('a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'),
             ('a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'),
             ('a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'),
             ('a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'),
             ('a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'),
             ('a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'))

    @classmethod
    def get_coords_by_name(cls, name: str) -> tuple:  # turn chess position to prg. coords (x, y)
        a = None
        b = None
        for line in Board.BOARD:
            for i in line:
                if name == i:
                    a = line
                    b = i
                    break
        if a and b:
            return (Board.BOARD.index(a), a.index(b))
        else:
            raise ValueError('Ivalid input')

    @classmethod
    def get_name_by_coords(self, coords: tuple) -> str:  # turn prg. coords to chess position
        return Board.BOARD[coords[0]][coords[1]]


class Knight:
    ALL_MOVES = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))  # how knight can move

    def __init__(self, start_position: str, target_position: str):
        self.__shortest_way = []
        self.start_position = Board.get_coords_by_name(start_position)
        self.target_position = Board.get_coords_by_name(target_position)

    @property
    def shortest_way(self):  # store shortest way to be returned
        ret = []
        for i in self.__shortest_way:
            ret.append(Board.get_name_by_coords(i).capitalize())
        return ' -- '.join(ret)


    def get_possible_moves(self, position: tuple) -> list: # sublist of ALL_MOVES - how knight can move from current pos.
        ret = []
        try:                     #  не знаю даже почему, но без трай-эксепт валилось
            for move in Knight.ALL_MOVES:
                if 0 <= position[0] + move[0] < 8 and 0 <= position[1] + move[1] < 8:
                    ret.append((move[0], move[1]))
        except:
            print(position)
        return ret


    def way_to_finish(self, start: tuple, visited_positions=[]):   #  так и не получилось сделать, чтоб ретурнила
        finish = self.target_position
        if len(self.__shortest_way) != 0 and len(visited_positions) >= len(self.__shortest_way):
            return

        if len(visited_positions) == 0:
            visited_positions.append(start)
        moves_to_do = self.get_possible_moves(start)

        for move in moves_to_do:
            if (start[0] + move[0], start[1] + move[1]) in visited_positions:  # skip visited positions
                continue
            current = (start[0] + move[0], start[1] + move[1])
            new_visited_positions = visited_positions + [current]

            if current == finish:
                if len(self.__shortest_way) == 0 or len(new_visited_positions) < len(self.__shortest_way):
                    self.__shortest_way = new_visited_positions
                    # print(f'shortest current: {self.__shortest_way}')  # для проверки
            else:
                self.way_to_finish(current, new_visited_positions)


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_clicks()

    @property
    def input_start_pos(self):
        return self.ui.lineEdit.text().strip().lower()

    @property
    def input_finish_pos(self):
        return self.ui.lineEdit_2.text().strip().lower()


    def connect_clicks(self):
        self.ui.pushButton.clicked.connect(self.button_click_calculate)

    def button_click_calculate(self):  #  a kind of main function
        try:
            knight = Knight(self.input_start_pos, self.input_finish_pos)
            knight.way_to_finish(knight.start_position)
            result = str(knight.shortest_way)
        except ValueError:
            self.ui.label_4.setText('Please enter position in format: a1')
        else:
            self.ui.label_4.setText(result)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())


