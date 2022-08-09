import unittest
import OOP_additional_task as Shop


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.prod_example1_true = Shop.Product("T-shirt", 200, 20)
        self.prod_example2_false = Shop.Product(125, "fgh", True)

    def test_prod_input(self):
        self.assertEqual(type(self.prod_example1_true.prod_name), str)
        self.assertNotEqual(type(self.prod_example2_false.prod_name), str)
        self.assertEqual(type(self.prod_example1_true.prod_price_uah), int)
        self.assertNotEqual(type(self.prod_example2_false.prod_price_uah), int)
        self.assertEqual(type(self.prod_example1_true.prod_amount), int)
        self.assertNotEqual(type(self.prod_example2_false.prod_amount), int)


class TestProductStorage(unittest.TestCase):

    def setUp(self):
        self.example_storage = Shop.ProductStorage()
        self.prod_example1_true = Shop.Product("T-shirt", 200, 20)

    def test_add_to_storage(self):
        self.example_storage.add_to_storage(self.prod_example1_true)
        self.assertIn(self.prod_example1_true, self.example_storage.storage)

    def test_delete_from_storage(self):
        self.example_storage.add_to_storage(self.prod_example1_true)
        self.example_storage.delete_from_storage(self.prod_example1_true)
        self.assertNotIn(self.prod_example1_true, self.example_storage.storage)


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.prod_example1_true = Shop.Product("T-shirt", 200, 20)
        self.example_storage = Shop.ProductStorage()
        self.cart_example = Shop.ShoppingCart(self.example_storage)
        self.adder_example = self.cart_example.add_item('T-shirt', 2)

    def test_add_item_to_cart(self):
        self.assertIsInstance(self.adder_example.name, str)
