# setup.py

from setuptools import setup, find_packages

setup(
    name='my-python-app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Lista de dependencias de tiempo de ejecución
    ],
    setup_requires=[
        'setuptools',
        'wheel'
    ],
)
