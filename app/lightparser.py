import re
from typing import List
import urllib.request


class LightParser:
    URL_SIMILAR = (
        'https://play.google.com/store/apps/collection/' +
        'cluster?clp={clp}&hl={lang}&gl={country}'
    )

    def extract(self, clp, lang, country) -> List[str]:
        url = self.URL_SIMILAR.format(
            clp=clp,
            lang=lang,
            country=country
        )
        with urllib.request.urlopen(url) as f:
            data = f.read().decode('utf-8')
            apps = re.findall(r'/store/apps/details\?id=([.\w]+)"><div', data)
            return apps
