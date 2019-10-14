import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fonkle_sysinfo",
    version="0.0.2",
    author="Fonkle",
    author_email="fonkle@gmx.com",
    description="Python System information package for educational purposes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fonkle-experiment/fonkle_sysinfo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.3',
)

