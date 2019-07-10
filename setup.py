import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kanglish",
    version="0.0.1",
    author="Royston S",
    author_email="sroystona13@gmail.com",
    description="Text Conversion: Converts Kannada text to English",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FDrKSequeira/nltk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
