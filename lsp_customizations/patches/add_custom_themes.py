import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def execute():
    custom_themes = ["lsp_theme", "arp_theme"]

    try:
        field = frappe.get_meta("User").get_field("desk_theme")
        if not field:
            frappe.throw("Cannot find 'desk_theme' field in User DocType")

        current_options = set(field.options.split("\n"))
        updated_options = list(current_options.union(custom_themes))

        make_property_setter(
            "User",
            "desk_theme",
            "options",
            "\n".join(sorted(updated_options)),
            "Select"
        )

        frappe.db.commit()
        frappe.clear_cache(doctype="User")
        frappe.msgprint("Custom themes added to Desk Theme options.")

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Failed to patch desk_theme options")
        raise