from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read version from version.py without importing it
version = "1.0.0"
with open("version.py", "r") as f:
    for line in f:
        if line.startswith("CURRENT_VERSION"):
            version = line.split("=")[1].strip().strip('"\'')
            break

setup(
    name="writeupforge",
    version=version,
    author="fsociety-pk",
    author_email="cybersecurity@organization.com",
    description="Convert raw cybersecurity lab notes into professional writeups",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fsociety-pk/writeupforge",
    project_urls={
        "Bug Tracker": "https://github.com/fsociety-pk/writeupforge/issues",
        "Documentation": "https://github.com/fsociety-pk/writeupforge",
        "Source Code": "https://github.com/fsociety-pk/writeupforge",
        "Releases": "https://github.com/fsociety-pk/writeupforge/releases",
    },
    packages=find_packages(exclude=["tests"]),
    py_modules=["cli", "run"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Text Processing :: Markup",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.8",
    install_requires=[
        "groq>=0.4.0",
        "click>=8.0",
        "reportlab>=4.0",
        "python-dotenv>=1.0",
        "customtkinter>=5.0",
        "pillow>=10.0",
        "requests>=2.28",
    ],
    entry_points={
        "console_scripts": [
            "writeupforge=cli:main",
            "fgwrite=cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
