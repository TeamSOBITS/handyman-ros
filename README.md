<a name="readme-top"></a>

[JA](README.md) | [EN](README.en.md)

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License: Custom][license-shield]][license-url]

# ROS2 Package for Handyman

<!-- 目次 -->
<details>
  <summary>目次</summary>
  <ol>
    <li>
      <a href="#概要">概要</a>
    </li>
    <li>
      <a href="#環境構築">環境構築</a>
      <ul>
        <li><a href="#環境条件">環境条件</a></li>
        <li><a href="#インストール方法">インストール方法</a></li>
      </ul>
    </li>
    <li><a href="#実行操作方法">実行・操作方法</a></li>
    <li><a href="#マイルストーン">マイルストーン</a></li>
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <li><a href="#ライセンス">ライセンス</a></li> 
    <li><a href="#参考文献">参考文献</a></li>
  </ol>
</details>

<!-- レポジトリの概要 -->
## 概要

このプロジェクトは，RoboCup@Home シミュレーションの Handyman タスク用の ROS2 パッケージです．

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


<!-- 環境構築 -->
## 環境構築

ここで，本レポジトリのセットアップ方法について説明します．

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>

### 環境条件

正常動作のため，以下の必要な環境を整えてください．

| System  | Version |
| ------------- | ------------- |
| Ubuntu | 22.04 (Jammy Jellyfish) |
| ROS | Humble Hawksbill |
| Python | 3.10 |

[HSR Sim Common](https://github.com/TeamSOBITS/hsr_sim_common)パッケージをインストールしていない場合はインストールしてください．

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


### インストール方法

1. ROSの`src`フォルダに移動します．
   ```sh
   cd ~/colcon_ws/src/
   ```
2. 本レポジトリをcloneします．
   ```sh
   git clone -b humble-devel https://github.com/TeamSOBITS/handyman-ros.git
   ```
3. パッケージをコンパイルします．
   ```sh
   cd ~/colcon_ws/
   ```
   ```sh
   colcon build --symlink-install
   ```
   ```sh
   source ~/colcon_ws/install/setup.sh
   ```

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>

<!-- 実行・操作方法 -->
## 実行・操作方法

これは，Handyman アプリケーションと通信するシンプルな ROS2 ノードです．

  ```sh:
  ros2 launch handyman_ros sample.launch.py​​
  ```

### 遠隔操作ツールの実行方法

HSR をキーボード操作で操作できます．
デバッグ用です．

  ```sh:
  ros2 launch handyman_ros teleop_key.launch.py
  ```

## ライセンス

このプロジェクトは SIGVerse ライセンスに基づいてライセンスされています．詳細については，LICENSE.txt ファイルを参照してください．


 <p align="right">(<a href="#readme-top">上に戻る</a>)</p>

<!-- マイルストーン -->
## マイルストーン

現時点のバッグや新規機能の依頼を確認するために[Issueページ](issues-url) をご覧ください．

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>

<!-- 参考文献 -->
## 参考文献
* [handyman-ros](https://github.com/RoboCupatHomeSim/handyman-ros)
* [OS and ROS2 version](https://github.com/RoboCupatHomeSim/documents/blob/master/SoftwareManual/Environment.md#ubuntu-pc)
* [rosbridge_suite](http://wiki.ros.org/rosbridge_suite)
* [sigverse_ros_bridge](https://github.com/SIGVerse/ros_package/tree/humble-devel/sigverse_ros_bridge)
* [wiki page](https://github.com/RoboCupatHomeSim/handyman-ros/wiki).

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>

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
[license-shield]: https://img.shields.io/badge/License-SIGVerse_License-orange.svg?style=for-the-badge
[license-url]: https://github.com/TeamSOBITS/handyman-ros/blob/humble-devel/license/LICENSE.txt
