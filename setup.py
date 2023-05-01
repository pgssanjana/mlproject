#with setup.py is responsible for creating machine learning applicaiton as a package, which can be used further and also be deployed in python
#setup.py is a python script that is used to install python packages

# from setuptools import find_packages,setup
# from typing import List


# HYPHEN_E_DOT='-e .'
# def get_requirements(file_path:str)->List[str]:
#     '''
#     this fucntion will return the list of packages that are mentioned in the requirements.txt
#     '''

#     requirements = []
#     with open(file_path) as file_obj:
#         requirements = file_obj.readlines()
#         requirements = [req.replace("\n","") for req in requirements]

#         if HYPHEN_E_DOT in requirements:
#             requirements.remove(HYPHEN_E_DOT)
#     return requirements

# setup(
#     name='mlproject',
#     version='0.0.1',
#     author='Sanjana',
#     author_email='sanjanaparepalli@gmail.com',
#     packages=find_packages(),
#     install_requires=get_requirements("requirements.txt"),
# )
from setuptools import find_packages,setup
from typing import List

E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    requirement = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]     
        if E_DOT in requirements:
            requirements.remove(E_DOT)
    return requirements        
    
    
setup(
    name = 'mlproject',
    version = '0.0.1',
    author = "sanjana",
    author_email = "sanjanaparepalli@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements("requirements.txt")
    )


#setup.py is going to find out the number of packages by considering src as package and then it is going to install the packages that are mentioned in the install_requires