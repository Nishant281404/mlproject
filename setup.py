from setuptools import find_packages,setup
from typing import List

hypen_e="-e ."
def get_requirements(file_path:str)->list[str]:
    """ this function will return the list of requirements"""
    requiremnets=[]
    with open(file_path) as file_obj:
         requirements=file_obj.readlines()
         requirements=[req.replace("\n"," ") for req in requirements]         

         if hypen_e in requirements:
            requirements.remove(hypen_e)
    return requirements        



setup(

name= 'mlproject',
version= '0.0.1',
author="nishant",
author_email="nistyagi281@gamil.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')



)