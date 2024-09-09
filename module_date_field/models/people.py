from odoo import models, fields

class People(models.Model):
    _name = 'people'
    _description = 'People'
    
    name = fields.Char(string='Name')
    
    # Date fields
    date = fields.Date(string='Date')
    
    # Datetime fields
    datetime = fields.Datetime(string='Date time')
    
    def action_check(self):
        pass
    