from pathlib import Path
import setuptools
# from PIL import Image


def get_install_requires() -> list[str]:
    """Returns requirements.txt parsed to a list"""
    fname = Path(__file__).parent / 'requirements.txt'
    targets = []
    if fname.exists():
        with open(fname, 'r') as f:
            targets = f.read().splitlines()
    return targets


setuptools.setup(
    name="Python Project",
    description="Python Project",
    version="0.1.0",
    author="Prasanna",
    author_email="plimaye15@gmail.com",
    install_requires=get_install_requires(),
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires='>=3.7',
)
