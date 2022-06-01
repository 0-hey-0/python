import yaml
import os.path


class Loader(yaml.Loader):
    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super(Loader, self).__init__(stream)

    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        with open(filename, 'r',encoding="utf-8") as fr:
            return yaml.load(fr, Loader)

Loader.add_constructor('!include', Loader.include)

def load_yaml(file_name):
    """Load YAML file to be dict"""
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding="utf-8") as fr:
            dict_obj = yaml.load(fr, Loader=Loader)
        return dict_obj
    else:
        raise FileNotFoundError('NOT Found YAML file %s' % file_name)

# if __name__ == '__main__':
#     f=os.getcwd()
#     # print(f)
#     yaml_dict = load_yaml(f+"/data/aa.yaml")
#     print(yaml_dict)
