class Unknown:

  def __init__(self, f_name, l_name, age) -> None:

    self.f_name = f_name
    self.l_name = l_name 
    self.age = age
    self.wage = 2000
    self.year_salary = 0
    self.hobbies = []
    
  def raise_error(self):
      if not isinstance(self.f_name, str):
        raise TypeError("First name should be a string")
      if not isinstance(self.l_name, str):
        raise TypeError("Last name should be a string")
      if not isinstance(self.age, int):
        raise TypeError("Age has to be a interger")

  def first_name(self) -> str:
    return f"{self.f_name}"
  
  def last_name(self) -> str:
    return f"{self.l_name}"
  
  def full_name(self) -> str:
    return f"{self.f_name + ' ' + self.l_name}"
  
  def person_age(self) -> int:
    return f"{self.age}"
  
  def bank_acc(self) -> int:
    self.year_salary += self.wage * 12
    return f"{self.year_salary}"
  
  def list_of_hobbies(self) -> str:
    list_h = ["Ji jitsu", "Football", "Tennis", "Site Viewing", "Travelling"]

    for word in list_h:
      self.hobbies.append(word)
    return f"{self.hobbies}"

     
     




