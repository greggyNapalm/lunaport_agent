#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
agent.plugg_views.base
~~~~~~~~~~~~~~~~~~~~~~

Base class for Lunaport Agent REST API class-based views.
"""

from flask.views import MethodView

class BaseView(MethodView):
    str_params = []
    int_params = []

    @classmethod
    def cmpl_query(cls):
        query = {}
        for p, v in request.args.items():
            if p in cls.int_params:
                if not ((v.isdigit()) and (int(v) >= 0)):
                    raise ValueError('*{}* parameter malformed'.format(p))
                query.update({p: int(v)})

            if p in cls.str_params:
                v_spltd = v.split(',')
                if len(v_spltd) > 1:  # list of values in HTTP param
                    query.update({p: v_spltd})
                else:  # singular string param
                    query.update({p: str(v)})
        return query

    @staticmethod
    def cmpl_link_hdr(r, per_page, next_page, prev_page):
        link_hdr = []
        orig_qs = r.url.split('?')[0]
        orig_params = dict(r.args.items())

        def new_url(params_diff):
            p = copy.deepcopy(orig_params)
            p.update(params_diff)
            return '{}?{}'.format(orig_qs, urllib.urlencode(p))

        if next_page:
            link_hdr.append('<{}>; rel="next"'.format(new_url({
                'per_page': per_page,
                'page': next_page,
            })))
        if prev_page:
            link_hdr.append('<{}>; rel="prev"'.format(new_url({
                'per_page': per_page,
                'page': prev_page,
            })))
        return ','.join(link_hdr)
