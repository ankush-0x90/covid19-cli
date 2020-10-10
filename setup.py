import os
import re

from setuptools import setup, find_packages


setup(
    name='covid19-cli',
    author="Ankush Patil",
    version="1.1.2",
    url="https://github.com/asprazz/covid19-cli",
    description="A CLI for getting covid19 status at lightning speed.",
    packages=["covid19"],
    install_requires=[
        'requests>=2.23',
        'argparse',
        'prettytable',
        'colorama',
        'halo'
    ],
    # we requires python 3+
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'covid19=covid19.__main__:main'
        ]
    },
    author_email="aspraz2658@gmail.com",
    keywords=["covid19", "covid19-india", "coronavirus", "cli python"],
    project_url={
        "Source Code": "http://github.com/asprazz/covid19-cli",
        "Issues": "http://github.com/asprazz/covid19-cli/issues",
        "Documentation": "https://ankush.tech/projects/covid19-cli/docs/",
    },
    license="MIT"
)
