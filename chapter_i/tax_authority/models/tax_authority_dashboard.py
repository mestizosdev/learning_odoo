from odoo import models, fields


class TaxAuthorityDashboard(models.Model):
    _name = 'tax.authority.dashboard'
    _description = 'Tax Authority Dashboard'

    name = fields.Char(required=True)