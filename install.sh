# Checks to be perform on windows and mac
if [[ "$OSTYPE" == "linux-gnu" ]]; then
    sudo -H pip3 install -e .
elif [[ "$OSTYPE" == "darwin"* ]]; then
    sudo -H pip3 install -e .
elif [[ "$OSTYPE" == "msys" ]]; then
    pip3 install -e .
elif [[ "$OSTYPE" == "win32" ]]; then
    pip3 install -e .
elif [[ "$OSTYPE" == "freebsd"* ]]; then
    pip3 install -3 .
else
    echo "UPDATE"
fi