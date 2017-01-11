# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name' : 'Shark Invoice Report',
    'version' : '1.1',
    'author' : 'OpenERP SA',
    'category' : 'Accounting & Finance',
    'description' : """
Accounting and Financial Management.
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
    'website': 'https://www.odoo.com/page/billing',
    'depends' : ['base', 'product', 'analytic', 'board', 'edi', 'report','sale'],
    'data': [ 'report_style.xml','invoice_report_inherit.xml','invoice_report_template_inherit.xml'
    ],


    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
