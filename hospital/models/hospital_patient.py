# -*- encoding: utf-8 -*-
# © 2017 Mackilem Van der Laan, Trustcode
# © 2017 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'

    
    patient_name = fields.Char(string='Patient Name',)
    test = fields.Char(string='test Name',)
    doctor_id = fields.Many2one('hospital.doctor',string="Doctor")    
    #slkflnsdgndjng


    