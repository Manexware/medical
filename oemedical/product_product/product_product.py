from openerp import models,fields


class ProductProduct(models.Model):
    _inherit = 'product.product'


    is_medicament = fields.Boolean(string='Medicament', help='Check if the product is a medicament')
    is_bed = fields.Boolean(string='Bed', help='Check if the product is a bed on the gnuhealth.center')
    is_vaccine = fields.Boolean(string='Vaccine', help='Check if the product is a vaccine')
    is_medical_supply = fields.Boolean(string='Medical Supply', help='Check if the product is a medical supply')
    is_insurance_plan = fields.Boolean(string='Insurance Plan', help='Check if the product is an insurance plan')

