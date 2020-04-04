python setup.py sdist bdist_wheel

if [[ "test" == "test" ]]; then
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
elif [[ "$OSTYPE" == "darwin"* ]]; then
    python upload dist/*
fi