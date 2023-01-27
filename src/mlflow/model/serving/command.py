""" MLFlow `Model` Serving Launch Command """

import shlex
import subprocess

from anaconda.enterprise.server.contracts import BaseModel

from .dto.launch_parameters import LaunchParameters


# pylint: disable=too-few-public-methods
class MLFlowServingServerCommand(BaseModel):
    """
    Responsible for the invocation of the mlflow process.
    """

    @staticmethod
    def _process_launch_wait(shell_out_cmd: str) -> None:
        """
        Internal function for wrapping process launches [and waiting].

        Parameters
        ----------
        shell_out_cmd: str
            The command to be executed.
        """

        args = shlex.split(shell_out_cmd)

        with subprocess.Popen(args, stdout=subprocess.PIPE) as process:
            for line in iter(process.stdout.readline, b""):
                print(line)

    @staticmethod
    def execute(params: LaunchParameters) -> None:
        """
        This function is responsible for mapping AE5 arguments to mlflow launch arguments and then
        executing the service.

        Parameters
        ----------
        params: LaunchParameters
            Parameters needed for mlflow configuration.
        """

        # https://www.mlflow.org/docs/latest/cli.html#mlflow-server
        # execution command
        model_uri: str = f"'models:/{params.model}/{params.stage}'"
        print(f"Loading model: {model_uri}")

        # https://www.mlflow.org/docs/latest/cli.html#mlflow-models-serve
        cmd: str = (
            f"mlflow models serve --env-manager {params.env_manager} "
            f"--model-uri {model_uri} "
            f"--port {params.port} "
            f"--host {params.address}"
        )
        print(cmd)

        MLFlowServingServerCommand._process_launch_wait(shell_out_cmd=cmd)
