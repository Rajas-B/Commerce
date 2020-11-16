from django.test import TestCase
import datetime
# Create your tests here.
a = datetime.datetime.now()
print(a.time().minute)
