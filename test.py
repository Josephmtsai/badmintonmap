from django.test import Client
def testView():
    client = Client()
    assert 200 == 200