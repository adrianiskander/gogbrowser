import sys
from server.wsgi import application as app


COMMANDS = {
    'runserver': app.run()
}


if __name__ == '__main__':
    COMMANDS[sys.argv[1]]()
