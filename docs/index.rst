Flatline
========

Flatline is a lispy language for the specification of values to be
extracted or generated from an input dataset, using a finite sliding
window of input rows.

In `BigML <https://bigml.com>`__, it is used either as a row filter
specifier or as a field generator.

In the former case, the input consists of dataset rows on which a
single, boolean expression is computed, and only those for which the
result is true are kept in the output dataset.

When used to generate new datasets from given ones, a list of Flatline
expressions is provided, each one generating either a value or a list of
values, which are then concatenated together to conform the output rows
(each value representing therefore a field in the generated dataset).

-  `User manual <user-manual.html>`__
-  `Quick reference <quick-reference.html>`__
