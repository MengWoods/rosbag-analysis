# rosbag-analysis

This repository contains Python scripts for analyzing ROS bag files.

## Prerequisites

To use the scripts in this repository, you will need:

- Python 3
- ROS
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

## Getting Started

To get started with using the scripts in this repository, follow these steps:

1. Clone this repository to your local machine and enter the repository directory: `cd rosbag-analysis`.
2. Activate the virtual envrionment in the repo directory: `source .venv/bin/activate`

## Usage

This script can be used to plot different aspects of a ROS bag file. The following command line arguments are available:

- `bag_file`: The path to the ROS bag file to analyze (default: "example.bag").
- `topic_names`: A list of topic names to plot (default: ["/topic1"]).
- `--plot-timestamps` (`-t`): Plot topic timestamps.
- `--plot-timediff` (`-td`): Plot rostime difference.
- `--plot-header-timediff` (`-htd`): Plot difference between header timestamps.
- `--plot-odometry` (`-o`): Plot odometry topic values.
- `--plot-std-values` (`-s`): Plot topic standard values.

Below are some examples:

To plot the rostime difference for the topic `/topic2` in the bag file `mybag.bag`, run the following command:
```
# Timediff of headers (common used)
python main.py mybag.bag /topic2 -htd
# Timediff of ROS messages
python main.py mybag.bag /topic2 -td
```

To plot the standard type topic values for the topics `/topic1` and `/topic2` in the bag file `mybag.bag`, run the following command:

```
python main.py mybag.bag /topic1 /topic2 -s
```

To plot the timestamps for the topic `/topic1` in the bag file `mybag.bag`, run the following command:
```
python main.py mybag.bag /topic1 -t
```


