from pathlib import Path

import click
import starfile


@click.command()
@click.argument('input_star', nargs = 1, type=click.Path(exists=True))
def starsplitter(input_star: Path):
    """
    Splits a given star input_star by rlnMicroGraphName column.

    input: .star input_star detailing particles from relion.

    output: one .star input_star with particles belonging to one tomogram, written to the same location as input.
    """
    input_star = Path(input_star)

    star = starfile.read(input_star)

    # Do a check whether the star input_star contains a separate optics group header
    if len(star) == 2:
        particles = star['particles']
    else:
        particles = star

    particles_grouped = particles.groupby(particles['rlnMicrographName'])

    for tomo in particles['rlnMicrographName'].unique():
        file_split = input_star.with_name(f'{input_star.stem}_{tomo}.star')

        particles_split = particles_grouped.get_group(tomo)

        if len(star) == 2:
            starfile.write({'optics': star['optics'], 'particles': particles_split}, file_split, overwrite=True)
        else:
            starfile.write(particles_split, file_split,overwrite=True)

def by_tomo():
    pass

def by_session():
    pass

