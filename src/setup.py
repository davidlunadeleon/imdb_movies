from setuptools import setup, find_packages

setup(
    name="movies",
    version="0.1",
    packages=find_packages(where=".", include="movies*"),
)
