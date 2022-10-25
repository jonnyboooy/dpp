from random import randint
import os.path
import pandas as pd

# Класс апельсинов, включающий в себя метод "creating_hist", позволяющий
# сгенерировать случайную гистограмму(hist) для объекта, а также поле
# "type", хранящее в себе тип объекта 'orange'
class Oranges():

    hist = []
    type = 'orange'

    def creating_hist(self):
        a = randint(0, 9)
        b = randint(0, 9)
        self.hist = [a, b]

# Класс яблок, включающий в себя метод "creating_hist", позволяющий
# сгенерировать случайную гистограмму(hist) для объекта, а также поле
# "type", хранящее в себе тип объекта 'apple'
class Apples():
    hist = []
    type = 'apple'

    def creating_hist(self):
        a = randint(0, 9)
        b = randint(0, 9)
        self.hist = [a, b]

# Класс, читающий из текстового файла данные о существующих известных
# объъектах и позволяющий определить на основе гистограммы тип нового
# объекта. Также, методы данного класса позволяют генерировать и
# записывать в файл(базу) базовые гистограммы с соответствующими типами
# (яблоко или апельсин) и сортировку по возрастанию вычисленных расстояний
# между гистограммами нового и базовых объектов
class NNClassifier:
    name_file = 'file.txt'
    base_hists = []
    base_hists_distances = []
    base_types = []
    new_obj_distances = []
    min_dist = []

    def read_from_file(self):
        buff_hists = []

        data = pd.read_table(self.name_file,sep=',',header = None)
        self.base_types = list(data[0])

        buff_hists.insert(0, data[1])
        buff_hists.insert(1, data[2])
        self.base_hists = pd.DataFrame(buff_hists)
        self.base_hists = self.base_hists.T
        self.base_hists.columns = range(self.base_hists.shape[1])
        self.base_hists.index = list(data[0])

    def write_to_file(self, base_type, base_hist):

        file = open(self.name_file, 'a')

        buff = str(base_hist)
        buff = buff.replace('[','')
        buff = buff.replace(']','')
        buff = buff.replace(' ','')

        file.write(str(base_type))
        file.write(',')
        file.write(str(buff))
        file.write('\n')

        file.close()

    def type_definition(self):
        count = 0

        for i in range(0,3):
            if self.new_obj_distances.index[i] == 'orange':
                count += 1
            self.min_dist.append(self.new_obj_distances.iloc[i])

        if count > 1:
            obj = Oranges()
        else:
            obj = Apples()

        return obj

    def hist_distance(self, hist1, hist_new_obj):

        buff = []

        for i in range(len(hist1)):
            buff.append(list(hist_new_obj - hist1.iloc[i]))

        for i in range(len(buff)):
            sum = 0
            for j in range(len(buff[0])):
                sum += (buff[i][j])**2

            self.base_hists_distances.append(sum**0.5)

        self.new_obj_distances = pd.Series(self.base_hists_distances, self.base_types)

        self.new_obj_distances = self.new_obj_distances.sort_values(ascending=True)

    def sort(self):
        for i in range(len(self.new_obj_distances)-1):
            for j in range(len(self.new_obj_distances)-1):
                if self.new_obj_distances[j + 1] < self.new_obj_distances[j]:
                    sort_buff_series = self.new_obj_distances[j + 1]
                    self.new_obj_distances[j + 1] = self.new_obj_distances[j]
                    self.new_obj_distances[j] = sort_buff_series

# Функция, позволяющая сгенерировать случайную гистограмму
# для нового объекта
def create_new_object_hist():
    hist = pd.Series([randint(0, 9), randint(0, 9)])
    return hist


if __name__ == '__main__':

    new_object_hist = create_new_object_hist()

    classifier = NNClassifier()

    # Проверка на существование файла с именем "file.txt"
    if os.path.exists(classifier.name_file) == True:
        file = open(classifier.name_file, 'w')
        file.close()

    for i in range(0,5):
        if randint(0,1) == 1:
            apple = Apples()
            apple.creating_hist()
            classifier.write_to_file(apple.type,apple.hist)
        else:
            orange = Oranges()
            orange.creating_hist()
            classifier.write_to_file(orange.type, orange.hist)

    classifier.read_from_file()

    classifier.hist_distance(classifier.base_hists,new_object_hist)

    classifier.sort()

    new_object = classifier.type_definition()
    new_object.hist = new_object_hist

    print('\nГистограмма нового объекта:\n',list(new_object_hist))
    print('\nГистограммы из базы:\n',classifier.base_hists)
    print('\nРасстояния между гистограммами нового и базовыми объектами:\n',classifier.new_obj_distances)
    print('\nМинимальные три расстояния:\n',classifier.min_dist)
    print('\nКласс, которому принадлежит новый объект:\n',
          type(new_object),'\n')