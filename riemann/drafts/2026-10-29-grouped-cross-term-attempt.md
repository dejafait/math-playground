# Grouped cross term: bounded arithmetic attempt

Invocation-start coverage is the unchanged EXPLORE assessment at
`drafts/literature/2026-10-29-grouped-residual-cross-term-coverage.md`.
The sole target is its exact TARGET. Existing L478 and L319 failures
remain; neither is a bound on the actual signed moment.

Main gap: L477's absolute residual has neither defect threshold.
Intermediate target: evaluate the complete L478 (13) cross term with
error o(T(log T)^8), retaining all weights and the closed interval.
Downstream use: one component of the complete second moment, still
requiring the other terms, fourth moment and L1 transfer. Continue only
with a summed error below the stated scale and control of the signed
arithmetic main sum; a transform or another power-sized bound alone
does not pass.

Unfinished reasoning saved before the calculation: L316's phase gives
2 theta(t)=t log(t/(2 pi e))-pi/4+O(1/T). Gonek Lemma 2 with a=1/2
suggests J(1,m/h)=2 pi sqrt(h/m) exp(-2 pi i h/m) in its stationary
range, plus the explicit two endpoint errors. After multiplying by
g_(h,m), its main coefficient is 2 pi/m times the exact logarithmic
weight. A finite geometric sum in one original factor could exploit
the rational phase. All endpoint-error sums and composite-modulus
cases must still be proved. These formulas are provisional here.

Potential elementary refinement: in the stationary range nkl is
comparable to M^2 m, so m cannot exceed the other factors by an
arbitrary amount. Dyadic counting may both reduce logarithmic weight
losses and give a summable endpoint majorant without Shiu. Test the
full sum, not a selected box. No new non-elementary input is assumed.

Intermediate calculation, still to be written and checked canonically:
the two endpoint errors sum to O(T(log T)^6). For fixed m,k,l the
saddle parameters r=2 pi nkl/m have spacing at least T/(2M) whenever
one lies in [T/2,4T]; the sum of the endpoint kernels over this lattice
is O(sqrt(T) log T). The coefficient there is at most
C(log T)^4/(m sqrt(T)); summing m,k,l gives the claimed error.

For the rational main sum, let q=m/gcd(k,m). Summing in n with its
monotone log(n/m)^2 weight costs O((log T)^2/||kl/m||) if q does not
divide l. Summing those reciprocal distances over l<=M costs
O(M log(2m)), even for composite m. Hence all nonresonant terms cost
O(T(log T)^6). The terms m|kl have phase one and are nonnegative.
Their n sum can be replaced by its elementary integral with total
error O(T(log T)^4), using sum tau(m)/m^2<infinity. This would give
an explicit nonoscillatory main term, not an unevaluated signed dual sum.

A possible full-scale lower bound for that main term uses the unique
parametrization k=da, m=db, l=bc, gcd(a,b)=1. On the polynomial boxes
a in [M^.78,M^.80], b,d in [M^.08,M^.10], c in [M^.58,M^.60],
the n interval has both endpoints below M and both logarithmic weights
are bounded below by constants times (log M)^2. Its integrated weight
is at least c T(log M)^4/(abcd). An elementary common-divisor union
bound gives harmonic coprime mass of order (log M)^2 for a,b;
the other two harmonic sums give another (log M)^2. This lower-bound
argument and exact boundary conventions still require canonical review.

Completed in `lemmas/L479-grouped-cross-term-resonant-evaluation.md`.
The provisional transform, endpoint bounds, residue-class separation
and full-scale lower bound are now proved there with exact hypotheses.
The total error is O(T(log T)^6)=o(T(log T)^8); its explicit positive
main term is comparable to T(log T)^8. No further result is claimed in
this working file. A separate independent critical audit remains;
PROGRESS.md holds the sole current continuation and routing.
