from typing import NamedTuple


class DnsServer(NamedTuple):
    nameservers: list[str]
    qname: str
    type: str


IPv4: list[DnsServer] = [
    DnsServer(
        [
            "216.239.32.10",  # ns1.google.com
            "216.239.34.10",  # ns2.google.com
            "216.239.36.10",  # ns3.google.com
            "216.239.38.10",  # ns4.google.com
        ],
        "o-o.myaddr.l.google.com",
        "TXT",
    ),
    DnsServer(
        [
            "208.67.220.220",
            "208.67.222.222",
        ],
        "resolver1.opendns.com",
        "A",
    ),
    DnsServer(
        [
            "193.108.88.1",  # ns1-1.akamaitech.net
        ],
        "whoami.akamai.net",
        "A",
    ),
]


IPv6: list[DnsServer] = [
    DnsServer(
        [
            "2001:4860:4802:32::a",
            "2001:4860:4802:34::a",
            "2001:4860:4802:36::a",
            "2001:4860:4802:38::a",
        ],
        "o-o.myaddr.l.google.com",
        "TXT",
    ),
    DnsServer(
        [
            "2620:119:35::35",
            "2620:119:53::53",
        ],
        "resolver1.opendns.com",
        "AAA",
    ),
]
