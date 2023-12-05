import pygame

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
purple = (255, 0, 255)
yellow = (255, 255, 0)
fps = 60

# Add music
#pygame.mixer.init()
#pygame.mixer.music.load('папка пнг/bg_music.mp3')
#pygame.mixer.music.play(-1, 0.0)


# Этот класс представляет собой панель внизу, которой управляет игрок
class Wall(pygame.sprite.Sprite):
    # Функция конструктора
    def __init__(self, x, y, width, height, color):
        # Вызов родительского конструктора
        pygame.sprite.Sprite.__init__(self)

        # Делаем синюю стену указанного в параметрах размера
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Сделайте наш верхний левый угол местом передачи.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x


# Создаются все стены в комнате 1
def setupRoomOne(all_sprites_list):
    # Make the walls. (x_pos, y_pos, width, height)
    wall_list = pygame.sprite.RenderPlain()

    # This is a list of walls. Each is in the form [x, y, width, height]
    # Create an 900x750 sized screen
    walls = [[0, 0, 10, 750],  #левая стенка
             [0, 0, 800, 10], #верхняя стенка
             [0, 740, 800, 10], #нижняя стенка
             [800, 0, 10, 750], #правая стенка
             # верхний выступ
             [390, 0, 6, 125],
             [390, 125, 39, 6],
             [423, 0, 6, 125],
             # правый островок
             [755, 60, 6, 65],
             [630, 60, 6, 65],
             [630, 60, 130, 6],
             [630, 125, 131, 6],
             # левее правого островка
             [480, 60, 6, 65],
             [480, 60, 97, 6],
             [480, 125, 101, 6],
             [575, 60, 6, 65],
             #левый островок
             [60, 60, 6, 65],
             [60, 60, 130, 6],
             [185, 60, 6, 65],
             [60, 125, 131, 6],
             #правее левого островка
             [240, 60, 6, 65],
             [240, 60, 97, 6],
             [335, 60, 6, 65],
             [240, 125, 101, 6],
            #левая однушка сверху
             [60, 175, 6, 15],
             [60, 175, 130, 6],
             [185, 175, 6, 15],
             [60, 190, 131, 6],
             #левый выступ
             [0, 240, 188, 6],
             [0, 485, 191, 6],
             [185, 240, 6, 245],
             #нижний левый угол
             [60, 530, 126, 6],
             [60, 530, 6, 20],
             [60, 550, 95, 6],
             [180, 535, 6, 105],
             [151, 550, 6, 90],
             [151, 640, 35, 6],
             #отгрызок слева снизу
             [0, 600, 90, 6],
             [0, 640, 90, 6],
             [90, 600, 6, 46],
             #перевернутая Т снизу слева
             [60, 683, 180, 6],
             [60, 683, 6, 20],
             [60, 698, 280, 6],
             [240, 600, 6, 89],
             [240, 600, 36, 6],
             [276, 600, 6, 89],
             [276, 683, 64, 6],
             [334, 683, 6, 20],
             #правый выступ
             [630, 240, 190, 6],
             [630, 240, 6, 245],
             [630, 485, 190, 6],
             #правая однушка сверху
             [630, 175, 130, 6],
             [630, 175, 6, 15],
             [630, 190, 131, 6],
             [755, 175, 6, 15],
             #нижний правый угол
             [630, 530, 126, 6],
             [630, 530, 6, 110],
             [630, 640, 35, 6],
             [661, 550, 6, 96],
             [661, 550, 95, 6],
             [750, 530, 6, 20],
             #отгрызок справа снизу
             [720, 600, 90, 6],
             [720, 600, 6, 46],
             [720, 640, 90, 6],
             #перевернутая Т снизу справа
             [480, 698, 280, 6],
             [480, 683, 6, 20],
             [480, 683, 60, 6],
             [536, 600, 6, 89],
             [536, 600, 36, 6],
             [572, 600, 6, 89],
             [572, 683, 185, 6],
             [754, 683, 6, 20],
             #нижняя Т
             [391, 698, 36, 6],
             [330, 600, 155, 6],
             [330, 600, 6, 36],
             [330, 636, 67, 6],
             [391, 636, 6, 67],
             [485, 600, 6, 36],
             [421, 636, 70, 6],
             [421, 636, 6, 67],
             #средняя Т
             [391, 545, 37, 6],
             [391, 480, 6, 70],
             [423, 480, 6, 70],
             [330, 480, 67, 6],
             [330, 450, 6, 36],
             [330, 450, 155, 6],
             [423, 480, 65, 6],
             [485, 450, 6, 36],
             #спавн
             [330, 330, 60, 6],
             [330, 390, 158, 6],
             [330, 330, 6, 66],
             [432, 330, 56, 6],
             [482, 330, 6, 63],
             #верхняя Т
             [330, 175, 6, 40],
             [330, 175, 158, 6],
             [483, 175, 6, 40],
             [330, 210, 65, 6],
             [420, 210, 68, 6],
             [420, 210, 6, 70],
             [390, 210, 6, 70],
             [390, 280, 36, 6],
             #нижняя правая однушка
             [480, 550, 100, 6],
             [480, 535, 6, 20],
             [480, 535, 100, 6],
             [574, 535, 6, 20],
             #нижняя лева однушка
             [240, 550, 100, 6],
             [240, 535, 6, 20],
             [240, 535, 100, 6],
             [334, 535, 6, 20],
             #однушка посередине справа
             [540, 390, 36, 6],
             [540, 390, 6, 100],
             [540, 484, 36, 6],
             [570, 390, 6, 100],
             #однушка посередине слева
             [240, 390, 36, 6],
             [240, 390, 6, 100],
             [240, 484, 36, 6],
             [270, 390, 6, 100],
             #боком Т справа
             [540, 175, 36, 6],
             [540, 175, 6, 94],
             [570, 175, 6, 160],
             [540, 330, 36, 6],
             [480, 264, 6, 20],
             [480, 264, 64, 6],
             [480, 278, 64, 6],
             [540, 278, 6, 58],
             #боком Т слева
             [240, 175, 36, 6],
             [240, 175, 6, 160],
             [270, 175, 6, 94],
             [240, 329, 36, 6],
             [270, 263, 70, 6],
             [334, 263, 6, 20],
             [270, 277, 70, 6],
             [270, 277, 6, 58],
             ]

    # Пройти по списку. Создайте стену, добавьте ее в список
    for item in walls:
        wall = Wall(item[0], item[1], item[2], item[3], blue)
        wall_list.add(wall)
        all_sprites_list.add(wall)

    # return our new list
    return wall_list

