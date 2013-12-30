# Flatline, a language for data rows generation and filtering

Flatline is a lispy language for the specification of values to be
extracted or generated from an input dataset, using a finite sliding
window of input rows.

In BigML, it is used either as a row filter specifier or as a field
generator.

In the former case, the input consists of dataset rows on which a
single, boolean expression is computed, and only those for which the
result is true are kept in the output dataset.

When used to generate new datasets from given ones, a list of Flatline
expressions is provided, each one generating either a value or a list
of values, which are then concatenated together to conform the output
rows (each value representing therefore a field in the generated
dataset).

## Documentation

  - [Flatline's user manual](user-manual.md).
  - [Quick reference](quick-reference.md) with all pre-defined
    functions.


## License

All documentation in this repository is licensed under the following Creative
Commons 4.0 license:

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Flatline reference documentation</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://bigml.com" property="cc:attributionName" rel="cc:attributionURL">BigML Inc</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

All code in this repository is released under the Apache License 2.0.
