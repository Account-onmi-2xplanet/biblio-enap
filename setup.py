from setuptools import setup, find_packages

setup(
    name='biblio-enap',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',  # Adicionando requests à lista de dependências
    ],
)