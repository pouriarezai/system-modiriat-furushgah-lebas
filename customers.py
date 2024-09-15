# maker: pouria rezaie
# این فایل شامل کلاس‌هایی برای مدیریت مشتریان است.

class Customer:
    # کلاس برای ذخیره اطلاعات مربوط به یک مشتری
    def __init__(self, id, name, email):
        self.id = id  # شناسه مشتری
        self.name = name  # نام مشتری
        self.email = email  # ایمیل مشتری

    def __str__(self):
        return f"Customer: {self.name} ({self.email})"

class CustomerManager:
    # کلاس برای مدیریت مشتریان
    def __init__(self):
        self.customers = []  # لیست مشتریان

    def add_customer(self, customer):
        # اضافه کردن مشتری به لیست
        self.customers.append(customer)
        print(f"Customer added: {customer}")

    def update_customer(self, id, **kwargs):
        # به‌روزرسانی اطلاعات مشتری
        for customer in self.customers:
            if customer.id == id:
                for key, value in kwargs.items():
                    setattr(customer, key, value)
                print(f"Customer updated: {customer}")
                return
        print("Customer not found.")

    def view_customers(self):
        # نمایش لیست مشتریان
        print("---- Customers ----")
        for customer in self.customers:
            print(customer)