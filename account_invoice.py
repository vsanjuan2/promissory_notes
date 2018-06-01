# -*- coding: utf-8 -*-
# © 2018 Tosin Komolafe @ Ballotnet Solutions Ltd <komolafetosin@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api, _


class account_invoice(models.Model):
    _inherit = 'account.invoice'

    payment_status = fields.Selection([
            ('na','Na'),
            ('pending','Pending'),
            ('received','Received'),
            ('pledged','Pledged'),
            ('deposited','Deposited'),
        ], string='Payment Status', 
        default='na',
        required=True)

    promissory_note_number = fields.Char(
        string='Promissory Note Number')

    pledged_number = fields.Char(
        string='Pledge Number')

    pledged_date = fields.Date(
        string='Pledge Date')

    pledge_bank_id = fields.Many2one(
        comodel_name='res.partner.bank', 
        string='Pledge Bank')

    payment_pledge = fields.Boolean(
        string='Promissory note')

    @api.multi
    def onchange_payment_term_date_invoice(self, payment_term_id, date_invoice):
        if not date_invoice:
            date_invoice = fields.Date.context_today(self)
        return {'value': {'date_due': self.date_due or date_invoice}}