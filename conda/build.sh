pip install -e .

python setup.py sdist
cd dist
pip install *.tar.gz
