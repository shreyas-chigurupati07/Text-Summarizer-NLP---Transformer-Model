import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-NLP---Transformer-Model"
AUTHOR_USER_NAME = "shreyas-chigurupati07"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "chigurupatishreyas@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shreyas-chigurupati07/Text-Summarizer-NLP---Transformer-Model",
    project_urls={
        "Bug Tracker": "https://github.com/shreyas-chigurupati07/Text-Summarizer-NLP---Transformer-Model/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)    