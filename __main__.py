# Fetch the used arguments
from sys import argv, path

# Command-handling
from cmd.input import handle_input


def main():
    # Take care of the input
    handle_input(argv)
    return


if __name__ == '__main__':
    main()
