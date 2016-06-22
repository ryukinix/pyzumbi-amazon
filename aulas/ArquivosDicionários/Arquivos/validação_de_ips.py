#validação de ips no arquivo 'ips'
def ip_ok(ip):
    ip = ip.rstrip()
    ip = ip.split('.')
    for value in ip:
        if int(value) > 255:
            return False
    return True
ips = open('ips', 'r')
ip_check = open('ip_válidos', 'w')
ip_mismatch = open('ip_inválidos', 'w')
for ip in ips.readlines():
	if ip_ok(ip):
		ip_check.write('%s\n' %ip.rstrip())
	else:
		ip_mismatch.write('%s\n' %ip.rstrip())
ips.close()
ip_check.close()
ip_mismatch.close()