# maker: pouria rezaie
# این فایل شامل کلاس‌هایی برای مدیریت سفارشات است.

class Order:
    # کلاس برای ذخیره اطلاعات مربوط به یک سفارش
    def __init__(self, id, customer_id, product_id, quantity, status):
        self.id = id  # شناسه سفارش
        self.customer_id = customer_id  # شناسه مشتری
        self.product_id = product_id  # شناسه محصول
        self.quantity = quantity  # تعداد سفارش داده شده
        self.status = status  # وضعیت سفارش

    def __str__(self):
        return f"Order ID: {self.id}, Customer ID: {self.customer_id}, Product ID: {self.product_id}, Quantity: {self.quantity}, Status: {self.status}"

class OrderManager:
    # کلاس برای مدیریت سفارشات
    def __init__(self):
        self.orders = []  # لیست سفارشات

    def add_order(self, order):
        # اضافه کردن سفارش به لیست
        self.orders.append(order)
        print(f"Order added: {order}")

    def update_order(self, id, **kwargs):
        # به‌روزرسانی اطلاعات سفارش
        for order in self.orders:
            if order.id == id:
                for key, value in kwargs.items():
                    setattr(order, key, value)
                print(f"Order updated: {order}")
                return
        print("Order not found.")

    def view_orders(self):
        # نمایش لیست سفارشات
        print("---- Orders ----")
        for order in self.orders:
            print(order)