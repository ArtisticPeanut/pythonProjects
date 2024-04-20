from collections import deque
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def move_blank(board, direction):
    blank_row, blank_col = find_blank(board)

    if direction == 'up' and blank_row > 0:
        board[blank_row][blank_col], board[blank_row - 1][blank_col] = board[blank_row - 1][blank_col], board[blank_row][blank_col]
    elif direction == 'left' and blank_col > 0:
        board[blank_row][blank_col], board[blank_row][blank_col - 1] = board[blank_row][blank_col - 1], board[blank_row][blank_col]
    elif direction == 'down' and blank_row < 2:
        board[blank_row][blank_col], board[blank_row + 1][blank_col] = board[blank_row + 1][blank_col], board[blank_row][blank_col]
    elif direction == 'right' and blank_col < 2:
        board[blank_row][blank_col], board[blank_row][blank_col + 1] = board[blank_row][blank_col + 1], board[blank_row][blank_col]

def find_blank(board):
    for i in range(3):
        for z in range(3):
            if board[i][z] == 0:
                return i, z

def generate_the_puzzle(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def is_goal_state(board, final_state):
    return board == final_state

def bfs(initial_puzzle_state, final_state):
    queue = deque([(initial_puzzle_state, [])])

    while queue:
        current_state, path = queue.popleft()
        # print(current_state)
        # generate_visual_puzzle(current_state)

        if is_goal_state(current_state, final_state):
            return current_state  # Return the final state when a solution is found

        for direction in ['right', 'left', 'up', 'down']:
            new_state = [row.copy() for row in current_state]
            move_blank(new_state, direction)

            if new_state not in [state for state, _ in queue] + [current_state]:
                new_path = path + [direction]
                queue.append((new_state, new_path))

    return None

def generate_visual_puzzle(board):
    # Flatten the nested list and concatenate the parts horizontally
    visual_puzzle = np.concatenate([np.concatenate(row, axis=1) for row in board], axis=0)
    plt.imshow(visual_puzzle, cmap='Blues', interpolation='nearest')
    plt.xticks([])
    plt.yticks([])
    plt.show()


def image_to_puzzle(image_path):
    img = Image.open(image_path)
    img = img.resize((300, 300))  # Resize the image to fit a 3x3 puzzle
    img_array = np.array(img)
    
    # Split the image into 3x3 parts
    puzzle = [np.hsplit(row, 3) for row in np.vsplit(img_array, 3)]
    
    return puzzle


if __name__ == "__main__":
    # Change the image path to the desired input image
    input_image_path ="tes_images/roses2.jpeg"

    
    initial_puzzle = image_to_puzzle(input_image_path)
    print(f"this is the final image",initial_puzzle)
    final_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    print("Initial state:")
    generate_the_puzzle(initial_puzzle)
    generate_visual_puzzle(initial_puzzle)

    print("Final State")
    print(" ")
    print(" ")
    
    final_puzzle_state = bfs(initial_puzzle, final_state)

    if final_puzzle_state:
        print("Final State of the Puzzle:")
        generate_the_puzzle(final_puzzle_state)
        generate_visual_puzzle(final_puzzle_state)
    else:
        print("No solution found.")
