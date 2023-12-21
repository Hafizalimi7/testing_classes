## Test Driven Metholodgy


## Ways To Run Test
cd [directory]

$ python3 -m unittest test.test_person

Running a single test case or test method:

Also you can run a single TestCase or a single test method:

$ python3 -m unittest test.test_person.TestClass

$ python3 -m unittest test.test_greeting.TestClass.test_type_error

# Running all tests
You can also use test discovery which will discover and run all the tests for you, they must be modules or packages named test*.py (can be changed with the -p, --pattern flag):

cd [directory] -$ python3 -m unittest discover or python3 -m unittest
