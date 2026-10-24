# Validated nonlinear enclosure — primary theorem input

## Hypotheses

Let F:D→R^n be continuously differentiable on a box domain D. Choose
a point a, a finite closed error box E containing zero, and a real
n-by-n matrix R, with a+E contained in D. Let J enclose every Jacobian
on a+E entrywise. All interval operations below mean enclosing operations.

## Conclusion

Import the modified Krawczyk criterion

    S = -R F(a) + (I-R J) E  contained in int(E).

It certifies a root in a+S, unique within a+E, and nonsingularity of R
and every enclosed Jacobian. Thus nonsingularity need not be assumed
from a numerical inverse. A failed inclusion gives no converse.

## Proof

Siegfried M. Rump, *Verification methods: Rigorous results using
floating-point arithmetic*, Acta Numerica **19** (2010), 287–449,
DOI [10.1017/S096249291000005X](https://doi.org/10.1017/S096249291000005X),
[corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
Theorem 13.3 and proof, author p.89 (PDF page 89, zero-based 88).
The proof applies Brouwer to the preconditioned map, then Lemma 10.5
to obtain invertibility and uniqueness. Import this proof without
reproving it. Outward interval evaluation is covered by §5.3–5.5,
(5.14)–(5.17), author pp.27–28.

Read on 2026-10-23: Theorems 13.1–13.3 with proofs and Algorithm 13.4,
author pp.88–90; the failure discussion and §13.1, author p.91.
Theorem 13.2 is the interval-Newton alternative; it additionally requires
regularity of its whole Jacobian interval. The present planned checker
uses Theorem 13.3 only. Its enclosures must cover coefficient conversion,
residual, Jacobian and matrix arithmetic. Exact rational endpoints are
also permissible: no floating-point endpoint approximation is then used.

This is a standard theorem input, not an enclosure of L111. The finite
polynomial residual, its complete derivative enclosure, positive box,
strict inclusions and capacity comparison remain future verification
obligations. No global uniqueness in the positive orthant is imported.

## Mathlib

Full matching modified-Krawczyk theorem and this 64-factor application:
not checked. Supporting interval arithmetic, differentiability and
fixed-point results: not checked. Unknown coverage is not absence.

## Source addition: mean-value enclosure (2026-10-24)

### Hypotheses

Let f:D→R^n be continuously differentiable on a real box D, with
a,v in D. Let J enclose all Jacobians on hull({a,v}).

### Conclusion

Import f(v) in f(a)+J*(v-a). The enclosing matrix may use different
evaluation points for different rows; no common intermediate Jacobian
is required. A scalar function on R^n is covered by adjoining n-1
zero output components.

### Proof

Rump, cited above, corrected author PDF, Theorem 13.1, (13.1)–(13.4),
author pp.87–88 (zero-based PDF pages 86–87). Read the complete
row-wise mean-value justification and convex-hull inclusion. The
integral-Jacobian argument (13.6) on p.88 was also inspected. This is
an imported theorem, without reproof. Section 11.6, (11.10), p.84
discusses centered forms and warns that they can overestimate.

This generic input establishes no bound for the proposed root functional.
Its residual correction, derivatives and interval arithmetic require
separate verification. The original enclosure and preconditioner remain
unchanged.

### Mathlib

Supporting mean-value norm bounds were checked in
[Mathlib.Analysis.Calculus.MeanValue](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/MeanValue.html#Convex.norm_image_sub_le_of_norm_fderiv_le):
`Convex.norm_image_sub_le_of_norm_fderiv_le` and its primed variant
require differentiability and a uniform derivative (or derivative-minus-
fixed-map) norm bound on a convex set, with both points in the set.
These support error control; a full interval residual-functional theorem
and the proposed 64-variable specialization were not checked in Mathlib.
