import unittest
from claim_payment_act.service_layer.abstracts import AddClaimPaymentAct


class TestAddClaimPaymentAct(unittest.TestCase):
    def setUp(self):
        self.data = {"title": "This is title   ", "description": "This is descriptions"}

    def test_add_claim_payment(self):
        expected_reasult = {
            "title": "This is title",
            "description": "This is descriptions",
        }
        payment_act = AddClaimPaymentAct(**self.data)
        self.assertDictEqual(payment_act.__dict__, expected_reasult)

    def test_empty_title_validator(self):
        self.data = {"title": "", "description": ""}
        with self.assertRaises(Exception) as context:
            AddClaimPaymentAct(**self.data)
            self.assertTrue(
                "Claim Payment Act Title cannot be empty or whitespace or null!"
                in context.exception
            )


if __name__ == "__main__":
    unittest.main()
