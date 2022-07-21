import dns
import dns.resolver
import socket


def reverse_DNS(ip):
    try:
        result = socket.gethostbyaddr(ip)
    except:
        return []
    return [result[0]] + result[1]


def DNS_request(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        if result:
            print(domain)
            for answer in result:
                print(answer)
                print("Domain names: %s" % reverse_DNS(answer.to_text()))
    except:
        return


def subdomain_search(domain, dictionary, nums):
    for word in dictionary:
        subdomain = word + "." + domain
        DNS_request(subdomain)
        if nums:
            for i in range(0,10):
                s = word + str(i) + "." + domain
                try:
                    DNS_request(s)
                except:
                    pass



domain = "google.com"
d = "subdomains.txt"
dictionary = []
with open(d, "r") as f:
    dictionary = f.read().splitlines()
subdomain_search(domain, dictionary, True)