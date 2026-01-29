# -*- coding: utf-8 -*-
{
    'name': "QLVB",

    'summary': """
        Đổi theo ý tưởng của bạn""",

    'description': """
        mô tả ý tưởng của bạn
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','nhan_su','quan_ly_khach_hang'],

    # always loaded
    'data': [
    'security/ir.model.access.csv',
    'views/loai_van_ban.xml',
    'views/van_ban_den.xml',
    'views/van_ban_di.xml',
    'views/menu.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
