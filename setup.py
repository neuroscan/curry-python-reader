import setuptools

setuptools.setup(
    name="curryreader-fgasca",
    version="0.0.1",
    mantainer="Fernando Gasca",
    mantainer_email="fgasca@neuroscan.com",
    description="Python reader for CURRY MEG/EEG files",
    long_description=open('README.txt').read(),
    long_description_content_type="text/markdown",
    url = "https://compumedicsneuroscan.com/products/by-name/curry/",
    download_url="https://github.com/curry-tools/curryreader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD (3-clause)",
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
