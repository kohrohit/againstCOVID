from djchoices import DjangoChoices, ChoiceItem


class TransactionTypeChoices(DjangoChoices):
    REFERRAL = ChoiceItem("RFL")
    CASH_BACK = ChoiceItem("CBK")
    RECHARGE = ChoiceItem("RCH")
    EXPENDITURE = ChoiceItem("EXR")
    DISBURSEMENT = ChoiceItem("DSB")
    UNKNOWN = ChoiceItem("UKW")
    DEDUCTION = ChoiceItem("DED")
