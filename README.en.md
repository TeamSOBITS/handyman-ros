<a name="readme-top"></a>

[JA](README.md) | [EN](README.en.md)

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

# ROS2 Package for Handyman

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#launch-and-usage">Usage</a></li>
    <li><a href="#milestones">Milestones</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#references">References</a></li>
  </ol>
</details>

## Introduction

This project is a ROS2 package for the RoboCup@Home Simulation's Handyman task.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Getting Started

This section explains how to set up this repository.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Prerequisites

To ensure proper operation, please set up the following required environment:

| System | Version |
|---|---|
| Ubuntu | 22.04 (Jammy Jellyfish) |
| ROS | Humble Hawksbill |
| Python | 3.10 |

If you have not installed the [HSR Sim Common](https://github.com/TeamSOBITS/hsr_sim_common) package, please install it.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Installation

1. Navigate to your ROS `src` folder.
    ```sh
    cd ~/colcon_ws/src/
    ```
2. Clone this repository.
    ```sh
    git clone -b humble-devel [https://github.com/TeamSOBITS/handyman-ros.git](https://github.com/TeamSOBITS/handyman-ros.git)
    ```
3. Compile the package.
    ```sh
    cd ~/colcon_ws/
    ```
    ```sh
    colcon build --symlink-install
    ```
    ```sh
    source ~/colcon_ws/install/setup.sh
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Launch and Usage

This is a simple ROS2 node that communicates with the Handyman application.

```sh
ros2 launch handyman_ros sample.launch.py
````

### How to Run the Teleoperation Tool

You can control the HSR robot using keyboard input. This is for debugging purposes.

```sh
ros2 launch handyman_ros teleop_key.launch.py
```

-----

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

This project is licensed under the SIGVerse License. See the `LICENSE.txt` file for details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

-----

## Milestones

Please check the [Issue page](https://www.google.com/search?q=issues-url) to see current bugs and new feature requests.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

-----

## References

  * [handyman-ros](https://github.com/RoboCupatHomeSim/handyman-ros)
  * [OS and ROS2 version](https://github.com/RoboCupatHomeSim/documents/blob/master/SoftwareManual/Environment.md#ubuntu-pc)
  * [rosbridge\_suite](http://wiki.ros.org/rosbridge_suite)
  * [sigverse\_ros\_bridge](https://github.com/SIGVerse/ros_package/tree/humble-devel/sigverse_ros_bridge)
  * [wiki page](https://github.com/RoboCupatHomeSim/handyman-ros/wiki).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/TeamSOBITS/handyman-ros.svg?style=for-the-badge
[contributors-url]: https://github.com/TeamSOBITS/handyman-ros/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TeamSOBITS/handyman-ros.svg?style=for-the-badge
[forks-url]: https://github.com/TeamSOBITS/handyman-ros/network/members
[stars-shield]: https://img.shields.io/github/stars/TeamSOBITS/handyman-ros.svg?style=for-the-badge
[stars-url]: https://github.com/TeamSOBITS/handyman-ros/stargazers
[issues-shield]: https://img.shields.io/github/issues/TeamSOBITS/handyman-ros.svg?style=for-the-badge
[issues-url]: https://github.com/TeamSOBITS/handyman-ros/issues
[license-shield]: https://img.shields.io/github/license/TeamSOBITS/handyman-ros.svg?style=for-the-badge
[license-url]: LICENSE
