from odoo import api, fields, models, _

class CRMStage(models.Model):
    _inherit = "crm.stage"

    is_custom_status = fields.Boolean("Is Custom Status", default=False)
