import pygame

import random


SEGMENT_SIZE = 150
SEGMENT_MARGIN = 10
SEGMENT_STEP = SEGMENT_SIZE + SEGMENT_MARGIN

class Segments(object):
    def __init__(self, segment_color="#CAC0B4"):
        self.segment_size = SEGMENT_SIZE
        self.segment_margin = SEGMENT_MARGIN
        self.segment_color = segment_color
        self.segments = []
        for i in range(1, screen_height // self.segment_size + 1):
            for k in range(1, screen_width // self.segment_size + 1):
                current = (
                    self.segment_margin * k + self.segment_size * (k - 1),
                    self.segment_margin * i + self.segment_size * (i - 1),
                )
                self.segments.append(current)

    def segments_draw(self, screen):
        for segment in self.segments:
            pygame.draw.rect(screen, self.segment_color, (*segment, self.segment_size, self.segment_size), border_radius=3)


class PlayableSegments(Segments):
    def __init__(self):
        super().__init__(segment_color = "#ECE5DB")
        self.active_segments = [ self.segments[random.randrange(len(self.segments))], self.segments[random.randrange(len(self.segments))] ]
        self.x, self.y = None, None
        self.direction = None

    def move(self):
        if self.direction == 'up':
            bump = False
            while not bump:
                if self.y > 10:
                    self.y -= 160
                else:
                    bump = True
        elif self.direction == 'down':
            bump = False
            while not bump:
                if self.y < 490:
                    self.y += 160
                else:
                    bump = True
        elif self.direction == 'left':
            bump = False
            while not bump:
                if self.x > 10:
                    self.x -= 160
                else:
                    bump = True
        elif self.direction == 'right':
            bump = False
            while not bump:
                if self.x < 490:
                    self.x += 160
                else:
                    bump = True

    def merge(self):
        pass

    def draw(self, screen):
        for x, y in self.active_segments:
            pygame.draw.rect(screen, self.segment_color,
                         (x, y, self.segment_size, self.segment_size), border_radius=3)



screen_width, screen_height = 650, 650
def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("2048")


    field = Segments()
    segments = PlayableSegments()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            segments.direction = "up"
            segments.move()
        elif keys[pygame.K_DOWN]:
            segments.direction = "down"
            segments.move()
        elif keys[pygame.K_LEFT]:
            segments.direction = "left"
            segments.move()
        elif keys[pygame.K_RIGHT]:
            segments.direction = "right"
            segments.move()



        screen.fill("#B9ADA1")
        field.segments_draw(screen)
        segments.draw(screen)
        pygame.display.update()
    pygame.quit()



if __name__ == '__main__':
    main()