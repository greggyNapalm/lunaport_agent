#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
agent.plugg_views.job
~~~~~~~~~~~~~~~~~~~~~

Job - test execution.
"""

#import json
import pprint
pp = pprint.PrettyPrinter(indent=4).pprint

from flask import jsonify, request, Response, url_for, session

from Base import BaseView
from .. dao.exceptions import StorageError
from .. dao.job import SideEffect, RDBMS
from .. domain.job import JobBuilder, JobAdaptor


class Job(BaseView):
    str_params = [
        'owner',
    ]
    int_params = [
        'page',
        'per_page',
    ]
    dao = SideEffect(RDBMS)

    def get(self, job_id):
        if job_id is None:  # walk through all ammo
            return self.get_by_id(job_id)
        else:
            return self.looku()

    def post(self):
        try:
            job = JobBuilder.from_Flask_req(request, session)
        except ValueError as e:
            msg = {
                'error_type': 'Malformed body attributes',
                'error_text': str(e),
            }
            return jsonify(msg), 422

        try:
            job_id = self.dao.insert(job)
            job = self.dao.get_by_id(job_id)
        except StorageError as e:
            msg = {
                'error_type': 'Storage call fails',
                'error_text': str(e),
            }
            return jsonify(msg), 500
        except ValueError as e:
            msg = {
                'error_type': 'Malformed body attributes',
                'error_text': str(e),
            }
            return jsonify(msg), 409

        hdrs = {
            'Content-Type': 'application/json; charset=utf-8',
            'Location': '{}{}'.format(url_for('job'), job.id),
        }
        return Response(response=JobAdaptor.to_resp(job), status=201,
                        headers=hdrs)

    def patch(self, job_id):
        diff = request.json
        if not diff:
            msg = {
                'error_type': 'Malformed body attributes',
                'error_text': 'Can\'t deserialize json document',
            }
            return jsonify(msg), 422

        try:
            job = self.dao.update_by_id(job_id, diff)
        except StorageError as e:
            msg = {
                'error_type': 'Storage call fails',
                'error_text': str(e),
            }
            return jsonify(msg), 500
        except AssertionError as e:
            msg = {
                'error_type': 'Malformed request data',
                'error_text': str(e),
            }
            return jsonify(msg), 422

        hdrs = {
            'Content-Type': 'application/json; charset=utf-8',
            'Location': '{}{}'.format(url_for('job'), job.id),
        }
        return Response(response=JobAdaptor.to_resp(job), status=200,
                        headers=hdrs)
