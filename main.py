import os
import pygame
import chardet

# 初始化 Pygame
pygame.init()

# 设置屏幕大小
screen_width = 800
screen_height = 600

# 设置屏幕
screen = pygame.display.set_mode((screen_width, screen_height))

# 加载图片
steve_img = pygame.image.load('./skin/default.png')
images = {}
ids = []

# 检测文件编码方式
with open('./id.txt', 'rb') as f:
    content = f.read()
    encoding = chardet.detect(content)['encoding']
    print('Detected encoding:', encoding)

# 使用检测到的编码方式读取文件
with open('./id.txt', 'r', encoding=encoding) as f:
    for line in f:
        id = line.strip()
        ids.append(id)
        image_path = os.path.join('./skin', f'{id}.png')
        if os.path.exists(image_path):
            images[id] = pygame.image.load(image_path)
        else:
            images[id] = steve_img

# 设置角色宽度和间距
char_width = images[ids[0]].get_width()
spacing = 10

# 设置字体
font_path = './font.otf'
font = pygame.font.Font(font_path, 18)

# 创建角色类
class Character():
    def __init__(self, id, x, y):
        self.id = id
        self.image = images[id]
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

    def update(self):
        self.y += 1
        if self.y >= screen_height:
            if self in characters:
                self.kill()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        name_text = font.render(self.id, True, (255, 255, 255))
        name_x = self.x + self.rect.width + spacing
        name_y = self.y + self.rect.height // 2 - name_text.get_height() // 2
        screen.blit(name_text, (name_x, name_y))

    def kill(self):
        if self in characters:
            characters.remove(self)

# 设置添加角色事件
ADD_CHARACTER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_CHARACTER_EVENT, 500)
last_add_time = 0

# 定义角色列表
characters = []

# 主循环
clock = pygame.time.Clock()
column_count = int(screen_width / (char_width + spacing))
x = (screen_width - char_width * column_count - spacing * (column_count - 1)) // 2
y = 0
index = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # 每隔 600 毫秒添加一个角色
        if event.type == ADD_CHARACTER_EVENT and index < len(ids):
            current_time = pygame.time.get_ticks()
            time_since_last_add = current_time - last_add_time
            if time_since_last_add >= 600:
                character = Character(ids[index], x, y)
                characters.append(character)
                index += 1
                last_add_time = current_time


    # 更新角色位置和状态
    for character in characters:
        character.update()
        if character.y > screen_height:
            character.kill()

    # 绘制屏幕
    screen.fill((0, 0, 0))
    for character in characters:
        character.draw()
    pygame.display.update()

    clock.tick(60)
