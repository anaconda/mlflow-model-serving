""" Anaconda Enterprise Service Wrapper Definition """

import sys
from argparse import ArgumentParser, Namespace

from anaconda.enterprise.server.common.sdk import demand_env_var, load_ae5_user_secrets

from .command import MLFlowServingServerCommand
from .dto.launch_parameters import LaunchParameters

if __name__ == "__main__":
    # This function is meant to provide a handler mechanism between the AE5 deployment arguments
    # and those required by the called process (or service).

    # arg parser for the standard anaconda-project options
    parser = ArgumentParser(
        prog="mlflow-model-serving-launch-wrapper", description="mlflow model serving launch wrapper"
    )
    parser.add_argument("--anaconda-project-host", action="append", default=[], help="Hostname to allow in requests")
    parser.add_argument("--anaconda-project-port", action="store", default=8086, type=int, help="Port to listen on")
    parser.add_argument(
        "--anaconda-project-iframe-hosts",
        action="append",
        help="Space-separated hosts which can embed us in an iframe per our Content-Security-Policy",
    )
    parser.add_argument(
        "--anaconda-project-no-browser", action="store_true", default=False, help="Disable opening in a browser"
    )
    parser.add_argument(
        "--anaconda-project-use-xheaders", action="store_true", default=False, help="Trust X-headers from reverse proxy"
    )
    parser.add_argument("--anaconda-project-url-prefix", action="store", default="", help="Prefix in front of urls")
    parser.add_argument(
        "--anaconda-project-address",
        action="store",
        default="0.0.0.0",
        help="IP address the application should listen on",
    )
    parser.add_argument(
        "--env-manager",
        action="store",
        type=str,
        choices=["local", "conda", "virtualenv"],
        default="local",
        help="The environment manager to use for runtime dependencies",
    )

    # Load command line arguments
    args: Namespace = parser.parse_args(sys.argv[1:])
    print(args)

    # load defined environmental variables
    load_ae5_user_secrets(silent=False)

    launch_params: LaunchParameters = LaunchParameters(
        port=args.anaconda_project_port,
        address=args.anaconda_project_address,
        model=demand_env_var(name="MLFLOW_SERVING_MODEL_NAME"),
        stage=demand_env_var(name="MLFLOW_SERVING_MODEL_STAGE"),
        env_manager=args.env_manager,
    )
    MLFlowServingServerCommand.execute(params=launch_params)
