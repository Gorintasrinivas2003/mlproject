from setuptools import find_packages, setup
from typing import List

hypen_e_dot ='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Vasu',
    author_email='balajivarmagorinta@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)