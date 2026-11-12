import serial
import time

# Connect to the STM32 (adjust port as necessary)
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
time.sleep(2)  # Give STM32 time to reset after opening serial

def send_command(cmd_char):
    ser.write(cmd_char.encode())
    print(f"Sent: '{cmd_char}'")

def main():
    try:
        while True:
            print("Control options:")
            print("    w → Forward")
            print("    a → Turn Left")
            print("    d → Turn Right")
            print("    x → Stop (not implemented in STM yet)")
            print("    q → Quit")
            key = input("Enter command: ").strip().lower()

            if key == 'w':
                send_command('3')  # Forward
            elif key == 'a':
                send_command('1')  # Turn Left
            elif key == 'd':
                send_command('2')  # Turn Right
            elif key == 'x':
                send_command('x')  # Stop (add handling in STM to use)
            elif key == 'q':
                send_command('x')  # Stop before quitting
                print("Exiting.")
                break
            else:
                print("Invalid key. Try w, a, d, x, or q.")

    except KeyboardInterrupt:
        send_command('x')
        print("\nInterrupted. Motors stopped.")
    finally:
        ser.close()

if __name__ == '__main__':
    main()