from ipaddress import *
net = ip_network('192.168.240.0/255.255.255.0')
k = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('1') == b.count('0'):
        k += 1
print(k)
for mask in range(33):
    net1 = ip_network(f'165.112.200.70/{mask}', 0)
    net2 = ip_network(f'165.112.175.80/{mask}', 0)
    if net1 == net2:
        print(mask)
for mask in range(33):
    net = ip_network(f'118.193.30.139/{mask}', 0)
    print(net, net.netmask)
