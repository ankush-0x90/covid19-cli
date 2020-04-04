# Checks to be perform on windows and mac
if [[ "$OSTYPE" == "linux-gnu" ]]; then
    python setup.py install
elif [[ "$OSTYPE" == "darwin"* ]]; then
    python setup.py install
elif [[ "$OSTYPE" == "msys" ]]; then
    python setup.py install
elif [[ "$OSTYPE" == "win32" ]]; then
    python setup.py install
elif [[ "$OSTYPE" == "freebsd"* ]]; then
    python setup.py install
else
    echo "UPDATE"
fi