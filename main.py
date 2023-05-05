#!/usr/bin/env python

import rosbag
import rospy
import matplotlib.pyplot as plt
import argparse

def plot_topic_difference(topic_name, bag_file):
    """
    Plots the rostime difference for a given topic in a ROS bag file
    """
    bag = rosbag.Bag(bag_file)
    timestamps = []
    for topic, msg, t in bag.read_messages(topics=[topic_name]):
        timestamps.append(t.to_nsec())

    differences = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]

    plt.plot(differences)
    plt.ylabel('Time Difference (nanoseconds)')
    plt.xlabel('Message Number')
    plt.title(f'ROSTime Difference for topic: {topic_name}')
    plt.show()

def plot_topic_values(topic_name, bag_file):
    """
    Plots the values of a given topic in a ROS bag file
    """
    bag = rosbag.Bag(bag_file)
    values = []
    timestamps = []
    for topic, msg, t in bag.read_messages(topics=[topic_name]):
        values.append(msg.data)
        timestamps.append(t.to_sec())

    plt.plot(timestamps, values)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Value')
    plt.title(f'Values for topic: {topic_name}')
    plt.show()

def plot_topic_timestamps(topic_name, bag_file):
    """
    Plots the timestamps for a given topic in a ROS bag file
    """
    bag = rosbag.Bag(bag_file)
    timestamps = []
    for topic, msg, t in bag.read_messages(topics=[topic_name]):
        timestamps.append(t.to_sec())

    plt.plot(timestamps)
    plt.ylabel('ROS Timestamp (seconds)')
    plt.xlabel('Message Number')
    plt.title(f'ROS Timestamp for topic: {topic_name}')
    plt.show()

def show_bag_info(bag_file):
    """
    Displays basic information about a ROS bag file
    """
    bag = rosbag.Bag(bag_file)
    print(f'Bag file: {bag_file}')
    print(f'Time range: {bag.get_start_time()} - {bag.get_end_time()}')
    print(f'Duration: {bag.get_end_time() - bag.get_start_time()}')
    print(f'Topics: {bag.get_type_and_topic_info()}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot rostime difference, timestamps, or topic values for one or several topics in a ROS bag file.')
    parser.add_argument('bag_file', nargs='?', default='example.bag', help='path to the ROS bag file (default: "example.bag")')
    parser.add_argument('topic_names', nargs='*', default=['/topic1'], help='list of topic names to plot (default: ["/topic1"])')
    parser.add_argument('--plot-values', '-v', action='store_true', help='plot topic values instead of rostime difference')
    parser.add_argument('--plot-timestamps', '-t', action='store_true', help='plot topic timestamps instead of rostime difference')
    parser.add_argument('--show-info', '-i', action='store_true', help='show basic information about the ROS bag file')
    args = parser.parse_args()

    if args.plot_values:
        plot_function = plot_topic_values
    elif args.plot_timestamps:
        plot_function = plot_topic_timestamps
    else:
        plot_function = plot_topic_difference

    if args.show_info:
        show_bag_info(args.bag_file)
    else:
        for topic_name in args.topic_names:
            plot_function(topic_name, args.bag_file)

