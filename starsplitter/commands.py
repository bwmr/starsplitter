from pathlib import Path

import click
import starfile


@click.command()
def starsplitter(file: Path):
    """
    Splits a given star file by rlnMicroGraphName column.

    input: .star file detailing particles from relion.

    output: one .star file with particles belonging to one tomogram, written to the same location as input.
    """
    file = Path(file)

    star = starfile.read(file)

    # Do a check whether the star file contains a separate optics group header
    if len(star) == 2:
        particles = star['particles']
    else:
        particles = star

    particles_grouped = particles.groupby(particles['rlnMicrographName'])

    for tomo in particles['rlnMicrographName'].unique():
        file_split = file.with_name(f'{file.stem}_{tomo}.star')

        particles_split = particles_grouped.get_group(tomo)

        if len(star) == 2:
            starfile.write({'optics': star['optics'], 'particles': particles_split}, file_split)
        else:
            starfile.write(particles_split, file_split)
