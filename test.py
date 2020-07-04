import json

class Test:
    def __init__(self, lang):
        self.lang = lang
        self.set_list = []
        self.test_num = 0
    
    def get_dataset(self):
        with open('{}.json'.format(self.lang)) as json_file:
            for line in json_file:
                self.set_list.append(json.loads(line))

            return self.set_list

    def show_all_datasets(self):
        print(self.set_list)

    def pick_test(self):
        self.test_num = input("Pick a number between 0 and {}".format(len(self.set_list))
        return self.test_num
        

def main():
    fr_test = Test('fr')
    fr_test.get_dataset()
    #fr_test.show_all_datasets()


if __name__ == '__main__':
    main()