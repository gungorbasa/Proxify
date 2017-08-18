# Proxify
Crawls web and finds proxy servers.

## Usage
```
proxy = ProxyList()
proxy.find_proxy(size=None, types=None)
```
If size is ```None``` it will return as much as it can find. However, size can be set and returns size number of proxies.
If types is ```None``` it returns any type of proxies. Type looks for a list of types. Possible types are ``` anonymous, elite proxy, transparent ```.

Below commands result with the same output.
```
proxy.find_proxy(size=None, types=None)
proxy.find_proxy(size=None, types=["anonymous", "elite proxy", "transparent"])
```

If someone is looking for 20 ```elite proxy```. Below, command will work for her.
```
proxy = ProxyList()
proxy.find_proxy(size=20, types=["elite proxy"])
```

### Finding Online Proxies
Due to extra requests, this operation takes longer time than using ```find_proxy```. Use with caution.
Note: If you trust ```us-proxy.org``` you don't have to use method to find online proxies.

```
proxy = ProxyList()
proxy.find_online_proxies(size=20, types=['anonymous', 'elite proxy'])
```

### Proxy Output Format
Returns list of proxies in the format of:
```
[["http/https", "ip:port"]]
```
#### Example Output

```
[['http', '47.89.185.47:80'], ['https', '204.57.105.150:8080'], ['https', '66.70.191.215:1080'], ['http', '45.32.223.119:8088'], ['https', '45.55.194.88:3128'], ['https', '52.11.203.152:8083'], ['https', '50.203.117.22:80'], ['http', '47.52.24.117:80'], ['http', '192.95.18.162:8080'], ['https', '38.87.235.166:53281']]
```


