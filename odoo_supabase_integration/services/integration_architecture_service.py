```python
from odoo import api, models
from odoo.addons.queue_job.job import job
from supabase_py import create_client, Client
import json

class IntegrationArchitectureService(models.Model):
    _name = 'odoo_supabase_integration.integration_architecture_service'
    _description = 'Service for handling integration architecture tasks'

    supabase_url = fields.Char()
    supabase_key = fields.Char()
    supabase_client = None

    def setup_supabase_client(self):
        self.supabase_client = create_client(self.supabase_url, self.supabase_key)

    @job
    def handle_data_synchronization(self, odoo_model_name, supabase_table_name):
        odoo_model = self.env[odoo_model_name]
        records = odoo_model.search([])
        for record in records:
            self.sync_record_to_supabase(record, supabase_table_name)

    def sync_record_to_supabase(self, record, supabase_table_name):
        data = json.loads(record.export_data(record.ids, record._fields.keys()).get('datas'))
        response = self.supabase_client.from(supabase_table_name).insert(data).execute()
        if response.error:
            _logger.error('Failed to sync record to Supabase: %s', response.error.message)

    @api.model
    def create(self, vals):
        record = super(IntegrationArchitectureService, self).create(vals)
        record.setup_supabase_client()
        return record

    @api.multi
    def write(self, vals):
        result = super(IntegrationArchitectureService, self).write(vals)
        self.setup_supabase_client()
        return result
```