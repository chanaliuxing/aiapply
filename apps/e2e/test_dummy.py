import pytest

@pytest.mark.skip(reason="browser not available in CI")
def test_placeholder():
    assert True
