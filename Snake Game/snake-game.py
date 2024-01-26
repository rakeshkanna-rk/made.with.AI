import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
SNAKE_SPEED = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize clock
clock = pygame.time.Clock()

# Snake initial position and direction
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
direction = (1, 0)

# Apple initial position
apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Score
score = 0

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_apple(apple):
    pygame.draw.rect(screen, RED, (apple[0] * GRID_SIZE, apple[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def check_collision(snake):
    head = snake[0]
    if head in snake[1:]:
        return True
    if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
        return True
    return False

def move_snake(snake, direction):
    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])
    snake.insert(0, new_head)

def handle_input(direction):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, 1):
        return (0, -1)
    if keys[pygame.K_DOWN] and direction != (0, -1):
        return (0, 1)
    if keys[pygame.K_LEFT] and direction != (1, 0):
        return (-1, 0)
    if keys[pygame.K_RIGHT] and direction != (-1, 0):
        return (1, 0)
    return direction

def show_score(score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def show_game_over():
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", True, RED)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

def show_try_again():
    font = pygame.font.Font(None, 36)
    text = font.render("Press SPACE to Try Again", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + 50))


def main():
    global direction, apple, score

    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]  # Initialize snake within the main function
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not game_over:
            direction = handle_input(direction)

            # Create a new head based on the current direction
            head = snake[0]
            new_head = (head[0] + direction[0], head[1] + direction[1])

            # Check if the new head coincides with the apple
            if new_head == apple:
                score += 1
                apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            else:
                # Remove the last segment to keep the same length
                snake.pop()

            # Add the new head to the snake
            snake.insert(0, new_head)

            if check_collision(snake):
                game_over = True

            screen.fill((0, 0, 0))
            draw_grid()
            draw_snake(snake)
            draw_apple(apple)
            show_score(score)
        else:
            screen.fill((0, 0, 0))
            show_game_over()
            show_score(score)
            show_try_again()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
                direction = (1, 0)
                apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
                score = 0
                game_over = False

        pygame.display.flip()

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    print("Game Over! Your Score:", score)

if __name__ == "__main__":
    main()
