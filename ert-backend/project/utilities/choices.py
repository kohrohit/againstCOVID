from djchoices import DjangoChoices, ChoiceItem


class PlatformChoices(DjangoChoices):
    ANDROID = ChoiceItem('Android')
    IOS = ChoiceItem('iOS')
    WEB = ChoiceItem('Web')
    DASHBOARD = ChoiceItem('Dashboard')


class TagChoices(DjangoChoices):
    OTHER = ChoiceItem("OTH")
