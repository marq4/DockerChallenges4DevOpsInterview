""" Just give the current time and exit. """

from datetime import datetime

def main() -> None:
    """ Using datetime module. """
    now = datetime.now()
    print( now.strftime("%H:%M:%S") )

if __name__ == '__main__':
    main()

