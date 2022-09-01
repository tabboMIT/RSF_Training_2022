# -*- encoding: utf-8 -*-
# © 2017 Mackilem Van der Laan, Trustcode
# © 2017 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _rec_name = 'doctor_name'

    
    doctor_name = fields.Char(string='Doctor Name',)
    phone = fields.Integer(string="Phone", ) 
    patient_ids = fields.One2many(string='Patient',comodel_name='hospital.patient',inverse_name='doctor_id' )   
   
    



    