from data_parsers import read_xml_and_convert, read_json_and_convert
from pprint import pprint

# def make_sources_list(file_names_list, path):
#     sources_list = list()
#
#     for file_name in file_names_list:
#         sources_list += [path + file_name]
#
#     return sources_list


def read_files(source_path, file_names_list, reader):
    file_data_list = list()

    for file_name in file_names_list:
        file_data_list += [reader(source_path, file_name)]

    return file_data_list


def concat_dicts(list_of_dicts):
    result_dict = dict()

    for item in list_of_dicts:
        result_dict.update(item)

    return result_dict


def core():
    sources_path = './sources/'
    xml_source_path = sources_path + 'xml/'
    json_file_names = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']
    xml_file_names = ['newsafr.xml', 'newscy.xml', 'newsfr.xml', 'newsit.xml']

    xml_data_list = read_files(xml_source_path, xml_file_names, read_xml_and_convert)
    xml_merged_data = concat_dicts(xml_data_list)

    pprint(xml_merged_data)

core()
