from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="webscout",
    version="1.0.0",
    author="Mursalin",
    description="Web Application Vulnerability & Technology Scanner",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mursalin/webscout",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "webscout=main:run",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
