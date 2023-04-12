from setuptools import setup, find_packages

setup(
    name='musa',
    version='0.1.0',
    description='A simple and lightweight program to download video and audio from YouTube.',
    author='iluzioDev',
    author_email='luischinearangel@gmail.com',
    license='GNU General Public License v3.0',
    packages=find_packages(),
    install_requires=[
        'PySimpleGUI',
        'pytube',
    ],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
