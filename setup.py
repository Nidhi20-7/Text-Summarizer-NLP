import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()
    
    
__version__="0.0.0"

REPO_NAME= "Text Summarizer NLP"
AUTHOR_USER_NAME="Nidhi20-7"
SRC_REPO="TextSummarizer"

setuptools.setup(name=REPO_NAME.replace(" ", "_").lower(),
    version=__version__,
    author=AUTHOR_USER_NAME,
    
    description="A text summarization tool using natural language processing.",
    long_description="A text summarization tool that utilizes natural language processing techniques to condense large text documents into shorter summaries.",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"))