#создаем белую стену где появляются призраки
def setupGate(all_sprites_list):
    gate = pygame.sprite.RenderPlain()
    gate.add(Wall(390, 332, 42, 2, white))
    all_sprites_list.add(gate)
    return gate


# Этот класс представляет мяч
# Он наследуется от класса Sprite в Pygame.
class Block(pygame.sprite.Sprite):

    # Конструктор. Передайте цвет блока,
    # и его положение x и y
    def __init__(self, color, width, height):
        # Вызов конструктора родительского класса (Sprite)
        pygame.sprite.Sprite.__init__(self)

        # Создайте изображение блока и залейте его цветом.
        # Это также может быть изображение, загруженное с диска.
        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.image.set_colorkey(white)
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])

        # Извлекаем прямоугольный объект, имеющий размеры изображения
        # изображение.
        # Обновите положение этого объекта, установив значения
        # rect.x и rect.y
        self.rect = self.image.get_rect()

    # Этот класс представляет собой панель внизу, которой управляет игрок


class Player(pygame.sprite.Sprite):
    # Set speed vector
    change_x = 0
    change_y = 0

    # Constructor function
    def __init__(self, x, y, filename):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Set height, width
        self.image = pygame.image.load(filename).convert()

        # Сделайте наш верхний левый угол местом передачи.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.prev_x = x
        self.prev_y = y

    # Очистить скорость игрока
    def prevdirection(self):
        self.prev_x = self.change_x
        self.prev_y = self.change_y

    # Изменить скорость игрока
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    # Находим новую позицию для игрока
    def update(self, walls, gate):
        # Получаем старую позицию на случай, если нам понадобится вернуться к ней

        old_x = self.rect.left
        new_x = old_x + self.change_x
        prev_x = old_x + self.prev_x
        self.rect.left = new_x

        old_y = self.rect.top
        new_y = old_y + self.change_y
        prev_y = old_y + self.prev_y

        # Это обновление заставило нас застрять?
        x_collide = pygame.sprite.spritecollide(self, walls, False)
        if x_collide:
            # Упс, врезался в стену. Вернитесь на старую позицию
            self.rect.left = old_x
        else:
            self.rect.top = new_y
            # Did this update cause us to hit a wall?
            y_collide = pygame.sprite.spritecollide(self, walls, False)
            if y_collide:
                # Whoops, hit a wall. Go back to the old position
                self.rect.top = old_y

        if gate != False:
            gate_hit = pygame.sprite.spritecollide(self, gate, False)
            if gate_hit:
                self.rect.left = old_x
                self.rect.top = old_y


