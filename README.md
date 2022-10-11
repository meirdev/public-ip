# public-ip

Get your public IP address. Inspired by https://github.com/sindresorhus/public-ip.

# Example

```python
import public_ip

# Sync
public_ip.ipv4()
public_ip.ipv6()

# Async
async def foo():
    await public_ip.async_ipv4()
    await public_ip.async_ipv6()
```
