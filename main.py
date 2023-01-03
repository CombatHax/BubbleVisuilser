import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = ""
import pygame
pygame.init()
import time
import random

WIDTH, HEIGHT = 1400, 600
NUMS = WIDTH
WIDTH_OF_BAR, HEIGHT_OF_BAR = WIDTH / NUMS, HEIGHT / NUMS
print(WIDTH_OF_BAR)
surf = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort Visualizer")
clock = pygame.time.Clock()

def make_bar(pos: tuple, width: int):
    pygame.draw.rect(surf, (255, 255, 255), pos + (width, HEIGHT - pos[1]))
def randomize_list(nums: list):
    for i in range(len(nums)):
        num = random.randint(0, len(nums) - 1)
        nums[i], nums[num] = nums[num], nums[i]
    return nums

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
    
    for i, n in enumerate(nums):
        make_bar((i * WIDTH_OF_BAR, HEIGHT - n * HEIGHT_OF_BAR), WIDTH_OF_BAR)
    pygame.display.flip()