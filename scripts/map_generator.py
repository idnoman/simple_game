#!/usr/bin/env python3
import rospy
import pygame
import os
from geometry_msgs.msg import Pose


# Pawn class
class Pawn():
    def __init__(self, x, y):
        self.image = pawn_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.image, self.rect)


# Change the pawn position according to the callback from get_pawn_position topic and update the board
def get_pawn_position_callback(position: Pose):
    # Change the pawn position 
    pawn.rect.x = position.position.x
    pawn.rect.y = position.position.y

    # Update the board
    screen.blit(bg_image, (0,0))
    pawn.draw()
    pygame.display.update()


if __name__ == "__main__":
    rospy.init_node("map_generator")
    get_pawn_position_sub = rospy.Subscriber("/simple_game/get_pawn_position", Pose, callback = get_pawn_position_callback)

    pygame.init()

    # Create & setup the game window
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("A simple game")

    # Get the Python file & assets directory paths
    dir_path = os.path.dirname(os.path.realpath(__file__))
    assets_path = os.path.join(dir_path, "assets")

    # Load images
    bg_image = pygame.image.load(os.path.join(assets_path, "bg.png")).convert_alpha()
    pawn_image = pygame.image.load(os.path.join(assets_path, "pawn.png")).convert_alpha()

    pawn = Pawn(50, 50) # Create the pawn

    # Initial drawing of the board
    screen.blit(bg_image, (0,0))
    pawn.draw()
    pygame.display.update()

    # Main loop
    while not rospy.is_shutdown():
        # Pygame event handler
        for event in pygame.event.get():
                # Check for quit event to properly shut down
                if event.type == pygame.QUIT:
                    rospy.signal_shutdown("Shutting down!")
                    break