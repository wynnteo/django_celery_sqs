from celery import shared_task
from .models import Product 
import time

@shared_task(bind=True, max_retries=3, acks_late=True)
def update_product_stock(self, order_id, product_id, quantity):
    try:
        print("Start process_order: %s" % time.ctime())
        print("Order ID : %s" % order_id)
        print("Product ID : %s" % product_id)

        # Simulate some time-consuming operation
        time.sleep(20)

        product = Product.objects.get(pk=product_id)
        
        product.stock -= quantity
        product.save()

        print(f"Task completed for Order ID {order_id}")
    except Product.DoesNotExist:
        print(f"Product with ID {product_id} does not exist.")
    except Exception as e:
        print(f"An error occurred while updating product stock. Error: {e}")
        raise self.retry(exc=e)