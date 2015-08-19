# -*- coding: utf-8 -*-
{
    'name': 'Tunisia - Accounting',
    'version': '1.0',
    'author': 'Aimas',
    'website': 'https://github.com/aimas/TuniErp',
    'category': 'Localization/Account Charts',
    'description': """
This is the module to manage the accounting chart for Tunisia in OpenERP.
========================================================================

This module applies to companies based in Tunisia.

""",
    'depends': ['base', 'account', 'account_chart', 'base_vat'],
    'data': [
        'l10n_tu_reports.xml',
        'tu_report.xml',
        'plan_comptable_general.xml',
        'l10n_tu_wizard.xml',
       
        'security/ir.model.access.csv',
        'wizard/tu_report_bilan_view.xml',
        'wizard/tu_report_compute_resultant_view.xml',
    ],
    'test': ['test/l10n_tu_report.yml'],
    'demo': [],
    'active': True,
    'auto_install': False,
    'installable': True,
    'images': [],
}
