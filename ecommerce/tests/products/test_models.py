import pytest

# //// Function Base ////

# @pytest.mark.django_db
# def test_category_str():
#     category = Category.objects.create(name="Clothes")
#     assert str(category) == "Clothes"

# @pytest.mark.django_db
# def test_brand_str():
#     brand = Brand.objects.create(name="Nike")
#     assert str(brand) == "Nike"


# @pytest.mark.django_db
# def test_product_str():
#     brand = Brand.objects.create(name="Apple")
#     product = Product.objects.create(name="iPhone", brand=brand)
#     assert str(product) == "iPhone"
    
    
# //// Class Base ////    
    
pytestmark = pytest.mark.django_db
class TestCategoryModel:
    def test_str_method(self,category_factory):
        category= category_factory(name='test_cat')    
        assert category.__str__() == 'test_cat'
        
        
class TestBrandModel:
    def test_str_method(self,brand_factory):
        brand=brand_factory(name="test_brand")
        assert brand.__str__() == "test_brand"
        
class TestProductModel:
    def test_str_method(self, product_factory):
       product = product_factory(name='test_product')        
       assert product.__str__() == 'test_product'          