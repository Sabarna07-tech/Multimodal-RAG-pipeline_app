from setuptools import setup, find_packages

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> list[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
