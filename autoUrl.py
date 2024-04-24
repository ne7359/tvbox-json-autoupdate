import re  # 导入正则表达式模块
import datetime  # 导入日期时间模块
import requests  # 导入HTTP请求模块
import json  # 导入JSON模块，用于JSON文件的读写
import urllib3  # 导入一个用于打开HTTP连接的库

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # 禁用不安全请求警告

# 以读取模式打开url.json文件, 加载文件内容到urlJson变量
with open('./url.json', 'r', encoding='utf-8') as f:
    urlJson = json.load(f)

nameList = []  # 初始化一个空的列表，用来存放名字

# 初始化重定向列表，包含不同的代理服务URLs
reList = ["https://ghproxy.net/https://raw.githubusercontent.com", "https://raw.kkgithub.com",
          "https://gcore.jsdelivr.net/gh", "https://mirror.ghproxy.com/https://raw.githubusercontent.com",
          "https://github.moeyy.xyz/https://raw.githubusercontent.com", "https://fastly.jsdelivr.net/gh"]

# 对应上面的reList，标记是否需要对URL进行特殊处理
reRawList = [False, False,
          True, False,
          False, True]

# 遍历urlJson中的每一个条目
for item in urlJson:
    urlReq = requests.get(item["url"], verify=False)  # 发送请求获取数据，关闭SSL认证
    # 遍历代理服务URLs
    for reI in range(len(reList)):
        urlName = item["name"]  # 获取JSON条目中的"name"
        urlPath = item["path"]  # 获取JSON条目中的"path"
        reqText = urlReq.text  # 获取请求的文本内容

        # 如果urlName不是"gaotianliuyun_0707"，则替换文本中的路径标识
        if urlName != "gaotianliuyun_0707":
            reqText = reqText.replace("'./", "'" + urlPath) \
                .replace('"./', '"' + urlPath)
        # 根据reRawList中的标记决定是否替换URL路径中的'/raw/'部分
        if reRawList[reI]:
            reqText = reqText.replace("/raw/", "@")
        else:
            reqText = reqText.replace("/raw/", "/")
        # 替换所有GitHub链接为对应的代理服务URLs
        reqText = reqText.replace("'https://github.com", "'" + reList[reI]) \
            .replace('"https://github.com', '"' + reList[reI]) \
            .replace("'https://raw.githubusercontent.com", "'" + reList[reI]) \
            .replace('"https://raw.githubusercontent.com', '"' + reList[reI])
        
        # 打开对应文件，写入修改后的请求文本内容
        fp = open("./tv/" + str(reI) + "/" + urlName + ".json", "w+", encoding='utf-8')
        fp.write(reqText)

# 获取当前的日期和时间
now = datetime.datetime.now()
# 打开README.md文件，并设置编码格式为'utf-8'
fp = open('README.md', "w+", encoding='utf-8')
fp.write("# 提示\n\n")
fp.write("感谢各位大佬的无私奉献.\n\n")
fp.write("如果有收录您的配置，您也不希望被收录请[issues](https://github.com/hl128k/tvbox/issues)，必将第一时间移除\n\n")
fp.write("# 免责声明\n\n")
fp.write("本项目（tvbox）的源代码是按“原样”提供，不带任何明示或暗示的保证。使用者有责任确保其使用符合当地法律法规。\n\n")
fp.write("所有以任何方式查看本仓库内容的人、或直接或间接使用本仓库内容的使用者都应仔细阅读此声明。本仓库管理者保留随时更改或补充此免责声明的权利。一旦使用、复制、修改了本仓库内容，则视为您已接受此免责声明。\n\n")
fp.write("本仓库管理者不能保证本仓库内容的合法性、准确性、完整性和有效性，请根据情况自行判断。本仓库内容，仅用于测试和学习研究，禁止用于商业用途，不得将其用于违反国家、地区、组织等的法律法规或相关规定的其他用途，禁止任何公众号、自媒体进行任何形式的转载、发布，请不要在中华人民共和国境内使用本仓库内容，否则后果自负。\n\n")
fp.write("本仓库内容中涉及的第三方硬件、软件等，与本仓库内容没有任何直接或间接的关系。本仓库内容仅对部署和使用过程进行客观描述，不代表支持使用任何第三方硬件、软件。使用任何第三方硬件、软件，所造成的一切后果由使用的个人或组织承担，与本仓库内容无关。\n\n")
fp.write("所有直接或间接使用本仓库内容的个人和组织，应 24 小时内完成学习和研究，并及时删除本仓库内容。如对本仓库内容的功能有需求，应自行开发相关功能。所有基于本仓库内容的源代码，进行的任何修改，为其他个人或组织的自发行为，与本仓库内容没有任何直接或间接的关系，所造成的一切后果亦与本仓库内容和本仓库管理者无关 \n\n")
fp.write("# 介绍\n\n")
fp.write("自用请勿宣传\n\n")
fp.write("所有数据全部搜集于网络，不保证可用性\n\n")
fp.write("因电视对GitHub访问问题，所以将配置中的GitHub换成镜像源\n\n")
fp.write("本次自动更新时间为：" + now.strftime("%Y-%m-%d %H:%M:%S") + "\n\n")
fp.write("当前内容来源详情请查看url.json\n\n")
fp.write("如果感兴趣,请复制项目后自行研究使用\n\n")
fp.close()
