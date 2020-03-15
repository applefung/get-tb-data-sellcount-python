import requests
import json
import schedule
import time
def job():
    url10='https://mdskip.taobao.com/core/initItemDetail.htm?isUseInventoryCenter=true&cartEnable=true&service3C=false&isApparel=false&isSecKill=false&tmallBuySupport=true&isAreaSell=false&tryBeforeBuy=false&offlineShop=false&itemId=611224893062&showShopProm=false&startSellTime=1584064800000&isPurchaseMallPage=false&itemGmtModified=1583548265000&isRegionLevel=false&household=false&sellerPreview=false&queryMemberRight=true&addressLevel=4&isForbidBuyItem=false&callback=setMdskip&timestamp=1583567041030&isg=dBQ22ycnqGWdd9jTBOCih4X4aSbOLIRAgukuoNbXi_5QA1ThQH7Ooo00Oe96cfWftaTp41wTN1y9-etl2gHmndCP97RNKxDc.&isg2=BJubqIJjQUHJdL5lmNONitPZKv8FcK9yXVVBT43YKRqubLtOFEI8writBsRizAdq&ref=https%3A%2F%2Fxiaomi.tmall.com%2Fshop%2Fview_shop.htm%3Fspm%3Da230r.7195193.1997079397.2.7786ab38e3qqvS'
    url10pro='https://mdskip.taobao.com/core/initItemDetail.htm?isUseInventoryCenter=true&cartEnable=true&service3C=false&isApparel=false&isSecKill=false&tmallBuySupport=true&isAreaSell=false&tryBeforeBuy=false&offlineShop=false&itemId=611467146894&showShopProm=false&startSellTime=1583805600000&isPurchaseMallPage=false&itemGmtModified=1583555975000&isRegionLevel=false&household=false&sellerPreview=false&queryMemberRight=true&addressLevel=4&isForbidBuyItem=false&callback=setMdskip&timestamp=1583567512128&isg=dBQ22ycnqGWdd1a-BOCil4X4aSbtxIRfgukuoNbXi_5Q-681kjbOoo0jQFJ6cfWATDLp41wTN1y9-cx8JgMmndLhwTvQblH2B&isg2=BLu7SAPLYaHrw17FeHNtKrN5Sp8lEM8SPfWhr6140LrRDNruNOBfY48NJqRCLCcK&ref=https%3A%2F%2Fxiaomi.tmall.com%2Fshop%2Fview_shop.htm%3Fspm%3Da230r.7195193.1997079397.2.7786ab38e3qqvS'
    headers={
        'authority': 'mdskip.taobao.com',
        'method': 'GET',
        'path': '/core/initItemDetail.htm?isUseInventoryCenter=false&cartEnable=true&service3C=false&isApparel=false&isSecKill=false&tmallBuySupport=true&isAreaSell=false&tryBeforeBuy=false&offlineShop=false&itemId=553747748505&showShopProm=false&isPurchaseMallPage=false&itemGmtModified=1583295333000&isRegionLevel=false&household=false&sellerPreview=false&queryMemberRight=true&addressLevel=2&isForbidBuyItem=false&callback=setMdskip&timestamp=1583306749951&isg=dBxqZh-7qug7-p7OBOfZIS-eZXbTPIOb8oVr0N_reICP9DC65WDFWZ2n6rLBCnGVn6PJJ3umks4gB_FkqyCSnxv9-_BkdlRIFd6G.&isg2=BKqqCQNYgDoH8g9V0JSGl1RK-xBMGy51bpzSQTRiev2IZ0shHasFhUrW95P7k6YN',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'thw=cn; t=a362735a02d2cba85226bc1957ac8ab3; tracknick=%5Cu6C34%5Cu69AD%5Cu8BFA%5Cu5FC3; tg=0; hng=CN%7Czh-CN%7CCNY%7C156; miid=1641234026532733252; ucn=center; cna=D1XhFYSFKkUCAXzv0NeAJIzO; _m_h5_tk=3176969b756e424a717f11143022e89c_1582859984224; _m_h5_tk_enc=ab86dd8d81274088cc05d1ce26d6c4e8; _samesite_flag_=true; cookie2=12d7cbbb33c606221047a83791135a2e; _tb_token_=3e1133e36e575; enc=uZvuyne84%2Fm%2Fajv%2BQ7qtxjpLXpCTb%2BsvlC4q2LnTCXbgq48mWuYQ3BcHX%2BtJA7CWdljYPWayGRBSIr4pW%2F34Ug%3D%3D; v=0; sgcookie=DaBT2BkQEo6iEOIy7PdwT; unb=1121692648; uc3=vt3=F8dBxd35a%2F9M%2B%2F%2BHb%2F4%3D&nk2=qAaDf%2FHHR7s%3D&id2=UoCLFugi1cSKpg%3D%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; csg=e34a44aa; lgc=%5Cu6C34%5Cu69AD%5Cu8BFA%5Cu5FC3; cookie17=UoCLFugi1cSKpg%3D%3D; dnk=%5Cu6C34%5Cu69AD%5Cu8BFA%5Cu5FC3; skt=418553d15cfccc4b; existShop=MTU4MzI5OTkwOQ%3D%3D; uc4=id4=0%40UOg3sQHjeFg5TeRH2yZMxyqf1dlf&nk4=0%40qj2abBWXbFONve8Z570xilgBMQ%3D%3D; _cc_=UIHiLt3xSw%3D%3D; _l_g_=Ug%3D%3D; sg=%E5%BF%8383; _nk_=%5Cu6C34%5Cu69AD%5Cu8BFA%5Cu5FC3; cookie1=U7hDiSBkqPm%2Fzoc%2BUmOBcs7qGDO1yGCrbiLA3T43aC8%3D; tfstk=c4qNBFXcWGINVg_hP0oqGuqZ_JyOZJE0VNHxSzYn1EpAbv0GiQdxd_vz6SyAVVf..; mt=ci=36_1; uc1=cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie21=URm48syIYRhCU6d3XQ%3D%3D&cookie15=UtASsssmOIJ0bQ%3D%3D&existShop=true&pas=0&cookie14=UoTUOa2xOqSnLg%3D%3D&tag=8&lng=zh_CN; isg=BFtbZMe3gb0P0v4kh_bCDfvK6r8FmG-SJ0dDvk2YI9pxLHsO1QD_gnmNwoyiCMcq; l=dBI-6oAqqGmRKD_ZBOCwoS-eZXb9QIRYmuo2Taoyi_5de6L15PQOoJcsjFp6cjWfTUYB4q0AiPv9-etk23HmndHgcGAwBxDc.',
        'referer': 'https://detail.tmall.com/item.htm?id=553747748505',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        }
    response10 = requests.get(url10, headers=headers)
    jsonData10 = response10.text[12:-1]
    jsonData10 = json.loads(jsonData10, strict=False)
    data10=jsonData10['defaultModel']['sellCountDO']['sellCount']
    print("Xiaomi 10 sales number: "+data10)

    response10pro = requests.get(url10pro, headers=headers)
    jsonData10pro = response10pro.text[12:-1]
    jsonData10pro = json.loads(jsonData10pro, strict=False)
    data10pro=jsonData10pro['defaultModel']['sellCountDO']['sellCount']
    print("Xiaomi 10 pro sales number: "+data10pro)


if __name__ == '__main__':
    schedule.every().day.at("10:30").do(job)
    #schedule.every(1).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

