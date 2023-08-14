import unittest

from claim_payment_act.service_layer.handlers import add_claim_payment_act
from DDD import tests


class TestPaymentAct(tests.VariconTestCase):
    def setUp(self):
        self.user_id = self.user.id
        self.cmd = {"title": "This is title", "description": "This is description"}
        return super().setUp()

    def test_add_claim_payment_act(self):
        expected_reasult = self.cmd
        reasult = add_claim_payment_act(user=self.user_id, cmd_=self.cmd)
        self.assertEqual(expected_reasult, reasult)


if __name__ == "__main__":
    tests.login(
        username="test_info@varicon.com.au",
        email="test_info@varicon.com.au",
    )
    unittest.main()
