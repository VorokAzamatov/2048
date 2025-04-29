

# import pygame
#
# import random
# import copy
#
#
# SEGMENT_SIZE = 150
# SEGMENT_MARGIN = 10
# SEGMENT_STEP = SEGMENT_SIZE + SEGMENT_MARGIN
#
# class Segments(object):
#     def __init__(self, segment_color="#CAC0B4"):
#         self.segment_size = SEGMENT_SIZE
#         self.segment_margin = SEGMENT_MARGIN
#         self.segment_color = segment_color
#         self.segments = []
#         for i in range(1, screen_height // self.segment_size + 1):
#             for k in range(1, screen_width // self.segment_size + 1):
#                 current = [
#                     self.segment_margin * k + self.segment_size * (k - 1),
#                     self.segment_margin * i + self.segment_size * (i - 1),
#                 ]
#                 self.segments.append(current)
#
#     def segments_draw(self, screen):
#         for segment in self.segments:
#             pygame.draw.rect(screen, self.segment_color, (*segment, self.segment_size, self.segment_size), border_radius=3)
#
#
# class PlayableSegments(Segments):
#     def __init__(self):
#         super().__init__(segment_color = "#ECE5DB")
#         self.active_segments = [
#             [self.segments[random.randrange(len(self.segments))], 2],
#             [self.segments[random.randrange(len(self.segments))], 2]
#         ]
#         print(self.active_segments)
#         # self.active_segments = [ self.segments[10], self.segments[2] ]
#         self.x, self.y = None, None
#         self.direction = None
#
#     def move(self):
#         for i in range(0, len(self.active_segments)):
#             segments_without_current = copy.deepcopy(self.active_segments)
#             del segments_without_current[i][0]
#
#             print(segments_without_current)
#             self.x, self.y = self.active_segments[i][0]
#             if self.direction == 'up':
#                 bump = False
#                 while not bump:
#                     if self.y > 10 and [self.x, self.y - SEGMENT_STEP] not in segments_without_current[i+1][0]:
#                         self.y -= SEGMENT_STEP
#                     else:
#                         bump = True
#             elif self.direction == 'down':
#                 bump = False
#                 while not bump:
#                     if self.y < 490 and [self.x, self.y + SEGMENT_STEP] not in segments_without_current:
#                         self.y += SEGMENT_STEP
#                     else:
#                         bump = True
#             elif self.direction == 'left':
#                 bump = False
#                 while not bump:
#                     if self.x > 10 and [self.x - SEGMENT_STEP, self.y] not in segments_without_current:
#                         self.x -= SEGMENT_STEP
#                     else:
#                         bump = True
#             elif self.direction == 'right':
#                 bump = False
#                 while not bump:
#                     if self.x < 490:
#                         self.x += SEGMENT_STEP
#                     else:
#                         bump = True
#             self.active_segments[i][0][0] = self.x
#             self.active_segments[i][0][1] = self.y
#
#     def merge(self):
#         pass
#
#     def draw(self, screen):
#         for i in range(0, len(self.active_segments)):
#             pygame.draw.rect(screen, self.segment_color,
#                          (*tuple(self.active_segments[i][0]), self.segment_size, self.segment_size), border_radius=3)
#
#
#
# screen_width, screen_height = 650, 650
# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((screen_width, screen_height))
#     pygame.display.set_caption("2048")
#
#
#     field = Segments()
#     segments = PlayableSegments()
#
#
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
#
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_UP]:
#             segments.direction = "up"
#             segments.move()
#         elif keys[pygame.K_DOWN]:
#             segments.direction = "down"
#             segments.move()
#         elif keys[pygame.K_LEFT]:
#             segments.direction = "left"
#             segments.move()
#         elif keys[pygame.K_RIGHT]:
#             segments.direction = "right"
#             segments.move()
#
#
#
#         screen.fill("#B9ADA1")
#         field.segments_draw(screen)
#         segments.draw(screen)
#         pygame.display.update()
#     pygame.quit()
#
#
#
# if __name__ == '__main__':
#     main()
#
#
#
#
#
#
#
# # segment_size = 150
# # segment_margin = 10
# #
# # list = []
# #
# # for i in range(1, 5):
# #     for k in range(1, 5):
# #         current = (segment_margin * k + segment_size * (k - 1),segment_margin * i + segment_size * (i - 1))
# #         list.append(current)
# #
# #
# # print(list)