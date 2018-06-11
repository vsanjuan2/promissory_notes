# -*- coding: utf-8 -*-
# © 2018 Salvador Sanjuan @ Acelerem salvador@aceleratuempresa.net
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name' : 'Acelerem Promissory',
    'version' : '1.0',
    'author' : 'Acelerem',
    'category' : 'Accounting & Finance',
    'description' : """
Chimpex Accounting and Financial Management.
====================================

Financial and accounting module that covers:
--------------------------------------------
    * General Accounting
    * Cost/Analytic accounting
    * Third party accounting
    * Taxes management
    * Budgets
    * Customer and Supplier Invoices
    * Bank statements
    * Reconciliation process by partner

Creates a dashboard for accountants that includes:
--------------------------------------------------
    * List of Customer Invoices to Approve
    * Company Analysis
    * Graph of Treasury

Processes like maintaining general ledgers are done through the defined Financial Journals (entry move line or grouping is maintained through a journal)
for a particular financial year and for preparation of vouchers there is a module named account_voucher.
    """,
    'website': 'odoo.acelerem.com',
    'depends' : ['account'],
    'data': [
        'account_invoice_view.xml',

    ],
    'qweb' : [],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
