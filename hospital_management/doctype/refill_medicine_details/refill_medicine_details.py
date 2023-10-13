# Copyright (c) 2023, Satheesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class RefillMedicineDetails(Document):
    @frappe.whitelist()
    def refill_item(self):
        medi = frappe.db.get_value('Medicine Details', {'name': self.medicine_names}, ['quantity'])
        refill_medicine = frappe.new_doc("Refill Medicine Details")
        refill_medicine.quantity = self.quantity
        refill_medicine.medicine_names = self.medicine_names
        refill_medicine.insert()
        frappe.db.commit()
        frappe.msgprint("Refill Successfully..!")
        aft = float(medi) + float(self.quantity)
        frappe.db.set_value("Medicine Details", self.medicine_names, 'quantity', aft)
