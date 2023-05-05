# rosbag-analysis

This repository contains Python scripts for analyzing ROS bag files.

## Prerequisites

To use the scripts in this repository, you will need:

- Python 3
- ROS Melodic or later installed on your system
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

## Getting Started

To get started with using the scripts in this repository, follow these steps:

1. Clone this repository to your local machine:
2. Activate the virtual envrionment: `source .venv/bin/activate`
3. Run the scripts using the following command:

## Usage

``` bash
python main.py [<path_to_bag_file>] [<topic_name_1> <topic_name_2> ...] [--plot-values] [--plot-timestamps] [--show-info]
```

By default, the `main.py` script will plot the rostime difference for the `/topic1` topic in the `example.bag` file. You can specify a different bag file and topic name(s) to plot using the command line arguments.


The `main.py` script can plot the rostime difference, timestamps, or topic values for one or several topics in a ROS bag file. The script takes the following command line arguments:

- `bag_file`: The path to the ROS bag file to analyze (default: "example.bag").
- `topic_names`: A list of topic names to plot (default: ["/topic1"]).
- `--plot-values` (`-v`): Plot topic values instead of rostime difference.
- `--plot-timestamps` (`-t`): Plot topic timestamps instead of rostime difference.
- `--show-info` (`-i`): Show basic information about the ROS bag file.

To plot the rostime difference for the topic `/topic2` in the bag file `mybag.bag`, run the following command:
```
python main.py mybag.bag /topic2
```

To plot the topic values for the topics `/topic1` and `/topic2` in the bag file `mybag.bag`, run the following command:

```
python rosbag_plot.py mybag.bag /topic1 /topic2 --plot-values
```

To plot the timestamps for the topic `/topic1` in the bag file `mybag.bag`, run the following command:
```
python rosbag_plot.py mybag.bag /topic1 --plot-timestamps
```

To show basic information about the bag file `mybag.bag`, run the following command:
```
python rosbag_plot.py mybag.bag --show-info
```


