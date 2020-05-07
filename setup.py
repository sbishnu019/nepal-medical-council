import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nepal-medical-council",
    version="0.0.1",
    author="Bishnu Sharma",
    author_email="sbishnu019@gmail.com",
    description="A package for nepal medical council",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sbishnu019/nepal-medical-council.git",
    download_url='',
    install_requires=[
          'requests',
          'beautifulsoup4',
      ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
