import public_ip


def test_ipv4():
    public_ip.ipv4()


def test_ipv6():
    public_ip.ipv6()


async def test_async_ipv4():
    await public_ip.async_ipv4()


async def test_async_ipv6():
    await public_ip.async_ipv6()
