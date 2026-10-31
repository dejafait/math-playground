# Small absolute error alone: multiple-zero compensation stop

The generic inference from an arbitrarily small absolute C^2 remainder
to D(P)>=|B(P,R)|+|D(R)| is false at an admissible multiple zero.
[L569](../lemmas/L569-multiple-zero-absolute-compensation-jet-obstruction.md)
contains the complete necessary-and-sufficient two-jet classification
and the exact epsilon-small violating family for every fixed F in its
hypotheses, including polynomial examples of each multiplicity m>=2.

WHY IT FAILS: D(F)=0 at a multiple zero leaves no surplus for separated
absolute losses. The full signed decomposition must cancel exactly;
the absolute budget additionally forces both signed remainder pieces
to be nonpositive. A small affine remainder can violate this condition
at every positive size while preserving the zero value and leaving F
unchanged. The proof and all boundary cases are canonical in L569.

This stops small-error-only sufficiency, not actual Hermite compensation,
full signed cancellation, or RH. L564's bounds remain valid. No actual
multiple Xi zero or actual-coefficient counterexample is provided.
Reopening the absolute route requires independent actual joint-jet
information; a smaller absolute bound or a larger probe grid is not
new input. A zero-preserving approximation mechanism is a distinct
unassessed possibility, not an established repair.
