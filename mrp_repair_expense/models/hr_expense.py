# -*- coding: utf-8 -*-
# (c) 2015 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import api, fields, models


class HrExpenseExpense(models.Model):
    _inherit = 'hr.expense.expense'

    repair_id = fields.Many2one(string='Repair order',
                                comodel_name='mrp.repair')
    repair_analytic_account = fields.Many2one(
        string='Analytic account', comodel_name='account.analytic.account',
        related='repair_id.analytic_account')
    repair_state = fields.Selection(string='Repair State',
                                    related='repair_id.state')

    @api.multi
    @api.onchange('repair_id')
    def onchange_repair_id(self):
        self.ensure_one()
        for line in self.line_ids:
            line.analytic_account = self.repair_id.analytic_account
            line.repair_id = self.repair_id


class HrExpenseLine(models.Model):
    _inherit = 'hr.expense.line'

    repair_id = fields.Many2one(string='Repair order',
                                comodel_name='mrp.repair')
