import re
import time
import urllib.parse
import string
import requests
from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By


def parse_selenium():
    path_chrom_driver = r'C:\Users\python_django\chromedriver.exe'

    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    # options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--blink-settings=imagesEnabled=false')
    # options.add_argument("--disable-notifications")
    # options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument('--headless')

    driver = webdriver.Chrome(
        executable_path=f'{path_chrom_driver}',
        options=options
    )
    url = 'https://translate.google.ru/?sl=ru&tl=en&op=translate'
    driver.get(url)
    driver.implicitly_wait(3)
    try:
        with open(r'C:\Users\python_django\mysite\locale\en\LC_MESSAGES\django.po', 'r', encoding='utf-8') as f:
            with open(r'C:\Users\python_django\mysite\locale\en\LC_MESSAGES\django_result.po', 'w',
                      encoding='utf-8') as result:
                for row in f.read().split('\n'):
                    if row.startswith('msgid "'):
                        try:
                            line = re.search(r'\"[^"]*\"', row)[0].split('"')[1]

                            window = driver.find_element(
                                by=By.CSS_SELECTOR,
                                value='#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > '
                                      'div.ccvoYb.EjH7wc > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd > span'
                                      ' > span > div > textarea')
                            window.send_keys(line)
                            time.sleep(3)

                            window2 = driver.find_element(
                                by=By.CLASS_NAME,
                                value='ryNqvb').text

                            driver.find_element(
                                by=By.CLASS_NAME,
                                value='DVHrxd'
                            ).click()

                            result.write(row + '\n')
                            result.write('msgstr "{}"{}'.format(window2, '\n'))
                            print(row)
                            print(window2)
                        except Exception as ex:
                            result.write(row + '\n')
                            result.write('msgstr ""{}'.format('\n'))
                    elif not row.startswith('msgstr "'):
                        result.write(row + '\n')

    except Exception as ex:
        logger.debug(ex)
    finally:
        driver.quit()


