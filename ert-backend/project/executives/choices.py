from djchoices import DjangoChoices, ChoiceItem


class RoleTypeChoices(DjangoChoices):
    STAFF = ChoiceItem("STF")
    OTHER = ChoiceItem("OTH")
