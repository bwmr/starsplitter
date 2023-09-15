import click
import starfile
import collections
import starsplitter.utils as utils

from pathlib import Path


@click.command()
@click.argument('input_star', nargs=1, type=click.Path(exists=True))
def by_tomo(input_star: Path):
    """
    Splits a given star input_star by rlnMicrographName column.

    input: .star input_star detailing particles from relion.

    output: one .star input_star with particles belonging to one tomogram, written to the same location as input.
    """
    input_star = Path(input_star)

    star = starfile.read(input_star)

    # Do a check whether the star input_star contains a separate optics group header
    if type(star) is collections.OrderedDict:
        particles = star['particles']
    else:
        particles = star

    particles_grouped = particles.groupby(particles['rlnMicrographName'])

    for tomo in particles['rlnMicrographName'].unique():

        particles_split = particles_grouped.get_group(tomo)
        
        prefix = utils.return_session(particles_split.iloc[0]['rlnImageName'])
        
        file_split = input_star.with_name(f'{input_star.stem}_{prefix}_{tomo}.star')

        if type(star) is collections.OrderedDict:
            starfile.write({'optics': star['optics'], 'particles': particles_split}, file_split, overwrite=True)
        else:
            starfile.write(particles_split, file_split, overwrite=True)

    return


@click.command()
@click.argument('input_star', nargs=1, type=click.Path(exists=True))
def by_session(input_star):
    """
    Splits a given star input_star by Warp session.

    Assumes that rlnImageName contains Warp-reconstructed subtomograms with the following naming scheme:
    $warp_folder/subtomo/$tomo/$tomo_$nr_$angpix.mrc

    input: .star input_star detailing particles from relion.

    output: one .star input_star with particles belonging to one session, written to the same location as input.
    """

    input_star = Path(input_star)

    star = starfile.read(input_star)

    # Do a check whether the star input_star contains a separate optics group header
    if type(star) is collections.OrderedDict:
        particles = star['particles']
    else:
        particles = star

    particles['wrpSession'] = particles['rlnImageName'].apply(utils.return_session)

    particles_grouped = particles.groupby(particles['wrpSession'])

    for session in particles['wrpSession'].unique():
        file_split = input_star.with_name(f'{input_star.stem}_{session}.star')

        particles_split = particles_grouped.get_group(session)

        if type(star) is collections.OrderedDict:
            starfile.write({'optics': star['optics'], 'particles': particles_split}, file_split, overwrite=True)
        else:
            starfile.write(particles_split, file_split, overwrite=True)
    return
