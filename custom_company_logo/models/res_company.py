from odoo import api, fields, models


class ResCompanyReport(models.Model):
    _inherit = 'res.company'

    header = fields.Binary(string='Report Header')
    footer = fields.Binary(string='Report Footer')


class BaseDocumentLayout(models.TransientModel):
    _inherit = 'base.document.layout'

    header = fields.Binary(related="company_id.header")
    footer = fields.Binary(related="company_id.footer")
