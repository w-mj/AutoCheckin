import json

import requests

from checkin import Checkin
from result import Result


class AirTCP(Checkin):
    def __init__(self, email, psw="1"):
        super().__init__("AirTCP")
        self.email = email
        self.psw = psw

    def checkin(self) -> Result:
        airtcp_headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"
        }

        login_data = {"email": self.email, "passwd": self.psw, "code": ""}
        airtcp_session = requests.Session()
        login_result = airtcp_session.post(
            "https://airtcp6.com/auth/login", headers=airtcp_headers, data=login_data
        )
        login_result = json.loads(login_result.text.encode())
        if login_result["ret"] == 0:
            return Result.fail(login_result["msg"])
        airtcp_headers.update(
            {
                "Origin": "https://airtcp6.com",
                "Referer": "https://airtcp6.com/user",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "X-Requested-With": "XMLHttpRequest",
            }
        )
        airtcp_checkin_page = airtcp_session.post(
            "https://airtcp6.com/user/checkin", headers=airtcp_headers
        )
        airtcp_checkin_json = json.loads(airtcp_checkin_page.text.encode())
        checkin_result = airtcp_checkin_json["msg"]
        return Result.success(checkin_result)
