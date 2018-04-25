try:
    import requests
except ImportError:
    import sys
    print(sys.path)


URL = 'https://translate.google.com/translate_a/single'
HEADERS = {
    'Host': 'translate.google.com',
    'Accept': '*/*',
    'Cookie': '',
    'User-Agent': 'GoogleTranslate/5.9.59004 (iPhone; iOS 10.2; ja; iPhone9,1)',
    'Accept-Language': 'ja-jp',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'
}
PARAMS = {
    'client': 'it',
    'dt': ['t', 'rmt', 'bd', 'rms', 'qca', 'ss', 'md', 'ld', 'ex'],
    'otf': '2',
    'dj': '1',
    'hl': 'ja',
    'ie': 'UTF-8',
    'oe': 'UTF-8'
}


def _trans(words='', src='en', dst='ja'):
    params = PARAMS.copy()
    params.update({
        'sl': src,
        'tl': dst,
        'q': words
    })
    res = requests.get(
        url=URL,
        headers=HEADERS,
        params=params
    )
    res = res.json()
    print(res['sentences'][0]['trans'])


def en2ja(words=''):
    _trans(words, src='en', dst='ja')


def ja2en(words=''):
    _trans(words, src='ja', dst='en')
