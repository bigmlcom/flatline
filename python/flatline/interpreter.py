# -*- coding: utf-8 -*-

# Copyright (c) 2015 BigML, Inc
# All rights reserved.


"""
flatline.interpreter

User level interface to the flatline JS interpreter.

:author: jao <jao@bigml.com>
:date: Sun Apr 05, 2015 01:40

"""

import execjs
import pkg_resources

class Interpreter:
    """A bridge to an underlying nodejs Flatline interpreter.

    This class uses execjs to launch a Nodejs interpreter that loads
    Flatline's javascript implementation and allows interaction via
    Python constructs.

    Example:

      inter = Interpreter()
      inter.check_lisp('(+ 1 2)')
      inter.check_json(["f", 0], dataset=dataset)

    """

    __FLATJS = pkg_resources.resource_filename('flatline', 'flatline-node.js')
    __REQFLATJS = "f__ = require('%s')" % __FLATJS

    def __init__(self):
        self._interpreter = execjs.get("Node")
        self._context = self._interpreter.compile(Interpreter.__REQFLATJS)

    def __eval_in_flatline(self, fun, *args):
        return self._context.call('f__.flatline.%s' % fun, *args)

    @staticmethod
    def infer_fields(row):
        """Utility function generating a mock list of fields.

        Usually, checks and applications of Flatline expressions run
        in the context of a given dataset's field descriptors, but
        during testing it's useful sometimes to provide a mock set of
        them, based on the types of the values of the test input rows.

        Example:

           In[1]: Interpreter.infer_fields([0, 'a label'])
           Out[2]: [{'column_number': 0,
                      'datatype': 'int64',
                      'id': '000000',
                      'optype': 'numeric'},
                     {'column_number': 1,
                      'datatype': 'string',
                      'id': '000001',
                      'optype': 'categorical'}]

        """
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

    def defined_functions(self):
        """A list of the names of all defined Flaline functions"""
        return self.__eval_in_flatline('defined_primitives')

    def check_lisp(self, sexp, dataset=None):
        """Checks whether the given lisp s-expression is valid.

        Any operations referring to a dataset's fields will use the
        information found in the provided dataset, which should have
        the structure of the 'object' component of a BigML dataset
        resource.

        """
        r = self.__eval_in_flatline('evaluate_sexp', sexp, dataset)
        r.pop(u'mapper', None)
        return r

    def check_json(self, json_sexp, dataset=None):
        """Checks whether the given JSON s-expression is valid.

        Works like `check_lisp` (which see), but taking a JSON
        expression represented as a native Python list instead of a
        Lisp sexp string.

        """
        r = self.__eval_in_flatline('evaluate_js', json_sexp, dataset)
        r.pop(u'mapper', None)
        return r

    def lisp_to_json(self, sexp):
        """ Auxliary function transforming Lisp to Python representation."""
        return self.__eval_in_flatline('sexp_to_js', sexp)

    def json_to_lisp(self, json_sexp):
        """ Auxliary function transforming Python to lisp representation."""
        return self.__eval_in_flatline('js_to_sexp', json_sexp)

    def apply_lisp(self, sexp, rows, dataset=None):
        """Applies the given Lisp sexp to a set of input rows.

        Input rows are represented as a list of lists of native Python
        values. If no dataset is provided, the field characteristics
        of the input rows are guessed using `infer_fields`.

        """
        return self.__eval_in_flatline('eval_and_apply_sexp',
                                       sexp,
                                       Interpreter.__dataset(dataset, rows),
                                       rows)

    def apply_json(self, json_sexp, rows, dataset=None):
        """Applies the given JSON sexp to a set of input rows.

        As usual, JSON sexps are represented as Python lists,
        e.g. ["+", 1, 2].

        Input rows are represented as a list of lists of native Python
        values. If no dataset is provided, the field characteristics
        of the input rows are guessed using `infer_fields`.

        """
        return self.__eval_in_flatline('eval_and_apply_js',
                                       json_sexp,
                                       Interpreter.__dataset(dataset, rows),
                                       rows)
