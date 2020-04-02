from setuptools import setup


setup(
    name = 'covid19',
    version = '0.1.0',
    packages = ['covid19'],
    entry_points = {
        'console_scripts': [
            'covid19 = covid19.__main__:main'
        ]
    })