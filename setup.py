from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''This function returns a list of requirements from a file.'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='sensorfault',
    version='0.0.1',
    author='Md Kamran Ahmad',
    author_email='ahmadmdkamran462@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
