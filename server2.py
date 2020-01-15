import socket
import os
import io
import os.path
from PIL import Image
import pygame
from threading import Thread


s = socket.socket()
host = socket.gethostname()
print(host)
port = 12345
s.bind(('0.0.0.0', port))
SURFACE_SIZE = (800, 600)
pygame.init()

screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()
while True:
    s.listen(1)
    print("Waiting for a connection...")

    img_str = b''
    c, addr = s.accept()
    print("Connection from: " + str(addr))

    if os.path.isfile("image.png"):
        os.remove("image.png")

    file = open("image.png", "w+b")
    while True:
        data = c.recv(1024)
        if not data:
            break
        file.write(data)
        print(str(list(data)))
    file.close()
    image = pygame.image.load('image.png')
    image_rect = image.get_rect(center=screen_rect.center)
    screen.blit(image, image_rect)
    # blit


   # pygame.display.flip()
    print("Done.")

c.close()
s.close()

if __name__ == "__main__":
    Main()