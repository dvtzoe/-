from collections import deque


def main() -> None:
    try:
        before_with, after_with = input().split("with")
        players = deque(before_with.strip().split(", "))
        passes = int(after_with.split("p")[0].strip())
    except ValueError, IndexError:
        print("Invalid input")
        return

    gulag = []

    while len(players) > 1:
        for _ in range(passes):
            players.append(players.popleft())
        gulag.append(players.popleft())

    if gulag:
        print(*gulag, sep=", ", end="")
        print(" are out, ", end="")
    if players:
        print(f"Winner: {players[0]}")


if __name__ == "__main__":
    main()
