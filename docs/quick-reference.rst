Quick reference
===============

Field accessors and properties
------------------------------

Access to input field values:

.. code:: lisp

         (field <field-designator> [<shift>])
         (f <field-designator> [<shift>])
         (fields <field-designator> ... <field-designator-n>)
         (random-field-value <field-designator>)
         (weighted-random-field-value <field-designator>)
         (ensure-value <field-designator>)
         (ensure-weighted-value <field-designator>)

All fields in a row:

.. code:: lisp

         (all)
         (all-but <field-designator> ... <field-designator-n>)
         (all-with-defaults <field-designator-0> <field-value-0>
                            <field-designator-1> <field-value-1>
                            ...
                            <field-designator-n> <field-value-n>)
         (all-with-numeric-default ["mean" "median" "minimum" "maximum" <number>]

Row properties:

.. code:: lisp

        (row-number) ;;  current row number, 0-based

Field properties:

.. code:: lisp

        (bin-center <field-designator> <bin-number>)  ;;  number
        (bin-count <field-designator> <bin-number>) ;;  number
        (category-count <field-designator> <category>) ;;  number
        (maximum <field-designator>) ;;  number
        (mean <field-designator>) ;;  number
        (median <field-designator>) ;;  number
        (minimum <field-designator>) ;;  number
        (missing? <field-designator> [<shift>]) ;;  boolean
        (missing-count <field-designator>) ;;  number
        (preferred? <field-designator>) ;;  boolean
        (population <field-designator>) ;;  integer
        (sum <field-designator>) ;;  number
        (sum-squares <field-designator>) ;;  number
        (variance <field-designator>) ;;  number
        (standard-deviation <field-designator>) ;;  number

Normalization:

.. code:: lisp

         (normalize <id> [<from> <to>]) ;; [from to] defaults to [0, 1]
         (z-score <id>)

Percentiles and population:

.. code:: lisp

        (percentile <field-designator> <fraction>) ;;  number
        (population-fraction <field-designator> <fraction>) ;;  integer
        (within-percentiles? <field-designator> <lower> <upper>) ;;  boolean
        (percentile-label <field-designator> <label-0> ... <label-n>)

Segments:

.. code:: lisp

        (segment-label <field-designator>
                       <label-1> <bound-1>
                       ...
                       <label-n-1> <bound-n-1>
                       <label-n>)
        (segment-label <field-designator> <label-1> <label-2> ... <label-n>)

Vectorize categorical and text fields:

.. code:: lisp

         (vectorize <field-designator> [<max-fields>])

Items:

.. code:: lisp

         (contains-items? <field-designator> <item0> ... <itemn>)
         (equal-to-items? <field-designator> <item0> ... <itemn>)

Clustering:

.. code:: lisp

         (row-distance <list-of-field-values> [<list-of-field-values> <weights>])
         (row-distance-squared <list-of-field-values> [<list-of-field-values> <weights>])

Strings and regular expressions
-------------------------------

Conversion of any value to a string:

.. code:: lisp

        (str <sexp0> ...) ;;  string

Substrings:

.. code:: lisp

        (subs <string> <start> [<end>]) ;;  string

Regexps:

.. code:: lisp

        (matches? <string> <regex-string>)  ;;  boolean
        (re-quote <string>)  ;;  regexp that matches <string> literally
        (replace <string> <regexp> <replacement>) ;;  string
        (replace-first <string> <regexp> <replacement>) ;;  string

Utilities:

.. code:: lisp

        (length <string>) ;;  integer
        (levenshtein <str-sexp0> <str-sexp1>)  ;;  number
        (occurrences <string> <term> [<case-insensitive?> <lang>]) ;;  number
        (language <string>) ;;  ["en", "es", "ca", "nl"]

Hashing:

.. code:: lisp

         (md5 <string>) ;;  string of length 32
         (sha1 <string>) ;;  string of length 40
         (sha256 <string>) ;;  string of length 64

Math and logic
--------------

Arithmetic operators:

.. code:: lisp

       + - * / div mod

Relational operators:

.. code:: lisp

       < <= > >= = !=

Logical operators:

.. code:: lisp

      and or not

Mathematical functions:

.. code:: lisp

        (abs <x>)     ;; Absolute value
        (acos <x>)
        (asin <x>)
        (atan <x>)
        (ceil <x>)
        (cos <x>)     ;; <x> := radians
        (cosh <x>)
        (exp <x>)     ;; Exponential
        (floor <x>)
        (ln <x>)      ;; Natural logarithm
        (log <x>)     ;; Natural logarithm
        (log2 <x>)    ;; Base-2 logarithm
        (log10 <x>)   ;; Base-10 logarithm
        (max <x0> ... <xn>)
        (min <x0> ... <xn>)
        (mod <n> <m>) ;; Modulus
        (div <n> <m>) ;; Integer division (quotient)
        (pow <x> <n>)
        (rand)            ;; a random double in [0, 1)
        (rand-int <n>)    ;; a random integer in [0, n) or (n, 0]
        (round <x>)
        (sin <x>)     ;; <x> := radians
        (sinh <x>)
        (sqrt <x>)
        (square <x>)  ;; (* <x> <x>)
        (tan <x>)     ;; <x> := radians
        (tanh <x>)
        (to-degrees <x>) ;; <x> := radians
        (to-radians <x>) ;; <x> := degrees
        (linear-regression <x1> <y1> ... <xn> <yn>) ;; slope, intercept, pearson
        (chi-square-p-value <degrees of freedom> <value>)

Coercions
---------

.. code:: lisp

        (integer <sexp>) ;;  integer
        (real <sexp>) ;;  real
        ;; (integer true) = 1, (integer false) = 0

Dates and time
--------------

Functions taking a number representing the *epoch*, i.e., the number of
**milliseconds** since Jan 1st 1970.

.. code:: lisp

        (epoch-year <n>) ;;  number
        (epoch-month <n>) ;;  number
        (epoch-day <n>) ;;  number
        (epoch-weekday <n>) ;;  number
        (epoch-hour <n>) ;;  number
        (epoch-minute <n>) ;;  number
        (epoch-second <n>) ;;  number
        (epoch-millisecond <n>) ;;  number
        (epoch-fields <n>) ;;  list of numbers

Any string can be coerced to an epoch:

.. code:: lisp

        (epoch <string> [<format>])

Conditionals and local variables
--------------------------------

Conditionals:

.. code:: lisp

       (if <cond> <then> [<else>])

       (cond <cond0> <then0>
             <cond1> <then1>
             ... ...
             <default>)

For example:

.. code:: lisp

        (cond (> (f "000001") (mean "000001")) "above average"
              (= (f "000001") (mean "000001")) "below average"
              "mediocre")

Local variables:

.. code:: lisp

        (let <bindings> <body>)
        <bindings> := (<varname0> <val0> ...  <varnamen> <valn>)
        <body> := <expression with varname0 ... varnamen>

For example:

.. code:: lisp

        (let (x (+ (window "a" -10 10))
              a (/ (* x 3) 4.34)
              y (if (< a 10) "Good" "Bad"))
          (list x (str (f 10) "-" y) a y))

Lists
-----

Creation and elememt access:

.. code:: lisp

        (list <sexp-0> ... <sexp-n>) ;;  list of given values
        (cons <head> <tail>) ;;  list
        (head <list>) ;;  first element
        (tail <list>) ;;  list sans first element
        (nth <list> <n>) ;;   0-based nth element

Inclusion:

.. code:: lisp

        (in <value> <list>) ;;  boolean

Properties of lists:

.. code:: lisp

        (count <list>)         ;; (count (list (f 1) (f 2))) => 2
        (mode <list>)          ;; (mode (list a b b c b a c c c))  => "c"
        (max <list>)           ;; (max (list -1 2 -2 0.38))  => 2
        (min <list>)           ;; (min (list -1.3 2 1))  => -1.3
        (avg <list>)           ;; (avg (list -1 -2 1 2 0.8 -0.8)) => 0

List transformations:

.. code:: lisp

        (map <fn> (list <a0> <a1> ... <an>))
        (filter <fn> (list <a0> ... <an>))

Field lists and windows:

.. code:: lisp

        (fields <field-designator> ... <field-designator-n>)
        (window <field-designator> <start> <end>)
        (avg-window <field-designator> <start> <end>)  ;; average of values
        (sum-window <field-designator> <start> <end>) ;; sum of values
        (diff-window <fdes> <start> <end>) ;; differences of consecutive values
        (cond-window <fdes> <sexp>)        ;; values that satisfy boolean sexp
