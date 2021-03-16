import allure
import pytest

from base.get_driver import get_phone_driver
from base.page import Page



class TestDependenc:

    # def setup_class(self):
    #     self.driver = get_phone_driver("com.hsl.stock", ".module.main.StartV2Activity")
    #     self.page = Page(self.driver)
    #
    # def teardown_class(self):
    #     self.driver.quit()


    @pytest.mark.dependency()
    @pytest.mark.xfail(reason="deliberate fail")
    def test_a(self):
        assert False

    @pytest.mark.dependency()
    def test_b(self):
        pass

    @pytest.mark.dependency(depends=['test_a'])
    def test_c(self):
        pass

    @pytest.mark.dependency(depends=['test_b'])
    def test_d(self):
        pass