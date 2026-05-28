"""
Lars Schougaard 406
jeux de roche papier ciseaux
"""

import random

import arcade
import arcade.color

from game_state import GameState
from attack_animation import AttackType, AttackAnimation

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Jeu: Roche Papier Ciseaux"


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
        self.ord_sprite.position = (950, 400)

        self.paper_sprite = AttackAnimation(AttackType.PAPER)
        self.paper_sprite.position = (345, 170)

        self.rock_sprite = AttackAnimation(AttackType.ROCK)
        self.rock_sprite.position = (190, 170)

        self.scissor_sprite = AttackAnimation(AttackType.SCISSORS)
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
        self.choix_list = [AttackType.ROCK, AttackType.SCISSORS, AttackType.PAPER]
        self.resultat = " "

        self.score_J = 0
        self.score_O = 0

    def change_position(self):
        self.paper_sprite.position = (950, 170)
        self.rock_sprite.position = (950, 170)
        self.scissor_sprite.position = (950, 170)

    def return_position(self):
        self.paper_sprite.position = (345, 170)
        self.rock_sprite.position = (190, 170)
        self.scissor_sprite.position = (520, 170)

    def reset(self):
        """Reset the game to the initial state."""
        # Do changes needed to restart the game here if you want to support that
        self.game_state = GameState.NOT_STARTED
        self.choix = ""
        self.choix_ord = ""
        self.resultat = " "
        self.score_J = 0
        self.score_O = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        arcade.draw_text("Roche Papier Ciseaux", 0, 650, arcade.color.WHITE, 60, align="center", width=WINDOW_WIDTH)

        if self.game_state == GameState.NOT_STARTED:
            arcade.draw_text("appuyer sur espace pour commencer", 0, 400, arcade.color.WHITE, 50, align="center", width=WINDOW_WIDTH)

        elif self.game_state == GameState.GAME_OVER:

            arcade.draw_text("Appuyer sur espace pour recommencer", 0, 300, arcade.color.WHITE, 50, align="center",
                             width=WINDOW_WIDTH)

            if self.score_J > self.score_O:
                arcade.draw_text("Vous avez gagné!", 0, 400, arcade.color.WHITE, 50, align="center", width=WINDOW_WIDTH)

            else:
                arcade.draw_text("Vous avez perdu!", 0, 400, arcade.color.WHITE, 50, align="center", width=WINDOW_WIDTH)
        else:
            arcade.draw_text("Roche          Papier           Ciseaux", 140, 100, arcade.color.WHITE, 25)
            self.players_sprites.draw()

            self.return_position()

            if self.choix == "":
                self.scissor_sprite_list.draw()
                self.rock_sprite_list.draw()
                self.paper_sprite_list.draw()
            else:
                if self.choix == AttackType.ROCK:
                    self.rock_sprite_list.draw()

                if self.choix == AttackType.SCISSORS:
                    self.scissor_sprite_list.draw()

                if self.choix == AttackType.PAPER:
                    self.paper_sprite_list.draw()

            if self.game_state == GameState.ROUND_ACTIVE:
                arcade.draw_text(f"point: {self.score_J}", 300, 250, arcade.color.WHITE, 20)
                arcade.draw_text(f"point: {self.score_O}", 910, 250, arcade.color.WHITE, 20)

            elif self.game_state == GameState.ROUND_DONE:
                arcade.draw_text(self.resultat, 0, 540, arcade.color.WHITE, 65, align="center", width=WINDOW_WIDTH)

                self.change_position()

                if self.choix_ord == "":
                    self.scissor_sprite_list.draw()
                    self.rock_sprite_list.draw()
                    self.paper_sprite_list.draw()
                else:
                    if self.choix_ord == AttackType.ROCK:
                        self.rock_sprite_list.draw()

                    if self.choix_ord == AttackType.SCISSORS:
                        self.scissor_sprite_list.draw()

                    if self.choix_ord == AttackType.PAPER:
                        self.paper_sprite_list.draw()

    def on_update(self, delta_time: float = 1 / 60):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.rock_sprite.on_update()
        self.paper_sprite.on_update()
        self.scissor_sprite.on_update()

        if self.game_state != GameState.ROUND_ACTIVE:
            return

        if self.choix == "":
            return

        self.choix_ord = random.choice(self.choix_list)
        print(self.choix_ord)

        if self.choix == self.choix_ord:
            self.resultat = "NULL"

        if self.choix == AttackType.PAPER and self.choix_ord == AttackType.SCISSORS:
            self.resultat = "POINT ORDINATEUR"
            self.score_O += 1

        if self.choix == AttackType.SCISSORS and self.choix_ord == AttackType.ROCK:
            self.resultat = "POINT ORDINATEUR"
            self.score_O += 1

        if self.choix == AttackType.ROCK and self.choix_ord == AttackType.PAPER:
            self.resultat = "POINT ORDINATEUR"
            self.score_O += 1

        if self.choix_ord == AttackType.PAPER and self.choix == AttackType.SCISSORS:
            self.resultat = "POINT JOUEUR"
            self.score_J += 1

        if self.choix_ord == AttackType.SCISSORS and self.choix == AttackType.ROCK:
            self.resultat = "POINT JOUEUR"
            self.score_J += 1

        if self.choix_ord == AttackType.ROCK and self.choix == AttackType.PAPER:
            self.resultat = "POINT JOUEUR"
            self.score_J += 1

        self.game_state = GameState.ROUND_DONE

        # si déterminé gagnant, passer en ROUND_DONE
        if self.score_J == 3 or self.score_O == 3:
            arcade.schedule_once(self.remove_info, 0.5)

    def remove_info(self, _delta_time):
        self.game_state = GameState.GAME_OVER

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """

        if key == arcade.key.SPACE:

            if self.game_state == GameState.NOT_STARTED:
                self.game_state = GameState.ROUND_ACTIVE

            elif self.game_state == GameState.GAME_OVER:
                self.reset()

            elif self.game_state == GameState.ROUND_DONE:
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
            self.choix = AttackType.ROCK
            print(self.choix)
        elif self.paper_sprite.collides_with_point((x, y)):
            self.choix = AttackType.PAPER
            print(self.choix)
        elif self.scissor_sprite.collides_with_point((x, y)):
            self.choix = AttackType.SCISSORS
            print(self.choix)


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
