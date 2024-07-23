#responsible in creating ML application as a package
from setuptools import find_packages,setup
from typing import List

a='-e .'
def get_requirements(file_path:str)->List[str]:
      ''' 
      this func will return the list of requirements
      '''
      requirements=[]
      with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            requirements=[req.replace("\n","") for req in requirements]
            if a in requirements:
                  requirements.remove(a)
      return requirements        
setup(
    name='MLproject',
    version='0.0.1',
    author='Harshit',
    author_email='harshitjain5670@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')   

   ) 