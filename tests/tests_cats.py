from random import choice


class TestsCats:

    def test_api_key_valid(self, cat, auth):
        content_type_header = "application/json; charset=utf-8";
        response = cat.get_cats_image(auth)
        assert response.status_code == 200, f'Expected status code 200, got {response.status_code}'
        assert response.headers['Content-Type'] == content_type_header, \
            f'The response does not include a header {content_type_header}, ' \
            f'but we received, {response.headers["Content-Type"]}'


    def test_image_retrieval(self, cat, auth):
        response = cat.get_cats_image(auth, params={'limit': 1})
        data = response.json()
        assert len(data) > 0, 'An empty object was received in the response'
        assert "url" in data[0], 'Data does not contain a URL'

    def test_invalid_api_key(self, cat):
        response = cat.get_cats_image('invalid_api_key')
        print(response.request.headers,
              response.json())
        assert response.status_code == 401, f'Expected status code 401, got {response.status_code}'

    def test_no_api_key(self, cat):
        response = cat.get_cats_image('')
        print(response.request.headers)
        assert response.status_code == 400, f'Expected status code 400, got {response.status_code}'

    def test_check_filter_by_breed(self, cat, auth):
        breed_id = choice(cat.get_cats_breeds().json()).get('id')
        response = cat.get_cats_image(auth, params={'breed_ids': breed_id, 'limit': 1})
        data = response.json()
        assert len(data) > 0, 'An empty object was received in the response'
        breeds = data[0].get('breeds', [])
        assert any(breed['id'] == breed_id for breed in breeds), f'Image does not match breed filter: {breed_id}'
