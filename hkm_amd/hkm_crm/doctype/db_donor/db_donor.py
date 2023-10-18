# Copyright (c) 2023, HKM Ahmedabad and contributors
# For license information, please see license.txt

import frappe

@frappe.whitelist()
def calculate_sms_count(doc):
    sms_count = frappe.get_all('Donor SMS', filters={'mobile_no': doc.mobile_no}, fields='count(name) as sms_count')[0]['sms_count']
    return sms_count

