from os import system


# Tarefa para abrir gmail, facebook e twitter
# e tocar música.


def main():
    commands = [
        # Open Gmail
        'start "" "https://mail.google.com"',
        # Open Facebook
        'start "" "https://facebook.com"',
        # Open Twitter
        'start "" "https://twitter.com"',
        # Play some music
        'start wmplayer'
    ]
    concat_commands = commands[0]
    for i in range(1, len(commands)):
        concat_commands += ' | ' + commands[i]
    system(concat_commands)


if __name__ == '__main__':
    main()
