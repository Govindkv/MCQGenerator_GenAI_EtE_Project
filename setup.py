from setuptools import find_packages,setup

setup(
    name='mcq_genrator',
    version='0.0.1',
    author='govindkv',
    author_email='govind26663355@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)