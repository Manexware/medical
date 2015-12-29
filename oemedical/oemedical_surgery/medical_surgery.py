from openerp.osv import osv,fields


class surgery (osv.osv):
    _name = "oemedical.surgery"
    _description = "Surgery"
    _columns = {
        'name' : fields.many2one ('oemedical.procedure','Code', help="Procedure Code, for example ICD-10-PCS Code 7-character string"),
        'pathology' : fields.many2one ('oemedical.pathology','Base condition', help="Base Condition / Reason"),
        'classification' : fields.selection ([
                ('o','Optional'),
                ('r','Required'),
                ('u','Urgent'),
                                ], 'Surgery Classification', select=True),
        'surgeon' : fields.many2one('oemedical.physician','Surgeon', help="Surgeon who did the procedure"),
        'date': fields.datetime ('Date of the surgery'),
        'age': fields.char ('Patient age',size=3,help='Patient age at the moment of the surgery. Can be estimative'),
        'description' : fields.char ('Description', size=128),
        'extra_info' : fields.text ('Extra Info'),
        }

surgery ()


class medical_patient (osv.osv):
    _name = "oemedical.patient"
    _inherit = "oemedical.patient"
    _columns = {
        'surgery' : fields.many2many ('oemedical.surgery', 'patient_surgery_rel','patient_id','surgery_id', 'Surgeries'),

    }

medical_patient ()




