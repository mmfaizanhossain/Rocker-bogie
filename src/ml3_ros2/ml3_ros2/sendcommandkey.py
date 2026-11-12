# import serial
# import time

# # Connect to the STM32 (adjust port as necessary)
# ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
# time.sleep(2)  # Give STM32 time to reset after opening serial

# def send_command(cmd_char):
#     ser.write(cmd_char.encode())
#     print(f"Sent: '{cmd_char}'")

# def main():
#     try:
#         key = input("Enter command: ").strip().lower()
#         print("Control options:")
#         print("    w → Forward")
#         print("    a → Turn Left")
#         print("    d → Turn Right")
#         print("    x → Stop (not implemented in STM yet)")
#         print("    q → Quit")
#         while True:


#             if key == 'i':
#                 send_command('i')  # Forward
#             elif key == 'j':
#                 send_command('j')  # Turn Left
#             elif key == 'l':
#                 send_command('l')  # Turn Right
#             elif key == 'm':        #stop
#                 send_command('m')  # Stop (add handling in STM to use)
#             elif key == '9':
#                 send_command('x')  # Stop before quitting
#                 print("Exiting.")
#                 #DC motor command end here

#             #Servo 1
#             elif key == 'q':
#                 send_command('q')  # Stop before quitting
#                 print("motor1_inc")
#             elif key == 'a':
#                 send_command('a')  # Stop before quitting
#                 print("motor1_dec")
#             elif key == 'x':
#                 send_command('x')  # Stop before quitting
#                 print("motor1false")

#             #Servo 2
#             elif key == 'w':
#                 send_command('w')  # Stop before quitting
#                 print("motor2_inc")
#             elif key == 's':
#                 send_command('s') # Stop before quitting
#                 print("motor2_dec")
#             elif key == 'y':
#                 send_command('y')  # Stop before quitting
#                 print("motor2false")
#             #Servo 3
#             elif key == 'e':
#                 send_command('e')  # Stop before quitting
#                 print("motor3_inc")
#             elif key == 'd':
#                 send_command('d') # Stop before quitting
#                 print("motor3_dec")
#             elif key == 'z':
#                 send_command('z')  # Stop before quitting
#                 print("motor3false")
#             #Servo 4
#             elif key == 'r':
#                 send_command('r')  # Stop before quitting
#                 print("motor4_inc")
#             elif key == 'f':
#                 send_command('f') # Stop before quitting
#                 print("motor4_dec")
#             elif key == 't':
#                 send_command('t')  # Stop before quitting
#                 print("motor4false")
#                 break
#             else:
#                 print("Invalid key. Try w, a, d, x, or q.")

#     except KeyboardInterrupt:
#         send_command('b')
#         print("\nInterrupted. Motors stopped.")
#     finally:
#         ser.close()

# if __name__ == '__main__':
#     main()

# import serial
# import time
# import sys
# import tty
# import termios

# # Connect to the STM32 (adjust port as necessary)
# ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
# time.sleep(2)  # Wait for STM32 to reset

# # def __init__(self):
# #         super().__init__('keyboard_control')
# #         # self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
# #         # self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)
# #         self.get_logger().info("Keyboard Control Node Initialized")
        
# #         # Define speed and turn rates
# #         # self.linear_speed = 0.5  # Linear speed (m/s)
# #         # self.angular_speed = 1.0  # Angular speed (rad/s)

# #         # Timer to read keyboard input and publish TF
# #         self.timer = self.create_timer(0.1, self.read_keyboard)

# def send_command(cmd_char):
#     ser.write(cmd_char.encode())
#     print(f"Sent: '{cmd_char}'")

# def getch():
#     """Reads a single character without Enter key (Unix only)"""
#     fd = sys.stdin.fileno()
#     old_settings = termios.tcgetattr(fd)
#     try:
#         tty.setraw(fd)  # Set raw mode
#         ch = sys.stdin.read(1)
#     finally:
#         termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#     return ch



