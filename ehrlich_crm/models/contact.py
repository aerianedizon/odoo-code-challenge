from odoo import api, fields, models, _

class Contact(models.Model):
    _inherit = "res.partner"

    notes = fields.Char("Notes")
