from brownie import network, config, AdvancedCollectible
import pytest
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    fund_with_link,
)
import time


def test_can_create_advanced_collectible_integration():
    # deploy the contract
    # create an NFT
    # get a random breed back
    # Arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("This test only for integration environment")
    # Act
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(advanced_collectible.address)
    creating_tnx = advanced_collectible.createCollectible({"from": get_account()})
    creating_tnx.wait(1)
    time.sleep(60)

    # Assert
    print(advanced_collectible.tokenCounter())
    assert advanced_collectible.tokenCounter() > 1
