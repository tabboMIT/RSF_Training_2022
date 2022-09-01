{
    'name': 'Hospital TEST ',
    'version': '1.0',
    'license': 'LGPL-3',
    'category': 'Health Care',
    # 'depends': [
    # ],
    #ctrl+/ to comment line or multiple lines
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_patient.xml',
        'views/hospital_doctor.xml',
    ],
    
    'auto_install': False,
    'application': True,
    
}