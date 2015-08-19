# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class l10n_tu_report(osv.osv):
    _name = 'l10n.tu.report'
    _description = 'Report for l10n_tu'
    _columns = {
        'code': fields.char('Code', size=64),
        'name': fields.char('Name', size=100),
        'line_ids': fields.one2many('l10n.tu.line', 'report_id', 'Lines', copy=True),
    }
    _sql_constraints = [
        ('code_uniq', 'unique (code)','The code report must be unique !')
    ]

l10n_tu_report()
class l10n_tu_line(osv.osv):
    _name = 'l10n.tu.line'
    _description = 'Report Lines for l10n_tu'
    _columns = {
        'code': fields.char('Variable Name', size=64),
        'definition': fields.char('Definition'),
        'name': fields.char('Name'),
        'report_id': fields.many2one('l10n.tu.report', 'Report'),
    }
    _sql_constraints = [
        ('code_uniq', 'unique (code)', 'The variable name must be unique !')
    ]

l10n_tu_line()
