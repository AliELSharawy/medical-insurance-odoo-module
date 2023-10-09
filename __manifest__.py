# -*- coding: utf-8 -*-
{
    'name': "demo",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/doctor.xml',
        'views/visit.xml',
        'views/patient.xml',
        'views/insurance_company.xml',
        'views/insurance_plan.xml',
        'views/insurance_plan_line.xml',
        'views/claim.xml',
        'views/claim_line.xml',
        'views/visit_line.xml',
        'views/demo_config_settings.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}