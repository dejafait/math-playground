# Lemma 791: fixed central degree-five matching model

## Hypotheses

Use the actual completion of L018, the moment normalization of L021 and
the ordinary coefficients of L776:
G(w)=xi(1/2+sqrt(w)/2)/8=sum a_j w^j. Put
gamma(j)=8*4^j*j!*a_j, R_j=gamma(j)/gamma(0), and
q_k=R_(k+1)^2/(R_k R_(k+2)). The shift is n=0 throughout.
Use L778's audited polynomial evaluator P_0 and its uniform analytic
error on |w|<=1600, including its documented Decimal software contracts.
The numerical evidence remains a computer-assisted informal certificate;
neither the binary nor the arithmetic is formally verified.

Define T=(q_0-1)/(q_1-1), A_J=2q_0/(T-q_0),
B_J=1/[q_0(1+1/A_J)-1], and D=B_J/2. Fix degree d=5.

## Conclusion

These first-stage quantities are defined and positive. There is an exact
positive solution (A,B,C) of

q_k = (A+k)(B+k+1)(C+k)(D+k+1)
      /[(A+k+1)(B+k)(C+k+1)(D+k)], k=0,1,2,

in the rational box defined below. With S=B R_1, the model ratios

F_j=S^j (A)_j(C)_j D^j/[A^j C^j(B)_j(D)_j]

equal R_j for j=0,...,4. The polynomial

p(y)=sum_(j=0)^5 (-1)^j binom(5,j)
                 (A)_j(C)_j D^j/[A^j C^j(B)_j(D)_j] y^j

has five simple positive roots, respectively in
(5.87,5.88), (10.26,10.27), (14.27,14.28), (18.76,18.77),
and (23.63,23.64).

This is a specialization of known matching and validation methods, not
a new sign theorem beyond the sources checked. It gives no matching at
index5, residual multiplier bound, actual Jensen root certificate,
growing-degree estimate, all-degree mixed positivity or RH conclusion.
The finite calculation passed the separate conceptual audit in step478
below, subject to the inherited evaluator and software contracts.

## Proof

