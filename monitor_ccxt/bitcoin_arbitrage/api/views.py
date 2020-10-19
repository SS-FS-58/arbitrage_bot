import logging
import pdb

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from bitcoin_arbitrage.models import Spread

from .serializers import (
    ActionSerialier,
    serialize_uxchange_buy,
    serialize_xchange_sell
)

from . import mixins 


logger = logging.getLogger(__name__)


class RealTimeSpreadEndpoint(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        try:
            all_spreads = []
            for spread in Spread.objects.all().order_by('-recorded_date')[:5]:
                xchange_buy = spread.xchange_buy 
                xchange_sell = spread.xchange_sell
                all_spreads.append({
                    "id": spread.id,
                    "exchange_buy_id": spread.exchange_buy_id,
                    "exchange_sell_id": spread.exchange_sell_id,
                    "xchange_buy": serialize_uxchange_buy(xchange_buy),
                    "xchange_sell": serialize_xchange_sell(xchange_sell),
                    "recorded_date": spread.recorded_date,
                    "spread": spread.spread
                })
        except Exception as error:
            logger.exception(str(error))
            return Response({"status": "error"}, status=400)
        return Response({"spreads": all_spreads}, status=200)


class MonitorEndpoint(APIView, mixins.MonitorMixin):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        serializer = ActionSerialier(data=request.data)
        if serializer.is_valid():
            action = serializer.cleaned_data["action"]
            if action == "start":
                if self.start_bitcoin_monitor():
                    return Response({"status" : "success"}, status=200)
                return Response({"status" : "error"}, status=400)
            elif action == "stop":
                if self.stop_bitcoin_monitor():
                    return Response({"status": "success"}, status=200)
                return Response({"status" : "error"}, status=400)
            return Response({"status" : "error"}, status=400)
        return Response({"status" : serializer.errors}, status=400)