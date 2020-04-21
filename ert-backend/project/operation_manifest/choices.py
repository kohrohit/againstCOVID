from djchoices import DjangoChoices, ChoiceItem


class IndianStateChoices(DjangoChoices):
    ANDAMAN_AND_NICOBAR = ChoiceItem("AN")
    ANDRA_PRADESH = ChoiceItem("AP")
    ARUNACHAL_PRADESH = ChoiceItem("AR")
    ASSAM = ChoiceItem("AS")
    BIHAR = ChoiceItem("BR")
    CHHATTISGARH = ChoiceItem("CT")  # Google give CT instead CG
    CHANDIGARH = ChoiceItem("CH")
    DAMAN_AND_DIU = ChoiceItem("DD")
    DELHI = ChoiceItem("DL")
    DADRA_AND_NAGAR_HAVELI = ChoiceItem("DN")
    GOA = ChoiceItem("GA")
    GUJARAT = ChoiceItem("GJ")
    HARYANA = ChoiceItem("HR")
    HIMACHAL_PRADESH = ChoiceItem("HP")
    JHARKHAND = ChoiceItem("JH")
    JAMMU_AND_KASHMIR = ChoiceItem("JK")
    KARNATAKA = ChoiceItem("KA")
    KERALA = ChoiceItem("KL")
    LAKSHADWEEP = ChoiceItem("LD")
    MAHARASHTRA = ChoiceItem("MH")
    MADHYA_PRADESH = ChoiceItem("MP")
    MIZORAM = ChoiceItem("MZ")
    NAGALAND = ChoiceItem("NL")
    ODISHA = ChoiceItem("OD")
    PUNJAB = ChoiceItem("PB")
    PUDUCHERRY = ChoiceItem("PY")
    RAJASTHAN = ChoiceItem("RJ")
    SIKKIM = ChoiceItem("SK")
    TAMIL_NADU = ChoiceItem("TN")
    TRIPURA = ChoiceItem("TR")
    TELANGANA = ChoiceItem("TS")
    UTTARAKHAND = ChoiceItem("UK")
    UTTAR_PRADESH = ChoiceItem("UP")
    WEST_BENGAL = ChoiceItem("WB")


class CurrencyChoices(DjangoChoices):
    USD = ChoiceItem("USD")
