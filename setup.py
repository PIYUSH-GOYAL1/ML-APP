from setuptools import find_packages , setup
from typing import List

HYPHEN = "-e ."

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n" , "") for req in requirements]

        if HYPHEN in requirements:
            requirements.remove(HYPHEN)
    return requirements

setup(
    name = "ML APP",
    version= "0.0.1",
    author= "Piyush Goyal",
    author_email= "piyushgoyal11824@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements("requirements.txt")  #["pandas" , "seaborn" , "numpy" , "matplotlib" , ""]
)