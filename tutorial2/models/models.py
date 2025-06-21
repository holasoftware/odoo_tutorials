from odoo import models, fields


class MyModel(models.Model):
    _name = 'tutorial2.my_model'
    _description = 'My Model'

    field1 = fields.Char(string='field1')
    field2 = fields.Char(string='field2')