# def main():
#     print("Control options:")
#     print("    i → Forward")
#     print("    j → Turn Left")
#     print("    l → Turn Right")
#     print("    m → Stop")
#     print("    9 → Stop & Quit")
#     print("    q/a/x, w/s/y, e/d/z, r/f/t → Servo Control")
#     print("Press keys directly to control (Ctrl+C to quit).")

#     try:
#         while True:
#             key = getch().lower()
            
#             if key == 'i':
#                 send_command('i')
#             elif key == 'j':
#                 send_command('j')
#             elif key == 'l':
#                 send_command('l')
#             elif key == 'm':
#                 send_command('m')
#             elif key == '9':
#                 send_command('x')
#                 print("Exiting.")
#                 break

#             # Servo 1
#             elif key == 'q':
#                 send_command('q')
#                 print("motor1_inc")
#             elif key == 'a':
#                 send_command('a')
#                 print("motor1_dec")
#             elif key == 'x':
#                 send_command('x')
#                 print("motor1false")

#             # Servo 2
#             elif key == 'w':
#                 send_command('w')
#                 print("motor2_inc")
#             elif key == 's':
#                 send_command('s')
#                 print("motor2_dec")
#             elif key == 'y':
#                 send_command('y')
#                 print("motor2false")

#             # Servo 3
#             elif key == 'e':
#                 send_command('e')
#                 print("motor3_inc")
#             elif key == 'd':
#                 send_command('d')
#                 print("motor3_dec")
#             elif key == 'z':
#                 send_command('z')
#                 print("motor3false")

#             # Servo 4
#             elif key == 'r':
#                 send_command('r')
#                 print("motor4_inc")
#             elif key == 'f':
#                 send_command('f')
#                 print("motor4_dec")
#             elif key == 't':
#                 send_command('t')
#                 print("motor4false")

#             else:
#                 print("Invalid key.")
#     except KeyboardInterrupt:
#         send_command('b')
#         print("\nInterrupted. Motors stopped.")
#     finally:
#         ser.close()

# if __name__ == '__main__':
#     main()

import serial
import time
import sys
import tty
import termios

# Connect to the STM32 (adjust port as necessary)
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
time.sleep(2)  # Wait for STM32 to reset

def send_command(cmd_char):
    ser.write(cmd_char.encode())
    print(f"Sent: '{cmd_char}'")

