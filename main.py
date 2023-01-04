import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = ""
import pygame
pygame.init()
import time
import random

WIDTH, HEIGHT = 1920 * 4, 600
NUMS = WIDTH
WIDTH_OF_BAR, HEIGHT_OF_BAR = WIDTH / NUMS, HEIGHT / NUMS
print(WIDTH_OF_BAR)
surf = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort Visualizer")
clock = pygame.time.Clock()

def make_bar(pos: tuple, width: int, color: tuple):
    pygame.draw.rect(surf, color, pos + (width, HEIGHT - pos[1]))
def randomize_list(nums: list):
    for i in range(len(nums)):
        num = random.randint(0, len(nums) - 1)
        nums[i], nums[num] = nums[num], nums[i]
    return nums

from pyaudio import PyAudio
p = PyAudio()
stream = p.open(
        22050,
        1,
        p.get_format_from_width(4),
        output=True
    )

import numpy as np
def make_sound(freq: int, volume: float, duration: float):
    sample_amt = int(22050 * duration)
    samples = (np.sin(2*np.pi*np.arange(sample_amt)*freq/22050) * volume).astype(np.float32)
    stream.write(samples)

nums = [i for i in range(1, NUMS + 1)]
nums = randomize_list(nums)
done = False
bar = 0

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit(0)
    surf.fill((0, 0, 0))
    done = True
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            done = False
        make_bar((i * WIDTH_OF_BAR, HEIGHT - nums[i] * HEIGHT_OF_BAR), WIDTH_OF_BAR, (255, 255, 255))
    if done:
        break
    pygame.display.flip()
for i in range(len(nums)):
    make_bar((i * WIDTH_OF_BAR, HEIGHT - nums[i] * HEIGHT_OF_BAR), WIDTH_OF_BAR, (0, 255, 0))
index = 0
while True:
    is_quit = False
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            is_quit = True
    if is_quit:
        break
    try:
        make_sound(nums[index] * 2 + 440, .1, .1)
        pygame.display.flip()
        index += 1
    except:
        pass
stream.stop_stream()
stream.close()
p.terminate()