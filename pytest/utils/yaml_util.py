import os
import yaml
from yamlinclude import YamlIncludeConstructor

# 获取上层路径
# os.path.abspath(os.path.dirname(os.getcwd()))

#读取
def read_yaml(yaml_name):
    with open(os.getcwd()+'/data/'+yaml_name,mode='r',encoding='utf-8') as f:
        value=yaml.load(stream=f,Loader=yaml.FullLoader)
        return value

#读取extract.yaml文件
def read_ex_yaml():
    with open(os.getcwd()+'/extract.yaml',mode='r',encoding='utf-8') as f:
        value=yaml.load(stream=f,Loader=yaml.FullLoader)
        return value

#写入
def write_yaml(data):
    with open(os.getcwd()+'/extract.yaml',mode='a',encoding='utf-8') as f:
        yaml.dump(data=data,stream=f,allow_unicode=True)

#清空
def clear_yaml():
    with open(os.getcwd()+'/extract.yaml',mode='w',encoding='utf-8') as f:
        f.truncate()



#读取配置文件
def read_config():
    with open(os.getcwd()+'/config/config.yaml',mode='r',encoding='utf-8') as f:
        value=yaml.load(stream=f,Loader=yaml.FullLoader)
        return value

#rootfile:文件路径
#basePath:根目录路径
def add_base_yaml(rootfile,basePath):
    YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader, base_dir=basePath)
    with open(rootfile) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


# a=read_config()
# print(a)