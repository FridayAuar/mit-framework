from setuptools import setup, find_packages

setup(
    name="mit-framework",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.20.0",
        "scipy>=1.7.0",
        "matplotlib>=3.3.0"
    ],
    author="Ayakhu Kem'Nabi Ausar",
    description="Mathematical Impossibility Theory Framework",
)