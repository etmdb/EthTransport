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
        (1, _('Planned')),
        (2, _('Under construction')),
        (3, _('Opened')),
        (4, _('Under maintenance')),
        (4, _('Closed')),
    )

    ENTRY_STATUSES = (
        (1, _('Still draft')),
        (2, _('New')),
        (3, _('Approved')),
        (4, _('Published')),
    )

    PLACE = (
        (1, _('Addis Ababa')),
        (2, _('Adama')),
        (3, _('Gondar')),
        (4, _('Mekele')),
        (5, _('Hawassa')),
        (6, _('Bahir Dar')),
        (7, _('Dire Dawa')),
        (8, _('Dessie')),
        (9, _('Jimma')),
        (10, _('Jijiga')),
        (11, _('Shashamane')),
        (12, _('Arba Minch')),
        (13, _('Hosaena')),
        (14, _('Dila')),
        (15, _('Nekemte')),
        (16, _('Debre Birhan')),
        (17, _('Asella')),
        (18, _('Harar')),
        (19, _('Asmera')),
        (19, _('Woliso')),
        (20, _('Unspecified')),
    )

    SOCIAL_MEDIA = (
        (1, _('Facebook')),
        (2, _('Twitter')),
        (3, _('LinkedIn')),
        (4, _('Instagram')),
        (5, _('Google+')),
        (6, _('Pinterest')),
        (7, _('Other')),
    )
