def rprint(text):
    counter = 0
    for i in range(int(len(text) / 8)):
        for c in range(30, 38):
            try:
                print(f"\033[0;{c}m{text[counter]}\033[0m", end="")
                counter += 1
            except IndexError:
                pass
    for i in range(len(text) % 8):
        for c in range(30, 38):
            try:
                print(f"\033[0;{c}m{text[counter]}\033[0m", end="")
                counter += 1
            except IndexError:
                pass
