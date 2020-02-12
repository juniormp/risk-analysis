from django.test import TestCase
from domain.entity.product.product import Product, PRODUCT_SCORE_DEFAULT


class TestProduct(TestCase):
    def test_should_add_points(self):
        product = Product(status=PRODUCT_SCORE_DEFAULT, score=0)

        product.add_score_points(1)
        product.add_score_points(2)
        product.add_score_points(10)

        self.assertEqual(product.get_score(), 13)

    def test_should_deduct_points(self):
        product = Product(status=PRODUCT_SCORE_DEFAULT, score=0)

        product.deduct_score_points(1)
        product.deduct_score_points(2)
        product.deduct_score_points(13)

        self.assertEqual(product.get_score(), -16)
