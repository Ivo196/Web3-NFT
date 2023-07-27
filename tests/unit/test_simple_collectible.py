from scripts.simple_collectible.deploy_and_create import deploy_and_create
from scripts.helpful_scripts import (
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from brownie import network
import pytest


def test_can_create_simple_collectible():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    simple_collectible = deploy_and_create()
    # Quiero asegurarme que el owner del token es el que creo el contrato
    assert simple_collectible.ownerOf(0) == get_account()
