import factory
from products.models import Category, Product, Brand


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n:"category_%d" %n)


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand
        
    name = "brand_test"    
    
    



class ProductFactory(factory.django.DjangoModelFactory):
    name = "product_test"
    category = factory.SubFactory(CategoryFactory)
    description = "product_description"
    is_digital = True
    brand = factory.SubFactory(BrandFactory)

    class Meta:
        model = Product
