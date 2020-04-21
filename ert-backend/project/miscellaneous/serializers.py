from moneyed import Money
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class MoneyField(serializers.Field):
    def to_representation(self, money):
        if not isinstance(money, Money):
            return float(money)
        return float(money.amount)

    def to_internal_value(self, amount):
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            raise ValidationError("Value must be a float")

        return Money(amount=amount, currency="INR")

