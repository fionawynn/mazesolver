from cell import Cell
import random
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        self.break_entrance_and_exit()
        self.break_walls(0, 0)
        self.reset_cells_visted()

        if seed:
            random.seed(seed)
    
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self._cells.append(col_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def break_entrance_and_exit(self):
        self._cells[0][0].t_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].b_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
    
    def break_walls(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].r_wall = False
                self._cells[i + 1][j].l_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].l_wall = False
                self._cells[i - 1][j].r_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].b_wall = False
                self._cells[i][j + 1].t_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].t_wall = False
                self._cells[i][j - 1].b_wall = False

            # recursively visit the next cell
            self.break_walls(next_index[0], next_index[1])
            
    def reset_cells_visted(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self.solve_r(0, 0)
    
    def solve_r(self, i, j):
        self._animate()
        this_cell = self._cells[i][j]
        this_cell.visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        if (
            i > 0
            and not self._cells[i][j].l_wall
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self.solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        
        if (
            i < self.num_cols - 1
            and not self._cells[i][j].r_wall
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self.solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        if (
            j > 0
            and not self._cells[i][j].t_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self.solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        if (
            j < self.num_rows - 1
            and not self._cells[i][j].b_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self.solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False

