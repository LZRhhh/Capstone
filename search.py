import requests
from json import JSONDecoder

http_url = "https://api-us.faceplusplus.com/facepp/v3/search"
# 你要调用API的URL

key = "VNCZtFdxdjm_HxsXNrjQpwClTzqLNQdU"
secret = "nIvoeZySRcHxJm9Q4YYZhNSogg9jNg9r"
# face++提供的一对密钥
faceset_token = "563d2545c76ca1f05feee5c9151ffe17"
outer_id = "zhuoran"
faceToken = "58e72cf214888d32891d5be0b86e10c8"

user_dict = {"58e72cf214888d32891d5be0b86e10c8": "zhuoran", "a8dd2b98dca33553ba3d77b79dbfb1a1": "boyang"}

filepath = "D:\Pictures\微信图片_20200224164925.jpg"
# 图片文件的绝对路径

data = {"api_key": key, "api_secret": secret, "outer_id": outer_id}
# 必需的参数，注意key、secret、"gender,age,smiling,beauty"均为字符串，与官网要求一致

files = {"image_file": open(filepath, "rb")}
'''以二进制读入图像，这个字典中open(filepath1, "rb")返回的是二进制的图像文件，所以"image_file"是二进制文件，符合官网要求'''

response = requests.post(http_url, data=data, files=files)
# POTS上传

req_con = response.content.decode('utf-8')
# response的内容是JSON格式

req_dict = JSONDecoder().decode(req_con)
# 对其解码成字典格式

print(req_dict)
confidence = req_dict["results"][0]["confidence"]
face_token = req_dict["results"][0]["face_token"]
print("confidence: ", confidence)
user = user_dict[face_token]
print("user: ", user)

