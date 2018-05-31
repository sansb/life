from curses import wrapper
from time import sleep

# TODO: Accept initial game state as input with some fallback defaults
BOARD_SIZE = 25
INITIAL_GAME_STATE = [[0 for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
INITIAL_GAME_STATE[9][12] = 1
INITIAL_GAME_STATE[10][9] = 1
INITIAL_GAME_STATE[10][10] = 1
INITIAL_GAME_STATE[11][11] = 1
INITIAL_GAME_STATE[12][12] = 1

def render(stdscr, game_state):
  # TODO: Can we make the rendering more "square"?
  #       Terminal character width is much less than line height,
  #       so our game state always looks long. Can we make it more square?
  stdscr.clear()
  for i in range(len(game_state)):
    for j in range(len(game_state[i])):
      if game_state[i][j] == 1:
        char = '*'
      else:
        char = ' '
      stdscr.addstr(i, j, '{}'.format(char))
  stdscr.refresh()

def update_game_state(game_state):
  new_game_state = []
  for i in range(len(game_state)):
    new_game_state.append([])
    for j in range(len(game_state)):
      num_neighbors = 0
      for m in [-1, 0, 1]:
        for n in [-1, 0, 1]:
          # TODO: make this wrap
          if i+m >= len(game_state) or j+n >= len(game_state[i]):
            continue
          if game_state[i+m][j+n] == 1:
            num_neighbors += 1
      if game_state[i][j] == 1 and num_neighbors in [2,3]:
        new_cell = 1
      elif game_state[i][j] == 0 and num_neighbors in [3]:
        new_cell = 1
      else:
        new_cell = 0
      new_game_state[i].append(new_cell)
  return new_game_state

def main(stdscr):
  stdscr.clear()
  game_state = INITIAL_GAME_STATE
  while True:
    render(stdscr, game_state)
    game_state = update_game_state(game_state)
    sleep(0.5) # Savor the moment

if __name__ == '__main__':
  wrapper(main)
