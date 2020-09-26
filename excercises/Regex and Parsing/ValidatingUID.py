import re

if __name__ == '__main__':
    N = int(input())

    character_validation = re.compile(r'^(?=.*\d.*\d.*\d.*)(?=.*[A-Z].*[A-Z].*)[a-zA-Z0-9]{10}$')
    duplicate_character_validation = re.compile(r'^.*(\w).*\1.*$')

    for _ in range(N):
        line = input()
        print("Valid" if character_validation.match(line) and not duplicate_character_validation.match(
            line) else "Invalid")
