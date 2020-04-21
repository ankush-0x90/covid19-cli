  
> 
>    Don't Forget To Update Covid19-Cli Frequently, Thank You For Using

>    Use `pip install -U covid19-cli` or `pip install covid19-cli==x.y.z` x.y.z is the latest version
>

## Covid19-Cli

<P>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A CLI application for getting covid-19 coronavirus :space_invader:	 status of your country, state or district at lightning :zap: speed right on your terminal :computer: built using https://api.covid19india.org.
</p>

<p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Made with :heavy_heart_exclamation: using Python3.

[![PyPI version](https://badge.fury.io/py/covid19-cli.svg)](https://badge.fury.io/py/covid19-cli) ![PyPI - Downloads](https://img.shields.io/pypi/dm/covid19-cli)

</p>

![image](https://github.com/asprazz/covid19-cli/blob/master/screenshots/screenshot4.png)


### Dependencies
- `Covid19` runs on Python3.x
- [`pip3`](https://pip.pypa.io/en/stable/installing/)
- [`requests`](https://requests.readthedocs.io/en/master/user/install/)
- [`argparse`](https://pypi.org/project/argparse/)
- [`prettytable`](https://ptable.readthedocs.io/en/latest/installation.html)
and our beloved
- [`colorama`](https://pypi.org/project/colorama/)
- Thanks to all :pray:


### Installation (Not for development)
- <strong>Note: Please update globally installed package frequently. :innocent:	</strong>
- Installing from `pypi`
    - `pip install covid19-cli` (use pip for Python3)
    - Already installed ?
        - Update using `pip install -U covid19-cli`
        - see [How To Update Pip Package](https://stackoverflow.com/questions/4536103/how-can-i-upgrade-specific-packages-using-pip-and-a-requirements-file)
- Installing Manually :
    - `git clone https://github.com/asprazz/covid19-cli.git`
    - `cd covid19-cli`
        - Option 1:
            - (if windows) `pip install .`
            - (if linux/mac) `sudo pip install . -H`
        - Option 2:
            - (optional for linux users) if requires `chmod +x install.sh`
            - then run `scripts/./install.sh`


### Usage
- `covid19 -e` or `covid19 --emergency` : for printing emergency numbers
- `covid19 -h` or `covid19 --help` : for printing emergency numbers
- `covid19 {COUNTRY}` :
    - `covid19 World` : for whole World's status world is special keyword
    - `covid19 India` or `covid19 Ind` or `covid19 In` : for India's status
    - `covid19 USA` or `covid19 Us` : for Fetching Usa's status
    - `covid19 UK` or `covid19 GBR` : for Fetching UK's status
    - `covid19 World -a` or `covid19 World --all` : for Fetching all countries at once
    - `covid19 India -a` or `covid19 India --all` : for Fetching all states at once (alternative to `covid India -s mh`)
    - For fetching states in India (only for India)
        - `covid19 India -s maharashtra` or `covid19 Ind -s=maharashtra` : for both country's and state's status
        - `covid19 India -s mh` : will work the same way
        - `covid19 India -s all` or `covid19 In -s=ALL` : for all states of India
- See CODES.md (https://github.com/asprazz/covid19-cli/blob/master/CODES.md)
- See Documentation (https://github.com/asprazz/covid19-cli/blob/master/docs/)

### Contributing Guidelines
- Thank you for Showing interest in contributing to this project
- Please see https://github.com/asprazz/covid19-cli/blob/master/CONTRIBUTORS.md

#### Development
- Please, follow the contributing guidelines
- Fork the repository and clone it to your local environment
- Activate environment if any (
    [`venv`](https://docs.python.org/3/library/venv.html)
    or [`conda`](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
    for more details
  )
- Running `covid19`
  - Running locally
      - `cd covid19-cli`
      - `python covid19/__main__.py`
  - Installing globally from your local repository
      - `cd covid19-cli`
          - Option 1:
              - (if windows) `pip install .`
              - (if linux/mac) `sudo pip install . -H`
          - Option 2:
              - (optional for linux users) if requires `chmod +x install.sh`
              - then run `scripts/./install.sh`
          - option 3:
              - `python setup.py install`
- Fix :wrench: something broken or Build :hammer: something interesting
- Don't forget to target `develop` branch only

### Contributing Guidelines
- Thank you for Showing interest in contributing to this project
- Please see https://github.com/asprazz/covid19-cli/blob/master/CONTRIBUTORS.md

#### Development
- Please, follow the contributing guidelines
- Fork the repository and clone it to your local environment
- Activate environment if any (
    [`venv`](https://docs.python.org/3/library/venv.html)
    or [`conda`](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
    for more details
  )
- Running `covid19`
  - Running locally
      - `cd covid19-cli`
      - `python covid19/__main__.py`
  - Installing globally from your local repository
      - `cd covid19-cli`
          - Option 1:
              - (if windows) `pip install .`
              - (if linux/mac) `sudo pip install . -H`
          - Option 2:
              - (optional for linux users) if requires `chmod +x install.sh`
              - then run `scripts/./install.sh`
          - option 3:
              - `python setup.py install`

### Error reports
- First of all thank you.
- https://github.com/asprazz/covid19-cli/issues


### Special Thanks To Covid19India
- Built on API by :  https://api.covid19india.org/
- For more details : https://github.com/covid19india/api
- Also Visit: https://www.covid19india.org/


### Contributors
- Ankush Patil (https://github.com/asprazz)
- Suraj Kulkarni (https://github.com/KulkarniSuraj)
