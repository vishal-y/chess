import serial
import time

ser = serial.Serial('COM3', 9600)

def blink_led(row, col, row2, col2):
    row_byte = bytes([row])
    col_byte = bytes([col])
    row_byte2 = bytes([row2])
    col_byte2 = bytes([col2])
    ser.write(row_byte)
    ser.write(col_byte)
    ser.write(row_byte2)
    ser.write(col_byte2)

while True:
    row = int(input("Enter the row number (0-7): "))
    col = int(input("Enter the column number (0-7): "))
    row2 = int(input("Enter the row number (0-7): "))
    col2 = int(input("Enter the column number (0-7): "))
    blink_led(row, col, row2, col2)
