from django.test import Client
def testView():
    client = Client()
    response = client.get('/')
    assert 200 == response.status_code