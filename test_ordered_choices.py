import unittest

from ordered_choices import OrderedChoices, OrderedChoiceItem

class TestOrderedChoices(unittest.TestCase):
    def setUp(self):
        class MyChoices(OrderedChoices):
            var_1 = OrderedChoiceItem('var_1')
            var_2 = OrderedChoiceItem('var_2')

        self.MyChoices = MyChoices

    def test_class_attributes(self):
        self.assertEqual(self.MyChoices.var_1, 'var_1')
        self.assertEqual(self.MyChoices.var_2, 'var_2')

    def test_get_django_choices_input(self):
        res = self.MyChoices.get_django_choices_input()
        print(res)
        # TODO: change the assert statements after OrderedChoices has a fixed attributes order
        self.assertTrue(res == [('var_1', ), ('var_2', )] or res == [('var_2', ), ('var_1', )])


if __name__ == '__main__':
    unittest.main()