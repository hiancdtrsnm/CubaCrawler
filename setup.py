# coding: utf8

import toml
from setuptools import setup


# TODO: Update version whenever changes
VERSION = '1.0.0'


def get_install_requirements():
    """Automatically pull requirements from Pipfile.
    Adapted from: <https://medium.com/homeaway-tech-blog/simplifying-python-builds-74e76802444f>
    """
    try:
        # read my pipfile
        with open('Pipfile', 'r') as fh:
            pipfile = fh.read()
        # parse the toml
        pipfile_toml = toml.loads(pipfile)
    except FileNotFoundError:
        return []
    # if the package's key isn't there then just return an empty
    # list
    try:
        required_packages = pipfile_toml['packages'].items()
    except KeyError:
        return []
    # If a version/range is specified in the Pipfile honor it
    # otherwise just list the package
    return ["{0}{1}".format(pkg, ver) if ver != "*"
            else pkg for pkg, ver in required_packages]


setup(
    name='CubaCrawler',
    packages=['CubaCrawler'],
    url='https://github.com/fsadannn/CubaCrawler', # cambiar
    download_url='https://github.com/fsadannn/CubaCrawler/tarball/{}'.format(VERSION), # cambiar
    license='MIT',
    author='Frank Sadan Naranjo Noda, Hian Cañizares Días',
    author_email='fsadannn@gmail.com, hiancdtrsnm@gmail.com',
    description='This library aims to obtain information from the sites of Cuban news.',

    # This should automatically take your long description from Readme.md
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    # This should automatically pull your requirements from `Pipfile`
    install_requires=get_install_requirements(),
    version=VERSION,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
