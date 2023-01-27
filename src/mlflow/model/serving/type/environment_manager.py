""" Environment Manager Type Definition """

from enum import Enum


class EnvironmentManagerType(str, Enum):
    """Environment Manager Type"""

    LOCAL = "local"
    CONDA = "conda"
    VIRTUALENV = "virtualenv"
