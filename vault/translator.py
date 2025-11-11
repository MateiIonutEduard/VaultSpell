import json as js
import requests as req


class GoogleTranslate(object):
    def __init__(self):
        self.baseUrl = "https://translate.googleapis.com/translate_a/single?client=gtx"

    def GetText(self, text, src, dest):
        if not text or not text.strip():
            return text
            
        url = "{0}&sl={1}&tl={2}&dt=t&q={3}".format(self.baseUrl, src, dest, text)
        try:
            res = req.get(url)
            res.raise_for_status()
            
            obj = res.json()

            if obj[0] is None:
                return text

            result = ''
            for segment in obj[0]:
                if segment[0]:
                    result += segment[0]

            return result if result else text
        except Exception as e:
            print(f"Translation error: {e}")
            return text