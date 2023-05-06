#!/usr/bin/env python

import argparse
import utils.plot_topic as plot

parser = argparse.ArgumentParser(description='Plot rostime difference, timestamps, or topic values for one or several topics in a ROS bag file.')
parser.add_argument('bag_file', nargs='?', default='example.bag', help='path to the ROS bag file (default: "example.bag")')
parser.add_argument('topic_names', nargs='*', default=['/topic1'], help='list of topic names to plot (default: ["/topic1"])')

parser.add_argument('--plot-timestamps', '-t', action='store_true', help='plot ros timestamps')
parser.add_argument('--plot-timediff', '-td', action='store_true', help='plot rostime difference')
parser.add_argument('--plot-header-timediff', '-e', action='store_true', help='plot header timestamps difference')

parser.add_argument('--plot-odometry', '-o', action='store_true', help='plot odometry topic values')
parser.add_argument('--plot-std-values', '-s', action='store_true', help='plot topic standard values')

args = parser.parse_args()

def main():

    if args.plot_timediff:
        plot_function = plot.plot_ros_timediff
    elif args.plot_header_timediff:
        plot_function = plot.plot_header_timediff
    elif args.plot_odometry:
        plot_function = plot.plot_odometry
    elif args.plot_std_values:
        plot_function = plot.plot_topic_values
    elif args.plot_timestamps:
        plot_function = plot.plot_topic_timestamps

    plot.show_bag_info(args.bag_file)
    for topic_name in args.topic_names:
        plot_function(topic_name, args.bag_file)

if __name__ == '__main__':
    main()
