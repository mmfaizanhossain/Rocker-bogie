import serial
import time

# Connect to the STM32 (adjust port if needed)
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
time.sleep(2)  # Wait for STM32 to reboot/reset after opening serial

def send_command(cmd_char):
    ser.write(cmd_char.encode())
    print(f"Sent: '{cmd_char}'")

def main():
    try:
        while True:
            key = input("Press w/s/a/d/x to control, q to quit: ").strip().lower()

            if key in ['w', 's', 'a', 'd', 'x']:
                send_command(key)
            elif key == 'q':
                send_command('x')  # stop before exiting
                print("Exiting.")
                break
            else:
                print("Invalid key. Use w, s, a, d, x, or q.")
    except KeyboardInterrupt:
        send_command('x')
        print("\nInterrupted. Motors stopped.")
    finally:
        ser.close()

if __name__ == '__main__':
    main()