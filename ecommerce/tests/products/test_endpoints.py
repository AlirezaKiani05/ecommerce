from urllib import response
import pytest
import json

from ecommerce.tests.conftest import api_client

pytestmark = pytest.mark.django_db

class TestCategoryEndpoints:
    
    endpoint="/api/category/"
    def test_category_get(self,category_factory,api_client):
        #Arrange
        category_factory.create_batch(4)
        #Act
        response = api_client().get(self.endpoint)
        #Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestBrandEndpoints:
    endpoint="/api/brand/"
    def test_brand_get(self,brand_factory,api_client):
        #arrange
        brand_factory.create_batch(3)
        #act
        response = api_client().get(self.endpoint)
        #assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3



class TestProductEndpoints:
    endpoint="/api/"
