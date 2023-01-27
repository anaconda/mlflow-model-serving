""" MLFlow `Model` Serving Supported Launch Parameters """

from anaconda.enterprise.server.contracts import BaseModel

from ..type.environment_manager import EnvironmentManagerType


# pylint: disable=too-few-public-methods
class LaunchParameters(BaseModel):
    """
    MLFlow `Model` Serving Supported Launch Parameters (DTO)
    port: str
        The port to start the server listening on.  This is meant to be automatically set by AE5.
    address: str
        The address to start the server listening on.  This is meant to be automatically set by AE5.
    model: str
        The model name in the model registry which will served.
    stage: str
        The stage or version of the model to serve.
    env_manager: EnvironmentManagerType
        The environment manager to use for runtime dependencies
    """

    port: str = "8086"
    address: str = "0.0.0.0"
    model: str
    stage: str
    env_manager: EnvironmentManagerType = EnvironmentManagerType.LOCAL
