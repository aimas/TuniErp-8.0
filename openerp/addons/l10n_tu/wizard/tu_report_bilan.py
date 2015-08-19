# -*- coding: utf-8 -*-

from openerp.osv import fields, osv


class account_bilan_report(osv.osv_memory):
    _name = 'account.bilan.report'
    _description = 'Account Bilan Report'

    def _get_default_fiscalyear(self, cr, uid, context=None):
        fiscalyear_id = self.pool.get('account.fiscalyear').find(cr, uid)
        return fiscalyear_id

    _columns = {
        'fiscalyear_id': fields.many2one('account.fiscalyear', 'Fiscal Year', required=True),
    }

    _defaults = {
        'fiscalyear_id': _get_default_fiscalyear
    }

    def print_bilan_report(self, cr, uid, ids, context=None):
        active_ids = context.get('active_ids', [])
        data = {}
        data['form'] = {}
        data['ids'] = active_ids
        data['form']['fiscalyear_id'] = self.browse(cr, uid, ids)[0].fiscalyear_id.id
        return self.pool['report'].get_action(
            cr, uid, ids, 'l10n_tu.report_l10ntubilan', data=data, context=context
        )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
