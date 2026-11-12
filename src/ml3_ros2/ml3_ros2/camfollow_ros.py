#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from mbedros2.SerialSimple import SerialSimple

class LineFollowerNode(Node):
    def __init__(self):
        super().__init__('line_follower_node')
        
        # Initialize serial connection to Nucleo
        try:
            self.ser = SerialSimple(baudrate=115200, port='/dev/ttyACM0')
            self.ser.init()
            self.ser.start()
            self.get_logger().info("Serial connection established with Nucleo")
        except Exception as e:
            self.get_logger().error(f"Failed to initialize serial: {str(e)}")
            rclpy.shutdown()
            return
        
        # Initialize camera
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 160)  # Width
        self.cap.set(4, 120)  # Height
        
        if not self.cap.isOpened():
            self.get_logger().error("Cannot open camera")
            rclpy.shutdown()
            return
            
        # Create timer for processing frames
        self.timer = self.create_timer(0.1, self.process_frame)  # 10Hz
    
    def send_command(self, command):
        """Send simple number command to Nucleo"""
        try:
            self.ser.write(f"{command}\n".encode('utf-8'))
            self.get_logger().info(f"Sent command: {command}")
        except Exception as e:
            self.get_logger().error(f"Error sending command: {str(e)}")
    
    def process_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().error("Failed to capture frame")
            return

        # Convert to HSV and threshold for line detection
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_black = np.array([0, 0, 0])
        upper_black = np.array([180, 255, 30])
        mask = cv2.inRange(hsv, lower_black, upper_black)

        # Find contours
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contours) > 0:
            largest_contour = max(contours, key=cv2.contourArea)
            M = cv2.moments(largest_contour)
            
            if M["m00"] != 0:
                cx = int(M['m10'] / M['m00'])
                
                # Determine and send command
                if cx >= 120:
                    self.send_command(1)  # Turn Left
                elif cx <= 40:
                    self.send_command(2)  # Turn Right
                else:
                    self.send_command(3)  # Move Forward
                
                # Visualization
                cv2.drawContours(frame, [largest_contour], -1, (0, 255, 0), 2)
                cv2.circle(frame, (cx, int(M['m01']/M['m00'])), 5, (0, 0, 255), -1)
        
        # Display frames
        cv2.imshow("Mask", mask)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.cleanup()
    
    def cleanup(self):
        """Clean up resources"""
        self.get_logger().info("Shutting down node...")
        
        # Send stop command (assuming 0 means stop)
        try:
            self.send_command(0)
        except:
            pass
            
        # Release resources
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()
        if hasattr(self, 'ser'):
            try:
                self.ser.close()
            except:
                pass
        cv2.destroyAllWindows()
        
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = LineFollowerNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.cleanup()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()