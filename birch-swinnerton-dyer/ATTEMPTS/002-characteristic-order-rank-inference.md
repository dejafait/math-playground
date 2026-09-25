# Exact rank from characteristic order and control

Date: 2026-09-24. Outcome: informative negative for the inference from the
specified module data. The cyclotomic method and its rank upper bound remain
available with additional arithmetic input.

The intermediate target was to recover the specialized Selmer dimension
from the characteristic series of the entire cyclotomic module. This could
have supplied an arithmetic input to a later analytic-order comparison.
Unlike the preceding finite-descent test, it retains information about a
global Iwasawa module rather than a finite observation depth.

## WHY IT FAILS

[L002](../lemmas/L002-characteristic-order-specialization-defect.md) proves
that characteristic order counts the sum of the lengths of the cyclic
summands at (T), whereas specialization counts the summands themselves.
The explicit modules there have the same characteristic ideal and different
even specialized dimensions; each admits exact abstract base-level control.
The resulting upper bound falls short of exact rank because a nonzero
length(T X_(T)) can remain, independently of the base Kummer defect. These
modules are not asserted to arise from elliptic curves. This excludes a
formal inference from the characteristic ideal and control, not an
arithmetic theorem using extra structure or BSD itself.

The precise missing module condition is semisimplicity at (T), equivalently
that the natural invariant-to-coinvariant map in L002 be an isomorphism.
An arithmetic height criterion addresses information not contained in the
characteristic ideal. Merely knowing that ideal more accurately would not
resolve the exhibited ambiguity.
