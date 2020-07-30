import json
from api.tests import FunctionalTest


class TestRootController(FunctionalTest):

    def test_get_all(self):
        response = self.app.get('/people/')
        assert response.status_int == 200
        assert response.namespace[1] == 'Luke'
        assert response.namespace[2] == 'Leia'
        assert response.namespace[3] == 'Han'
        assert response.namespace[4] == 'Anakin'

    def test_get_one(self):
        response = self.app.get('/people/1/')
        assert response.status_int == 200
        assert response.body.decode() == 'Luke'

    def test_post(self):
        response = self.app.post('/people/')
        assert response.status_int == 201

    def test_put(self):
        response = self.app.put('/people/1/')
        assert response.status_int == 204

    def test_delete(self):
        response = self.app.delete('/people/1/')
        assert response.status_int == 204

    def test_not_found(self):
        response = self.app.get('/missing/', expect_errors=True)
        assert response.status_int == 404
        assert json.loads(response.body.decode()) == {
            'reason': 'The resource could not be found.'
        }
