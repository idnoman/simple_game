#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Pose
from std_msgs.msg import String

move_history = [] # Current session move history
def get_move_info_callback(user_input: String):
    global move_history
    last_move = user_input.data

    move_history.append(last_move)

# Display current session statistics
def display_statistics():
    print("--------------------")
    print("SESSION STATISTICS")
    print("Moves made:")

    total_moves = 0
    for el in ["w", "a", "s", "d"]:
        if el in move_history:
            move_count = move_history.count(el)
            total_moves += move_count
            print(el + " - " + str(move_count))

    print("Total - " + str(total_moves))
    print("--------------------")

if __name__ == "__main__":
    rospy.init_node("session_stats")
    get_move_info_sub = rospy.Subscriber("/simple_game/get_move_info", String, callback = get_move_info_callback)
    
    rospy.spin()

    # Display stats after node shutdown
    display_statistics()