from .models import *

customers = Customer.objects.all()
firstCustomer = Customer.objects.first()
lastCustomer = Customer.objects.last()
customerByName = Customer.objects.get(name = 'Injus')
customerById = Customer.objects.get(id = 3)
firstCustomer.order_set.all()
order = Order.objects.first()
parentName = order.customer.name
products = Product.objects.filter(category = 'Out Door')
LeastToGreatest = Product.objects.all().order_by('id')
GreatestToLeast = Product.objects.all().order_by('-id')
ProductsFiltered = Product.objects.filter(tags__name = 'sports')

#RELATED SET EXAMPLE
class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(Customer)
	name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#Returns all child models related to parent
parent.childmodel_set.all()


