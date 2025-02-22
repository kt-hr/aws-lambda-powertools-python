import pytest

from tests.e2e.utils.infrastructure import LambdaLayerStack, deploy_once


@pytest.fixture(scope="session")
def lambda_layer_arn(lambda_layer_deployment):
    yield lambda_layer_deployment.get("LayerArn")


@pytest.fixture(scope="session")
def lambda_layer_deployment(request: pytest.FixtureRequest, tmp_path_factory: pytest.TempPathFactory, worker_id: str):
    """Setup and teardown logic for E2E test infrastructure

    Parameters
    ----------
    request : pytest.FixtureRequest
        pytest request fixture to introspect absolute path to test being executed
    tmp_path_factory : pytest.TempPathFactory
        pytest temporary path factory to discover shared tmp when multiple CPU processes are spun up
    worker_id : str
        pytest-xdist worker identification to detect whether parallelization is enabled

    Yields
    ------
    Dict[str, str]
        CloudFormation Outputs from deployed infrastructure
    """
    yield from deploy_once(
        stack=LambdaLayerStack,
        request=request,
        tmp_path_factory=tmp_path_factory,
        worker_id=worker_id,
        layer_arn="",
    )
