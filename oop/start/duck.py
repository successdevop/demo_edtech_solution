class Duck:
    def walk(self):
        print("waddle waddle, I waddle")

    def swim(self):
        print("Come on in, but it's a bit chilly")

    def quack(self):
        print("Are you 'arvin' or a 'larf'")


class Penguin():
    def walk(self):
        print("waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far south")

    def quack(self):
        print("Are you 'arvin' or 'larf', I'm Penguin")


def run_fuc(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == "__main__":
    for attr in (Duck(), Penguin()):
        run_fuc(attr)
        print()
    # bird = Duck()
    # peng = Penguin()
    # run_fuc(bird)