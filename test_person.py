import unittest

from Person import Unknown



class TestClass(unittest.TestCase):
  user1 = Unknown("Hafiz", "Alimi", 28) 
  """creating another object""" 
  class Person1:
    def __init__(self,f_name, s_name, age) -> None:
      pass
  user2 = Person1("Mike", "Jones", 30)
  """testing if object exists"""
  def test_obj_in_class(self):
   self.assertIsInstance(self.user1, Unknown)
   self.assertNotIsInstance(self.user2, Unknown)
  """"""
  def test_first_name(self):
    self.user3 = Unknown("mike", "Alimi", 28) 
    
    with self.assertRaises(TypeError) as exc:
      name = self.user3.f_name
      self.assertEqual(name(exc.exception), "must be letter")
    
    
    # with self.assertRaises(Exception) as context:
    #         broken_function()

    #     self.assertTrue('This is broken' in context.exception)
    
    # self.assertTrue(self.user4.f_name,self.user4.raise_error())
   


if __name__ == "__main__":
  unittest.main()