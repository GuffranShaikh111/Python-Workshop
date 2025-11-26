class Notification:
    def get_notification(self):
        pass
class Instagram(Notification):
    def get_notification(self):
        print("Notification from Instagram")

class Twitter(Notification):
    def get_notification(self):
        print("Notification from Twitter")
instagram = Instagram()
twitter = Twitter()
instagram.get_notification()
twitter.get_notification()
