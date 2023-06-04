from setuptools import setup, find_packages

VERSION = "0.0.6"
DESCRIPTION = "A Batch Parser"
LONG_DESCRIPTION = "Easy Way to Parse Batch Code in Python"

setup(
    name="BatchParse",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="kdot227",
    license="MIT",
    packages=find_packages(),
    install_requires=["rich"],
    keywords="conversion",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
