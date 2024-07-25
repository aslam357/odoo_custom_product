from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    brand_id = fields.Many2one('product.brand', string='Brand')
    @api.onchange('brand_id')
    def onchange_brand_id(self):
        if self.brand_id:
            self.name = f"{self.brand_id.name}"

