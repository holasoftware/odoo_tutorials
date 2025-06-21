from odoo import models, fields


class MyModel(models.Model):
    _name = 'tutorial1.my_model'
    _description = "My Model"

    color1 = fields.Integer(string='Color1')
    color2 = fields.Char(string='Color2')