from odoo import models, fields

class People(models.Model):
    _inherit = 'people'
    
    gender = fields.Selection(selection_add=[('lgbt', 'LGBT')], ondelete={'lgbt': 'set null'})
    