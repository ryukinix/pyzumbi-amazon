ips = open("ips.txt", 'r')
ips_valids = []
ips_invalids = []
for ip in ips.readlines():
    for number in ip.split('.'):
        if int(number) > 255:
            ips_invalids.append(ip)
            break
    if ip not in ips_invalids:
        ips_valids.append(ip)
ips.close()

ips_out = open("ips_valids_and_invalids.txt", 'w')
ips_out.write("[Endereços válidos:]\n")
for ip in ips_valids:
    ips_out.write(ip)
ips_out.write("\n[Endereços inválidos:]\n")
for ip in ips_invalids:
    ips_out.write(ip)
ips_out.close()
