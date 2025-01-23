import allure
import pytest

@allure.title(" verify the positive tc")
@allure.description("This is about 5 should match with 5pytest")
@pytest.mark.first
def test_method_positive_tc():
    print("testcase creation")
    assert 5==5

@allure.title(" verify the negative tc")
@pytest.mark.second
def test_negative_one():
    print("testcase creation")
    assert 2==5


