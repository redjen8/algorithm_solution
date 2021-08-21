N = int(input())
ipAddr = list(input().rstrip().split('.') for _ in range(N))
net_addr, net_mask = [], []
for i in range(4):
    min_ip = int(ipAddr[0][i])
    max_ip = int(ipAddr[0][i])
    for tmp in ipAddr:
        if max_ip < int(tmp[i]):
            max_ip = int(tmp[i])
        if min_ip > int(tmp[i]):
            min_ip = int(tmp[i])
    if ~max_ip^min_ip == -1:
        net_mask.append(255)
    else:
        for j in range(9):
            if -(~max_ip^min_ip) <= 1 << j:
                net_mask.append(256 - (1 << j))
                for k in range(3):
                    net_mask.append(0)
                break
    net_addr.append(int(ipAddr[0][i])&net_mask[i])
net_mask = net_mask[:4]
print("{}.{}.{}.{}".format(net_addr[0], net_addr[1], net_addr[2], net_addr[3]))
print("{}.{}.{}.{}".format(net_mask[0], net_mask[1], net_mask[2], net_mask[3]))
