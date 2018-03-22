'''
Création : 12 janv. 2010

@author: Eric Lapouyade
'''
from django import template
from django.utils.safestring import mark_safe
from ..listing import Listing, ListingVariations
register = template.Library()


@register.simple_tag(takes_context=True)
def create_listing(context, listing=None, *args, **kwargs):
    # developper will specify a Listing class,
    # but Django will automatically instanciate it with no argument
    if not isinstance(listing,(Listing,ListingVariations)):
        listing = Listing()
    listing.store_kwargs(**kwargs)
    return listing


@register.simple_tag()
def setopt_listing(listing, **kwargs):
    if isinstance(listing,Listing):
        listing.store_kwargs(**kwargs)
    return ''


@register.simple_tag()
def setopt_column(listing, name, **kwargs):
    if isinstance(listing,Listing):
        listing.store_column_kwargs(name, **kwargs)
    return ''


@register.simple_tag(takes_context=True)
def render_listing(context, listing=None, data=None, *args, **kwargs):
    if listing is None:
        listing = context.get('listing')
    if isinstance(listing,str) or listing is None:
        return mark_safe(
                '<b>ERROR :</b> The listing/class/data you specified is '
                'empty : do you have set the corresponding variable '
                'in view context ?')
    if not isinstance(listing,(Listing,ListingVariations)):
        data = listing
        listing = Listing()
    # if there is data or a model is specified in columns (if exsiting)
    if data or listing.get_model():
        listing.init(data, **kwargs)
    else:
        listing.set_kwargs(**kwargs)
    if isinstance(listing.data,str) or listing.data is None:
        return mark_safe(
                '<b>ERROR :</b> The listing has no data or model specified : '
                'May be you passed a listing class and forgot to specify data '
                'or model or you passed only a listing instance but without any'
                ' bound data. Please check you have '
                '<tt>{% render_listing your_listing_class_or_instance your_data'
                ' %}</tt> or specify data or a django model when creating '
                'the listing class or instance in your python code.')
    return mark_safe(listing.render(context))


@register.simple_tag(takes_context=True)
def geturl_listing(context, listing, **kwargs):
    return mark_safe(listing.get_url(context, **kwargs))

