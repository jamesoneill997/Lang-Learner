import json

class Test:
    def __init__(self, lang):
        self.lang = lang
        self.set_list = []
        self.test_num = 0
        self.score = 0
    
    #fetch dataset
    def get_dataset(self):
        with open('{}.json'.format(self.lang)) as json_file:
            for line in json_file:
                self.set_list.append(json.loads(line))

            return self.set_list

    #show all current datasets
    def show_all_datasets(self):
        print(self.set_list)

    #Pick a dataset
    def pick_test(self):
        self.test_num = int(input("Pick a number between 1 and {}: ".format(len(self.set_list))))
        if self.test_num > len(self.set_list):
            print("Invalid number selected.")
            self.pick_test()

        return self.set_list[self.test_num-1]

    def make_test(self):
        ds = self.pick_test()
        for item in ds:
            attempt = str(input("Comment dit en fran¢ais {}? \n".format(item))).lower().strip()
            if attempt == ds[item].lower().strip():
                print("Oui, c'est correct!")
                self.score+=1
            else:
                print("Incorrect, study harder")
    
    def results(self):
        tot_questions = len(self.set_list[self.test_num-1])
        tot_correct = self.score

        return "Your result is: {}/{}".format(tot_correct, tot_questions)
    
    def start(self):
        self.get_dataset()
        self.make_test()
        print(self.results())
    
    


def main():
    fr_test = Test('fr')
    fr_test.start()

if __name__ == '__main__':
    main()