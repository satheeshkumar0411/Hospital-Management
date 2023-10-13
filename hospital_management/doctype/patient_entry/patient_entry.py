# Copyright (c) 2023, Satheesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class PatientEntry(Document):
    @frappe.whitelist()
    def confirm_appointment(self):
        patient_type = self.patient_type
        if patient_type == "For Buying Medicine":
            med = frappe.db.get_value('Medicine Details', {'name': self.medicine_name}, ['quantity'])
            if med is None or self.quantity is None:
                frappe.throw(_('Invalid quantity data. Please check the medicine details and quantity entered.'))
            elif med < self.quantity:
                frappe.throw(_('The available quantity of {0} is {1}, so kindly take the available quantity.').format(self.medicine_name, med))
            patient_records_list = frappe.new_doc("Patient Records List")
            # total = self.mrp * self.quantity if self.mrp is not None and self.quantity is not None else None
            patient_records_list.medicine_name = self.medicine_name
            patient_records_list.costumer_name = self.costumer_name
            patient_records_list.quantity = self.quantity
            patient_records_list.mrp = self.mrp
            # patient_records_list.total_amount = total
            patient_records_list.date = self.date
            patient_records_list.insert()
            frappe.db.commit()
            frappe.msgprint("Saved Record Successfully..!")
            after = float(med)-float(self.quantity)
            frappe.db.set_value("Medicine Details",self.medicine_name,'quantity',after)

        else:
            doctors = frappe.get_all('Doctor', ['*'])
            for doctor in doctors:
                if doctor.get('status') == "Non-Active":
                    frappe.throw(_("The Doctor is not available right now."))
                else:
                    # total = self.mrp * self.quantity if self.mrp is not None and self.quantity is not None else None
                    patient_records_list = frappe.new_doc("Patient Records List")
                    patient_records_list.patient_type = self.patient_type
                    patient_records_list.patient_name = self.patient_name
                    patient_records_list.service = self.service
                    patient_records_list.problem = self.problem
                    patient_records_list.date = self.date
                    patient_records_list.doctor_name = self.doctor_name
                    patient_records_list.lab_name = self.lab_name
                    patient_records_list.costumer_name = self.costumer_name

                    # patient_records_list.medicine_name = self.medicine_name
                    # patient_records_list.costumer_name = self.costumer_name
                    # patient_records_list.quantity = self.quantity
                    # patient_records_list.mrp = self.mrp
                    # patient_records_list.total_amount = total
                    patient_records_list.insert()
                    frappe.db.commit()
            frappe.msgprint("Saved Record Successfully..!")


   
