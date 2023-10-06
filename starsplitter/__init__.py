import click

from starsplitter.commands import by_tomo
from starsplitter.commands import by_session
from starsplitter.commands import unique_tomo


@click.group()
def starsplitter():
    click.echo('starsplitter \n')


starsplitter.add_command(by_tomo)
starsplitter.add_command(by_session)
starsplitter.add_command(unique_tomo)