from typing import NamedTuple

import dns.asyncresolver
import dns.resolver

from .dns_servers import DnsServer


class Options(NamedTuple):
    filename: str = "/etc/resolv.conf"
    configure: bool = True
    tcp: bool = False
    source: str | None = None
    source_port: int = 0
    lifetime: float | None = None

    def resolver(self):
        return dict(
            filename=self.filename,
            configure=self.configure,
        )

    def resolve(self):
        return dict(
            tcp=self.tcp,
            source=self.source,
            source_port=self.source_port,
            lifetime=self.lifetime,
        )


DEFAULT_OPTIONS = Options()


def _get_first_answer(answer: dns.resolver.Answer) -> str:
    return next(map(str, answer)).strip('"').strip()  # type: ignore


async def async_resolver(dns_server: DnsServer, options: Options | None = None) -> str:
    options = options or DEFAULT_OPTIONS

    dns_resolver = dns.asyncresolver.Resolver(**options.resolver())
    dns_resolver.nameservers = dns_server.nameservers

    answer = await dns_resolver.resolve(
        dns_server.qname, dns_server.type, **options.resolve()
    )

    return _get_first_answer(answer)


def resolver(dns_server: DnsServer, options: Options | None = None) -> str:
    options = options or DEFAULT_OPTIONS

    dns_resolver = dns.resolver.Resolver(**options.resolver())
    dns_resolver.nameservers = dns_server.nameservers

    answer = dns_resolver.resolve(
        dns_server.qname, dns_server.type, **options.resolve()
    )

    return _get_first_answer(answer)
