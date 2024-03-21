import argparse
#task: include parser
def parser():
    parser= argparse.ArgumentParser(description= "give name")
    parser.add_argument("--name", #long form name
                        "-n",#short form name 
                        required= True, #must give it an input (file name e.g. csv) in the command 
                        help= "must give name") 
    args = parser.parse_args()
    return args


class Person:
    species = "homo sapiens" #global attribute
    def __init__(self, name):
        self.name = name 

    def hello (self):
        print("hello " + self.name)

    def preferences(self):
        print("i like python")



def main():
    args = parser()
    person= Person(args.name)
    #person2= Person("mina")
    person.hello() #can also write person2.hello()
    person.preferences()

#def main():
    #person= Person("Ross")
    #person2= Person("mina")
   # person.hello() #can also write person2.hello()
    #person.preferences()
    


if __name__== "__main__":
    main()

#in terminal run: python greeting.py -n "Ida"



#classes: data and function bundled up
#function in class context are called method = something that belongs to a unique class