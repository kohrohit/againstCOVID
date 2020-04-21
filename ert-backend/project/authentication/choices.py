from djchoices import DjangoChoices, ChoiceItem


class AddressTagChoices(DjangoChoices):
    ASSET = ChoiceItem("ASSET")
    OFFICE = ChoiceItem("OFC")
    HOME = ChoiceItem("HOM")
    OTHER = ChoiceItem("OTH")


class KYCDocumentTypeChoices(DjangoChoices):
    AADHAR = ChoiceItem("ADR")
    PASSPORT = ChoiceItem("PST")
    DRIVING_LICENSE = ChoiceItem("DLS")
    PAN_CARD = ChoiceItem("PAN")


class OrganizationTypeChoices(DjangoChoices):
    SCHOOL = ChoiceItem("SCL")
    HOTEL = ChoiceItem("HTL")
    CONSTRUCTION_COMPANY = ChoiceItem("CTC")
    OTHER = ChoiceItem("OTH")
