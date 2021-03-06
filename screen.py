from game import *


class GameScreen:
    '''Display the current state of a game in a text-based format.
    This class is fully implemented and needs no
    additional work from students.'''

    def initialize_game(self):
        '''(GameScreen) -> NoneType
        Initialize new game with new user-selected hero class
        and starting room files.'''
        self.current_room_list =[]
        hero = None
        #Get the text input and choose the hero
        while hero is None:
            text_input = input("Select hero type:\n(R)ogue (M)age (B)arbarian\n")
            text_input = text_input.lower()
            if text_input == 'r':
                hero = 'Rogue'
            elif text_input == 'm':
                hero = 'Mage'
            elif text_input == 'b':
                hero = 'Barbarian'
        #Initialize game with hero
        self.game = Game("rooms/startroom", hero)


    def play(self):
        '''(Game) -> NoneType
        The main game loop.'''
        exit = False
        while not exit:
            print(self)
            if self.game.game_over():
                break
            text_input = input("Next: ")
            if text_input in ['q', 'x']:
                print("Thanks for playing!")
                exit = True
            #Text input to control hero's movements
            elif text_input == 'w':  # UP
                self.game.move_hero(-1, 0)
            elif text_input == 's':  # DOWN
                self.game.move_hero(1, 0)
            elif text_input == 'a':  # LEFT
                self.game.move_hero(0, -1)
            elif text_input == 'd':  # RIGHT
                self.game.move_hero(0, 1)
            elif text_input == 'r':
                ## RESTART GAME
                self.initialize_game()
            else:
                pass


    def __str__(self):
        '''(GameScreen) -> String
        Return a string representing the current room.
        Include the game's Hero string representation and a
        status message from the last action taken.'''
        room = self.game.current_room
        room_string = ""
        #Render a GAME OVER screen with text mostly centered
        #In the space of the room in which the character died.
        if self.game.game_over():
            room_string = self.get_gameover_room()
        else:
            room_string = self.get_room(room_string, room)
        #Hero representation
        room_string += str(self.game.hero)
        #Last status message
        room_string += room.status
        return room_string


    def get_gameover_room(self):
        '''(GameScreen) -> String
        Return a string representing the current room
        with the words 'GAME OVER' written across the
        centre of the room'''
        string = " GAME OVER "
        for i in range(5,16):
            self.current_room_list[5][i] = string[i-5]
        return self.list_to_string()


    def get_room(self, room_string, room):
        '''(GameScreen, String, Object) -> String
        Return a string representing the current room'''
        self.current_room_list =[]
        for row in range(room.rows):
            self.current_room_list.append([])
            for column in room.grid[row]:
                self.current_room_list[row].append(column.symbol())
                if column is not None:
                    if column.visible:
                        room_string += column.symbol()
                    else:
                        #Not yet explored symbol : ?
                        room_string += "?"
            room_string += "\n"
        return room_string


    def list_to_string(self):
        '''(GameScreen, String, Object) -> String
        Process the contents of a list and return
        a string representing the current room'''
        game_string = ""
        for row in self.current_room_list:
            for column in row:
                game_string = game_string + column
            game_string += "\n"
        return game_string


#Start the game 
if __name__ == '__main__':
    game_screen = GameScreen()
    game_screen.initialize_game()
    game_screen.play()

