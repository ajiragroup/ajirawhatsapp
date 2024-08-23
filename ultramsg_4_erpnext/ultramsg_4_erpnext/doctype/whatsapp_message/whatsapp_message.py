# Copyright (c) 2023, ERPGulf and contributors
# For license information, please see license.txt

import frappe

# from frappe.model.document import Document
import requests
import frappe
from frappe.model.document import Document


class whatsappmessage(Document):
    @frappe.whitelist()
    def msg(
        self,
        token,
        recipient,
        message_url,
    ):
        #    message_url=message_url
        messagetosend = {"type": "text", "text": messagebody}
        payload = {
            "message": messagetosend,
            "src.name": srcname,
            "channel": "whatsapp",
            "source": source,
            "destination": recipient,
            "disablePreview": "False",
        }

        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "accept": "application/json",
            "apikey": apikey,
        }

        try:
            response = requests.post(message_url, data=payload, headers=headers)
            return response.text
        except Exception as e:
            return e
