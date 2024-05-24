#########################################################################
#########################################################################
#### THIS FILE HAS TO RUN IN A CMD PROMPT OTHERWISE IT WILL NOT WORK ####
#########################################################################
#########################################################################
import pytest
import os

## DONT TOUTCH
## This junk here is to get the path for all of the tests so that you guys don't have to manualy add them every time we run the tests.
path = str(os.getcwd())
tests = os.listdir(path)
remove = []
for i in tests:
    if i.title() == 'Starttests.Py' or i.title() == '__Pycache__' or i.title() == '.Pytest_Cache':
        remove.append(i)
for i in remove:
    tests.remove(i)

## DONT TOUTCH
## This code runs all the tests that are in de UnitTest folder.
def run_tests():
    for i in tests:
        test = str(path + "\\" + i)
        if pytest.main([test]) == 1:
            print(f"{i.title()} Tests failed.")
        else:
            print(f"{i.title()} Tests passed.")

if __name__ == '__main__':
    run_tests()
    print("Ran tests for ", tests)