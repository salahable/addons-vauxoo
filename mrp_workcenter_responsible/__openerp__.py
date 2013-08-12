#!/usr/bin/python
# -*- encoding: utf-8 -*-
###############################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://openerp.com.ve>).
#    All Rights Reserved
############# Credits #########################################################
#    Coded by: Katherine Zaoral          <katherine.zaoral@vauxoo.com>
#    Planified by: Katherine Zaoral      <katherine.zaoral@vauxoo.com>
#    Audited by: Humberto Arocha         <hbto@vauxoo.com>
###############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################

{
    "name": "MRP Workcenter Responsible",
    "version": "1.0",
    "author": "Vauxoo C.A.",
    "website": "http://www.openerp.com.ve",
    "category": "MRP",
    "description": """
MRP Workcenter Responsible
==========================

Add the functionality of a responsible from a work center and it childs work
orders.
""",
    "depends": ["mrp_operations"],
    "data": [
        "view/mrp_workcenter_responsible_view.xml",
    ],
    "demo": [],
    "test": [],
    "active": False,
    "installable": True,
}