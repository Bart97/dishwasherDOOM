import pygame
import serial;

ser = serial.Serial('/dev/ttyUSB0', 115200)

scancodeLut = {pygame.K_ESCAPE: 0x01,
        pygame.K_y: 0x15,
        pygame.K_LCTRL: 0x1D,
        pygame.K_RCTRL: 0x1D,
        pygame.K_RETURN: 0x1C,
        pygame.K_SPACE: 0x39,
        pygame.K_UP: 0x67,
        pygame.K_LEFT: 0x69,
        pygame.K_RIGHT: 0x6a,
        pygame.K_DOWN: 0x6c}

def to_scancode(key, pressed):
    pressedBit = 0 if pressed else 0x80
    return bytes([pressedBit | scancodeLut[key]])

def handle_key(key, pressed):
    try:
        ser.write(to_scancode(key, pressed))
    except KeyError:
        print("Unknown key")

pygame.init()
pygame.display.set_mode((50,50), pygame.RESIZABLE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

        if event.type == pygame.KEYDOWN:
            handle_key(event.key, True)
            print("Key down!")

        if event.type == pygame.KEYUP:
            handle_key(event.key, False)
            print("Key up!")
pygame.quit()
exit()
