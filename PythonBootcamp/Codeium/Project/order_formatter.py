# order_formatter.py
from jinja2 import Environment, FileSystemLoader
import jinja2

def format_order_email(customer_name, order_id, items, total_amount):
    env = Environment(loader=FileSystemLoader('.'))
    try:
        template = env.get_template('email_template.html')
    except jinja2.exceptions.TemplateNotFound:
        raise Exception("Unable to load email template. Ensure that 'email_template.html' is in the same directory as this script.")
    return template.render(
        customer_name=customer_name,
        order_id=order_id,
        items=items,
        total_amount=total_amount
    )
