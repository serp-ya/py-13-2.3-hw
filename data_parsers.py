import chardet
import json
import xml.etree.ElementTree as ET


def check_file(file):
    file_result = dict()

    file_data = file.read()
    file_info = chardet.detect(file_data)
    file_encoding = file_info['encoding']

    file_result['data'] = file_data
    file_result['info'] = file_info
    file_result['encoding'] = file_encoding

    return file_result


def read_xml_and_convert(file_path, file_name):
    xml_result = dict()
    xml_result[file_name] = list()

    with open(file_path + file_name, 'rb') as f:
        file = check_file(f)
        xml_root = ET.fromstring(file['data'].decode(file['encoding']))

        for item in xml_root.iter('item'):
            result_dict = dict()
            result_dict['title'] = item.find('title').text
            result_dict['description'] = item.find('description').text

            xml_result[file_name] += [result_dict]

    return xml_result


def read_json_and_convert(file_path, file_name):
    json_result = dict()
    json_result[file_name] = list()

    with open(file_path + file_name, 'rb') as f:
        file = check_file(f)
        json_data = json.loads(file['data'].decode(file['encoding']))
        items = json_data['rss']['channel']['items']

        for item in items:
            result_dict = dict()
            result_dict['title'] = item['title']
            result_dict['description'] = item['description']

            json_result[file_name] += [result_dict]

    return json_result
