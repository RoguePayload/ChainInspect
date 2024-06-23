import re
from datetime import datetime

def is_valid_url(url):
    """Check if a URL is valid."""
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or IP
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(url_pattern, url) is not None

def format_date(date):
    """Format a date string."""
    return date.strftime('%Y-%m-%d %H:%M:%S')

def truncate_string(s, length):
    """Truncate a string to a specified length."""
    if len(s) > length:
        return s[:length] + '...'
    return s

def calculate_hash(data):
    """Calculate a hash value for data."""
    # Example implementation; replace with your own logic
    return hash(data)

def encrypt_data(data):
    """Encrypt data."""
    # Example implementation; replace with your own logic
    return data

def decrypt_data(encrypted_data):
    """Decrypt encrypted data."""
    # Example implementation; replace with your own logic
    return encrypted_data

def validate_email(email):
    """Validate an email address."""
    # Example implementation; replace with your own logic
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return re.match(email_pattern, email) is not None

def generate_random_string(length):
    """Generate a random string of specified length."""
    # Example implementation; replace with your own logic
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Other helper functions can be added as needed

