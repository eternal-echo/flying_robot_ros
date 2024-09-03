#!/usr/bin/env python3
# encoding: utf-8

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from std_msgs.msg import Float32MultiArray
import struct
from test_py.flying_hardware_sdk import Board  


class FlyingHardwareNode(Node):
    def __init__(self):
        super().__init__('flying_hardware_node')
        
        # 初始化发布器
        self.imu_publisher = self.create_publisher(Imu, '/imu/data_raw', 10)
        
        # 创建Board对象，并启用接收
        self.board = Board('/dev/ttyACM0', 1000000)  # 根据实际情况修改串口号和波特率
        self.board.enable_reception()

        # 设置定时器，每0.1秒发布一次IMU数据
        self.timer = self.create_timer(0.1, self.publish_imu_data)

    def publish_imu_data(self):
        # 从串口获取IMU数据
        imu_data = self.board.get_imu()

        if imu_data:
            imu_msg = Imu()

            # 填充IMU消息
            imu_msg.header.stamp = self.get_clock().now().to_msg()
            imu_msg.header.frame_id = 'imu_frame'

            imu_msg.linear_acceleration.x = imu_data[0]
            imu_msg.linear_acceleration.y = imu_data[1]
            imu_msg.linear_acceleration.z = imu_data[2]

            imu_msg.angular_velocity.x = imu_data[3]
            imu_msg.angular_velocity.y = imu_data[4]
            imu_msg.angular_velocity.z = imu_data[5]
 
            # 发布IMU数据
            self.imu_publisher.publish(imu_msg)

def main(args=None):
    rclpy.init(args=args)
    node = FlyingHardwareNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
