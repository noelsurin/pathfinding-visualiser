import math
import pygame
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Pathfinding Algorith ProjectADA")


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class node:
      def __init__(self, row, col, width, total_rows):
            self.row = row
            self.col = col
            self.x = row * width
            self.y = col * width
            self.color = WHITE
            self.neighbors = []
            self.width = width
            self.total_rows = total_rows

      def get_pos(self):
            return self.row, self.col

      def is_closed(self):
            return self.color == RED

      def is_open(self):
            return self.color == GREEN

      def is_barrier(self):
            return self.color == BLACK
        
      def is_start(self):
            return self.color == ORANGE

      def is_end(self):
            return self.color == PURPLE

      def reset(self):
            self.color = WHITE

      def make_start(self):
            self.color = ORANGE

      def make_close(self):
            self.color = RED

      def make_open(self):
            self.color = GREEN

      def make_barrier(self):
            self.color = BLACK

      def make_end(self):
            self.color = TURQUOISE

      def make_path(self):
            self.color = PURPLE

      def draw(self, win):
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

      def updtade_neighbors(self, grid):
            pass

      def __lt__(self, other):
            return False

def h(p1, p2):
      x1, y1 = p1
      x2, y2 = p2
      return abs(x1-x2) + abs(y1-y2)

def make_grid(rows, width):
      grid = []
      gap = width // rows
      for i in range(rows):
            grid.append([])
            for j in range(rows):
                  spot = node(i, j, gap, rows)
                  grid[i].append(spot)

      return grid

def draw_grid(win, rows, width):
      gap = width // rows
      for i in range(rows):
            pygame.draw.line(win, GREY, (0, i*gap), (width, i*gap))
      for j in range(rows):
            pygame.draw.line(win, GREY, (j*gap, 0), (j*gap, width))

def draw(win, grid, rows, width):
      win.fill(WHITE)

      for row in grid:
            for spot in row:
                  spot.draw(win)

      draw_grid(win, rows, width)
      pygame.display.update()

def get_clicked_pos(pos, rows, width):
      gap = width // rows
      y, x = pos

      row = y // gap
      col = x // gap
      return row, col

def main(win, width):
      ROWS = 50
      grid = make_grid(ROWS, width)

      start = None
      end = None

      run = True
      started = False
      while run:
            draw(win, grid, ROWS, width)
            for event in pygame.event.get():
                  if event.type == pygame.quit:
                        run = False
                  if started:
                        continue

                  if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        row, col = get_clicked_pos(pos, ROWS, width)
                        node = grid[row][col]
                        if not start and node != end:
                              start = node
                              start.make_start()

                        elif not end and node != start:
                              end = node
                              end.make_end()

                        elif node != end and node != start:
                              node.make_barrier()
                        
                  elif pygame.mouse.get_pressed()[2]:
                        pos = pygame.mouse.get_pos()
                        row, col = get_clicked_pos(pos, ROWS, width)
                        node = grid[row][col]
                        node.reset()
                        if node == start:
                              start == None

                        elif node == end:
                              end == None

                  if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and not started:
                            pass  

      pygame.quit()

main(WIN, WIDTH)

