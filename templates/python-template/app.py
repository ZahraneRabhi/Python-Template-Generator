# Internal modules
from threading import Thread
from utils import do_stuff

# External modules

# import _________


if __name__ == '__main__':
    bg_thread = Thread(target=do_stuff)
    bg_thread.start()
