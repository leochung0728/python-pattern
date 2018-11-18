class Borg(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass


if __name__ == '__main__':
    rm1 = Borg()
    rm2 = Borg()

    rm1.state = 'Idle'
    rm2.state = 'Running'

    print('rm1: {}'.format(rm1))
    print('rm2: {}'.format(rm2), end='\n\n')

    rm2.state = 'Zombie'

    print('rm1: {}'.format(rm1))
    print('rm2: {}'.format(rm2), end='\n\n')

    rm3 = YourBorg()

    print('rm1: {}'.format(rm1))
    print('rm2: {}'.format(rm2))
    print('rm3: {}'.format(rm3))

### OUTPUT ###
# rm1: Running
# rm2: Running

# rm1: Zombie
# rm2: Zombie

# rm1: Init
# rm2: Init
# rm3: Init