from acunetix import Acunetix
scan_targets = ""
scanned_targets = ""
saved_targets = ""
acunetix = Acunetix(host="ip:port", api="API_KEY")

# delete all targets
# acunetix.delete_all_targets()

# scan domain list
# domains = ['domain1','domain2']

# print(acunetix.targets());


for i in acunetix.targets()['targets']:
    if(i['last_scan_session_status'] == 'completed'):
        acunetix.generated_report(i['last_scan_id'])
        acunetix.delete_target(i['target_id'])

# for domain in domains:
#     acunetix.start_scan(domain)
