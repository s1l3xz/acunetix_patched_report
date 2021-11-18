API_BASE = "/api/v1/"

API_SCAN = API_BASE + "scans"
API_TARGET = API_BASE + "targets"
API_REPORT = API_BASE + "reports"

target_criticality_list = {
    "critical":"10",
    "high":"20",
    "normal":"10",
    "low":"0",
}

target_criticality_allowed = list(target_criticality_list.keys())

scan_profiles_list = {
    "full_scan":"11111111-1111-1111-1111-111111111111",
    "high_risk_vuln": "11111111-1111-1111-1111-111111111112",
    "xss_vuln": "11111111-1111-1111-1111-111111111116",
    "sql_injection_vuln": "11111111-1111-1111-1111-111111111113",
    "weak_passwords": "11111111-1111-1111-1111-111111111115",
    "crawl_only": "11111111-1111-1111-1111-111111111117",
}

report_profile_list = {
    "developer":"11111111-1111-1111-1111-111111111111",
    "XML":"21111111-1111-1111-1111-111111111111",
    "OWASP Top 10":"11111111-1111-1111-1111-111111111119",
    "Quick":"11111111-1111-1111-1111-111111111112",
}

scan_profiles_allowed = list(scan_profiles_list.keys())
report_profile_allowed = list(report_profile_list.keys())
