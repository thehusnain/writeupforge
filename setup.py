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
    author="Your Name",
    author_email="your.email@example.com",
    description="Convert raw cybersecurity lab notes into professional writeups",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/WriteSec",
    project_urls={
        "Bug Tracker": "https://github.com/your-username/WriteSec/issues",
        "Documentation": "https://github.com/your-username/WriteSec",
        "Source Code": "https://github.com/your-username/WriteSec",
    },
    packages=find_packages(exclude=["tests"]),
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
        "openai",
        "click",
        "reportlab",
        "python-dotenv",
        "customtkinter",
        "pillow",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "writeupforge=run:run",
            "fgwrite=run:run",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