def getch():
    """Reads a single character without Enter key (Unix only)"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)  # Set raw mode
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def main():
    print("Control options:")
    print("    i → Forward")
    print("    j → Turn Left")
    print("    l → Turn Right")
    print("    m → Stop")
    print("    9 → Stop & Quit")
    print("    q/a/x, w/s/y, e/d/z, r/f/t → Servo Control")
    print("Press keys directly to control (Ctrl+C to quit).")

    try:
        while True:
            key = getch().lower()
            
            if key == 'i':
                send_command('i')
            elif key == 'j':
                send_command('j')
            elif key == 'l':
                send_command('l')
            elif key == 'k':
                send_command('k')
            elif key == 'm':
                send_command('m')
            elif key == '9':
                send_command('x')
                print("Exiting.")
                break

            # Servo 1
            elif key == 'q':
                send_command('q')
                print("motor1_inc")
            elif key == 'a':
                send_command('a')
                print("motor1_dec")
            elif key == 'x':
                send_command('x')
                print("motor1false")

            # Servo 2
            elif key == 'w':
                send_command('w')
                print("motor2_inc")
            elif key == 's':
                send_command('s')
                print("motor2_dec")
            elif key == 'y':
                send_command('y')
                print("motor2false")

            # Servo 3
            elif key == 'e':
                send_command('e')
                print("motor3_inc")
            elif key == 'd':
                send_command('d')
                print("motor3_dec")
            elif key == 'z':
                send_command('z')
                print("motor3false")

            # Servo 4
            elif key == 'r':
                send_command('r')
                print("motor4_inc")
            elif key == 'f':
                send_command('f')
                print("motor4_dec")
            elif key == 't':
                send_command('t')
                print("motor4false")

            else:
                print("Invalid key.")
    except KeyboardInterrupt:
        send_command('b')
        print("\nInterrupted. Motors stopped.")
    finally:
        ser.close()

if __name__ == '__main__':
    main()

# import serial
# import time
# import sys
# import tty
# import termios

# # Connect to the STM32 (adjust port as necessary)
# ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
# time.sleep(2)  # Wait for STM32 to reset

# def send_command(cmd_char):
#     ser.write(cmd_char.encode())
#     print(f"Sent: '{cmd_char}'")

# def getch():
#     """Reads a single character without Enter key (Unix only)"""
#     # fd = sys.stdin.fileno()
#     # old_settings = termios.tcgetattr(fd)
#     try:
#         # tty.setraw(fd)  # Set raw mode
#         ch = sys.stdin.read(1)
#     finally:
#         termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#     return ch

# def main():
#     print("Control options:")
#     print("    i → Forward")
#     print("    j → Turn Left")
#     print("    l → Turn Right")
#     print("    m → Stop")
#     print("    9 → Stop & Quit")
#     print("    q/a/x, w/s/y, e/d/z, r/f/t → Servo Control")
#     print("Press keys directly to control (Ctrl+C to quit).")

#     try:
#         while True:
#             key = getch().lower()
            
#             if key == 'i':
#                 send_command('i')
#             elif key == 'j':
#                 send_command('j')
#             elif key == 'l':
#                 send_command('l')
#             elif key == 'm':
#                 send_command('m')
#             elif key == '9':
#                 send_command('x')
#                 print("Exiting.")
#                 break

#             # Servo 1
#             elif key == 'q':
#                 send_command('q')
#                 print("motor1_inc")
#             elif key == 'a':
#                 send_command('a')
#                 print("motor1_dec")
#             elif key == 'x':
#                 send_command('x')
#                 print("motor1false")

#             # Servo 2
#             elif key == 'w':
#                 send_command('w')
#                 print("motor2_inc")
#             elif key == 's':
#                 send_command('s')
#                 print("motor2_dec")
#             elif key == 'y':
#                 send_command('y')
#                 print("motor2false")

#             # Servo 3
#             elif key == 'e':
#                 send_command('e')
#                 print("motor3_inc")
#             elif key == 'd':
#                 send_command('d')
#                 print("motor3_dec")
#             elif key == 'z':
#                 send_command('z')
#                 print("motor3false")

#             # Servo 4
#             elif key == 'r':
#                 send_command('r')
#                 print("motor4_inc")
#             elif key == 'f':
#                 send_command('f')
#                 print("motor4_dec")
#             elif key == 't':
#                 send_command('t')
#                 print("motor4false")

#             else:
#                 print("Invalid key.")
#     except KeyboardInterrupt:
#         send_command('b')
#         print("\nInterrupted. Motors stopped.")
#     finally:
#         ser.close()



# import serial
# import sys
# import tty
# import termios

# # Open serial connection to STM32 (adjust the port if needed)
# ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

# def get_key():
#     """Reads a single character from keyboard without Enter."""
#     fd = sys.stdin.fileno()
#     old_settings = termios.tcgetattr(fd)

#     try:
#         tty.setraw(sys.stdin.fileno())
#         key = sys.stdin.read(1)
#     finally:
#         termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

#     return key


# def main():
#     try:
#         print("Press 'w' to send 'w' over serial. Press 'q' to quit.")
#         while True:
#             key = get_key()
#             if key == 'i':
#                 ser.write(b'i')
#                 print("Sent: 'i'")
#             if key == 'j':
#                 ser.write(b'j')
#                 print("Sent: 'j'")
#             if key == 'l':
#                 ser.write(b'l')
#                 print("Sent: 'l'")
#             if key == 'm':
#                 ser.write(b'm')
#                 print("Sent: 'm'")
#             elif key == 'q':
#                 print("Exiting...")
#                 break

#     except KeyboardInterrupt:
#         print("\nInterrupted by user.")
#     finally:
#         ser.close()



# if __name__ == '__main__':
#     main()