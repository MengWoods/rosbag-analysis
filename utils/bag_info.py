#!/usr/bin/env python
import rosbag

def show_bag_info(bag_file):
    """
    Displays basic information about a ROS bag file
    """
    bag = rosbag.Bag(bag_file)
    print("[INFO] BAG INFO:")
    print(f'\tBag file: {bag_file}')
    print(f'\tTime range: {bag.get_start_time()} - {bag.get_end_time()}')
    print(f'\tDuration: {bag.get_end_time() - bag.get_start_time()}')
    print("\tTopics:")
    for topic, info in bag.get_type_and_topic_info().topics.items():
        print(f"\t\t{topic} \t\t({info.msg_type})")