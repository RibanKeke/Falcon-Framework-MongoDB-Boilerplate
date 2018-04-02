"""
Author: Robert Banziziki
Date: 21 february 2018
"""
import pytest
import json

class TestUsers():
    """
    Testing class for the users routes
    """

    def test_call_create_user_passes(self, client):
        response = client.simulate_post('/users', body=json.dumps({'name': 'Adam',
                                                                   'surname': 'Bradley'}),
                                        headers={"content-type": "application/json"})
        assert response.status_code == 200
        assert response.json['name'] == 'Adam'

    def test_call_delete_user_passes(self, client):
        response_1 = client.simulate_post('/users', body=json.dumps({'name': 'Adam',
                                                                   'surname': 'Bradley'}),
                                        headers={"content-type": "application/json"})
        user_id = response_1.json['id']

        response_2 = client.simulate_delete('/users', body=json.dumps({'user_id': user_id}),
                                        headers={"content-type": "application/json"})

        assert response_2.json['success'] == True

    def test_call_delete_user_fails(self, client):

        user_id = "afeafeafafeafeaeafea"

        response_2 = client.simulate_delete('/users', body=json.dumps({'user_id': user_id}),
                                        headers={"content-type": "application/json"})

        assert response_2.status == '400 Bad Request'
