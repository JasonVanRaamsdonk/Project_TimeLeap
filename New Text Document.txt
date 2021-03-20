from setuptools import setup, find_packages


setup(
    name='TimeLeap',
    version='0.1.0',
    install_requires=[
        'pytest',
        'torch',
        'requests'

    ],
    packages=find_packages()
)
