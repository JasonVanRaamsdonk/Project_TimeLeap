from setuptools import setup, find_packages


setup(
    name='awesomecode',
    version='1.0.0',
    install_requires=[
        'pytest',
        'torch',
        'requests',
        'tools'
    ],
    packages=find_packages()
)
