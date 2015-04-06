# -*- coding: utf-8 -*-

# Copyright (c) 2015 BigML, Inc
# All rights reserved.


"""
    flatline.interpreter

User level interface to the flatline interpreter.

:author: jao <jao@bigml.com>
:date: Sun Apr 05, 2015 01:40

"""

import execjs
import pkg_resources

class Interpreter:
    __FLATJS = pkg_resources.resource_filename('flatline', 'flatline-node.js')
    __REQFLATJS = "f__ = require('%s')" % __FLATJS

    def __init__(self):
        self._interpreter = execjs.get("Node")
        self._context = self._interpreter.compile(Interpreter.__REQFLATJS)

    def __eval_in_flatline(self, fun, *args):
        return self._context.call('f__.flatline.%s' % fun, *args)

    @staticmethod
    def infer_fields(row):
        result = []
        id = 0
        for v in row:
            t = type(v)
            optype = 'categorical'
            datatype = 'string'
            if (t is int or t is long or t is float):
                optype = 'numeric'
                if t is float:
                    datatype = 'float64'
                else:
                    datatype = 'int64'
            result.append({'id': '%06x' % id,
                           'optype':optype,
                           'datatype': datatype,
                           'column_number': id})
            id = id + 1
        return result

    @staticmethod
    def __dataset(dataset, rows):
        if dataset is None and len(rows) > 0:
            return {'fields': Interpreter.infer_fields(rows[0])}
        return dataset

    def check_lisp(self, sexp, dataset={}):
        r = self.__eval_in_flatline('evaluate_sexp', sexp, dataset)
        r.pop(u'mapper', None)
        return r

    def check_json(self, json_sexp, dataset={}):
        r = self.__eval_in_flatline('evaluate_js', json_sexp, dataset)
        r.pop(u'mapper', None)
        return r

    def lisp_to_json(self, sexp):
        return self.__eval_in_flatline('sexp_to_js', sexp)

    def json_to_lisp(self, json_sexp):
        return self.__eval_in_flatline('js_to_sexp', json_sexp)

    def apply_lisp(self, sexp, rows, dataset=None):
        return self.__eval_in_flatline('eval_and_apply_sexp',
                                       sexp,
                                       Interpreter.__dataset(dataset, rows),
                                       rows)

    def apply_json(self, json_sexp, rows, dataset=None):
        return self.__eval_in_flatline('eval_and_apply_js',
                                       json_sexp,
                                       Interpreter.__dataset(dataset, rows),
                                       rows)
