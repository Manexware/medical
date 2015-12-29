from openerp import models,fields,_,api
from time import mktime,strptime
#from openerp.osv import osv, fields

#from tools.translate import _
#from mx import DateTime
import datetime

class patient_data (models.Model):
    _name = "oemedical.patient"
    _inherit = "oemedical.patient"

    receivable = fields.Float(compute='_get_credit',string='Receivable',help='Total amount this patient owes you',readonly=True)

    @api.one
    @api.depends('credit')
    def _get_credit(self):
        self.receivable=self.credit


class appointment (models.Model):
    _name = "oemedical.appointment"
    _inherit = "oemedical.appointment"

    def copy(self, cr, uid, id, default=None, context={}):
        default.update({'validity_status':'tobe'})
        return super(appointment,self).copy(cr, uid, id, default, context)

    def onchange_appointment_date(self, cr, uid, ids, apt_date):
        if apt_date:
            validity_date = datetime.datetime.fromtimestamp(mktime(strptime(apt_date,"%Y-%m-%d %H:%M:%S")))
            validity_date = validity_date+datetime.timedelta(days=7)
            v = {'appointment_validity_date':str(validity_date)}
            return {'value': v}
        return {}


    no_invoice = fields.Boolean (string ='Invoice exempt')
    appointment_validity_date = fields.Datetime ('Validity Date')
    validity_status = fields.Selection([('invoiced','Invoiced'),('tobe','To be Invoiced')],'Status')
    consultations = fields.Many2one ('product.product', 'Consultation Service', domain=[('type', '=', "service")], help="Consultation Services", required=True)

    _defaults = {
        'validity_status': lambda *a: 'tobe',
        'no_invoice': lambda *a: True
    }


class labtest (models.Model):
    _name = "oemedical.patient.lab.test"
    _inherit = "oemedical.patient.lab.test"


    no_invoice = fields.Boolean ('Invoice exempt')
    invoice_status = fields.Selection([('invoiced','Invoiced'),('tobe','To be Invoiced')],'Invoice Status')


    _defaults={
        'invoice_status': lambda *a: 'tobe',
        'no_invoice': lambda *a: True

       }

class patient_prescription_order (models.Model):

    _name = "oemedical.prescription.order"
    _inherit = "oemedical.prescription.order"


    no_invoice = fields.Boolean ('Invoice exempt')
    invoice_status = fields.Selection([('invoiced','Invoiced'),('tobe','To be Invoiced')],'Invoice Status')

    _defaults = {
        'invoice_status': lambda *a: 'tobe',
        'no_invoice': lambda *a: True
                }

