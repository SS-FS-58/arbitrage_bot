from rest_framework import serializers


class ActionSerialier(serializers.Serializer):
    action = serializers.CharField(required=True)

    def clean_action(self, value):
        if value not in ["start", "stop"]:
            raise serializers.ValidationError()
        return value


def serialize_uxchange_buy(xchange_buy):
    return {
        "id": xchange_buy.id,
        "name": xchange_buy.name,
        "currency_pair": xchange_buy.currency_pair,
        "last_ask_price": xchange_buy.last_ask_price,
        "last_bid_price": xchange_buy.last_bid_price
    }


def serialize_xchange_sell(xchange_sell):
    return {
        "id": xchange_sell.id,
        "name": xchange_sell.name,
        "currency_pair": xchange_sell.currency_pair,
        "last_ask_price": xchange_sell.last_ask_price,
        "last_bid_price": xchange_sell.last_bid_price
    }

