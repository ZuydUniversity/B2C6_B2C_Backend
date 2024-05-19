import os
import django

os.environ.setdefault('DJANGOSETTINGSMODULE', 'MyDB.settings')


from MySQLdb import woordtest
django.setup()
def test_db_connection():
    # Voeg een string toe aan de database
    test_string = "Hello, World!"
    test_instance = woordtest(woord=test_string)
    test_instance.save()

    # Haal de string op uit de database
    retrieved_instance = woordtest.objects.get(woord=test_string)
    print("Retrieved string from database:", retrieved_instance.woord)

if __name__ == "__main__":
    test_db_connection()
    