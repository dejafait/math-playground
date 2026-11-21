# Step624 — approved quartic calculation, work in progress

The startup SPECIALIZE assessment is
`drafts/literature/2026-11-05-theta-quartic-free-square-root-scope.md`.
Work only on its exact target: the centered monic actual P_4 additive
self-convolution square root, using L791 coefficients through j=4.
L019/L021/L795 give normalization; L778's analytic/backend contracts
remain inherited premises. L823 is context only. No new evaluator or
degree sweep is intended. Existing notebook changes are preserved.

For H=P_4/R_4=x^4-4h*x^3+A*x^2+B*x+D, set
h=gamma(3)/gamma(4), A=6gamma(2)/gamma(4),
B=-4gamma(1)/gamma(4), D=gamma(0)/gamma(4).
Expanding H(y+h) gives C=y^4+p*y^2+q*y+r with
p=A-6h^2, q=B+2Ah-8h^3, r=D+Bh+Ah^2-3h^4.
These expansions and the convolution weights still need certificate
and final proof checks.

The imported d=4 coefficient formula gives, for
Q=y^4+b*y^3+c*y^2+e*y+f,
Q boxplus Q=y^4+2b*y^3+(2c+3b^2/4)*y^2+
(2e+bc)*y+(2f+be/2+c^2/6).
Triangular matching suggests the unique factor
b=0,c=p/2,e=q/2,f=r/2-p^2/48.
Check exact identity before using root criteria. Newton sums through
s_6 build a 4-by-4 Hermite matrix. Positive leading minors suffice;
otherwise all principal minors or a negative witness must be checked.
No signs have yet been evaluated.

Continue on certified positivity; a certified negative necessary minor
parks this factor. Invalid inherited inputs or straddling bounds are
inconclusive. Finite success leaves uniform realization and shifted/mixed
sign compensation unresolved; actual-Xi all-degree positivity is the
main gap. Full matching Mathlib coverage is unchecked.

Completed in L824: the expansions and exact uniqueness are verified;
the final certificate has 65 passing checks and all 15 principal minors
strictly positive. Full proofs and qualifications are canonical there.
The first-pass invalid interval-containment check and its failed evidence
are retained in `scripts/central-jacobi/quartic-624/`; symbolic identity
checking and generic Newton evaluation replace that check. Independent
audit remains open. The preceding text preserves the pre-calculation
reasoning, not another current next-action record.
