from setuptools import setup, find_packages

setup(
    name='data_vis',
    version='1.0.0',
    packages=find_packages(include=['data_vis', 'data_vis.*']),
    author='Magda Wójcicka',
    install_requires=['folium>=0.12.1', 'pandas>=1.2.3', 'numpy>=1.16.5']
)