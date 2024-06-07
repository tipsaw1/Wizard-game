import pygame

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 780))
clock = pygame.time.Clock()
running = True


# Function to calculate movement at a consistent speed at an angle
def calculate_movement(my_pos, target_pos, speed):
    x_distance = target_pos[0] - my_pos[0]
    y_distance = target_pos[1] - my_pos[1]
    total_distance = (x_distance ** 2 + y_distance ** 2) ** 0.5

    ratio = speed / total_distance

    dx, dy = x_distance * ratio, y_distance * ratio

    return dx, dy

# Function to determine if a circle is colliding with another circle
# circle_center = (x, y), target_center = (x, y)
def collide_circle_circle(circle_center, circle_radius, target_center, target_radius):
    pass

# Function to determine if a circle is colliding with a rectangle
# circle_center = (x, y), target_pos = (x, y) of the top left corner, target_size = (width, height)
def collide_circle_rect(circle_center, circle_radius, target_pos, target_size):
    pass

# Player class & Information
class Player:
    # Initialize class w/ variables
    # pos = (x, y), size = (width, height)
    def __init__(self, hp, pos, size):
        self.rect = pygame.Rect((0, 0), size)
        self.rect.center = pos
        self.max_hp = hp
        self.hp = hp
        self.dx, self.dy = 0, 0
        self.speed = 5

    # Draw an ellipse at the player's position, then reset the velocity
    def update(self):
        pygame.draw.ellipse(screen, "purple", self.rect)
        self.dx, self.dy = 0, 0

    # Move the player
    def move(self):
        self.dx, self.dy = calculate_movement(self.rect.center, (self.rect.centerx + self.dx, self.rect.centery + self.dy), self.speed)
        self.rect.centerx += self.dx
        self.rect.centery += self.dy


# Player 1 instance
p1 = Player(100, (screen.get_width() // 2, screen.get_height() // 2), (20, 20))

# Game loop
while running:

    # Background color
    screen.fill("black")

    # Events
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            running = False

    # Collect keyboard input
    key = pygame.key.get_pressed()

    # Arrow key player movement
    if key[pygame.K_RIGHT]:
        p1.dx += 1
    if key[pygame.K_DOWN]:
        p1.dy += 1
    if key[pygame.K_LEFT]:
        p1.dx -= 1
    if key[pygame.K_UP]:
        p1.dy -= 1

    if p1.dx != 0 or p1.dy != 0:
        p1.move()

    # Draw player
    p1.update()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
