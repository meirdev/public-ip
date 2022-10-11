from ipaddress import IPv4Address, IPv6Address
from typing import Type, TypeVar

from .dns_servers import IPv4, IPv6
from .resolver import Options, async_resolver, resolver

IPAddress = TypeVar("IPAddress", IPv4Address, IPv6Address)


DNS_SERVERS = {
    IPv4Address: IPv4,
    IPv6Address: IPv6,
}


async def _async_public_ip(
    ip_version: Type[IPAddress], options: Options | None = None
) -> IPAddress:
    last_error = Exception()

    for dns_server in DNS_SERVERS[ip_version]:
        try:
            return ip_version(await async_resolver(dns_server, options))
        except Exception as error:
            last_error = error

    raise last_error


def _public_ip(
    ip_version: Type[IPAddress], options: Options | None = None
) -> IPAddress:
    last_error = Exception()

    for dns_server in DNS_SERVERS[ip_version]:
        try:
            return ip_version(resolver(dns_server, options))
        except Exception as error:
            last_error = error

    raise last_error


async def async_ipv4(options: Options | None = None) -> IPv4Address:
    return await _async_public_ip(IPv4Address, options)


async def async_ipv6(options: Options | None = None) -> IPv6Address:
    return await _async_public_ip(IPv6Address, options)


def ipv4(options: Options | None = None) -> IPv4Address:
    return _public_ip(IPv4Address, options)


def ipv6(options: Options | None = None) -> IPv6Address:
    return _public_ip(IPv6Address, options)
