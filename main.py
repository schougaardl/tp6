"""
jeux de roche papier sciseaux
"""
import random

import arcade
import arcade.color

from game_state import GameState


WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Starting Template"



class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.AMAZON

        self.ord_sprite = arcade.Sprite("assets/compy.png", scale=2.3)
        self.ord_sprite.position = (900, 400)

        self.paper_sprite = arcade.Sprite("assets/spaper.png", scale=0.5)
        self.paper_sprite.position = (345, 170)

        self.rock_sprite = arcade.Sprite("assets/srock.png", scale=0.5)
        self.rock_sprite.position = (190, 170)

        self.scissor_sprite = arcade.Sprite( "assets/scissors.png", scale= 0.5)
        self.scissor_sprite.position = (520, 170)

        self.player_sprite = arcade.Sprite("assets/faceBeard.png", scale=0.5)
        self.player_sprite.position = (350, 400)

        self.paper_sprite_list = arcade.SpriteList()
        self.rock_sprite_list = arcade.SpriteList()
        self.players_sprites = arcade.SpriteList()
        self.scissor_sprite_list = arcade.SpriteList()

        self.paper_sprite_list.append(self.paper_sprite)
        self.rock_sprite_list.append(self.rock_sprite)
        self.scissor_sprite_list.append(self.scissor_sprite)
        self.players_sprites.append(self.player_sprite)
        self.players_sprites.append(self.ord_sprite)

        self.game_state = GameState.NOT_STARTED
        self.choix = ""
        self.choix_ord = ""
        self.choix_list = ["roche","papier","sciseau"]

    def reset(self):
        """Reset the game to the initial state."""
        # Do changes needed to restart the game here if you want to support that
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        arcade.draw_text("Roche Papier Ciseaux", 340, 600, arcade.color.WHITE, 60)
        if self.game_state == GameState.NOT_STARTED :
            arcade.draw_text("apuiyer sur espace pour commencer", 200, 400,arcade.color.WHITE,50)
        elif self.game_state == GameState.ROUND_ACTIVE :
            arcade.draw_text("Roche          Papier           Ciseaux", 140, 100, arcade.color.WHITE, 25)
            self.players_sprites.draw()
            self.scissor_sprite_list.draw()
            self.rock_sprite_list.draw()
            self.paper_sprite_list.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        if self.game_state != GameState.ROUND_ACTIVE:
            return

        if self.choix == "":
            return

        self.choix_ord = random.choice(self.choix_list)
        print(self.choix_ord)

        if self.choix == self.choix_ord:
            print("nulle")

        # si déterminé gagnant, passer en ROUND_DONE
        self.game_state = GameState.ROUND_DONE

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if key == arcade.key.SPACE:
            if self.game_state == GameState.NOT_STARTED:
                self.game_state = GameState.ROUND_ACTIVE
            if self.game_state == GameState.ROUND_DONE:
                self.game_state = GameState.ROUND_ACTIVE
                self.choix = ""
                self.choix_ord = ""


    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        if self.game_state != GameState.ROUND_ACTIVE:
            return


        if self.rock_sprite.collides_with_point((x, y)):
            self.choix = "roche"
            print((self.choix))
        elif self.paper_sprite.collides_with_point((x, y)):
            self.choix = "Papier"
            print((self.choix))
        elif self.scissor_sprite.collides_with_point((x, y)):
            self.choix = "sciseau"
            print((self.choix))





def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()



if __name__ == "__main__":
    main()