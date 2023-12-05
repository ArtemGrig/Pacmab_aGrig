
#создание музыки
pygame.mixer.init()
pygame.mixer.music.load('pacman.mp3')
pygame.mixer.music.play(-1, 0.0)

#добавление пнг формата в игру
Pacman = Player(w, p_h, "папка пнг/pacman.png")
    all_sprites_list.add(Pacman)
    pacman_collide.add(Pacman)