def parse_trance(word_ru):
    alfabet = list(string.ascii_lowercase)
    headers = {
        'authority': 'translate.google.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'HSID=AUVuAxsfaaTnglWHY; SSID=AWq4KfBaSa9KD4u6c; APISID=J97I-eaNcWahvb0t/Adb5iOOdq4jiVev09; SAPISID=Hl0CKFv8ecnfegcr/Ag8KbK16fpjXCZbTT; __Secure-1PAPISID=Hl0CKFv8ecnfegcr/Ag8KbK16fpjXCZbTT; __Secure-3PAPISID=Hl0CKFv8ecnfegcr/Ag8KbK16fpjXCZbTT; SEARCH_SAMESITE=CgQIkJYB; AEC=AakniGOpuyGOil7JjdLr71Pqh1Eg9KlH13TdWETiRaBNE6dvIajX-M1aDA; SID=PwiOaP-FdqyIjSafE4_ywBQZARXVGlWEXIFdftHmqSnzo6Ob2L_jJed8ExqyAMonF5yQfg.; __Secure-1PSID=PwiOaP-FdqyIjSafE4_ywBQZARXVGlWEXIFdftHmqSnzo6Ob4HNb4r3rGnM5i9r1eSo__A.; __Secure-3PSID=PwiOaP-FdqyIjSafE4_ywBQZARXVGlWEXIFdftHmqSnzo6ObT-ioWnIKb3xaY7MnasoIKg.; OTZ=6747600_28_32_123600_28_436080; NID=511=kVNnkRwg_vumQ7Wbdpf11nq-fkIYb_tIboU2S2bD3-EE7JnZURlUW0ZetEWh7sOz5eyi6u2kynhkigOYno4oO7NAuGa_N72EY49gNyUeCn4Q5TP912jcN1yjCm6dRyScnQBZHDVimfsndFZpbIh7zTAkcWO0CcHncfiVsj0P1rC4Or7s-ko3THUKzecl5mN1L5JKsfIP_BD2W5nf-2TMobMDl7i_fYIn6f5ITpwwPGzfE6WSvm8JQ-meEQxHyO8P1phtrHip6E79g1jFWA',
        'origin': 'https://translate.google.ru',
        'referer': 'https://translate.google.ru/',
        'sec-ch-ua': '"Chromium";v="106", "Not.A/Brand";v="24", "Opera";v="92"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"106.0.5249.119"',
        'sec-ch-ua-full-version-list': '"Chromium";v="106.0.5249.119", "Opera";v="106.0.5249.119", "Not;A=Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0',
        'x-goog-batchexecute-bgr': '[";7fO4877QAAZURN_vdERfgF_ycGPm4rImACkAIwj8Rloalp0iChqc4chOiBxc_jEiDkZSjRD1qlw7hZOTCJVs5EIEBB8AAAWyTwAAABR1AQcXAOoE0v2z07ig3G9TmTdrap3OpfveH1uGn-O3S6JMvC2eToMJiiY1SqmZ_XTG5SCFghEUyEPpTpnJrghomp4htpSweWnkxZxVECy4NKfP-keYHoptS0Qxc4gWBaoP0qdIkwZxT-eQCH7hMZTRabLeI_hpko7DIl0IiUBozs75RiJorarG55w0FLRco5WMf_YEyyHW_IUNRCnzHd5E8PxkTeg-RbL8QFblAh5XhnSd9AlPycMTkAcVQXqMVUTfrHYvXUipdm9ktcCUaDxoNrw74XwhONt6QgtiKa5Jbz07lNpnUhm-Prv3itbdUN-EAqTfj5GQh1HJ8TgKl2Pl1lfWitBnIbZ5TWOkY_hF8u8GfB_j6RroGQp7Je5mxMVZhAz7mjz9JOkWhUh7Qb5znJc6ngUfRVZCf3iaE1m1hPFpvw1d3Dj_ZaT6mM20qI6GVSU61sIaC_68MzlBSajWWg5CftOKe8DdMIgllf91SITv1uOOcEzrTFdoFcRu2xXQSXkmTbLO7uW6jxJdwCuItDHPiHNciMNfKkIufp2rMgnMsGY-jSKku88FdYic01da45nWyvYwHH3ejJJ-0t30bjsiPiOz6C-mwAchwlTekFzBvOZKLrvYEGSKiR6XP34Yo7QX6e2h2g6AnUHwWhhyILBHEFXl108wj03w9EgKINmCy6VIMrOQmBrfkjV5E1k4Z88y9mRR9a5z2xV9d8PbModGLuzOF-mA_JYbWbKj6j4TWGuWf8qPB0HQRREnDaMTB8nEXfRvNnxVHmViScRBBVTsIilCkyaTOEx82NucStbs6pmJSquiNb1-lyusY7Z4I4gjZ8du5UcLoKVYFYawxEz7LnnAWUlzCwjAAzUhMh8XpDfISzH_fui1JgWPlDWfYZO0CL26T9iySJl0kZsvFZmaAxTAaA5ZdjNCHx4TwJnqCAyaG-DoxrWXfni5_QD7KFimE1wu-j9bdbZGgTlCwEcU81vedj4vWBlNQfaQMRgbQLat2WOwGOoE6_vLqJ3eU5c0_LSGwDe2LDuJFmhV1YKlWcxjKGjJWI_uQMavPUR8RrO5b5BB4Oxrov9vnysUxpJFGDKts-Q28aMvlZDtSTFLFFWgQhzS90AHg57gDpB_dhY7lN04YUXD52I4yR3PsCxMh37xZUe3lXMgbrQC6-TCdojpX6zuhUSs0QHwCIxqiEpHb2PW75ucaIU1dc3iImgUFZMd",null,null,2328,221,null,null,0,"2"]',
        'x-same-domain': '1',
    }

    word = urllib.parse.quote(word_ru)

    data = f'f.req=%5B%5B%5B%22MkEWBc%22%2C%22%5B%5B%5C%22{word}%5C%22%2C%5C%22ru%5C%22%2C%5C%22en%5C%22%2Ctrue%5D%2C%5Bnull%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at=AOVbEn_PHmZkYXYnI0Mh3TRvvGM0%3A1668060395449&'

    response = requests.post('https://translate.google.ru/_/TranslateWebserverUi/data/batchexecute',
                             headers=headers, data=data)
    pattern = r'\\"[^"]*\"'
    word_en = re.findall(pattern, response.text)[3].split(r'\"')[1]
    if word_en[1] in alfabet:
        return word_en
    return re.findall(pattern, response.text)[2].split(r'\"')[1]


def main():
    try:
        with open(r'C:\Users\python_django\mysite\locale\en\LC_MESSAGES\django.po', 'r', encoding='utf-8') as f:
            with open(r'C:\Users\python_django\mysite\locale\en\LC_MESSAGES\django_result.po', 'w',
                      encoding='utf-8') as result:
                for row in f.read().split('\n'):
                    if row.startswith('msgid "'):
                        try:
                            word_ru = re.search(r'\"[^"]*\"', row)[0].split('"')[1]

                            word_en = parse_trance(word_ru)

                            result.write(row + '\n')
                            result.write('msgstr "{}"{}'.format(word_en, '\n'))
                            print(row)
                            print(word_en)
                        except Exception as ex:
                            result.write(row + '\n')
                            result.write('msgstr ""{}'.format('\n'))
                    elif not row.startswith('msgstr "'):
                        result.write(row + '\n')

    except Exception as ex:
        logger.debug(ex)


if __name__ == '__main__':
    main()
