# Affine Meixner-Pollaczek source review1595

## Working checkpoint

Literature-only review of assessment1594's exact target. Supplied overview
and DAG used directly; C028a and C028j hypotheses/interface, source-notes1503,
1591 and the relevant1587 comparison read. The three named Pollaczek failure
records concern flows, not reference expansions of unchanged P_d.

Inspected NIST DLMF v1.2.8 (released2026-09-15), (18.19.6)-(18.19.9),
(18.20.10), (18.22.7)-(18.22.8), (18.23.7), including lambda>0 and
0<phi<pi. Exact finite formulas, weight, leading coefficient and norms
are available. No affine matching or retained-cost calculation performed.

Completed: author-hosted Koekoek-Swarttouw Section1.7 formulas and the
varying-parameter paper's exact scope inspected. The publisher403 was
resolved by Numdam. Text extraction was readable; screenshot calls did
not supply inspectable images, so no visual verification is claimed.

Main gap remains L030-L032/C032a actual-Xi positivity and C028b's
H_d=o(d). Full Schmeisser payment, odd cancellation and unsmoothed
realization remain unresolved. No creative upper-payment mechanism is
justified by the reference-family nomination alone.

## Exact primary inputs

NIST DLMF v1.2.8, released2026-09-15, retrieved2026-11-18,
[Section18.19, (18.19.6)-(18.19.9)](https://dlmf.nist.gov/18.19),
defines the standard Meixner-Pollaczek polynomials on R for
lambda>0,0<phi<pi. Its weight and standard squared norm are

    w(z)=|Gamma(lambda+i*z)|^2 exp((2*phi-pi)*z),
    H_n=2*pi*Gamma(n+2*lambda)/((2*sin(phi))^(2*lambda)*n!),
    k_n=(2*sin(phi))^n/n!  (leading coefficient).

These are standard norms, not monic or probability-normalized norms.
No boundary parameter value is included. The weight is positive on R.
The source supplies a finite positive H_0; normalization uses that value.
For the all-moments requirement, also inspected
[DLMF (5.11.9)](https://dlmf.nist.gov/5.11#E9):
|Gamma(a+i*y)|~sqrt(2*pi)|y|^(a-1/2)exp(-pi|y|/2)
as y tends to either infinity. For each fixed lambda>0 and interior phi
the resulting exponential tails give all polynomial moments. This is
only the applicability check for the imported orthogonality theorem;
no uniform tail estimate as parameters approach a boundary is asserted.

[DLMF (18.20.10)](https://dlmf.nist.gov/18.20#E10) gives exactly

    P_n^(lambda)(z;phi)=(2*lambda)_n*exp(i*n*phi)/n!
        * 2F1(-n,lambda+i*z;2*lambda;1-exp(-2*i*phi)).

It terminates at n. Thus exact finite coefficients are available without
a fixed-parameter asymptotic. No top-three or top-five coefficients were
extracted in this review. The rising-factorial notation is the source's.

Roelof Koekoek and Rene F. Swarttouw, *The Askey-scheme of hypergeometric
orthogonal polynomials and its q-analogue*, author-hosted
[as98.pdf, Section1.7, p37, (1.7.1)-(1.7.4)](https://tudelft.roelofkoekoek.nl/documents/as98.pdf),
read in full for those four formulas, supplies the same definition and
orthogonality. Its explicitly monic p_n obeys

    z*p_n=p_(n+1)-(n+lambda)*cot(phi)*p_n
                +n*(n+2*lambda-1)/(4*sin(phi)^2)*p_(n-1),
    P_n^(lambda)=(2*sin(phi))^n*p_n/n!.

The n=0 term involving p_(-1) is zero. This fixes the diagonal sign and
the normalization independently of model memory. DLMF (18.22.7)-(18.22.8)
cross-checks the standard recurrence. The report's generating function
(1.7.11), p38, agrees with [DLMF (18.23.7)](https://dlmf.nist.gov/18.23#E7),
whose stated domain is |t|<1. It is optional; the finite formula or
recurrence suffices. No new proof of these classical identities is needed.

The proposed affine family is now specified by the target definition

    q_n(x)=sigma^n*n!/(2*sin(phi))^n
                         *P_n^(lambda)((x-m)/sigma;phi).

Use the pushforward under x=m+sigma*z of w(z)dz/H_0. The later
specialization must check all affine/norm factors, including sigma<0.
Pushforward positivity is retained under reflection; a density formula
would use an absolute Jacobian. One parameter tuple is common to all
0<=n<=d, although it may vary with d. No uniform asymptotic theorem is
being applied when lambda_d or phi_d varies. Endpoints lambda=0 or
phi=0,pi and sigma=0 remain excluded even for limiting sequences.

## Stronger-result comparison

Jun Wang, Weiyuan Qiu and Roderick Wong, *Uniform asymptotics for
Meixner-Pollaczek polynomials with varying parameters*, C.R.Acad.Sci.Paris,
Ser.I349(2011),1031-1035,
[doi:10.1016/j.crma.2011.08.020, Numdam PDF](https://www.numdam.org/item/10.1016/j.crma.2011.08.020.pdf).
Inspected abstract, parameter setup pp1031-1032 and Theorem4 pp1034-1035,
including its rectangle/interior and exterior cases. It treats
lambda_n=(n+1/2)*A for constant A>0 with angle phi fixed in (0,pi),
and gives spatially uniform asymptotic expansions using parabolic
cylinder functions inside the specified rectangle and elementary
functions outside. It does not state uniformity for arbitrary A_d,
phi_d or boundary approaches, or a fixed-P_d Schmeisser optimization.
The introductory printed weight uses the opposite exponential sign
from DLMF and its displayed orthogonality has a different constant;
these formulas are not imported or silently corrected. Detailed proofs
are deferred by the authors. Only its stated scope is used as contrast;
none of its asymptotics is an essential mathematical input here.

The Koekoek-Swarttouw Section2.7 limits (2.7.1)-(2.7.2), p56, were
also inspected: Laguerre arises in a small-angle rescaling and Hermite
in a large-lambda rescaling. These fixed-degree limits do not establish
an obstruction for the proposed joint degree/parameter problem. They
are a reason to retain boundary cases in the test, not to transfer
C028j or C028a's stops to the interior family without calculation.

Reuse Schmeisser2002 Theorem1/Corollary1, pp205-207, definitions
pp203-204 and complete relevant proof pp211-214 already assessed in
C028a/source-notes1503. No reproof or new source search of that interface
is needed. It bounds actual total imaginary height by the full real
coefficient statistic. A large statistic or retained-cost floor is
never a lower bound on actual heights.

## Discovery, duplicates and decision

Queries included: `Meixner Pollaczek polynomials orthogonality lambda phi
recurrence leading coefficient DLMF`; `"Meixner-Pollaczek" "prescribed"
coefficients zeros`; `"Meixner-Pollaczek" "leading coefficients" zeros`;
`"Meixner-Pollaczek" "prescribed coefficients"`; `"Meixner-Pollaczek"
"Schmeisser" "zeros"`; `"Jensen polynomials" "Meixner-Pollaczek"
"reference"`; `"Meixner-Pollaczek" "coefficient matching"`.
No inspected theorem supplies the exact actual-coefficient cancellation
or the proposed retained cost. This bounded search is not novelty proof.
Generalized/associated-family, multiple-orthogonality and interlacing
search hits remain unread leads, not inputs or claims about this target.
Secondary frontier pages were not relied on. The named earlier Romik
assessments are reused for their fixed-parameter flow scope.

C028j stops the affine Laguerre family at its positivity boundary.
C028c stops a Hermite-prefix reference with terminal changes; C028h/i
address companion norms and one shear. None states a theorem for this
common-variable-parameter reference. L530 and L955's recorded stops
concern propagation of other polynomials; this test expands unchanged
C028a P_d and claims no propagation theorem. The source recurrence
changes parameters throughout the basis, unlike a terminal-diagonal-only
change already absorbed by Schmeisser. No exact redundancy was found
in the inspected statements; no advantage or feasibility is proved.

Decision: SPECIALIZE for one finite matching/retained-cost test, with
separate next-turn approval. Classical input formulas are imports;
only their actual-P_d matching and necessary cost diagnostic need work.
Stop on eventual infeasibility or a uniform positive liminf of
B_d/d^2 over all feasible choices; otherwise require an explicit
unbounded feasible sequence with B_d/d^2 tending to zero, or record
inconclusiveness. A vanishing retained part leaves the full sum unpaid.
No parameter sweep or infinite expansion of Xi is authorized.

Mathlib: full matching coverage for the variable-parameter construction
and cost diagnostic was not checked and is unknown. No absence claim.
The review removes an essential source gap locally; it establishes no
new mathematical bound beyond the sources and no progress on RH signs.
