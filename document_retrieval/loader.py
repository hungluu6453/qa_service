import os
import json
import pandas as pd


class Document_Loader:
    def __init__(self, passage_paths, index_offset) -> None:
        self.data = list()
        self.passage_paths = passage_paths
        self.index_offset = index_offset
        self.__load_passage()

    def __load_passage(self):
        for passage_index, passage_path in enumerate(self.passage_paths):
            index = self.index_offset[passage_index]
            for filename in sorted(os.listdir(passage_path)):
                with open(passage_path+'/'+filename, 'r') as f:
                    self.data.append(
                        {
                            'name': filename.split('.')[0],
                            'text': f.read(),
                            'id': index
                        }
                    )
                    index += 1

    def get_passage(self):
        return self.data

    def get_id(self):
        return [i for i in range(len(self.data))]

    def get_context(self):
        return [text['text'] for text in self.data]

    def get_name(self):
        return [text['name'] for text in self.data]
    
    def get_id(self):
        return [text['id'] for text in self.data]


class FAQ_Loader:
    def __init__(self, faq_path, abbreviation_dict=None) -> None:
        self.data = list()
        self.faq_paths = faq_path
        self.abbreviation_dict = abbreviation_dict

        self.__load_faq()

    def __load_faq(self):
        csv_data = pd.read_csv(
            self.faq_paths,
            header=0,
            usecols=['Question']
            ).values.tolist()
        for index, text in enumerate(csv_data):
            name = 'faq_' + str(index)
            text = ' '.join(
                [
                    self.abbreviation_dict[word]
                    if word in self.abbreviation_dict.keys() else word
                    for word in text[0].split()
                ]
            )
            self.data.append(
                {
                    'name': name,
                    'text': text
                }
            )

    def get_faq(self):
        return self.data


class QA_Data_Loader:
    def __init__(self, data_path) -> None:
        self.data = list()

        self.context = list()
        self.question = list()
        self.answer = list()

        self.__load_passage(data_path)

    def __load_passage(self, data_path):
        for filename in os.listdir(data_path):
            with open(data_path+'/'+filename, 'r') as f:
                self.data.append(json.load(f))

    def create_dataset(self):
        for file in self.data:
            for group in file['data']:
                for paragraph in group['paragraphs']:
                    for query in paragraph['qas']:
                        self.context.append(paragraph['context'])
                        self.question.append(query['question'])
                        if len(query['answers']) == 1:
                            self.answer.append(query['answers'][0])
                        else:
                            print("There are one or more answer")

    def get_dataset_len(self):
        return len(self.context)
