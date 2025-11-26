class Mobile:
    def __init__(self):
        pass

    def callings(self):
        print('Invoking calling function')

    def sms(self):
        print('Invoking SMS function')

    def games(self):
        print('Invoking games')


class S_24(Mobile):
    def camera(self):
        print('Invoking camera function')

    def music(self):
        print('Invoking music function')

    def video_call(self):
        print('Invoking video call function')

s24=S_24()
s24.music()
s24.games()