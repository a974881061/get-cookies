import requests

url = 'https://jxjkhd.kerlala.com/activity/autographnew/register/31/8ZWXOq3w'

headers = {
    'Host': 'jxjkhd.kerlala.com',
    'Authorization': 'Bearer',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-XSRF-TOKEN': 'eyJpdiI6IlJFLy9VakNDV3FXdUpDSlhvb3Z2RGc9PSIsInZhbHVlIjoiNUl4VjA3aXB0ejNwY01BSUhkbTJEYXJ4aEhRdDB5c3c2dFB0cGc3NmVjdko1Nm9uLzVWZ0xFSFRtTUdKRjg2UjdwSlJOOUExQm1wYTM2bkFENGd0TE9GeXBZN1RlOW50Vzk4ZVRMb2ZZR2phR0lSdFg1L1padlFaV0ZLbDh1OFAiLCJtYWMiOiI0OGU0ZWU5MTAyZDczMGRmMzhhMDhkZDljOGI1MWE3ZjA5MTg0M2QzYTExM2RjNjY0OGI2MjRjNTgwZjdlMzAxIn0=',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://jxjkhd.kerlala.com',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 CCBSDK/2.4.0/CloudMercWebView',
    'Referer': 'https://jxjkhd.kerlala.com/a/31/8ZWXOq3w/index?cityid=350100&userCityId=350100&CITYID=350100&USERCITYID=350100&u=e59b633b-2799-4211-949a-2da7a5bd60b5',
    'Content-Length': '0',
    'Connection': 'keep-alive',
    'X-CSRF-TOKEN': '',
    'Cookie': 'XSRF-TOKEN=eyJpdiI6IlJFLy9VakNDV3FXdUpDSlhvb3Z2RGc9PSIsInZhbHVlIjoiNUl4VjA3aXB0ejNwY01BSUhkbTJEYXJ4aEhRdDB5c3c2dFB0cGc3NmVjdko1Nm9uLzVWZ0xFSFRtTUdKRjg2UjdwSlJOOUExQm1wYTM2bkFENGd0TE9GeXBZN1RlOW50Vzk4ZVRMb2ZZR2phR0lSdFg1L1padlFaV0ZLbDh1OFAiLCJtYWMiOiI0OGU0ZWU5MTAyZDczMGRmMzhhMDhkZDljOGI1MWE3ZjA5MTg0M2QzYTExM2RjNjY0OGI2MjRjNTgwZjdlMzAxIn0%3D; _session=eyJpdiI6IndjWVRRREsxaUE3REN4OVR5bldaeUE9PSIsInZhbHVlIjoicmplbTRhdWorN2NocFFmejcxRHZWTFVta2c3TDZTVWxHUHdBVHBzWDNKcS8wd0xsajFIejNQUkgzRmRldUxhV1E5NGlUTFhOclkzTUxEZDgzUWY3dG5jU1orQlB5Y3Mzc0o4TkhKTHlmS05TMFFEcDJoZGV2RjVodXpkSzd2TG4iLCJtYWMiOiI2OTAzMGEyOGJjZDE1OWUwYTEwODYyOWI5MzYyNDE4NzJlMzMxYzEyNGEyMTk3MTNkMTBkMmY4NjViZGYyNDllIn0%3D; _ck_bbq=eyJpdiI6InpTVlM0K2dUWEZKZEhtZDV6UGdySFE9PSIsInZhbHVlIjoibWhLdzQrZ3lwWUhaOHVkd0dJcmJuSHpwbmRjNzBzNWdvRXRheCs3SHRxekVLTFJoNWpCZ1ZLOEtOdGlkMkpHaldWUnAxU1NTV2xIb1lLOS9OcnFRdjlmS2J4SUI2UzdpTk5OQW9LeWpaUjg9IiwibWFjIjoiODFhZGU2NzJkMzdkN2ViOWIzYjgwMzczZjEwZGU3ZmFmZWVmMDA1ZmJjYTI3OWMwMzFlMjgzY2EwMTNhZmJjMiJ9; acw_tc=76b20f6916377142929605544e6a5209ef4d3ec190a39909946459ea6b13c0; uid=CgIACmEV0l8jIwjE26j5Ag=='
}

