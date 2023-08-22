from setuptools import setup, find_packages

# metadata
name = "pyxi_couchbase_client"
version = "0.0.1"
description = "A basic couchbase client for python."
long_description = ""
author = "Simon Stipcich"
author_email = "stipcich.simon@gmail.com"
url = "https://github.com/stiproot/py-couchbase-client"
license = "MIT"
keywords = ["python", "package", "couchbase", "beta"]

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# dependencies
install_requires = [
    "dotenv",
    "couchbase",
]

# setup
setup(
    packages=find_packages("src"),
    # package_dir={"", "src"},
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=author,
    author_email=author_email,
    url=url,
    license=license,
    keywords=keywords,
    install_requires=install_requires,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
    ],
)
