import pygame  # Impordime pygame'i mooduli
pygame.init()  # Initsialiseerime pygame'i

screen = pygame.display.set_mode([300, 300])  # Loome ekraani mõõtudega 300x300 pikslit
pygame.display.set_caption("My Screen")  # Seame aknale pealkirja
screen.fill([0, 0, 0])  # Täidame ekraani musta värviga

# Joonistame kolm valget ringi
pygame.draw.circle(screen, [255, 255, 255], [150, 80], 30, 0)
pygame.draw.circle(screen, [255, 255, 255], [150, 150], 40, 0)
pygame.draw.circle(screen, [255, 255, 255], [150, 240], 50, 0)

# Joonistame kaks musta silma
pygame.draw.circle(screen, [51, 0, 0], [140, 75], 5, 0)
pygame.draw.circle(screen, [51, 0, 0], [160, 75], 5, 0)

# Määratleme kolmnurga tipud
tipp1 = [150, 80 - 20 + 45]
tipp2 = [140, 80 - 40 + 45]
tipp3 = [160, 80 - 40 + 45]

# Joonistame täidetud kolmnurga
pygame.draw.polygon(screen, [255, 153, 51], [tipp1, tipp2, tipp3], 0)

pygame.display.flip()  # Värskendame ekraani

running = True  # Määrame muutuja "running" väärtuseks True
while running:  # Algatame pealoogi
    for event in pygame.event.get():  # Kontrollime sündmusi
        if event.type == pygame.QUIT:  # Kui sündmus on aken sulgemine
            running = False  # Lõpetame pealoogi töö

    pygame.display.flip()  # Värskendame ekraani

pygame.quit()  # Lõpetame pygame'i kasutamise
