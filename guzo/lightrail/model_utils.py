"""
Ethiopian Transport API
Models
"""

__author__ = "Dawit Nida (dawit@dawitnida.com)"
__date__ = "Date: 19-11-2017"
__version__ = "Version: 1.0.0"
__Copyright__ = "Copyright: @dawitnida"

from django.utils.translation import ugettext_lazy as _


class Choices:
    OPERATIONAL_STATUSES = (
        (u'1', u'Planned'),
        (u'2', u'Under construction'),
        (u'3', u'Opened'),
        (u'4', u'Under maintenance'),
        (u'4', u'Closed'),
    )

    ENTRY_STATUSES = (
        (u'1', u'Draft'),
        (u'2', u'New'),
        (u'3', u'Approved'),
        (u'4', u'Published'),
    )

    PLACE = (
        (u'1', u'Addis Ababa'),
        (u'2', u'Adama'),
        (u'3', u'Gondar'),
        (u'4', u'Mekele'),
        (u'5', u'Hawassa'),
        (u'6', u'Bahir Dar'),
        (u'7', u'Dire Dawa'),
        (u'8', u'Dessie'),
        (u'9', u'Jimma'),
        (u'10', u'Jijiga'),
        (u'11', u'Shashamane'),
        (u'12', u'Arba Minch'),
        (u'13', u'Hosaena'),
        (u'14', u'Dila'),
        (u'15', u'Nekemte'),
        (u'16', u'Debre Birhan'),
        (u'17', u'Asella'),
        (u'18', u'Harar'),
        (u'19', u'Asmera'),
        (u'19', u'Woliso'),
        (u'20', u'Unspecified'),
    )

    SOCIAL_MEDIA = (
        (u'1', u'Facebook'),
        (u'2', u'Twitter'),
        (u'3', u'LinkedIn'),
        (u'4', u'Instagram'),
        (u'5', u'Google+'),
        (u'6', u'Pinterest'),
        (u'7', u'Other'),
    )
