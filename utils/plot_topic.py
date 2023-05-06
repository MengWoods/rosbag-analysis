#!/usr/bin/env python
import rosbag
import rospy
import matplotlib.pyplot as plt

def plot_ros_timediff(topic_name, bag_file):
    """
    Plots the rostime difference for a given topic in a ROS bag file
    """
    print("[INFO] Plotting %s ROS timediff..." % topic_name)
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

def plot_header_timediff(topic_name, bag_file):
    """
    Plots the difference between header timestamps for a given topic in a ROS bag file
    """
    print("[INFO] Plotting %s header timediff..." % topic_name)
    bag = rosbag.Bag(bag_file)
    timestamps = []
    for topic, msg, t in bag.read_messages(topics=[topic_name]):
        # Extract the header timestamp from the message
        try:
            header_timestamp = msg.header.stamp
        except AttributeError:
            print(f"Topic {topic_name} does not contain a header with a timestamp.")
            return
        
        # Convert the header timestamp to nanoseconds and append to the list of timestamps
        timestamp_nsecs = header_timestamp.secs * 1e9 + header_timestamp.nsecs
        timestamps.append(timestamp_nsecs)

    differences = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]

    plt.plot(differences)
    plt.ylabel('Time Difference (nanoseconds)')
    plt.xlabel('Message Number')
    plt.title(f'Header Timestamp Difference for topic: {topic_name}')
    plt.show()

def plot_odometry(topic_name, bag_file):
    """
    Plots the values of a nav_msgs/Odometry topic in a ROS bag file
    """
    print("[INFO] Plotting %s odometry..." % topic_name)
    bag = rosbag.Bag(bag_file)
    pos_x = []
    pos_y = []
    pos_z = []
    orientation_x = []
    orientation_y = []
    orientation_z = []
    orientation_w = []
    linear_x = []
    linear_y = []
    linear_z = []
    angular_x = []
    angular_y = []
    angular_z = []
    timestamps = []
    for topic, msg, t in bag.read_messages(topics=[topic_name]):
        pos_x.append(msg.pose.pose.position.x)
        pos_y.append(msg.pose.pose.position.y)
        pos_z.append(msg.pose.pose.position.z)
        orientation_x.append(msg.pose.pose.orientation.x)
        orientation_y.append(msg.pose.pose.orientation.y)
        orientation_z.append(msg.pose.pose.orientation.z)
        orientation_w.append(msg.pose.pose.orientation.w)
        linear_x.append(msg.twist.twist.linear.x)
        linear_y.append(msg.twist.twist.linear.y)
        linear_z.append(msg.twist.twist.linear.z)
        angular_x.append(msg.twist.twist.angular.x)
        angular_y.append(msg.twist.twist.angular.y)
        angular_z.append(msg.twist.twist.angular.z)
        timestamps.append(t.to_sec())

    # plot position
    plt.figure(figsize=(12, 4))
    plt.plot(timestamps, pos_x, label='Position x')
    plt.plot(timestamps, pos_y, label='Position y')
    plt.plot(timestamps, pos_z, label='Position z')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Position (m)')
    plt.title(f'Position for topic: {topic_name}')
    plt.legend()
    # plt.show()

    # plot orientation
    plt.figure(figsize=(12, 4))
    plt.plot(timestamps, orientation_x, label='Orientation x')
    plt.plot(timestamps, orientation_y, label='Orientation y')
    plt.plot(timestamps, orientation_z, label='Orientation z')
    plt.plot(timestamps, orientation_w, label='Orientation w')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Orientation')
    plt.title(f'Orientation for topic: {topic_name}')
    plt.legend()
    # plt.show()

    # plot linear twist
    plt.figure(figsize=(12, 4))
    plt.plot(timestamps, linear_x, label='Linear x')
    plt.plot(timestamps, linear_y, label='Linear y')
    plt.plot(timestamps, linear_z, label='Linear z')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Linear Twist (m/s)')
    plt.title(f'Linear Twist for topic: {topic_name}')
    plt.legend()
    # plt.show()

    # plot angular twist
    plt.figure(figsize=(12, 4))
    plt.plot(timestamps, angular_x, label='Angular x')
    plt.plot(timestamps, angular_y, label='Angular y')
    plt.plot(timestamps, angular_z, label='Angular z')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Angular Twist (rad/s)')
    plt.title(f'Angular Twist for topic: {topic_name}')
    plt.legend()
    plt.show()

def plot_topic_values(topic_name, bag_file):
    """
    Plots the general type values of a given topic in a ROS bag file
    """
    print("[INFO] Plotting %s values..." % topic_name)
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
    print("[INFO] Plotting ROS timestampes")
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
    print("[INFO] BAG INFO:")
    print(f'\tBag file: {bag_file}')
    print(f'\tTime range: {bag.get_start_time()} - {bag.get_end_time()}')
    print(f'\tDuration: {bag.get_end_time() - bag.get_start_time()}')
    print("\tTopics:")
    for topic, info in bag.get_type_and_topic_info().topics.items():
        print(f"\t\t{topic} \t\t({info.msg_type})")