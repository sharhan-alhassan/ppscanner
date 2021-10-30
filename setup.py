
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()


setup(
    name = 'ppscanner',
    version = '0.0.1',
    author = 'Sharhan Alhassan',
    author_email = 'sharhanalhassan@gmail.com',
    license = 'MIT',
    description = 'A lightweight CLI tool for scanning ports and services on a host',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/sharhan-alhassan/ppscanner',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = [requirements],
    python_requires ='>=3.7',
    classifiers = [
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        ppscan=ppscan.cli:main
    '''
)
