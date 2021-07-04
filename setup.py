from setuptools import setup
import setuptools

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name = "pyyhtml",
    version = "0.0.2",    
    description = "A simple HTML pseudo for Python",
    project_urls={
        "GitHub": "https://github.com/yusantus/pyyhtml",
        "yusantus": "https://www.yusantus.de"
    },
    url = "https://github.com/yusantus/pyyhtml",
    author = "Yusuf Emre Samur",
    author_email = "yusantus.2021@gmail.com",
    license = "MIT License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)