import ZODB, transaction
import click
import os

from . import db, sync


@click.group()
def cli():
    pass


@cli.command()
def init():
    db_path = click.get_app_dir('katalog', force_posix=True)
    click.echo("Generating a database at %s" % db_path)

    try:
        os.mkdir(db_path)
    except OSError:
        click.echo(click.style("Error: ", fg='red', bold=True) +
                   "%s already exists." % db_path)

    root = db.get_root()
    from BTrees.OOBTree import OOBTree
    root['files'] = OOBTree()
    transaction.commit()


@cli.command()
def status():
    db_path = os.path.expanduser("~/.katalog")
    root = db.get_root()

    count_files = len(root['files'])

    click.echo("%i file(s) stored in the database." % count_files)


@cli.command()
@click.argument('path', type=click.Path(exists=True))
def add(path):
    root = db.get_root()
    old_count = len(root['files'])

    for f in sync.scan_files(path):
        root['files'][f.path] = f

    transaction.commit()

    new_count = len(root['files'])
    click.echo("%s files loaded" % (new_count - old_count))


@cli.command()
def shell():
    """
    Run an interactive shell, loading the root DB.
    """

    root = db.get_root()

    import readline
    import code
    vars = globals().copy()
    vars.update(locals())
    shell = code.InteractiveConsole(vars)
    shell.interact()


@cli.command()
def fetch():
    """
    Fetch additional metadata (title…)
    """

    from imdbpie import Imdb
    imdb_client = Imdb()

    from katalog.services.opensubtitles import OpenSubtitles
    opensub = OpenSubtitles()
    opensub.login()

    root = db.get_root()
    files = root['files'].values()

    with click.progressbar(files) as bar:
        for f in bar:
            f.identify(opensub)

            if not f.is_fetched and f.imdb_id is not None:
                f.fetch_metadata(imdb_client)

    transaction.commit()

if __name__ == '__main__':
    cli()
