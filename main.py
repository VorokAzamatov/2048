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
        self.active_segments = {
            tuple(self.segments[random.randrange(len(self.segments))]) : 2,
            tuple(self.segments[random.randrange(len(self.segments))]) : 2
        }
        # self.active_segments = [ self.segments[10], self.segments[2] ]
        self.direction = None

    def move(self):
        new_active_segments = {}
        # print("---------------")
        # print("all segments: ", segments_to_move)
        for segment, value in self.active_segments.items():
            segments_without_current = self.active_segments.copy()
            del segments_without_current[segment]
            # print("segments_without_current: ", segments_without_current)

            x, y = segment
            # print("x, y: ", new_x, new_y)
            if self.direction == 'up':
                new_y = y
                while new_y > SEGMENT_MARGIN:
                    new_y -= SEGMENT_STEP
                    potential_position = (x, new_y)
                    if potential_position in self.active_segments and value == self.active_segments[potential_position]:
                        value *= 2
                        break
                    elif potential_position in self.active_segments:
                        new_y += SEGMENT_STEP
                        break
                new_active_segments[(x, new_y)] = value
            elif self.direction == 'down':
                new_y = y
                while new_y < screen_height - SEGMENT_SIZE - SEGMENT_MARGIN:
                    new_y += SEGMENT_STEP
                    potential_position = (x, new_y)
                    if potential_position in self.active_segments and value == self.active_segments[potential_position]:
                        value *= 2
                        break
                    elif potential_position in self.active_segments:
                        new_y -= SEGMENT_STEP
                        break
                new_active_segments[(x, new_y)] = value
            elif self.direction == 'left':
                new_x = x
                while new_x > SEGMENT_MARGIN:
                    new_x -= SEGMENT_STEP
                    potential_position = (new_x, y)
                    if potential_position in self.active_segments and value == self.active_segments[potential_position]:
                        value *= 2
                        break
                    elif potential_position in self.active_segments:
                        new_x += SEGMENT_STEP
                        break
                new_active_segments[(new_x, y)] = value
            elif self.direction == 'right':
                new_x = x
                while new_x < screen_width - SEGMENT_SIZE - SEGMENT_MARGIN:
                    new_x += SEGMENT_STEP
                    potential_position = (new_x, y)
                    if potential_position in self.active_segments and value == self.active_segments[potential_position]:
                        value *= 2
                        break
                    elif potential_position in self.active_segments:
                        new_x -= SEGMENT_STEP
                        break
                new_active_segments[(new_x, y)] = value

        self.active_segments = new_active_segments


    def spawn_new_segment(self):
        available_segments = [segment for segment in self.segments if segment not in self.active_segments]
        if available_segments:
            new_segment = random.choice(available_segments)
            self.active_segments[new_segment] = 2

    def merge(self):
        pass

    def draw(self, screen):
        for segment in self.active_segments:
            if self.active_segments[segment] == 2:
                color = "#ECE5DB"
            elif self.active_segments[segment] == 4:
                color = "#EBE0CA"
            elif self.active_segments[segment] == 8:
                color = "#E8B482"
            elif self.active_segments[segment] == 16:
                color = "#E89A6C"
            elif self.active_segments[segment] == 32:
                color = "#E68266"
            pygame.draw.rect(screen, color,
                         (*segment, self.segment_size, self.segment_size), border_radius=3)



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
                segments.spawn_new_segment()
            elif keys[pygame.K_DOWN]:
                segments.direction = "down"
                segments.move()
                segments.spawn_new_segment()
            elif keys[pygame.K_LEFT]:
                segments.direction = "left"
                segments.move()
                segments.spawn_new_segment()
            elif keys[pygame.K_RIGHT]:
                segments.direction = "right"
                segments.move()
                segments.spawn_new_segment()




        screen.fill("#B9ADA1")
        field.segments_draw(screen)
        segments.draw(screen)
        pygame.display.update()
    pygame.quit()



if __name__ == '__main__':
    main()