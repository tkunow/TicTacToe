import time
import os

VK_LEFT = 0x25
VK_UP = 0x26
VK_RIGHT = 0x27
VK_DOWN = 0x28
VK_SPACE = 0x20

class dcolors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    ENDC = '\033[0m'

class Player():
    def __init__(self, mark, color: dcolors) -> None:
        self.current_pos = 0
        self.color = color
        self.mark = mark

    def move(self, direction):
        if direction == VK_UP:
            self.current_pos = self.current_pos - 3 if self.current_pos - 3 >= 0 else self.current_pos + 6
        elif direction == VK_LEFT:
            self.current_pos = self.current_pos - 1 if self.current_pos > 0 else 8
        elif direction == VK_DOWN:
            self.current_pos = self.current_pos + 3 if self.current_pos + 3 <= 8 else self.current_pos - 6
        elif direction == VK_RIGHT:
            self.current_pos = self.current_pos + 1 if self.current_pos < 8 else 0

class Game():
    def __init__(self, player_one: Player, player_two: Player) -> None:
        self.player_one = player_one
        self.player_two = player_two
        self.current_player = self.player_one
        self.field_val = [" "," "," ",
                        " "," "," ",
                        " "," "," ",]

        self._draw_field()

    def move(self, direction) -> None:
        self.current_player.move(direction)
        self._draw_field()

    def place(self) -> None:
        if self.field_val[self.current_player.current_pos] == " ":
            self.field_val[self.current_player.current_pos] = self.current_player.mark
            self.current_player.current_pos = 0
            if self._check_win():
                self._draw_field()
                exit()
            self._switch_player()
            self._draw_field()
        else:
            self._draw_field()
            print(f"{dcolors.RED}Field has to be empty{dcolors.ENDC}")

    def _check_win(self) -> bool:
        if self.field_val[0] == self.current_player.mark and self.field_val[1] == self.current_player.mark and self.field_val[2] == self.current_player.mark:
            print(f"{dcolors.GREEN}WIN for {self.current_player.mark}{dcolors.ENDC}")
            return True
        elif self.field_val[0] == self.current_player.mark and self.field_val[3] == self.current_player.mark and self.field_val[6] == self.current_player.mark:
            print(f"{dcolors.GREEN}WIN for {self.current_player.mark}{dcolors.ENDC}")
            return True
        elif self.field_val[0] == self.current_player.mark and self.field_val[4] == self.current_player.mark and self.field_val[8] == self.current_player.mark:
            print(f"{dcolors.GREEN}WIN for {self.current_player.mark}{dcolors.ENDC}")
            return True
        elif self.field_val[1] == self.current_player.mark and self.field_val[4] == self.current_player.mark and self.field_val[7] == self.current_player.mark:
            print(f"{dcolors.GREEN}WIN for {self.current_player.mark}{dcolors.ENDC}")
            return True
        elif self.field_val[2] == self.current_player.mark and self.field_val[5] == self.current_player.mark and self.field_val[8] == self.current_player.mark:
            print(f"{dcolors.GREEN}WIN for {self.current_player.mark}{dcolors.ENDC}")
            return True
        elif self.field_val[2] == self.current_player.mark and self.field_val[4] == self.current_player.mark and self.field_val[6] == self.current_player.mark:
            print(f"{dcolors.GREEN}WIN for {self.current_player.mark}{dcolors.ENDC}")
            return True
        elif self.field_val[3] == self.current_player.mark and self.field_val[4] == self.current_player.mark and self.field_val[5] == self.current_player.mark:
            print(f"{dcolors.GREEN}WIN for {self.current_player.mark}{dcolors.ENDC}")
            return True
        elif self.field_val[6] == self.current_player.mark and self.field_val[7] == self.current_player.mark and self.field_val[8] == self.current_player.mark:
            print(f"{dcolors.GREEN}WIN for {self.current_player.mark}{dcolors.ENDC}")
            return True
        return False

    def _draw_field(self):
        col = 0

        for i, x in enumerate(self.field_val):

            if i == self.current_player.current_pos:
                if x == " ":
                    print(f"|{self.current_player.color}_{dcolors.ENDC}", end="")
                else:
                    print(f"|{self.current_player.color}{x}{dcolors.ENDC}", end="")
            else:
                print(f"|{x}", end="")

            col += 1

            if col == 3:
                print("|\n", end="")
                col = 0

    def _switch_player(self) -> None:
        self.current_player = self.player_one if self.current_player != self.player_one else self.player_two
    


def is_pressed(key):
    state =  GetKeyState(key) & 0x8000
    time.sleep(0.05)
    return state

if __name__ == "__main__":
    if os.name == 'nt':
        from ctypes import windll, c_int
        from ctypes import wintypes

        GetKeyState = windll.user32.GetKeyState
        GetKeyState.argtypes = (c_int,)
        GetKeyState.restype = wintypes.USHORT

        clear = lambda: os.system('cls')
    elif os.name == "posix":
        clear = lambda: os.system('clear')

    p_one = Player("X", dcolors.RED)
    p_two = Player("Y", dcolors.BLUE)
    game = Game(p_one, p_two)

    while True:
        try:
            if is_pressed(VK_UP):
                clear()
                game.move(VK_UP)

            if is_pressed(VK_LEFT):
                clear()
                game.move(VK_LEFT)

            if is_pressed(VK_RIGHT):
                clear()
                game.move(VK_RIGHT)

            if is_pressed(VK_DOWN):
                clear()
                game.move(VK_DOWN)

            if is_pressed(VK_SPACE):
                clear()
                game.place()

        except KeyboardInterrupt:
            break
