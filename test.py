#pylint:disable=E0001
import os
base=os.path.abspath(os.path.dirname(__file__))
print (base)
print(os.path.dirname(__file__))
print(os.environ.get('DATABASE_URL'))