# Inheritime Player klassist
class Ghost(Player):
    # Изменить скорость призрака
    def changespeed(self, list, ghost, turn, steps, l):
        try:
            z = list[turn][2]
            if steps < z:
                self.change_x = list[turn][0]
                self.change_y = list[turn][1]
                steps += 1
            else:
                if turn < l:
                    turn += 1
                elif ghost == "clyde":
                    turn = 2
                elif ghost == "pinky":
                    turn = 2
                elif ghost == "blinky":
                    turn = 2
                elif ghost == "inky":
                    turn = 2
                else:
                    turn = 0
                self.change_x = list[turn][0]
                self.change_y = list[turn][1]
                steps = 0
            return [turn, steps]
        except IndexError:
            return [0, 0]


Pinky_directions = [
    [4,0,5],
    [0,-4,13],
    [-10,0,10],
    [0,10,19],
    [-6,0,13],
    [0,-10,46],
    [-6,0,28],
    [0,8,14],
    [8,0,20],
    [0,8,6],
    [-8,0,20],
    [0,-8,6],
    [8,0,20],
    [0,-8,14],
    [8,0,19],
    [0,8,14],
    [8,0,16],
    [0,8,10],
    [-8,0,6],
    [0,8,7],
    [8,0,7],
    [0,8,14],
    [-8,0,25],
    [0,-8,6],
    [-8,0,10],
    [0,-8,26],
    [8,0,9],
    [0,8,9],
    [8,0,7],
    [0,8,8],
    [8,0,5],
]

Blinky_directions = [
    [4,0,5],
    [0,-4,13],
    [8,0,4],
    [0,-8,7],
    [8,0,7],
    [0,-8,10],
    [-8,0,6],
    [0,-8,14],
    [8,0,40],
    [0,8,14],
    [-8,0,21],
    [0,8,7],
    [8,0,21],
    [0,-8,22],
    [-8,0,21],
    [0,8,40],
    [-8,0,10],
    [0,8,17],
    [-8,0,7],
    [0,8,7],
    [-8,0,10],
    [0,-8,7],
    [-8,0,19],
    [0,-8,16],
    [8,0,10],
    [0,-8,7],
    [8,0,13],
]

Inky_directions = [
    [4,0,5],
    [0,-4,13],
    [8,0,12],
    [0,8,25],
    [8,0,10],
    [0,8,7],
    [-8,0,10],
    [0,8,10],
    [-8,0,7],
    [0,8,7],
    [-8,0,51],
    [0,-8,7],
    [8,0,21],
    [0,-8,10],
    [8,0,30],
    [0,-8,7],
    [8,0,39],
    [0,8,7],
    [-8,0,12],
    [0,8,11],
    [8,0,11],
    [0,8,7],
    [-8,0,51],
    [0,-8,6],
    [-8,0,6],
    [0,-8,10],
    [-8,0,10],
    [0,-8,7],
    [8,0,10],
    [0,-8,25],
    [8,0,12],
]

Clyde_directions = [
    [4,0,5],
    [0,-4,13],
    [8,0,12],
    [0,8,14],
    [-8,0,25],
    [0,8,10],
    [-8,0,33],
    [0,8,7],
    [8,0,10],
    [0,8,10],
    [8,0,10],
    [0,-8,10],
    [8,0,11],
    [0,8,10],
    [8,0,7],
    [0,8,7],
    [8,0,52],
    [0,-8,7],
    [-8,0,21],
    [0,-8,19],
    [-8,0,17],
    [0,8,9],
    [8,0,6],
    [0,8,10],
    [-8,0,7],
    [0,8,7],
    [-8,0,52],
    [0,-8,7],
    [8,0,11],
    [0,-8,11],
    [-8,0,10],
    [0,-8,9],
    [8,0,22],
    [0,-8,19],
    [8,0,10],
    [0,-8,7],
    [8,0,12],
]

