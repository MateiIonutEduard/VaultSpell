import json as js
import requests as req


class GoogleTranslate(object):
    def __init__(self):
        self.baseUrl = "https://translate.googleapis.com/translate_a/single?client=gtx"

    def GetText(self, text, src, dest):
        url = "{0}&sl={1}&tl={2}&dt=t&q={3}".format(self.baseUrl, src, dest, text)
        res = req.get(url)

        obj = res.json()

        if obj[0] is None:
            return ""

        n = len(obj[0])
        result = ''

        for k in range(n):
            result += obj[0][k][0]

        return result
