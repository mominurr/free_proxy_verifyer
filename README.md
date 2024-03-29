# free_proxy_verifyer

free_proxy_verifyer is a Python library that allows you to verify whether a proxy is working or not. It checks the functionality of a given proxy by making requests to various proxy detection servers. This library is useful for anyone who needs to ensure the reliability of proxy for their applications.


# Proxy Judges/Checkers

## HTTP/HTTPS

- [ProxyJudge](http://proxyjudge.us/)
- [MojeIP](http://mojeip.net.pl/asdfa/azenv.php)
- [ifconfig.me](https://ifconfig.me/ip)
- [ipinfo.io](https://ipinfo.io/ip)
- [checkip.amazonaws.com](https://checkip.amazonaws.com)
- [ipify.org](https://api.ipify.org/)
- [httpbin.org](https://httpbin.org/ip)
- [icanhazip.com](https://www.icanhazip.com/)
- [jsonip.com](https://jsonip.com/)
- [SeeIP](https://api.seeip.org/jsonip)
- [SmartProxy](https://ip.smartproxy.com/json)


# Installation

You can install free_proxy_verifyer via pip:

```
pip install free_proxy_verifyer
```

or

```
pip install git+https://github.com/mominurr/free_proxy_verifyer.git
```

When installing free_proxy_verifyer using pip, the necessary dependencies (requests) will be automatically installed along with the package. You don't need to separately install these dependencies.

# Usage

```
from free_proxy_verifyer import proxyVerify

# Create an instance of proxyVerify
checker = proxyVerify()

# Define the proxy address to be verified
proxy = "37.187.17.89:3128"

# Verify the proxy
result = checker.verify_proxy(proxy=proxy)

# Print the result
print(result)  # True if the proxy is working, else False

```

# How it Works

ProxyVerify works by randomly selecting proxy detection services from a predefined list and making requests through the provided proxy. If a response is received within the specified timeout and the status code is 200, it considers the proxy to be working.

# Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or create a pull request on GitHub.

# License

This project is licensed under the MIT License - see the LICENSE file for details.