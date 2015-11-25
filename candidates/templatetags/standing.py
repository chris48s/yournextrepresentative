from slugify import slugify

from django import template
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from popolo.models import Membership

register = template.Library()

@register.filter
def post_in_election(person, election):
    # FIXME: this is inefficient, but similar to the previous
    # implementation.
    try:
        candidacy = person.memberships.get(
            role=election.candidate_membership_role,
            extra__election=election
        )
    except Membership.DoesNotExist:
        candidacy = None

    if candidacy:
        link = u'<a href="{cons_url}">{cons_name}</a>'.format(
            cons_url=reverse(
                'constituency',
                kwargs={
                    'election': election.slug,
                    'post_id': candidacy.post.id,
                    'ignored_slug': slugify(candidacy.post.extra.short_label),
                }
            ),
            cons_name=candidacy.post.extra.short_label
        )
        result = u'<span class="constituency-value-standing-link">{0}</span>'.format(
            link
        )
        result += u' <span class="party">{0}</span>'.format(
            candidacy.on_behalf_of.name
        )
    else:
        if election.current:
            result = u'<span class="constituency-value-not-standing">%s</span>' % _('Not standing')
        else:
            result = u'<span class="constituency-value-not-standing">%s</span>' % _('Did not stand')
    return mark_safe(result)

@register.filter
def election_decision_known(person, election):
    return person.extra.get_elected(election) is not None

@register.filter
def was_elected(person, election):
    return bool(person.extra.get_elected(election))
