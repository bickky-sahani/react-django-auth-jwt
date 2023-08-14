import unittest
from claim_payment_act.adapters.repository import FakeClaimPaymentActSQLRepository
from claim_payment_act.domain.models import ClaimPaymentAct


class TestFakeClaimPaymentActSQLRepository(unittest.TestCase):
    def setUp(self):

        self.repository = FakeClaimPaymentActSQLRepository()
        self.fake_model1 = ClaimPaymentAct(
            id_=1, title="Some Random Act", description="Some Random Descriptions"
        )

    def test_add(self):
        reasult = self.repository.add(self.fake_model1)

        self.assertEqual(self.fake_model1, reasult)
        self.assertEqual(self.repository.data, [self.fake_model1])

    def test_get(self):
        reasult = self.repository.get(1)
        self.assertEqual(reasult, self.fake_model1)
        self.assertIsNone(reasult)

    # def test_update(self):
    #     updated_data = ClaimPaymentAct(
    #         id_=1, title="Another Act", description="Another Random Description"
    #     )
    #     reasult = self.repository.update(self.fake_model1)
    #     print(reasult)
    #     self.assertEqual(reasult, updated_data)


if __name__ == "__main__":
    unittest.main()
