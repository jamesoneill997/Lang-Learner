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
        self.test_num = int(input("Pick a number between 1 and {}: ".format(len(self.set_list))))
        print(self.test_num)
        if self.test_num > len(self.set_list):
            print("Invalid number selected.")
            self.pick_test()

        return self.set_list[self.test_num-1]

    def start(self):
        self.get_dataset()
        test = self.pick_test()
        print(test)

def main():
    fr_test = Test('fr')
    fr_test.start()

if __name__ == '__main__':
    main()