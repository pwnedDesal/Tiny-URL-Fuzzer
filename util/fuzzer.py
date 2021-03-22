# coding: UTF-8

from urllib.parse import urlparse
import urllib
# import urllib2 # renamed into urllib
# import httplib renamed into http.client.
import requests
import http.client

print('inner fuzz.py')


class Fuzzer:
    def my_urlparse(self, url):
        try:
            parsed = urlparse(url)
            if parsed.port:
                return 'scheme=%s, host=%s, port=%d' % (parsed.scheme, parsed.netloc, parsed.port)
            else:
                return 'scheme=%s, host=%s, port=' % (parsed.scheme, parsed.netloc)
        except ValueError:
            return 'err'

    # def my_httplib(url):
    #     try:
    #         conn = httplib.HTTPConnection(urlparse(url).netloc)
    #         conn.request("GET", urlparse(url).path)
    #         data = conn.getresponse().read().strip()
    #         conn.close()
    #     except Exception:
    #         data = 'err'
    #     return data

    # def my_urllib(url):
    #     try:
    #         return urllib.urlopen(url).read().strip()
    #     except Exception:
    #         return 'err'
    def my_httpclient(self, url):
        try:
            conn = http.client.HTTPSConnection(url)
            return conn.request('GET', 'index.html').url
        except Exception:
            return 'err'

    def my_urllib(self, url):
        try:
            # return urllib.request.urlopen(url).read().strip()
            return urllib.request.urlopen(url).url
        except Exception:
            return 'err'

    def my_requests(self, url):
        try:
            return requests.get(url).content.strip()
        except Exception:
            return 'err'
