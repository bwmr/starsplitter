import click

from starsplitter.commands import by_tomo
from starsplitter.commands import by_session
@click.group()
def starsplitter():
    click.echo('starsplitter \n')

starsplitter.add_command(by_tomo)
starsplitter.add_command(by_session)