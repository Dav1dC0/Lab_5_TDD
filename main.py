import random
import pytest
from snake_game import SnakeGame

class SnakeGame:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.snake = [(width // 2, height // 2)]  # Initial snake position
        self.direction = 'up'  # Initial direction
        self.food_position = None
        self.score = 0
        self.game_over = False

    def move_snake(self, direction):
        # Update snake direction
        self.direction = direction

        # Move snake body
        head = self.snake[0]
        if direction == 'up':
            new_head = (head[0], head[1] - 1)
        elif direction == 'down':
            new_head = (head[0], head[1] + 1)
        elif direction == 'left':
            new_head = (head[0] - 1, head[1])
        elif direction == 'right':
            new_head = (head[0] + 1, head[1])

        # Check for collisions
        if new_head in self.snake or not (0 <= new_head[0] < self.width) or not (0 <= new_head[1] < self.height):
            self.game_over = True
        else:
            self.snake.insert(0, new_head)
            if new_head == self.food_position:
                self.score += 1
                self.generate_food()
            else:
                self.snake.pop()

    def generate_food(self):
        # Generate food at a random position not occupied by the snake
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) not in self.snake:
                self.food_position = (x, y)
                break

    def get_score(self):
        return self.score

    def is_game_over(self):
        return self.game_over



def game():
    return SnakeGame()

def test_initial_snake_length(game):
    assert len(game.snake) == 1

def test_initial_score(game):
    assert game.score == 0

def test_snake_movement(game):
    # Test that the snake moves correctly when given directions
    game.move_snake('up')
    assert game.snake.direction == 'up'

    game.move_snake('left')
    assert game.snake.direction == 'left'

    # Add more tests for other directions

def test_food_generation(game):
    # Test that food is generated at valid positions
    game.generate_food()
    assert game.food_position is not None
    assert game.food_position not in game.snake.body

def test_collision_with_self(game):
    # Test that the game detects collision with the snake's own body
    # Set up a scenario where the snake collides with itself
    # Assert that the game ends when the snake collides with itself

def test_collision_with_walls(game):
    # Test that the game detects collision with the walls
    # Set up a scenario where the snake collides with a wall
    # Assert that the game ends when the snake collides with a wall

def test_score_increase(game):
    # Test that the score increases when the snake eats food
    initial_score = game.score
    game.eat_food()
    assert game.score == initial_score + 1

def test_game_over_condition(game):
    # Test that the game ends when the snake collides with itself or with a wall
    # Set up scenarios for both cases and assert that the game ends

# Add more test cases as needed

if __name__ == "__main__":
    pytest.main()
