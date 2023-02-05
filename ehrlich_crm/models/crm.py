from odoo import api, fields, models, _

class CRMStage(models.Model):
    _inherit = "crm.stage"

    is_custom_status = fields.Boolean("Is Custom Status", default=False)

class CRMSalesTeam(models.Model):
    _inherit = "crm.team"

    opportunity_ids = fields.One2many("crm.lead", "team_id", string="Opportunity Ids")
