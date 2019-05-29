import re
from os.path import join, dirname

from setuptools import setup, find_packages


# reading package version (without reloading it)
with open(join(dirname(__file__), 'tlv', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S) \
        .match(v_file.read()) \
        .group(1)


setup(
    name='python-tlv',
    version=package_version,
    description='A library to parse TLV naming',
    author='Mehdi Azizi',
    author_email='mehdiazizi@outlook.com',
    packages=find_packages(),
    include_package_data=True,
    test_suite='tlv.tests',
    license='MIT',
)

