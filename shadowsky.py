import json

import requests
from checkin import Checkin
from result import Result


class ShadowSky(Checkin):
    def __init__(self, email, psw='1'):
        super().__init__("ShadowSky")
        self.email = email
        self.psw = psw

    def checkin(self) -> Result:
        shadowsky_headers = {
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

        login_data = {'email': self.email, 'passwd': self.psw, 'remember_me': 'week'}
        shadowsky_session = requests.Session()
        login_result = shadowsky_session.post('https://www.shadowsky.fun/auth/login',
                                                        headers=shadowsky_headers,
                                                        data=login_data)
        login_result = json.loads(login_result.text.encode())
        if 'error_code' in login_result:
            return Result.fail(login_result['msg'])
        shadowsky_headers.update({'Origin': 'https://www.shadowsky.fun', 'Referer': 'https://www.shadowsky.fun/user',
                                  'Accept': 'application/json, text/javascript, */*; q=0.01',
                                  'X-Requested-With': 'XMLHttpRequest'})
        shadowsky_checkin_page = shadowsky_session.post('https://www.shadowsky.fun/user/checkin',
                                                        headers=shadowsky_headers)
        shadowsky_checkin_json = json.loads(shadowsky_checkin_page.text.encode())
        checkin_result = shadowsky_checkin_json['msg']
        return Result.success(checkin_result)
