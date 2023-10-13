# Copyright (c) 2023, Satheesh and contributors
# For license information, please see license.txt

import datetime
import frappe

def execute(filters=None):
    columns, data = [], []
    columns = get_columns(filters)
    data = get_data(filters)
    return columns, data

def get_columns(filters):
    column = [
    ('Patient Type') + ':Data:150',
	('Date') + ':Date:90',
    ('Patient Name') + ':Data:150',
    ('Problem') + ':Data:180',
    ('Service') + ': Data:140',
    ('Doctor Name') + ': Data:110',
    ('Lab Name') + ':Data:120',
    ('Costumer Name') + ': Data:110',
    ('Medicine Name') + ': Data:110',
	('Quantity') + ':Data:120',
    ('Total Quantity') + ':Data:120',
	('MRP') + ':Currency:120',
    ('Total Amount') + ':Currency:120',

    ]
    return column

def get_data(filters):
	data = []
	record = frappe.db.get_all("Patient Records List",['*'])
	for r in record:
		qty = frappe.db.get_value('Medicine Details',{'name':r.medicine_name},['quantity'])
		mrp = frappe.db.get_value('Medicine Details',{'name':r.medicine_name},['mrp'])
		frappe.errprint(qty)
		row = [r.patient_type,r.date,r.patient_name,r.problem,r.service,r.doctor_name,r.lab_name,r.costumer_name,r.medicine_name,r.quantity,qty,mrp,r.total_amount]

			
		data.append(row)
	return data