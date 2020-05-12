import readline
import curses
from bank import WordBank
from commands import CommandParser
from commands import CommandKind

bank = WordBank('espanol')
def input_loop():
    global bank
    parser = CommandParser(bank)
    while True:
        info = ""
        command = input("\n" + info + "\n% ").strip()
        cmd = parser.parse_command(command)
        if not cmd:
            print("Not a valid command, try again")
        elif cmd[0] == CommandKind.WORD_ASSIGN:
            pass
        elif cmd[0] == CommandKind.EXIT:
            exit(1)

#readline.set_completer(bank.complete)
# ' ', '\t', '\n', '"', '\\', '\'', '`', '@', '$', '>', '<', '=', ';', '|', '&', '{', '(', '\0'
#readline.set_completer_delims(' \t\n"\'\\`@$><=;|&{(')
readline.set_completer_delims(' \t\n"\'\\`@$><=;|&{(')
readline.parse_and_bind('tab: complete')
input_loop()

