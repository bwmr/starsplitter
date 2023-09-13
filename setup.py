from setuptools import setup

setup(
    name='starsplitter',
    version='0.2',
    packages=['starsplitter'],
    url='https://github.com/bwmr/starsplitter',
    license='',
    author='bwmr',
    author_email='b.wimmer@bioc.uzh.ch',
    description='Split star files by tomogram for easy visualisation.',
    install_requires=['starfile', 'Click'],
    entry_points={
        'console_scripts': [
            'starsplitter = starsplitter:starsplitter',
        ],
    },
)
