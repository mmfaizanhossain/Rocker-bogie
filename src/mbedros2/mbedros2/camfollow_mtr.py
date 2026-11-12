import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32MultiArray
from mbedros2.SerialSimple import SerialSimple, setMotorSpeed, getMotorSpeed

class MotorControlNode(Node):
    def __init__(self):
        super().__init__('motor_control_node')
        
        # Initialize serial connection to STM
        self.ser = SerialSimple(baudrate=115200, port='/dev/ttyACM0')
        self.ser.init()
        self.ser.start()
        
        # Subscriber for line-following directions
        self.subscription = self.create_subscription(
            String,
            'direction',
            self.listener_callback,
            10
        )
        
        # Publisher for motor velocities (optional, for monitoring)
        self.publisher = self.create_publisher(Float32MultiArray, 'motor_vel', 10)

        # Motor speed parameters
        self.forward_speed = 10.5
        self.turn_speed = 8.0
        self.stop_speed = 0.0

    def listener_callback(self, msg: String):
        direction = msg.data.lower()  # Convert to lowercase for case-insensitive comparison
        motor_cmd = Float32MultiArray()

        try:
            if direction == "turn left":
                setMotorSpeed(self.ser, self.turn_speed, -self.turn_speed)
                motor_cmd.data = [self.turn_speed, -self.turn_speed]
            elif direction == "turn right":
                setMotorSpeed(self.ser, -self.turn_speed, self.turn_speed)
                motor_cmd.data = [-self.turn_speed, self.turn_speed]
            elif direction == "forward" or direction == "on track":
                setMotorSpeed(self.ser, self.forward_speed, self.forward_speed)
                motor_cmd.data = [self.forward_speed, self.forward_speed]
            elif direction == "stop":
                setMotorSpeed(self.ser, self.stop_speed, self.stop_speed)
                motor_cmd.data = [self.stop_speed, self.stop_speed]
            else:
                self.get_logger().warn(f"Unknown direction command: {direction}")
                return

            # Publish the motor velocities for monitoring
            self.publisher.publish(motor_cmd)
            self.get_logger().info(f"Executing: {direction} → Left: {motor_cmd.data[0]}, Right: {motor_cmd.data[1]}")

        except Exception as e:
            self.get_logger().error(f"Error in motor control: {str(e)}")

    def destroy_node(self):
        # Clean up serial connection
        try:
            setMotorSpeed(self.ser, 0.0, 0.0)  # Stop motors before shutdown
            self.ser.close()
        except Exception as e:
            self.get_logger().error(f"Error during shutdown: {str(e)}")
        finally:
            super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = MotorControlNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()