import unittest

from examples.Person import Unknown



class TestClass(unittest.TestCase):
  user1 = Unknown("Tom", "Bradly", 11) 
  """creating another object""" 
  class Person1:
    def __init__(self,f_name, s_name, age) -> None:
      pass
  user2 = Person1("Mike", "Jones", 30)

  """testing if object exists"""
  def test_obj_in_class(self):
   self.assertIsInstance(self.user1, Unknown)
   self.assertNotIsInstance(self.user2, Unknown)

  """testing if TypeError for first name, last name and age"""
  def test_type_error(self):
    self.user3 = Unknown(2, "Thomsom", 90) 
    self.user4 = Unknown("Harry", 34, 34)
    self.user5 = Unknown("Harry", "Wilson", "yellow")
    with self.assertRaises(TypeError) as content:
      self.user3.raise_error()
    self.assertEqual(str(content.exception), "First name should be a string")

    with self.assertRaises(TypeError) as content:
      self.user4.raise_error()
    self.assertEqual(str(content.exception),"Last name should be a string")

    with self.assertRaises(TypeError) as content:
      self.user5.raise_error()
    self.assertEqual(str(content.exception), "Age has to be a interger")
  
  """testing if first name function"""
  def test_first_name_func(self):
    assert self.user1.first_name() == "Tom"
    assert self.user1.first_name() != "Max"
  
  """testing if last name function"""
  def test_last_name_func(self):
    assert self.user1.last_name() == "Bradly"
    assert self.user1.last_name() != "Sa"
  
  """testing if fullname function"""
  def test_fullname_func(self):
    assert self.user1.full_name() == "Tom Bradly"
    assert self.user1.full_name() != "Max Sa"
  
  """testing if age function"""
  def test_age_func(self):
    assert int(self.user1.person_age()) == 11
    assert int(self.user1.person_age()) != 4
  
  """testingbank account function"""
  def test_bank_func(self):
    assert int(self.user1.bank_acc()) == 24000
    assert int(self.user1.bank_acc()) != 55000

  """testing list of hobbies function"""
  def test_list_of_hobbies(self):
    assert "Tennis" in self.user1.list_of_hobbies()
    assert "Swimming" not in self.user1.list_of_hobbies()


  
    




if __name__ == "__main__":
  unittest.main()