# maker: pouria rezaie
# این فایل شامل کلاس‌هایی برای مدیریت موجودی و محصولات فروشگاه است.

class Product:
    # کلاس برای ذخیره اطلاعات مربوط به یک محصول
    def __init__(self, id, name, size, color, price, quantity):
        self.id = id  # شناسه محصول
        self.name = name  # نام محصول
        self.size = size  # اندازه محصول
        self.color = color  # رنگ محصول
        self.price = price  # قیمت محصول
        self.quantity = quantity  # تعداد موجود

    def __str__(self):
        return f"{self.name} ({self.size}, {self.color}) - ${self.price} ({self.quantity} in stock)"

class Inventory:
    # کلاس برای مدیریت موجودی محصولات فروشگاه
    def __init__(self):
        self.products = []  # لیست محصولات

    def add_product(self, product):
        # اضافه کردن محصول به موجودی
        self.products.append(product)
        print(f"Product added: {product}")

    def update_product(self, id, **kwargs):
        # به‌روزرسانی اطلاعات محصول
        for product in self.products:
            if product.id == id:
                for key, value in kwargs.items():
                    setattr(product, key, value)
                print(f"Product updated: {product}")
                return
        print("Product not found.")

    def delete_product(self, id):
        # حذف محصول از موجودی
        self.products = [p for p in self.products if p.id != id]
        print(f"Product with ID {id} removed.")

    def view_inventory(self):
        # نمایش موجودی فعلی
        print("---- Inventory ----")
        for product in self.products:
            print(product)