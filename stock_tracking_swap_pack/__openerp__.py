# -*- coding: utf-8 -*-
#################################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 Julius Network Solutions SARL <contact@julius.fr>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################

{
    "name" : "Stock tracking swap",
    "version" : "1.0",
    "author" : "Julius Network Solutions,Odoo Community Association (OCA)",
    "description" : """Presentation:

This module add a wizard to swap packs in packaging.
This wizard is used to replace an object from a package.
Adding to the historical movements and parent objects

""",
    "website" : "http://www.julius.fr",
    "depends" : [
         "stock",
         "stock_tracking_extended",
#         "stock_move_packaging",
         "stock_tracking_child",
    ],
    "category" : "Warehouse Management",
    "images" : [],
    "demo" : [],
    "data" : [
        "wizard/swap_view.xml",
        'stock_view.xml',
    ],
    'test': [],
    'installable': False,
    'active': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
