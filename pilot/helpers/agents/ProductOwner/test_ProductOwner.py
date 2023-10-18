import builtins
from unittest.mock import patch
from dotenv import load_dotenv
from .ProductOwner import ProductOwner
from helpers.test_Project import create_project

from main import get_custom_print

load_dotenv()
builtins.print, ipc_client_instance = get_custom_print({})


@patch('helpers.AgentConvo.get_saved_development_step')
def test_inception(mock_get_step):
    # Given
    project = create_project()
    product_owner = ProductOwner(project)

    # When
    description = product_owner.run_inception()

    # Then
    assert description is not None