**Sources and applicability.** Jonathan Holland,
[arXiv:2608.08682v1](https://arxiv.org/html/2608.08682v1), 9 August2026,
equations (37)–(38),(49)–(52),(66)–(69), Lemma6.2 and its quotient-induction
proof give these definitions and matching identities. Its Lemma6.1 is
eventual in the shift and is not an existence input here. Instead use the
standard Banach fixed-point theorem for a closed real box, and the
intermediate value theorem for polynomial roots. Validated analytic Taylor
evaluation is an established method; see F. Johansson,
[arXiv:1802.07942v1](https://arxiv.org/pdf/1802.07942v1), Sections2/2.1,
pp.2–4, and Section4, pp.7–8. L778 documents the particular elementary
Taylor integrator, its full error bounds and subsequent audit. Only its
polynomial evaluator and uniform analytic error are imported here, not
its zero count or Fredholm norm. The step475 assessment approved this
finite specialization; the sources contain none of these central
parameter enclosures. No general theorem is reproved.

**Actual coefficients.** The inherited certificate is
`scripts/actual-fredholm/fixed-pair-certificate-431.json`. Its exact SHA256
is saved in `scripts/central-jacobi/fixed-model-certificate-476.json`.
The first five `evaluation/coefficients` intervals enclose coefficients
of P_0, not initially coefficients of G. L778 establishes the complex
uniform bound

|G(w)-P_0(w)| <= E_G < 3.141*10^(-48), |w|<=1600.

Cauchy's coefficient estimate, applied to this analytic difference,
therefore gives |a_j-[w^j]P_0|<=E_G/1600^j. Add this symmetric error to
each inherited interval before multiplying by 8*4^j*j!. This preserves
all quadrature, theta, integration, cosh-tail and rounding errors; no
derivative is inferred from a merely real pointwise bound. The complete
five actual coefficient and gamma intervals are recorded under
`actual_a` and `gamma` in the new certificate. Their approximate values
are .4971207781883141, .01148597215757272, .0002469040361406360,
.000004994132888313162, .00000009581343723225929. These decimals orient
the reader; the outward intervals, not those approximations, are inputs.

Directed interval division gives, conservatively,

1.07484394250019421126346157158 < q_0 < 1.07484394250019421126346157162,
1.06274366627144916855311401273 < q_1 < 1.06274366627144916855311401285,
1.05430333113463476927545484495 < q_2 < 1.05430333113463476927545484516.

The first-stage denominator intervals exclude zero. In particular
T-q_0>0, A_J>18.21636467726257, B_J>7.47114748671059 and
3.73557374335529<D<3.73557374335530. The full intervals for every
denominator and parameter appear in `first_stage`/`obligatory_bounds`.
All required positivity tests pass; no eventual-shift assertion was used.

**Exact solution.** Let x_0 be the following exact finite decimals:

A_0=35.6309307137600661975195539113178411836878763333606566614993963425894747837,
B_0=11.5396899408362113695275954198992597350375534869564808109911297157568358833,
C_0=4.05445979673638286096848518914467946155196456913726344707711370176031147267.

Let X=x_0+[-r,r]^3, r=10^(-15). All its coordinates and all rational
denominators in the system are strictly positive. Let F_k(x) be the
right side of the displayed quotient equation minus q_k, and let M be
the exact finite-decimal 3x3 matrix in `preconditioner`. Its approximate
inverse construction proposes a center and matrix only; existence uses
the following rigorous bounds with the actual D and q_k inside their
complete enclosures. If v_k=F_k+q_k, the derivative row is exactly

(v_k/[(A+k)(A+k+1)], -v_k/[(B+k)(B+k+1)],
 v_k/[(C+k)(C+k+1)]).

Interval evaluation throughout X gives

||I-M DF(X)||_infinity < 4.240*10^(-12) < 1,
||M F(x_0)||_infinity < 8.600*10^(-22),
||M F(x_0)||_infinity + r ||I-M DF(X)||_infinity
   < 8.601*10^(-22) < r.

Every entry of the preconditioned derivative, center residual, preconditioned
residual, row norm and self-map bound is stored in `attempts/0`.
For fixed actual data the map H(x)=x-MF(x) thus maps X into itself and
is a strict contraction in the max norm. Banach gives a unique fixed
point there. The bound ||I-M DF(x)||<1 also implies M DF(x) is invertible
at any x in X, hence the square matrix M is invertible. Thus a fixed
point satisfies F(x)=0, not merely MF(x)=0. This proves exact solution
existence and uniqueness within X, not global parameter uniqueness.
Allowing independent enclosures for the correlated q_k and D enlarges
the tested set and is valid. Only one box was tested; no refinement or
second candidate was required. Nine unvalidated Newton steps proposed
x_0 and contribute no mathematical premise.

The model has F_0=R_0=1 and F_1=S/B=R_1. Its consecutive quotient
invariants are exactly the three system expressions. Holland Lemma6.2
(equivalently Lemma2.1) applies since every ratio is positive, proving
F_j=R_j for j<=4. This imports the known finite identity with its
hypotheses verified; it does not extend matching by one index.

**Five simple positive model roots.** Evaluate the polynomial throughout
X and the D interval by its coefficient recurrence

c_0=1,
c_(j+1)=-c_j (5-j)/(j+1) (A+j)(C+j)D/[AC(B+j)(D+j)].

This is precisely equation(69), and its fifth coefficient is nonzero
because every factor except its prescribed sign is positive. All five
disjoint positive intervals in the conclusion have opposite endpoint
signs, respectively (+,-), (-,+), (+,-), (-,+), (+,-). Full outward
endpoint values are in `root_brackets`. Conservative lower bounds for
their endpoint absolute values are, respectively,
(8.28e-5,1.38e-4), (4.83e-5,4.09e-6), (1.79e-5,1.91e-5),
(7.31e-7,6.21e-5), (2.77e-4,5.49e-6).
Each bound holds for all parameter values in X. The intermediate value
theorem gives five distinct positive real roots. Degree exactly5 means
these exhaust all roots with multiplicity and each is simple. No root
count is inferred from an unvalidated plot or an approximate solver.
In particular C-D<1, so the sufficient classical condition C>D+4
does not apply; its failure is harmless because direct brackets supply
the required root certificate. No finite-free simplicity theorem is
needed for this calculation.

**Reproduction and qualifications.** Run
`python3 scripts/central-jacobi/fixed_model_476.py` from this notebook.
It imports only the directed interval arithmetic of the existing script
and reads the inherited audited evaluator certificate. It writes the
full new certificate to the path above and prints actual/required
contraction, self-map and root bounds. The installed runtime is
Python3.15.2, Decimal1.70, libmpdec4.0.1, matching L778's assessed
contracts. Precision is75 significant digits; no precision increase was
needed. Optional python-flint installation failed on PyPI DNS resolution;
no numerical evidence depends on it. This is one fixed finite model,
with all independent RH-level gaps still open.

### Separate conceptual audit, 5 November 2026 — step478

Reused the approved SPECIALIZE assessment
`drafts/literature/2026-11-05-fixed-central-model-audit.md`. This review
checks the existing finite statement only; it does not approve any new
residual or growing-degree calculation. No mathematical defect was found.
The evidence description above was corrected: `attempts/0/derivative`
stores I-M DF, not the raw DF. The raw interval Jacobian is now also
saved in the audit certificate.

**Inherited analytic input and normalization.** L778 defines P_0 by exact
finite integrals and encloses its coefficients using its cell errors.
Its bound (5) holds for the analytic difference G-P_0 throughout the
complex radius1600 disk, including the boundary. Thus Cauchy's formula
on that circle gives precisely E_G/1600^j for the ordinary coefficient
error, in addition to the retained quadrature widths. L018's completion
and L021's even expansion give gamma(j)=j! M_(2j)/(2j)!
=8*4^j*j!*a_j, without a further factorial or radius factor. The audit
checks all five coefficient-error additions and gamma, R and q intervals.
It also checks the inherited source hash against both step476 and the
step433 audit and compares the entire inherited evaluator record to
step433's audited replay. Rebuilding the transcendental integrator is
unnecessary here: its already audited analytic proof and software
contracts remain explicit premises. The new checker does not independently
verify that backend or the imported transcendental values.

**Exact existence and whole-box bounds.** For fixed actual q_k and D the
map is continuously differentiable on an open positive neighborhood of X.
Logarithmic differentiation of its four rational factors gives the
displayed derivative, treating D as constant with respect to (A,B,C).
All denominators stay positive on the full box. The independently
enclosed q_k and D may be correlated in reality; universal enclosure
over their Cartesian product includes those actual values. For x,y in
the convex box, integrating DH along their segment bounds the max-norm
Lipschitz constant by the displayed row bound. Likewise H(x_0)-x_0
equals -MF(x_0), so the self-map estimate applies to every point of X,
not only its center. X is closed and complete. Banach therefore applies.
The strict norm bound makes M DF(x) invertible by the Neumann-series
criterion, which forces the square matrix M invertible. Hence the fixed
point solves the actual system. An exact rational determinant check of
M independently confirms nonvanishing. Quotient induction then applies
to positive R_j and F_j with identical initial values; only j<=4 follows.

**Independent finite arithmetic and roots.** Run
`python3 scripts/central-jacobi/audit_478.py`. The checker uses Python
integer/Fraction arithmetic, rounding outward after each operation to
multiples of 10^(-100): the lower numerator is floor(10^100 l) and
the upper is ceil(10^100 u). This is an exact rational enclosure method,
independent of Decimal's finite-operation implementation. Every saved
coefficient, quotient, first-stage interval, center/preconditioned
residual and preconditioned derivative contains its recomputation;
all saved row/self-map upper bounds dominate the recomputed ones.
The resulting maxima satisfy the same strict bounds
4.240e-12<1 and 8.601e-22<1e-15 stated above.

The checker also forms each polynomial coefficient from the complete
Pochhammer product and evaluates an expanded sum at each of the ten
endpoints, independently of the original recurrence and Horner ordering.
All ten strict signs and all ten stated lower margins hold throughout
the full box and D interval. The fifth coefficient is strictly negative.
Thus the IVT/degree/simplicity reasoning applies to one exact polynomial,
including the one at the exact Banach solution. It does not mix roots
from different parameter choices. A fresh execution of the original
program writes to `scripts/central-jacobi/audit-478/` and exactly matches
the entire original certificate, including runtime fields. All original
source/program/certificate hashes are preserved. The full report is
`scripts/central-jacobi/audit-478/audit-report.json`: PASS, 142 checks,
no failures; all rational interval values and actual/required bounds
are retained there. This validates the finite input under the stated
contracts, not new mathematics beyond the cited methods or a resolution
of any independent Xi-sign gap.

## Mathlib

Full matching-result coverage is unchecked. Supporting named inputs are
Banach's fixed-point theorem, Cauchy's coefficient estimate and the
intermediate value theorem. No claim of absent Mathlib coverage or formal
verification is made.
