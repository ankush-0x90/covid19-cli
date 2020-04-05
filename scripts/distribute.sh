python setup.py sdist bdist_wheel

if [[ $1 == "test" ]]; then
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
elif [[ $1 == "prod"* ]]; then
    twine upload dist/*
fi