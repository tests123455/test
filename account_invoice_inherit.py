import itertools
from lxml import etree
from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp.tools import float_compare
import openerp.addons.decimal_precision as dp
from num2words import num2words

#Upated By Roniya
class account_invoice(models.Model):
    _inherit = "account.invoice"

    total_quantity = fields.Char('Total Quantity', compute='total_quant')

    def _amount_to_text(self, amount):
        text = num2words(amount)
        return text

    @api.one
    @api.depends('invoice_line')
    def _get_total_quantity(self):
        total = 0
        for item_line in self.invoice_line:
            total += item_line.quantity
        self.invoice_line = total
        self.total_quantity = total

    def total_quant(self):
        total = 0
        for item_line in self.invoice_line:
            total += item_line.quantity
        self.total_quantity = total
account_invoice()
class sale_order(models.Model):
    _inherit = "sale.order"

    tot_qty = fields.Char('Total Quantity',compute='total_quant')

    def total_quant(self):
        total = 0
        for item_line in self.order_line:
            total += item_line.product_uom_qty
        self.tot_qty = total
sale_order()


