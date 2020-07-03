import os
from setuptools import setup, find_packages

#dir_path = os.path.dirname(os.path.realpath(__file__))
# os.chdir(dir_path)

setup(
    name='samsung_remote',
    version='0.0.1',
    description='Simple gui for controlling a Samsung Tizen tv',
    long_description="Bla bla bla.",
    author='HEF',
    author_email='',
    url='',
    packages=find_packages(),
    setup_requires=['wheel'],
    install_requires=['pillow'],
    include_package_data=True,
    package_data={
        "static": ['*.png'],
    },
    entry_points={
        'console_scripts': [
            'lazy_remote=main:main'
        ],
    }
)
