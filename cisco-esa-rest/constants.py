"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

ORDER_BY_MAPPING = {
    "From Address": "from_address",
    "To Address": "to_address",
    "Subject": "subject"
}
SORT_MAPPING = {
    "Ascending": "asc",
    "Descending": "desc"
}
FILTER_MAPPING = {
    "Contains": "contains",
    "Is": "is",
    "Begins With": "begins_with",
    "Ends With": "ends_with",
    "Does Not Contain": "does_not_contain"
}

REPORT_TYPE_MAPPING = {
    "Mail Incoming Traffic Summary": "mail_incoming_traffic_summary",
    "Reporting System": "reporting_system",
    "Mail VOF threat Summary": "mail_vof_threat_summary",
    "Mail VOF Specific Threat Summary": "mail_vof_specific_threat_summary",
    "Mail AMP Threat Summary": "mail_amp_threat_summary"
}
