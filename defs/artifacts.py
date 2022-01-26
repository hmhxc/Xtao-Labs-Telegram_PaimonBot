from io import BytesIO
from os import sep
import requests, yaml, re
from json.decoder import JSONDecodeError
from PIL import Image
from defs.character import repl
from defs.weapons import headers


def get_url(name: str):
    res = requests.get(url=f'https://api.minigg.cn/artifacts?query={name}', headers=headers)
    if res.text == "undefined\n":
        raise JSONDecodeError("", "", 0)
    py_dict = yaml.safe_load(re.sub(r'\[? *(, *)+\]?', repl, res.text))
    return py_dict


def gen_artifacts(data: dict):
    base_img = Image.new(mode="RGBA", size=(1280, 256), color=(255, 255, 255))
    for index, value in enumerate(data):
        img = Image.open(BytesIO(requests.get(data[value]).content))
        base_img.paste(img, (256 * index, 0))

    jpg_img = Image.new('RGB', size=(1280, 256), color=(255, 255, 255))
    jpg_img.paste(base_img, (0, 0), mask=base_img)
    jpg_img.save(f'temp{sep}artifacts.jpg', format='JPEG', subsampling=0, quality=90)


async def get_artifacts(name: str):
    artifacts_im = '''<b>{}</b>
【稀有度】：{}
【2件套】：{}
【4件套】：{}
【{}】：{}
【{}】：{}
【{}】：{}
【{}】：{}
【{}】：{}
'''
    try:
        data = get_url(name)
    except JSONDecodeError:
        return f"没有找到该武器,派蒙也米有办法！是不是名字错了？", None
    try:
        star = ""
        for i in data["rarity"]:
            star = star + i + "星、"
        star = star[:-1]
        im = artifacts_im.format(data["name"], star, data["2pc"], data["4pc"], data["flower"]["name"],
                                 data["flower"]["description"],
                                 data["plume"]["name"], data["plume"]["description"], data["sands"]["name"],
                                 data["sands"]["description"],
                                 data["goblet"]["name"], data["goblet"]["description"], data["circlet"]["name"],
                                 data["circlet"]["description"])
        gen_artifacts(data['images'])
        return im, f'temp{sep}artifacts.jpg'
    except KeyError:
        return f"没有找到该武器,派蒙也米有办法！是不是名字错了？", None
    except:
        return f"没有找到该武器,派蒙也米有办法！是不是名字错了？", None
