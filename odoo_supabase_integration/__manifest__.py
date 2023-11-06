{
    "name": "odoo_supabase_integration",
    "version": "1.0",
    "category": "Extra Tools",
    "summary": "Advanced Integration between Odoo 16 Community Edition and Supabase",
    "sequence": 1,
    "author": "Your Company",
    "website": "http://www.yourcompany.com",
    "depends": [
        "base",
        "queue_job"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/odoo_supabase_view.xml",
        "data/odoo_supabase_data.xml"
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "description": """
Odoo-Supabase Advanced Integration Module
=========================================
This module provides a comprehensive, advanced integration solution between Odoo 16 Community Edition and Supabase, allowing for advanced data operations, real-time synchronization, and leveraging the full feature set of Supabase.
    """,
    "qweb": [
        "static/src/xml/odoo_supabase_templates.xml"
    ]
}