#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as hidden

    names = dir(hidden)
    for i in range(len(names)):
        if (names[i][0] != "_"):
            print(names[i])
