import dataset
import click
import sync
import os


@click.group()
def cli():
    pass


@click.command()
def init():
    click.echo("Generating a database at ~/.katalog/")

    db_path = click.get_app_dir('katalog', force_posix=True)

    try:
        os.mkdir(db_path)
        db = dataset.connect('sqlite:///' + db_path + '/katalog.db')
        print(db)
    except OSError:
        click.echo(click.style("Error: ", fg='red', bold=True) +
                   "%s already exists." % db_path)


@click.command()
def status():
    db_path = os.path.expanduser("~/.katalog")
    db = dataset.connect('sqlite:///' + db_path + '/katalog.db')

    count_files = len(db['files'])
    click.echo("%i file(s) stored in the database." % count_files)


@click.command()
@click.argument('path', type=click.Path(exists=True))
def add(path):
    files = list(sync.scan_files(path, sync.MEDIA_EXT))
    click.echo("%s files loaded" % len(files))


cli.add_command(add)
cli.add_command(init)
cli.add_command(status)

if __name__ == '__main__':
    cli()
