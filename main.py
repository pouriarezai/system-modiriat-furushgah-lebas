# maker: pouria rezaie
# این فایل برای اجرای برنامه و ارتباط بین کلاس‌ها استفاده می‌شود.

from inventory import Inventory, Product
from customers import CustomerManager, Customer
from orders import OrderManager, Order

def main():
    # ایجاد نمونه‌های مدیریت موجودی، مشتریان و سفارشات
    inventory = Inventory()
    customer_manager = CustomerManager()
    order_manager = OrderManager()

    while True:
        print("\n1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. View Inventory")
        print("5. Add Customer")
        print("6. Update Customer")
        print("7. View Customers")
        print("8. Add Order")
        print("9. Update Order")
        print("10. View Orders")
        print("11. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            # اضافه کردن محصول جدید
            id = int(input("Enter product ID: "))
            name = input("Enter product name: ")
            size = input("Enter product size: ")
            color = input("Enter product color: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Product(id, name, size, color, price, quantity)
            inventory.add_product(product)

        elif choice == '2':
            # به‌روزرسانی اطلاعات محصول
            id = int(input("Enter product ID to update: "))
            print("Leave fields empty if you don't want to update them.")
            name = input("Enter new product name (leave blank if no change): ")
            size = input("Enter new product size (leave blank if no change): ")
            color = input("Enter new product color (leave blank if no change): ")
            price = input("Enter new product price (leave blank if no change): ")
            quantity = input("Enter new product quantity (leave blank if no change): ")
            updates = {}
            if name:
                updates['name'] = name
            if size:
                updates['size'] = size
            if color:
                updates['color'] = color
            if price:
                updates['price'] = float(price)
            if quantity:
                updates['quantity'] = int(quantity)
            inventory.update_product(id, **updates)

        elif choice == '3':
            # حذف محصول
            id = int(input("Enter product ID to delete: "))
            inventory.delete_product(id)

        elif choice == '4':
            # نمایش موجودی
            inventory.view_inventory()

        elif choice == '5':
            # اضافه کردن مشتری جدید
            id = int(input("Enter customer ID: "))
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            customer = Customer(id, name, email)
            customer_manager.add_customer(customer)

        elif choice == '6':
            # به‌روزرسانی اطلاعات مشتری
            id = int(input("Enter customer ID to update: "))
            print("Leave fields empty if you don't want to update them.")
            name = input("Enter new customer name (leave blank if no change): ")
            email = input("Enter new customer email (leave blank if no change): ")
            updates = {}
            if name:
                updates['name'] = name
            if email:
                updates['email'] = email
            customer_manager.update_customer(id, **updates)

        elif choice == '7':
            # نمایش لیست مشتریان
            customer_manager.view_customers()

        elif choice == '8':
            # اضافه کردن سفارش جدید
            id = int(input("Enter order ID: "))
            customer_id = int(input("Enter customer ID: "))
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))
            status = input("Enter order status: ")
            order = Order(id, customer_id, product_id, quantity, status)
            order_manager.add_order(order)

        elif choice == '9':
# به‌روزرسانی اطلاعات سفارش
            id = int(input("Enter order ID to update: "))
            print("Leave fields empty if you don't want to update them.")
            customer_id = input("Enter new customer ID (leave blank if no change): ")
            product_id = input("Enter new product ID (leave blank if no change): ")
            quantity = input("Enter new quantity (leave blank if no change): ")
            status = input("Enter new status (leave blank if no change): ")
            updates = {}
            if customer_id:
                updates['customer_id'] = int(customer_id)
            if product_id:
                updates['product_id'] = int(product_id)
            if quantity:
                updates['quantity'] = int(quantity)
            if status:
                updates['status'] = status
            order_manager.update_order(id, **updates)

        elif choice == '10':
            # نمایش لیست سفارشات
            order_manager.view_orders()

        elif choice == '11':
            # خروج از برنامه
            break

if __name__ == "__main__":
    main()