import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="epispot",
    version="v2.0.1",
    author="quantum9innovation",
    description="A tool for modelling infectious diseases.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://quantum9innovation.github.io/epispot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=['matplotlib', 'numpy', ],
)
