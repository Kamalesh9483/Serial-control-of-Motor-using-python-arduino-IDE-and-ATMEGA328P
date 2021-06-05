import serial

ser = serial.Serial('COM3', 9600, timeout=1)

while True:
    # Getting input from user
    text = input("Enter 'C' for clockwise, 'A' for anticlockwise, 'O' for off")

     # converting text input to equivalent byte information
    byte = text.encode()


    if ser.isOpen():

        # sending byte information
        ser.write(byte)

        # printing the data sent information 
        print("Data sent over serial")

        # to confirm the byte is received at serial end this print is used, 
        # ie., to confirm serial information sent from python is received at serial end in Arduino IDE
        # readline reads all chracter untill newline (ie pressing enter)
        print(ser.readline())