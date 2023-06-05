from oscar.apps.offer.views import OfferDetailView as CoreOfferDetailView


class OfferDetailView(CoreOfferDetailView):
    template_name = 'oscar/offer/list.html'
