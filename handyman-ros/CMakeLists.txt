cmake_minimum_required(VERSION 3.8)
project(handyman_ros)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(trajectory_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(handyman REQUIRED)

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
include_directories(
  /usr/local/include
)

#-- for Launch
install(DIRECTORY launch/
DESTINATION share/${PROJECT_NAME}/launch)
#--- end Launch

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

include_directories(include)
link_directories(/usr/local/lib)
add_executable(handyman_sample src/handyman_sample.cpp)
add_executable(teleop_key_handyman src/teleop_key_handyman.cpp)

ament_target_dependencies(handyman_sample
  rclcpp
  geometry_msgs
  std_msgs
  trajectory_msgs
  tf2
  tf2_ros
  handyman
)

ament_target_dependencies(teleop_key_handyman
  rclcpp
  geometry_msgs
  sensor_msgs
  trajectory_msgs
  tf2
  tf2_ros
  tf2_geometry_msgs
  handyman
)

install(TARGETS
  handyman_sample
  teleop_key_handyman
  DESTINATION lib/${PROJECT_NAME}
)
#--- end C++

target_link_libraries(handyman_sample)
target_link_libraries(teleop_key_handyman)
ament_package()
