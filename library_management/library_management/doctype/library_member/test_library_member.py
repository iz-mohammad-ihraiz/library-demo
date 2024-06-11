# Copyright (c) 2024, Mohammad Ihraiz and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestLibraryMember(FrappeTestCase):
	def test_fullname_is_set_automatically(self):
		test_library_member = frappe.get_doc({
			"doctype": "Library Member",
			"first_name": "IZtech",
			"last_name": "Adel",
			"email_address": "test@mail.com",
			"phone": "+970-599-###-###"
		}).insert()

		self.assertEqual(test_library_member.full_name, "IZtech Adel")
