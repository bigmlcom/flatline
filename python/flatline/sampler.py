# -*- coding: utf-8 -*-

# Copyright (c) 2015 BigML, Inc
# All rights reserved.


"""flatline.sampler

Working locally with Flatline over dataset samples.

The Sampler class automatizes the process of sampling a dataset,
downloading a subset of its rows and subsequently applying to them any
desired Flatline generator.

:author: jao <jao@bigml.com>
:date: Mon Apr 06, 2015 04:14

"""

import interpreter
import bigml.api as api
import os

class Sampler:

    _interpreter = interpreter.Interpreter()

    def __init__(self, username=None, api_key=None, bigml=None):
        if bigml is None:
            username = username or os.environ['BIGML_USERNAME']
            api_key = api_key or os.environ['BIGML_API_KEY']
            self._bigml = api.BigML(username=username, api_key=api_key)
        else:
            self._bigml = bigml
        self._sample = None

    def take_sample(self, dataset_id, size=10):
        sample = self._bigml.create_sample(dataset_id)
        qs = "limit=-1&rows=%d" % size
        self._sample = self._bigml.check_resource(sample['resource'],
                                                  query_string=qs)

    def sample(self):
        if self._sample is None:
            return {}
        return self._sample['object']['sample']

    def rows(self):
        return self.sample().get('rows')

    def fields(self):
        return self.sample().get('fields')

    def apply_lisp(self, sexp):
        return self._interpreter.apply_lisp(sexp, self.rows(), self.sample())

    def apply_json(self, sexp):
        return self._interpreter.apply_json(sexp, self.rows(), self.sample())
