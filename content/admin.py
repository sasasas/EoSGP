from django.contrib import admin
from EoSGP201011.content.models import About, DoctrinalStatement, Apprenticeship, LinksBlurb, Link, PartnersBlurb, Partner

for cls in About, DoctrinalStatement, Apprenticeship, LinksBlurb, Link, PartnersBlurb, Partner:
	admin.site.register(cls)
