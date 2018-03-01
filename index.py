from data_parsers import read_xml_and_convert, read_json_and_convert


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


def lowercase_and_merge_texts(data_dict):
    result_dict = dict()

    for filename in data_dict:
        result_dict[filename] = str()

        for file_data in data_dict[filename]:
            merged_data = ' '.join([file_data['title'], file_data['description'], ' '])
            result_dict[filename] += merged_data

        result_dict[filename] = result_dict[filename].lower()

    return result_dict


def split_and_count_data(data_dict):
    result_dict = dict()

    for filename in data_dict:
        result_dict[filename] = dict()
        splited_words = data_dict[filename].split(' ')

        for word in splited_words:
            if (len(word) > 6) and not result_dict[filename].get(word):
                result_dict[filename][word] = splited_words.count(word)

    return result_dict


def format_and_sort_data_by_count(data_dict):
    result_dict = dict()

    def sort_by_count(data):
        return data['count']

    for filename in data_dict:
        result_dict[filename] = list()

        for word in data_dict[filename]:
            new_item = {'word': word, 'count': data_dict[filename][word]}
            result_dict[filename] += [new_item]

        result_dict[filename].sort(key=sort_by_count, reverse=True)

    return result_dict


def print_top_words(title, data, count = 10):
    merged_data = concat_dicts(data)
    formatted_data = lowercase_and_merge_texts(merged_data)
    counted_data = split_and_count_data(formatted_data)
    sorted_reformated_data = format_and_sort_data_by_count(counted_data)

    print('{0}{1}'.format('\n', title))

    for filename in sorted_reformated_data:
        print('{0}Файл {1}'.format('\n', filename))

        for i in range(count):
            item = sorted_reformated_data[filename][i]
            word = item['word']
            count = item['count']
            print(
                '{0}. Слово "{1}" - {2} повторений'
                .format(i + 1, word, count)
            )


def core():
    sources_path = './sources/'
    json_source_path = sources_path + 'json/'
    xml_source_path = sources_path + 'xml/'

    json_file_names = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']
    xml_file_names = ['newsafr.xml', 'newscy.xml', 'newsfr.xml', 'newsit.xml']

    json_data_list = read_files(json_source_path, json_file_names, read_json_and_convert)
    xml_data_list = read_files(xml_source_path, xml_file_names, read_xml_and_convert)

    print_top_words('Файлы JSON', json_data_list)
    print_top_words('Файлы XML', xml_data_list)


if __name__ == '__main__':
    core()