headers1 = {
    'Host': 'jxjkhd.kerlala.com',
    'Authorization': 'Bearer',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-XSRF-TOKEN': 'eyJpdiI6Imc3eXJLWlBpNDlyN1pIcWhwWXE1M3c9PSIsInZhbHVlIjoiMjM4TWFwVzB2bmVOWXNzOTd5ZlUvUmo4UzVGNWZmUjNoc0JuR0tOd0ZxczYyZVN1YkN3MVZMd3Zhc0FZdHdjTmovOCt4QzdHMFNNTjFEWjV2SlNncnQrMjdoVjlNeDdMd0FGYkI5RjR3UVZ5NTdnNUs5RnZETjNibTl4cUFLM2UiLCJtYWMiOiJlZjYwMzQ1MTdmNjk1ZTFiYzU4ZmZjYTI3NTY3NTVmYzhkYjk0NDE1OGI3MWM4OGJjNmUzM2EyZDBjYmUyODZlIn0=',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 CCBSDK/2.4.0/CloudMercWebView',
    'Connection': 'keep-alive',
    'Referer': 'https://jxjkhd.kerlala.com/a/31/8ZWXOq3w/index?cityid=350100&userCityId=350100&CITYID=350100&USERCITYID=350100&u=281496c9-b849-4add-b4d4-9fb427489384',
    'X-CSRF-TOKEN': '',
    'Cookie': 'XSRF-TOKEN=eyJpdiI6Imc3eXJLWlBpNDlyN1pIcWhwWXE1M3c9PSIsInZhbHVlIjoiMjM4TWFwVzB2bmVOWXNzOTd5ZlUvUmo4UzVGNWZmUjNoc0JuR0tOd0ZxczYyZVN1YkN3MVZMd3Zhc0FZdHdjTmovOCt4QzdHMFNNTjFEWjV2SlNncnQrMjdoVjlNeDdMd0FGYkI5RjR3UVZ5NTdnNUs5RnZETjNibTl4cUFLM2UiLCJtYWMiOiJlZjYwMzQ1MTdmNjk1ZTFiYzU4ZmZjYTI3NTY3NTVmYzhkYjk0NDE1OGI3MWM4OGJjNmUzM2EyZDBjYmUyODZlIn0%3D; _session=eyJpdiI6ImpSd291bk9BQituUGViYjEwNjZJNnc9PSIsInZhbHVlIjoiVzRNNTdkWnVUMjQwZENWNEdBbE5TdWVWSm9aMHU4b2pXRlFYOEdKU0ZKQmxzKzEvOHRGR2tDZ2NoNUVyRUFXTDJFdXRZd1czc28vbkgzOWYzV3k1Y2ZrWmtlVzBvV3Zwc3N6d2RCMVNhdS9jVmZ2UnVqU1pDdGY0UGgwSkdvbVUiLCJtYWMiOiJhMjFmOTVlNGFhOWM4NDIzZDlkODJhNTA2YzJjZTM0M2Q1NWQ2MWZlOTFkMjBiYzMyOGE4YWM3MjI0ODhkZjM2In0%3D; _ck_bbq=eyJpdiI6IlFpYTlHUVVCU3V0VW9jTkgvMmF2Vmc9PSIsInZhbHVlIjoiWkpvT2c0cWVtbk5pdFluM3AwMzVEY2dSUHNhNlRHeUxOcE1YY21RZncxbEREMTNSeEFuQkZteWYyZWJaOE1Xekx6TFdUcHp4MFpxNXF5VWlXcXFMWHVrWW5TYm1RN0p5aFkrL3hmUEg4MkdkNUFCcEkxR1ptY2x1M1dEMHA3UDQiLCJtYWMiOiIzODUwYmY3OGJhNGE1OGRjNjU5MjYwNDZhNTI4NWJlZTM2NzViMWY5ZjRiOTdlNzkxOGM3ZTY0M2UyN2I5MTY3In0%3D; acw_tc=76b20f7216377149559454261e2eb954ceff938da68279447e2dcdef109dcb; uid=CgIAEWFcbZe9f3n6aK/kAg=='
}

res = requests.post(url=url,headers=headers)

if res.json()["code"] != 20001:
    print(res.json()["message"])
    requests.get(url='https://api.day.app/fC842SsyD8qeqpFw2vp65S/建行生活/{}'.format("9192"+res.json()["message"]))
elif res.json()["code"] == 20001:
    print("9192"+res.json()["message"])

res1 = requests.post(url=url,headers=headers1)
if res.json()["code"] != 20001:
    print(res1.json()["message"])
    requests.get(url='https://api.day.app/fC842SsyD8qeqpFw2vp65S/建行生活/{}'.format("9107"+res.json()["message"]))
elif res1.json()["code"] == 20001:
    print("9107"+res1.json()["message"])
