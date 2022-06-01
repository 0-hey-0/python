import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.yaml")


class ReadConfig():
    def __init__(self):
        fd = open(configPath, encoding="UTF-8")
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w", encoding="UTF-8")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding="UTF-8")

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db_test(self):
        host = self.cf.get("DATABASE", "host_test")
        port = self.cf.get("DATABASE", "port_test")
        username = self.cf.get("DATABASE", "username_test")
        password = self.cf.get("DATABASE", "password_test")
        db_name = self.cf.get("DATABASE", "db_name_test")

        return host, port, username, password, db_name
    def get_db_dev(self):
        host = self.cf.get("DATABASE", "host_dev")
        port = self.cf.get("DATABASE", "port_dev")
        username = self.cf.get("DATABASE", "username_dev")
        password = self.cf.get("DATABASE", "password_dev")
        db_name = self.cf.get("DATABASE", "db_name_dev")

        return host, port, username, password, db_name
    def get_db_c1(self):
        host = self.cf.get("DATABASE", "host_c1")
        port = self.cf.get("DATABASE", "port_c1")
        username = self.cf.get("DATABASE", "username_c1")
        password = self.cf.get("DATABASE", "password_c1")
        db_name = self.cf.get("DATABASE", "db_name_c1")

        return host, port, username, password, db_name