"""
"""

from Products.ATContentTypes.content.folder import ATFolder
from Products.Archetypes.BaseContent import BaseSchema
from Products.Archetypes.Field import IntergerField
from Products.Archetypes.Widget import IntegerWidget
from Products.Archetypes.public import registerType, Schema
from zope.interface import implements, implementedBy
from Products.Musixmatch.content.interfaces import ITrack
from Products.Musixmatch import __copyright__, __license__, __docformat__, PRODUCT


class MusixmatchTrack(ATFolder):
    """
    """

    implements(ITrack, *implementedBy(ATFolder))
    schema = BaseSchema.copy() + Schema((
        IntergerField(
            name='track_id',
            widget=IntegerWidget(
                label="Musixmatch Track ID",
                label_msgid='Musixmatch_Track_label',
                description = "Track ID within the Musixmatch database",
                i18n_domain='Musixmatch',
                visible = {"new": "invisible", "edit": "invisible"},
            ),
            required=False
        )                                             
    ))

registerType(Track, PRODUCT)
