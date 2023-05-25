def print_hang(stdscr, tries, hidden_word):

    match tries:
        case 1:
            h, w = stdscr.getmaxyx()
            y = h // 2 - len(hidden_word)
            x = w // 2 - len(hidden_word) * 2
            stdscr.addstr(y, x, " +---+")
            stdscr.addstr(y + 1, x, " |   |")
            stdscr.addstr(y + 2, x, " |    ")
            stdscr.addstr(y + 3, x, " |    ")
            stdscr.addstr(y + 4, x, " |    ")
            stdscr.addstr(y + 5, x, "======")
            stdscr.refresh()

        case 2:
            h, w = stdscr.getmaxyx()
            y = h // 2 - len(hidden_word)
            x = w // 2 - len(hidden_word) * 2
            stdscr.addstr(y, x, " +---+")
            stdscr.addstr(y + 1, x, " |   |")
            stdscr.addstr(y + 2, x, " |   O")
            stdscr.addstr(y + 3, x, " |    ")
            stdscr.addstr(y + 4, x, " |    ")
            stdscr.addstr(y + 5, x, "======")
            stdscr.refresh()

        case 3:
            h, w = stdscr.getmaxyx()
            y = h // 2 - len(hidden_word)
            x = w // 2 - len(hidden_word) * 2
            stdscr.addstr(y, x, " +---+")
            stdscr.addstr(y + 1, x, " |   |")
            stdscr.addstr(y + 2, x, " |   O")
            stdscr.addstr(y + 3, x, " |   |")
            stdscr.addstr(y + 4, x, " |    ")
            stdscr.addstr(y + 5, x, "======")
            stdscr.refresh()

        case 4:
            h, w = stdscr.getmaxyx()
            y = h // 2 - len(hidden_word)
            x = w // 2 - len(hidden_word) * 2
            stdscr.addstr(y, x, " +---+ ")
            stdscr.addstr(y + 1, x, " |   | ")
            stdscr.addstr(y + 2, x, " |   O ")
            stdscr.addstr(y + 3, x, " |  /| ")
            stdscr.addstr(y + 4, x, " |     ")
            stdscr.addstr(y + 5, x, "====== ")
            stdscr.refresh()

        case 5:
            h, w = stdscr.getmaxyx()
            y = h // 2 - len(hidden_word)
            x = w // 2 - len(hidden_word) * 2
            stdscr.addstr(y, x, " +---+  ")
            stdscr.addstr(y + 1, x, " |   |  ")
            stdscr.addstr(y + 2, x, " |   O  ")
            stdscr.addstr(y + 3, x, " |  /|\ ")
            stdscr.addstr(y + 4, x, " |      ")
            stdscr.addstr(y + 5, x, "======  ")
            stdscr.refresh()

        case 6:
            h, w = stdscr.getmaxyx()
            y = h // 2 - len(hidden_word)
            x = w // 2 - len(hidden_word) * 2
            stdscr.addstr(y, x, " +---+  ")
            stdscr.addstr(y + 1, x, " |   |  ")
            stdscr.addstr(y + 2, x, " |   O  ")
            stdscr.addstr(y + 3, x, " |  /|\ ")
            stdscr.addstr(y + 4, x, " |  /   ")
            stdscr.addstr(y + 5, x, "======  ")
            stdscr.refresh()

        case 7:
            h, w = stdscr.getmaxyx()
            y = h // 2 - len(hidden_word)
            x = w // 2 - len(hidden_word) * 2
            stdscr.addstr(y, x, " +---+  ")
            stdscr.addstr(y + 1, x, " |   |  ")
            stdscr.addstr(y + 2, x, " |   O  ")
            stdscr.addstr(y + 3, x, " |  /|\ ")
            stdscr.addstr(y + 4, x, " |  / \ ")
            stdscr.addstr(y + 5, x, "======  ")
            stdscr.refresh()

        case 8:
            stdscr.clear()
            h, w = stdscr.getmaxyx()
            y = h // 2
            x = w // 2
            stdscr.addstr(y, x - len("YOU LOSE!") // 2, "YOU LOSE!")
            stdscr.addstr(
                y + 2,
                x - len(f"The hidden word was: {hidden_word}") // 2,
                f"The hidden word was: {hidden_word}",
            )
            stdscr.getch()

        case 9:
            stdscr.clear()
            h, w = stdscr.getmaxyx()
            y = h // 2
            x = w // 2
            stdscr.addstr(y, x - len("YOU WIN!") // 2, "YOU WIN!")
            stdscr.addstr(
                y + 2,
                x - len(f"The hidden word was: {hidden_word}") // 2,
                f"The hidden word was: {hidden_word}",
            )
            stdscr.getch()