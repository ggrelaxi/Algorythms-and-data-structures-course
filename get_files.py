from genericpath import isdir, isfile
import os


def get_files(catalog_path=''):
    files = []

    def inner_f(path, accumulator):
        folder_data = os.listdir(path)

        for i in range(len(folder_data)):
            current_item = folder_data[i]
            full_item_path = os.path.join(path, current_item)

            if os.path.isfile(full_item_path):
                accumulator.append(current_item)
            elif os.path.isdir(full_item_path):
                return inner_f(full_item_path, accumulator)

    inner_f(catalog_path, files)

    return files


print(get_files('C:/Users\Alex\Desktop\Обучение у Сергея Бобровского\Задачи на рекурсию\Algorythms-and-data-structures-course/folder'))
