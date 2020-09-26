import re


def load_matrix():
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    matrix = []

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    return matrix


def transpose_flatten(matrix):
    text = []

    rows, cols = len(matrix), len(matrix[0])

    for c in range(cols):
        for r in range(rows):
            text.append(matrix[r][c])

    return ''.join(text)


def regex_decoder(text):
    spaces = r'([a-zA-Z0-9])([^a-zA-Z0-9]+)([a-zA-Z0-9])'
    spaces = re.compile(spaces)

    text = spaces.sub(r'\1 \3', text)
    return text


if __name__ == '__main__':
    matrix = load_matrix()
    text = transpose_flatten(matrix)
    print(regex_decoder(text))
