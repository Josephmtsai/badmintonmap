from django.test import Client
def firstTest():
    client = Client()
    response = client.get('/')
    assert 200 == response.status_code