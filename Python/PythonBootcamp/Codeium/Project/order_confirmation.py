# order_confirmation.py
from order_formatter import format_order_email
from email_sender import send_email

def send_order_confirmation(customer_name, customer_email, order_id, items, total_amount):
    email_body = format_order_email(customer_name, order_id, items, total_amount)
    send_email(
        to_email=customer_email,
        subject="Order Confirmation",
        body=email_body,
        smtp_server="smtp.example.com",
        smtp_port=587,
        smtp_user="your_email@example.com",
        smtp_password="your_password"
    )

if __name__ == "__main__":
    customer_name = "John Doe"
    customer_email = "johndoe@example.com"
    order_id = "123456"
    items = [
        {"name": "Widget", "quantity": 2, "price": 19.99},
        {"name": "Gadget", "quantity": 1, "price": 29.99}
    ]
    total_amount = 69.97
    
    send_order_confirmation(customer_name, customer_email, order_id, items, total_amount)
