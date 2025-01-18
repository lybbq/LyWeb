# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import requests
import requests
from bs4 import BeautifulSoup
ssion = requests.session()
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.0.0',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        # ':authority': 'mail.163.com',
        # ':method': 'GET',
        "If-None-Match": 'W/"166d0-j44L171PIi2ReXLwo0u4Q4W1sGo"',
        'Cache-Control':'max-age=0',
        # ':paths': '/js6/main.jsp?sid=ZDsUdhRtwlHydbKpnGttjcEYJHrMXifJ&df=unknow',
        #'Connection': 'keep-alive',
        'Sec-Ch-Ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': "Windows",
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests':'1'
}
#param = {"wd": "python", 'pn': 10}
cookies_str = '_m_h5_tk=0e75cfee9012043dceb81eeed4f0c2f9_1695406603509; _m_h5_tk_enc=90f0efa639366fccd31af51e134bab7f; cna=Q5+UHQgJ8ncCAXOt6a8eH/IC; cookie2=1407ed331f5b76250b2fcd64d269686b; t=7fbcad7b10810cd8601dee66bb418d0b; _tb_token_=ef8db3bb7eeb7; _samesite_flag_=true; xlly_s=1; sgcookie=E100kFYxj1Pjt9TngymObhVD2jBlMmbe%2FCyN%2Fw0XZnOYtS20bryOWliAPSxKlYl5Ak1GWh8FXcI%2BSmt2kkmXQB%2F5Y2lncftlajPM3jAiUQQ6FpWwhm1Tnb3Noa2%2FLEIHWt%2BS; unb=2806450297; uc3=lg2=V32FPkk%2Fw0dUvg%3D%3D&vt3=F8dCsGSGkm2u5%2Fa0bWY%3D&id2=UUBYgra27ymGTQ%3D%3D&nk2=2nKy%2F3Cb7DdvorRUPPQ%3D; csg=cded36fb; lgc=%5Cu8FC7%5Cu6765%5Cu4FDD%5Cu8BC1%5Cu4E0D%5Cu5F04%5Cu4F60; cancelledSubSites=empty; cookie17=UUBYgra27ymGTQ%3D%3D; dnk=%5Cu8FC7%5Cu6765%5Cu4FDD%5Cu8BC1%5Cu4E0D%5Cu5F04%5Cu4F60; skt=58f5c46eff0e688d; existShop=MTY5NTM5NjIwNg%3D%3D; uc4=id4=0%40U2LK%2FwV7KPOuFmSMH0WFHg1E1HIz&nk4=0%402Ej3cpHHD9qj0JaoIquzF99tPX4gkqJLLg%3D%3D; tracknick=%5Cu8FC7%5Cu6765%5Cu4FDD%5Cu8BC1%5Cu4E0D%5Cu5F04%5Cu4F60; _cc_=UtASsssmfA%3D%3D; _l_g_=Ug%3D%3D; sg=%E4%BD%A074; _nk_=%5Cu8FC7%5Cu6765%5Cu4FDD%5Cu8BC1%5Cu4E0D%5Cu5F04%5Cu4F60; cookie1=BxNSpZm4svjVmHqTpWBaUM%2BgfP0xWwTZ2CFU8mqZ5m8%3D; mt=ci=10_1; thw=cn; uc1=existShop=false&pas=0&cookie21=UtASsssmeW6lpyd%2BB%2B3t&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&cookie14=Uoe9aOVtULoXgQ%3D%3D&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D; isg=BFBQA5Z9Ad61Nd3aS1J-YpKXIZ6iGTRjgIN_sEohHKt-hfAv8ikE86a3WU1lVew7; l=fBMoeESnPgRl-pfDBOfaFurza77OSIRYYuPzaNbMi9fPO6fB56MPW1hC8886C3GVF6mJR3SMFAL9BeYBqQAonxvtIosM_CkmndLHR35..; tfstk=dCQMp5qnqG-_edk6mlL_SWjkthrd1ATXVt3vHEp4YpJIBA3OgI8cLtF6Bsy1nZve7ns9HdpDos6u98U8y116lny8ezQTm1TjUzxs8zC11ET4e8U8yqb_gc60u1ynR237zkNlSB0quwzXjLfZDquV-Cxif1WNLDozfMgXTSQEcmtwOBvRC3mw_'

cookies = {'cookies': cookies_str}
ur = "https://www.taobao.com/"
response = ssion.get(url=ur, headers=head)
print(response.url)
with open('1.html', 'w', encoding='utf-8') as file:
    file.write(response.text)
print(response.text)

