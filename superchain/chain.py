

class chain():
    def __init__(self, *args):
        if not args:
            self.keys = None
        elif isinstance(args[0], str):
            self.keys = list(args)
        elif isinstance(args[0], (tuple, list)):
            self.keys = list(args[0])
        else:
            raise Exception('args must be a list or tuple of types')

    def getkeys(self):
        return self.keys

    # def add(self, *args):
    #     if not args:
    #         raise Exception('inputs is illegal')
    #     elif isinstance(args[0], str):
    #         self.keys = list(args)
    #     elif isinstance(args[0], (tuple, list)):
    #         self.keys = list(args[0])
    #     else:
    #         raise Exception('args must be a list or tuple of types')


if __name__ == '__main__':
    c0 = chain()
    c1 = chain('app', 'job')
    c2 = chain(['job', 'model'])
    c3 = chain(('job', 'model'))
    c3 = chain({'job', 'model'})
    print(c0.getkeys())
    print(c1.getkeys())
    print(c2.getkeys())
    print(c3.getkeys())
