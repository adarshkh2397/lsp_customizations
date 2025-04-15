import frappe

frappe.utils.logger.set_log_level("DEBUG")
logger = frappe.logger("api", allow_site=True, file_count=50)

@frappe.whitelist()
def company_theme():
    try:
        user_permissions = frappe.defaults.get_user_permissions(frappe.session.user)
        companies = user_permissions.get("Company")
        if not companies:
            return

        company_docname = companies[0].doc

        logger.info(f"{company_docname} is the company ")

        if company_docname == "Demo Test Corp":
            frappe.db.set_value("User", frappe.session.user, "desk_theme", "Modern_ui_theme")
        elif company_docname == "Reggie Steel":
            frappe.db.set_value("User", frappe.session.user, "desk_theme", "Dark")
        else:
            frappe.db.set_value("User", frappe.session.user, "desk_theme", "Light")
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "company_theme error")
