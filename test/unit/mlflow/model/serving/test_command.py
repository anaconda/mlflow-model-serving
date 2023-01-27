import unittest
from unittest.mock import MagicMock, patch

from anaconda.enterprise.server.common.sdk import demand_env_var
from src.mlflow.model.serving.command import MLFlowServingServerCommand
from src.mlflow.model.serving.dto.launch_parameters import LaunchParameters


class TestCommand(unittest.TestCase):
    # _process_launch_wait tests

    def test_process_launch_wait(self):
        with patch("subprocess.Popen.__new__") as patched_subprocess:
            patched_subprocess.reset_mock()

            class MockProcess:
                __enter__: MagicMock = MagicMock(side_effect=[Exception("MOCK")])
                __exit__: MagicMock = MagicMock()
                stdout: MagicMock = MagicMock()

            patched_subprocess.return_value = MockProcess()

            with self.assertRaises(Exception) as error:
                MLFlowServingServerCommand._process_launch_wait(shell_out_cmd="mock command")
                self.assertEqual(error.exception, "MOCK")

            self.assertEqual(patched_subprocess.call_count, 1)
            self.assertEqual(patched_subprocess.mock_calls[0].args[1], ["mock", "command"])

    # execute tests

    def test_execute(self):
        with patch(
            "src.mlflow.model.serving.command.MLFlowServingServerCommand._process_launch_wait"
        ) as patched_launch:
            patched_launch.reset_mock()

            # Set up tests
            mock_params: LaunchParameters = LaunchParameters(
                port="1234",
                address="localhost",
                model=demand_env_var(name="MLFLOW_SERVING_MODEL_NAME"),
                stage=demand_env_var(name="MLFLOW_SERVING_MODEL_STAGE"),
                env_manager="conda",
            )

            # Execute test
            MLFlowServingServerCommand.execute(params=mock_params)

            # Validate Test
            self.assertEqual(patched_launch.call_count, 1)

            expected_launch_cmd: str = (
                f"mlflow models serve --env-manager conda "
                f"--model-uri 'models:/{mock_params.model}/{mock_params.stage}' "
                f"--port {mock_params.port} "
                f"--host {mock_params.address}"
            )
            self.assertEqual(
                patched_launch.call_args[1],
                {"shell_out_cmd": expected_launch_cmd},
            )


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(TestCommand())
