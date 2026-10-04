import time

RED = "\u001b[41m"
RED1 = "\u001b[31m"
GREEN = "\u001b[102m"
YELLOW = "\u001b[103m"
BLACK = "\u001b[40m"
WHITE = "\u001b[47m"
END = "\u001b[0m"


def flag():
    pixel = "   "
    length = 12
    width = length // 3 * 2
    for i in range(width):
        if i < width // 2:
            print(GREEN + pixel * (length // 3) + YELLOW + pixel * (length // 3 * 2) + END)
        else:
            print(GREEN + pixel * (length // 3) + RED + pixel * (length // 3 * 2) + END)


def sequence():
    with open("sequence.txt", "r") as file:
        neg = 0
        pos = 0
        for line in file:
            num = float(line)
            if -5 < num < 0:
                neg += 1
            elif 0 < num < 5:
                pos += 1

    print(neg + pos, neg, pos)
    print(f"{GREEN}{' ' * round(neg / (neg + pos) * 100)}{END} {round(neg / (neg + pos) * 100, 2)}%")
    print(f"{RED}{' ' * round(pos / (neg + pos) * 100)}{END} {round(pos / (neg + pos) * 100, 2)}%")


def uzor():
    size = 8
    pixel = "   "
    half = size // 2
    colors = [87, 196, 226]

    while True:
        for col in colors:
            bg = f"\u001b[48;5;{col}m"

            for row in range(size + 1):
                offset = abs(half - row)
                width = 2 * (half - offset) + 1

                print(
                    pixel * offset +
                    bg + pixel * width + END +
                    pixel * (2 * offset - 1) +
                    bg + pixel * (width - (offset == 0)) + END
                )

            print(f"\u001b[{size + 1}A", end="")
            time.sleep(0.5)


def graph():
    plot_list = [[f"{y} "] + [RED1 + "-@-" + END if y == x + 1 else "-+-" for x in range(1, 10)] for y in range(1, 10)]
    for p in plot_list[::-1]:
        print("".join(p))
    print("  ".join(map(str, range(10))))


def loading():
    for i in range(100):
        print(f"\rLoading... {i+1}%", end="", flush=True)
        time.sleep(0.1)
    print(" Done!")


def multiple_progressbar(num_tasks):
    bar_width = 25
    for task in range(1, num_tasks+1):
        for progress in range(1, bar_width+1):
            bar = "#" * progress + "_" * (bar_width - progress)
            print(f"\rTask {task}/{num_tasks} [{bar}] {progress * 4}%", end="", flush=True)
            time.sleep(0.1)
    print(" Done")

flag()
sequence()
graph()
loading()
multiple_progressbar(3)
uzor()