pl = len(Pinky_directions) - 1
bl = len(Blinky_directions) - 1
il = len(Inky_directions) - 1
cl = len(Clyde_directions) - 1

# Вызовите эту функцию, чтобы библиотека Pygame могла инициализировать себя
pygame.init()

# Create an 810x750 sized screen
screen = pygame.display.set_mode([810, 750])

# Это список «спрайтов». Каждый блок программы
# добавлен в этот список. Список управляется классом RenderPlain.


# Устанавливаем заголовок окна
pygame.display.set_caption('Pacman')

# Создаем поверхность, на которой мы можем рисовать
background = pygame.Surface(screen.get_size())

# Используется для преобразования цветных карт и т.п.
background = background.convert()

#экран с черным фоном
background.fill(black)

clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.Font("папка пнг/freesansbold.ttf", 24)

# локации по умолчанию для Pacman и monstas
w = 378  # ширина
h_p = 407 #высота пакмана
h = 346 #высота монстров

def startGame():
    all_sprites_list = pygame.sprite.RenderPlain()

    block_list = pygame.sprite.RenderPlain()

    monsta_list = pygame.sprite.RenderPlain()

    pacman_collide = pygame.sprite.RenderPlain()

    wall_list = setupRoomOne(all_sprites_list)

    gate = setupGate(all_sprites_list)

    p_turn = 0
    p_steps = 0

    b_turn = 0
    b_steps = 0

    i_turn = 0
    i_steps = 0

    c_turn = 0
    c_steps = 0

    # Создайте объект ракетки игрока
    Pacman = Player(w, h_p, "папка пнг/pacman.png")
    all_sprites_list.add(Pacman)
    pacman_collide.add(Pacman)

    Blinky = Ghost(w, h, "папка пнг/Blinky.png")
    monsta_list.add(Blinky)
    all_sprites_list.add(Blinky)

    Pinky = Ghost(w, h, "папка пнг/Pinky.png")
    monsta_list.add(Pinky)
    all_sprites_list.add(Pinky)

    Inky = Ghost(w, h, "папка пнг/Inky.png")
    monsta_list.add(Inky)
    all_sprites_list.add(Inky)

    Clyde = Ghost(w, h, "папка пнг/Clyde.png")
    monsta_list.add(Clyde)
    all_sprites_list.add(Clyde)

    # Рисуем сетку
    for row in range(24):
        for column in range(26):
            if ((column==0  and (row==7 or row==8 or row==9 or row==10 or row==11 or row==12 or row==13 or row==14 or row==15 or row==19 or row==20))
                    or (column==1 and (row==1 or row==2 or row==3 or row==5 or row==7 or row==8 or row==9 or row==10 or row==11 or row==12 or row==13 or row==14 or row==15 or row==17 or row==19 or row==20 or row==22))
                    or (column==2 and (row==1 or row==2 or row==3 or row==5 or row==7 or row==8 or row==9 or row==10 or row==11 or row==12 or row==13 or row==14 or row==15 or row==17 or row==19 or row==20 or row==22))
                    or (column==3 and (row==1 or row==2 or row==3 or row==5 or row==7 or row==8 or row==9 or row==10 or row==11 or row==12 or row==13 or row==14 or row==15 or row==17 or row==22))
                    or (column==4 and (row==1 or row==2 or row==3 or row==5 or row==7 or row==8 or row==9 or row==10 or row==11 or row==12 or row==13 or row==14 or row==15 or row==17 or row==18 or row==19 or row==20 or row==22))
                    or (column==5 and (row==1 or row==2 or row==3 or row==5 or row==7 or row==8 or row==9 or row==10 or row==11 or row==12 or row==13 or row==14 or row==15 or row==17 or row==18 or row==19 or row==20 or row==22))
                    or (column==6 and row==22)
                    or (column==7 and (row==1 or row==2 or row==3 or row==5 or row==6 or row==7 or row==8 or row==9 or row==10 or row==12 or row==13 or row==14 or row==15 or row==17 or row==19 or row==20 or row==21 or row==22))
                    or (column==8 and (row==1 or row==2 or row==3 or row==5 or row==6 or row==7 or row==8 or row==9 or row==10 or row==12 or row==13 or row==14 or row==15 or row==17 or row==19 or row==20 or row==21 or row==22))
                    or (column==9 and (row==1 or row==2 or row==3 or row==8 or row==17 or row==22))
                    or (column==10 and (row==1 or row==2 or row==3 or row==5 or row==6 or row==8 or row==10 or row==11 or row==12 or row==14 or row==15 or row==17 or row==19 or row==20 or row==22))
                    or (column==11 and (row==5 or row==6 or row==10 or row==11 or row==12 or row==14 or row==15 or row==19 or row==20))
                    or (column==12 and (row==0 or row==1 or row==2 or row==3 or row==5 or row==6 or row==7 or row==8 or row==10 or row==11 or row==12 or row==14 or row==15 or row==16 or row==17 or row==19 or row==20 or row==21 or row==22))
                    or (column==13 and (row==0 or row==1 or row==2 or row==3 or row==5 or row==6 or row==7 or row==8 or row==10 or row==11 or row==12 or row==14 or row==15 or row==16 or row==17 or row==19 or row==20 or row==21 or row==22))
                    or (column==14 and (row==5 or row==6 or row==10 or row==11 or row==12 or row==14 or row==15 or row==19 or row==20))
                    or (column==15 and (row==1 or row==2 or row==3 or row==5 or row==6 or row==8 or row==10 or row==11 or row==12 or row==14 or row==15 or row==17 or row==19 or row==20 or row==22))
                    or (column == 16 and (row == 1 or row == 2 or row == 3 or row == 8 or row == 17 or row == 22))
                    or (column == 17 and (row == 1 or row == 2 or row == 3 or row == 5 or row == 6 or row == 7 or row == 8 or row == 9 or row == 10 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 19 or row == 20 or row == 21 or row == 22))
                    or (column == 18 and (row == 1 or row == 2 or row == 3 or row == 5 or row == 6 or row == 7 or row == 8 or row == 9 or row == 10 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 19 or row == 20 or row == 21 or row == 22))
                    or (column == 19 and row == 22)
                    or (column == 20 and (row == 1 or row == 2 or row == 3 or row == 5 or row == 7 or row == 8 or row == 9 or row == 10 or row == 11 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 18 or row == 19 or row == 20 or row == 22))
                    or (column == 21 and (row == 1 or row == 2 or row == 3 or row == 5 or row == 7 or row == 8 or row == 9 or row == 10 or row == 11 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 18 or row == 19 or row == 20 or row == 22))
                    or (column == 22 and (row == 1 or row == 2 or row == 3 or row == 5 or row == 7 or row == 8 or row == 9 or row == 10 or row == 11 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 22))
                    or (column == 23 and (row == 1 or row == 2 or row == 3 or row == 5 or row == 7 or row == 8 or row == 9 or row == 10 or row == 11 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 19 or row == 20 or row == 22))
                    or (column == 24 and (row == 1 or row == 2 or row == 3 or row == 5 or row == 7 or row == 8 or row == 9 or row == 10 or row == 11 or row == 12 or row == 13 or row == 14 or row == 15 or row == 17 or row == 19 or row == 20 or row == 22))
                    or (column==25  and (row==7 or row==8 or row==9 or row==10 or row==11 or row==12 or row==13 or row==14 or row==15 or row==19 or row==20))
                    ):
                continue
            else:
                block = Block(yellow, 4, 4)

                # Установите случайное место для блока
                block.rect.x = (30 * column + 6) + 26
                block.rect.y = (30 * row + 6) + 26

                b_collide = pygame.sprite.spritecollide(block, wall_list, False)
                p_collide = pygame.sprite.spritecollide(block, pacman_collide, False)
                if b_collide:
                    continue
                elif p_collide:
                    continue
                else:
                    # Добавляем блок в список объектов
                    block_list.add(block)
                    all_sprites_list.add(block)

    bll = len(block_list)

    score = 0

    done = False

    i = 0

    while done == False:
        # ВСЯ ОБРАБОТКА СОБЫТИЙ ДОЛЖНА РАСПОЛОЖАТЬСЯ НИЖЕ ЭТОГО КОММЕНТАРИЯ
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Pacman.changespeed(-30, 0)
                if event.key == pygame.K_RIGHT:
                    Pacman.changespeed(30, 0)
                if event.key == pygame.K_UP:
                    Pacman.changespeed(0, -30)
                if event.key == pygame.K_DOWN:
                    Pacman.changespeed(0, 30)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    Pacman.changespeed(30, 0)
                if event.key == pygame.K_RIGHT:
                    Pacman.changespeed(-30, 0)
                if event.key == pygame.K_UP:
                    Pacman.changespeed(0, 30)
                if event.key == pygame.K_DOWN:
                    Pacman.changespeed(0, -30)

        # ВСЯ ОБРАБОТКА СОБЫТИЙ ДОЛЖНА НАХОДИТЬСЯ ВЫШЕ ЭТОГО КОММЕНТАРИЯ

        # ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА РАСПОЛОЖАТЬСЯ НИЖЕ ЭТОГО КОММЕНТАРИЯ
        Pacman.update(wall_list, gate)

        returned = Pinky.changespeed(Pinky_directions, "pinky", p_turn, p_steps, pl)
        p_turn = returned[0]
        p_steps = returned[1]
        Pinky.changespeed(Pinky_directions, "pinky", p_turn, p_steps, pl)
        Pinky.update(wall_list, False)

        returned = Blinky.changespeed(Blinky_directions, "blinky", b_turn, b_steps, bl)
        b_turn = returned[0]
        b_steps = returned[1]
        Blinky.changespeed(Blinky_directions, "blinky", b_turn, b_steps, bl)
        Blinky.update(wall_list, False)

        returned = Inky.changespeed(Inky_directions, "inky", i_turn, i_steps, il)
        i_turn = returned[0]
        i_steps = returned[1]
        Inky.changespeed(Inky_directions, "inky", i_turn, i_steps, il)
        Inky.update(wall_list, False)

        returned = Clyde.changespeed(Clyde_directions, "clyde", c_turn, c_steps, cl)
        c_turn = returned[0]
        c_steps = returned[1]
        Clyde.changespeed(Clyde_directions, "clyde", c_turn, c_steps, cl)
        Clyde.update(wall_list, False)

        # Посмотрите, не столкнулся ли с чем-нибудь блок Pacman.
        blocks_hit_list = pygame.sprite.spritecollide(Pacman, block_list, True)

        # Проверьте список коллизий.
        if len(blocks_hit_list) > 0:
            score += len(blocks_hit_list)

        # ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА ВЫШЕ ЭТОГО КОММЕНТАРИЯ

        # ВЕСЬ КОД ДЛЯ РИСУНКА ДОЛЖЕН РАСПОЛОЖАТЬСЯ НИЖЕ ЭТОГО КОММЕНТАРИЯ
        screen.fill(black)

        wall_list.draw(screen)
        gate.draw(screen)
        all_sprites_list.draw(screen)
        monsta_list.draw(screen)

        text = font.render("Score: " + str(score) + "/" + str(bll), True, red)
        screen.blit(text, [10, 10])

        if score == bll:
            doNext("Congratulations, you won!", 145, all_sprites_list, block_list, monsta_list, pacman_collide,
                   wall_list, gate)

        monsta_hit_list = pygame.sprite.spritecollide(Pacman, monsta_list, False)

        if monsta_hit_list:
            doNext("Game Over", 235, all_sprites_list, block_list, monsta_list, pacman_collide, wall_list, gate)

        # ВЕСЬ КОД ДЛЯ РИСУНКА ДОЛЖЕН РАСХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ

        pygame.display.flip()

        clock.tick(10)


def doNext(message, left, all_sprites_list, block_list, monsta_list, pacman_collide, wall_list, gate):
    while True:
        # ВСЯ ОБРАБОТКА СОБЫТИЙ ДОЛЖНА РАСПОЛОЖАТЬСЯ НИЖЕ ЭТОГО КОММЕНТАРИЯ
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_RETURN:
                    del all_sprites_list
                    del block_list
                    del monsta_list
                    del pacman_collide
                    del wall_list
                    del gate
                    startGame()

        # Серый фон
        w = pygame.Surface((400, 200))  # размер вашего прямоугольника
        w.set_alpha(10)  # альфа-уровень
        w.fill((128, 128, 128))  # это заполняет всю поверхность
        screen.blit(w, (100, 200))  # (0,0) — координаты верхнего левого угла.

        # Won or lost
        text1 = font.render(message, True, white)
        screen.blit(text1, [left, 233])

        text2 = font.render("To play again, press ENTER.", True, white)
        screen.blit(text2, [135, 303])
        text3 = font.render("To quit, press ESCAPE.", True, white)
        screen.blit(text3, [165, 333])

        pygame.display.flip()

        clock.tick(10)


startGame()

pygame.quit()