import pygame  # Impordime pygame'i mooduli
pygame.init()  # Initsialiseerime pygame'i

screen = pygame.display.set_mode([300, 300])  # Loome ekraani mõõtudega 300x300 pikslit
pygame.display.set_caption("My Screen")  # Seame aknale pealkirja
screen.fill([0, 0, 0])  # Täidame ekraani musta värviga

# Joonistame halli ristküliku
pygame.draw.rect(screen, [179, 179, 179], [95, 35, 110, 210], 0)
# Joonistame ristküliku piiri
pygame.draw.rect(screen, [51, 51, 51], [100, 40, 100, 200], 2)
# Joonistame punase ringi
pygame.draw.circle(screen, [204, 41, 0], [150, 80], 28, 0)
# Joonistame oranži ringi
pygame.draw.circle(screen, [255, 153, 0], [150, 140], 28, 0)
# Joonistame rohelise ringi
pygame.draw.circle(screen, [51, 204, 51], [150, 200], 28, 0)

pygame.display.flip()  # Värskendame ekraani

running = True  # Määrame muutuja "running" väärtuseks True
while running:  # Algatame pealoogi
    for event in pygame.event.get():  # Kontrollime sündmusi
        if event.type == pygame.QUIT:  # Kui sündmus on aken sulgemine
            running = False  # Lõpetame pealoogi töö

    pygame.display.flip()  # Värskendame ekraani

pygame.quit()  # Lõpetame pygame'i kasutamise
