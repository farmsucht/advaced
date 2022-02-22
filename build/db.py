# Add to path
from sys import path

from os.path import join, isdir
from os import getcwd, mkdir, chmod

path.insert(0, getcwd())
print(path)

# Database-handler
from util.database.initialize import create_database, create_tables, DATABASE_FILE


def build():
    """Creates the database and its tables.

    :return: Successfulness of the build.
    :rtype: bool
    """

    # Check if the database does not exist
    if exists(DATABASE_FILE):
        create_database(False)

        return True

    # Create the directory
    try:
        mkdir('/usr/lib/advaced/database')
    except:
        pass

    # Create the database
    create_database(True)

    return True