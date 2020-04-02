#IDE :PyCharm
import netaddr as netaddr
from netaddr import *
import json
import requests
from operator import itemgetter
class ipv_4:
    def __init__(self,p,exp_reg,ipv4_pref):
        request = requests.get("https://ip-ranges.amazonaws.com/ip-ranges.json")
        request_txt = request.text
        read_content = json.loads(request_txt)
        self.prefix = read_content[ipv4_pref]
        self.v = p
        self.f = p
        self.i = p
        self.j = p
        self.exp_regn=exp_reg
        self.copydict = self.prefix.copy()

    def _subnetsort_ipv4_(self):
        for replies_data in self.prefix:
            self.subnet_data()
            value = self.subnet_value
            self.copydict[self.v]["subnets"] = value
            self.v += 1
            self.f += 1
        self.copydict.sort(key=itemgetter('subnets'))
    def _regionsort_ipv4_(self):
        for replies_data in self.prefix:
            regn_data = self.copydict[self.j]['region']
            self.j = self.j + 1
            if self.exp_regn == regn_data:
                self.i = self.j - 1
                ipv_4.print_data(self)

    def subnet_data(self):
        ip_data = self.prefix[self.f]['ip_prefix']
        list_ip = (ip_data.split("."))
        net_id = (list_ip[-1].split("/"))
        blk_id = int(net_id[1])
        self.subnet_value = 32 - blk_id
        return self.subnet_value

    def print_data(self):
        l = self.i
        region_sorted = self.copydict[l]
        print(region_sorted)

class ipv_6(ipv_4):
    def __init__(self, p, exp_regn, ipv6_pref):
        ipv_4.__init__(self,p,exp_regn,ipv6_pref)
    def _subnetsort_ipv6_(self):
        ipv_4._subnetsort_ipv4_(self)
    def _regionsort_ipv6_(self):
        ipv_4._regionsort_ipv4_(self)
        ipv_6.print_data(self)

    def subnet_data(self):
        ip_data = self.prefix[self.f]['ipv6_prefix']
        list_ip = (ip_data.split(":"))
        net_id = (list_ip[-1].split("/"))
        blk_id = int(net_id[1])
        self.subnet_value = 129 - blk_id
        return self.subnet_value

    def print_data(self):
        l = self.i
        region_sorted = self.copydict[l]
        print(region_sorted)


if __name__ == "__main__":
    x = ipv_4(0, "eu-west-1", 'prefixes')
    x._subnetsort_ipv4_()
    print('''\n\n\bSorted IPv_4 based on CIDR size and region "eu-west-1" :\n''')
    x._regionsort_ipv4_()
    y = ipv_6(0, "eu-west-1", 'ipv6_prefixes')
    y._subnetsort_ipv6_()
    print('''\n\nSorted IPv_6 based on CIDR size and region "eu-west-1" :\n''')
    y._regionsort_ipv6_()




