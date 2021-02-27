import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE", # Replace with your own username
    version="0.0.1",
    author="osman",
    author_email="osmangoni14@gmail.com",
    description="This is a simple project for date convertion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/osmancuet09/english-to-bangla-date.git",
    project_urls={
        "Bug Tracker": "https://github.com/osmancuet09/english-to-bangla-date.git",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)