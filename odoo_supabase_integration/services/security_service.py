```python
from odoo import api, models
import logging
from cryptography.fernet import Fernet

_logger = logging.getLogger(__name__)

class SecurityService(models.Model):
    _name = 'odoo_supabase.security_service'
    
    def generate_encryption_key(self):
        """
        Generate a new encryption key
        """
        key = Fernet.generate_key()
        _logger.info('New encryption key generated')
        return key

    def encrypt_data(self, data, key):
        """
        Encrypt the data using the provided key
        """
        cipher_suite = Fernet(key)
        encrypted_data = cipher_suite.encrypt(data)
        _logger.info('Data encrypted successfully')
        return encrypted_data

    def decrypt_data(self, encrypted_data, key):
        """
        Decrypt the data using the provided key
        """
        cipher_suite = Fernet(key)
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        _logger.info('Data decrypted successfully')
        return decrypted_data

    def handle_error(self, error):
        """
        Handle errors and log them
        """
        _logger.error('An error occurred: %s', error)
```
