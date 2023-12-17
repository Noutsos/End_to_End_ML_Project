from setuptools import find_packages,setup
from typing import List

minus_e='-e .'
def get_requirements(file_path:str)->List[str]:

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if minus_e in requirements:
            requirements.remove(minus_e)
    
    return requirements


setup(
name='mlproject',
version='0.0.1',
author='Giannis Vasileiou',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)