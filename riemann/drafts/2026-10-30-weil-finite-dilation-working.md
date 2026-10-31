# Complete Weil finite-dilation test — working record

2026-10-30. Gate: the pre-existing EXPLORE assessment
`drafts/literature/2026-10-30-weil-finite-dilation-remainder-test.md`.
One mathematical attempt; source coverage is reused. No withdrawn
Pohozaev identity or formal fractional-order limit is available.

The main gap is actual-Xi all-degree positivity. The intermediate
target is a justified one-sided weak-dilation identity retaining a
signed arithmetic remainder that could control endpoint flux by a
small positive eigenvalue. Full-Weil realization, source collar laws,
multiple branches and all-support/Xi transfer remain independent.

Read L512's complete form and retained source hypotheses, L513's
trace normalization and regularity statement, L514's fixed-interface
domain theorem, and L515's bounded-data assembly. Reused the completed
dilation source comparison and its withdrawn-import and automatic
support-propagation stops. There is no existing finite-dilation
arithmetic-remainder result in that scoped comparison. Mathlib is
unchecked; no novelty beyond the assessed search is certified.

Initial test: for zero-extended real u on (-a,a), use
U_r u(x)=sqrt(r)u(rx), r>1. Work with exact weak pairings and exact
quadratic finite differences before taking any derivative. Inward
dilation should preserve the logarithmic form domain, while each
prime autocorrelation is evaluated at r log(n). The bounded pole is
smooth in r, but differentiating those correlations is not supplied
by continuity or by the fixed-model trace theorem alone.

The intended discriminant is a rigorously normalized boundary defect
and a signed remainder sufficient for flux<=C lambda, uniformly as
lambda tends to zero on the stated bounded radius range. A formal
H1 argument, an absolute bound only, or the old support derivative
with no arithmetic criterion fails this version. Do not promote the
finite-difference observations to a theorem until the required limit
and its boundary contribution have actually been justified.

## Partial calculation saved before completion

For b the complete real bilinear form, u_r=U_r u and
v_r=U_(1/r)u, the weak equation and unitarity suggest the exact
identity b(u,v_r)-b(u,u_r)=integral_(I_ar minus I_a) F v_r,
where F=-n*u-mu_A*u outside I_a in the common signed-measure
realization. L514 must justify restriction of v_r to the old interval
and collars; treating that restriction as automatically admissible
would leave a domain gap.

The known trace at the right endpoint suggests
F(a+s)=-tau_R sqrt(log(1/s))+o(sqrt(log(1/s))). Its leading
coefficient can be checked directly by integrating
1/[2(s+t)sqrt(log(1/t))]; the finite-measure term is bounded.
With delta=a(r-1), v_r(a+s)=r^(-1/2)u(a-(delta-s)/r).
The collar integral divided by delta should then converge to
-tau_R^2 by domination with sqrt(1+log(1/y)), y=s/delta.
The left collar has the same coefficient. This uses no eigenbranch
derivative or collar resolvent theorem.

Changing variables in the two forms retains the exact multiplier
difference m(xi/r)-m(xi), pole kernel difference
2r cosh(r(x-y)/2)-2cosh((x-y)/2), and signed prime differences
T_(ell/r)+T_(-ell/r)-T_ell-T_(-ell), paired against u_r and u.
If the preceding passages hold, their combined limit yields
a flux=H-P+S, where H is the xi m'(xi) Fourier quadratic form,
P has kernel 2cosh(t/2)+t sinh(t/2), and S is the full prime
finite-difference limit. No individual prime derivative is assumed.

Primary formulas were narrowly checked at paper 67 v1 (2.1),
(3.1)–(3.5), and (9.5); the source identification remains conditional.
DLMF 5.15.8 was checked for the trigamma asymptotic in a sector
away from the negative real axis, sufficient for bounded xi m'(xi)
on the real frequency line. This is an elementary input to the
approved calculation, not a new target or a renewed literature turn.

The remaining sign estimate would have to be S<=P-H+K lambda
with one K independent of lambda. It is not established by the
calculation. A scalar shift commutes with dilation, so the formula
cannot itself manufacture the needed vanishing eigenvalue factor.
All limits and the zero contribution of exactly activating atoms
still need full justification in the canonical write-up.

## Completed bounded attempt

The complete local derivation is now in
`lemmas/L516-complete-weil-weak-dilation-flux-identity.md`.
The proof supplies the part-domain restriction, exterior asymptotic,
integrable collar domination and signed aggregate limit, and retains
every pole/prime term. Exactly activating atoms were bounded at
O(1/log(1/(r-1))) after division by r-1. The formula establishes
no arithmetic inequality at O(lambda) accuracy and has not received
an independent critical audit. The new audit-scope assessment is
REVIEW_REQUIRED; it does not approve this derivation in its own turn.
