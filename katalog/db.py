import ZODB
import click


def get_root():
    """
    Return the root object of the current database.
    """
    db_path = click.get_app_dir('katalog', force_posix=True)
    connection = ZODB.connection(db_path + '/data.fs')
    return connection.root()
