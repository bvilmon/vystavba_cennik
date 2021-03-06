# -*- coding: utf-8 -*-
{
    'name': "Vystavba",
    'summary': 'Výstavbový cenník',
    'description': "Vytváranie objednávky dodávateľom na základe definovaného cenníka",
    'author': "Igor Surovy / Branislav Vilmon",
    'website': "http://www.o2/sk",
    'category': 'Vystavba',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'security/vystavba_security.xml',
        'views/views.xml',
        'views/polozka_view.xml',
        'views/cenova_ponuka_view.xml',
        'views/cennik_view.xml',
        'views/osoba_view.xml',
        'workflows/cp_workflow.xml',
        'views/templates.xml',
        'report/report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}