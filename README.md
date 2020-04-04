## covi19-cli
<br/>

![image](https://github.com/asprazz/covid19-cli/blob/master/screenshots/screenshot1.png)

<br/>
<br/>

- `:rocket:` Get instant coronavirus status of India on terminal
- Clean user interface
- Making of README.md in progress Than you :)

## Dependencies
- >python3.5
- pip3

### Installation
- From pip :
- `pip3 install covid19-cli`
- Manual installation :
- `git clone https://github.com/asprazz/covid19-cli.git`
- `cd covid19-cli`
- (optional for linux users) if requires `chmod +x install.sh`
- then run `scripts/./install.sh`


### Usage
- `covid19 -e` or `covid19 --emergency` : for printing emergency numbers
- `covid19` : for country's status (default)
- `covid19 -s=maharashtra` or `covid19 -s maharashtra` : for both country's and state's status
- `covid19 -s mh` : will also work
- `covid19 -h` or `covid19 --help` : for help


### Developement
- fork the repo
- `git clone https://github.com/{your_username}/covid19-cli.git`
- Activate environment if available
- run `python covid19/__main__.py`
- run `python covid19/__main__.py -h` for help




### Error reports
- First of all thank you.
- https://github.com/asprazz/covid19-cli/issues

### Contributing Guidelines
- Suggesting a new feature ? Open an feature issue
- Sending PR, send it without worries
- Just `fork` `change` `send`
- Thank you

### Special Thanks To
- https://api.covid19india.org/
- argparse
- prettytable
