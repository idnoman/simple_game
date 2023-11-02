#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Pose
from std_msgs.msg import String


# Change the pawn_position based on the input
def handle_pawn_movement(user_input):
    correct_input = 1 # Indicates whether the input is correct and should be used 

    if user_input == "w" and pawn_position.position.y > MIN_POS:
        pawn_position.position.y -= MOVE_DISTANCE

    elif user_input == "s" and pawn_position.position.y < MAX_POS:
        pawn_position.position.y += MOVE_DISTANCE

    elif user_input == "d" and pawn_position.position.x < MAX_POS:
        pawn_position.position.x += MOVE_DISTANCE

    elif user_input == "a" and pawn_position.position.x > MIN_POS:
        pawn_position.position.x -= MOVE_DISTANCE
    else:
        correct_input = 0
        rospy.logwarn("INCORRECT INPUT")

    return correct_input


if __name__ == "__main__":
    rospy.init_node("pawn_controller")
    get_pawn_position_pub = rospy.Publisher("/simple_game/get_pawn_position", Pose, queue_size = 10)
    get_move_info_pub = rospy.Publisher("/simple_game/get_move_info", String, queue_size = 10)


    MAX_POS = 725 # Max x & y value
    MIN_POS = 25 # Min x & y value
    MOVE_DISTANCE = 100 # Determines how much the pawn moves by a single key press
    pawn_position = Pose () 
    pawn_position.position.x = MIN_POS 
    pawn_position.position.y = MIN_POS 

    print("--------------------")
    print("Possible moves: ")
    print("W (up), S (down), A (left), D (right)")
    print("To quit enter 'q' and then press Ctrl+C")
    while not rospy.is_shutdown():
        user_input = input("Enter your next move: ").lower()
        if user_input == "q":
            break

        correct_input = handle_pawn_movement(user_input)        

        if correct_input:
            # Publish the new pawn_position to the get_pawn_position topic
            get_pawn_position_pub.publish(pawn_position)

            # Publish user_input for further statistical analysis
            get_move_info_pub.publish(user_input)

