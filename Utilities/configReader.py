from configparser import ConfigParser


def read_config(section, key):
    config = ConfigParser()
    config.read("/home/ezetap/PycharmProjects/PortalAutomation/ConfigurationData/config.ini")
    return config.get(section, key)

def read_conf_with_spec_val(section, key, value):
    config = ConfigParser()
    config.read("/home/ezetap/PycharmProjects/PortalAutomation/ConfigurationData/config.ini")
    element = config.get(section, key)
    if "orgCode" in element:
        element = element.replace("orgCode",value)

    if "mobileNum" in element:
        element = element.replace("mobileNum", value)
    return element