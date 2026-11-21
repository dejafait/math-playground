# Residual-quartic count attempt1473

Reuse the supplied, unchanged EXPLORE assessment1468/review1469 for the
exact fixed-sextic (2,4) target. This is one established-route mathematical
attempt, not a new literature assessment. C020n/p/q and the relevant
1470--1472 failure/working passages were inspected; the old floating
collision scan is inconclusive and will not be repeated.

Main gap: L030--L032/C032a actual-Xi all-degree positivity and the unpaid
unshifted Jensen exceptional-root deficit. Intermediate target: decide
the residual quartic H on C020q's exact collision domain. A witness
would stop a finite partial-count shortcut; an exclusion would remove
this collision family only. Actual-factor correspondence, paid loss,
all degrees, signs, initialization and overlap remain independent.

Inputs: C020q, with 1/4<=t<=5/18, k!=0, l^2>4k, Delta<0,
M=4*N_C*Delta-N_B^2>0, B=N_B/Delta and C=N_C/Delta. The input is
k^-2*(1+l*x+k*x^2)^2*(x^2+B*x+C); its image is k^-2*x^2*H.
C020p supplies the checked-in proof of the Walsh degree-six
specialization, not a composition theorem. C020n is a quartic contrast;
C020o's inverse-positivity obstruction stays in force. C020p/q are
unaudited and their explicit formulas must be checked where used.

Bounded test: seek an exact root-count/sign condition for H on that
domain, retaining H(0)=0 and multiple residual roots. Continue only
with a certified witness, family exclusion, or a new discriminating
condition; a failed identity or sample does not decide the count.
A two-real-root residual needs a separate rational perturbation
certificate before it gives (2,4); a root-free residual gives it directly.
No global deformation or factor-composition principle is assumed.

Work in progress: examine exact quartic criteria and the collision
equations for a sign representation. Save complete algebraic evidence
under scripts/quartic-differential/ if a calculation is used. There is
no count conclusion at this checkpoint.

## Completion

The exact calculation is saved in
`scripts/quartic-differential/sector-sextic-residual-invariants-1473.py`
and its full adjacent JSON certificate. It uses standard-library
rational arithmetic; no packages, external sources or floating root
samples were used. The prior source assessment remains unchanged.

Write Delta*H=a*x^4+b*x^3+c*x^2+d*x+e, with the complete coefficient
array obtained directly by applying 1+D+t*D^2 to C020q's cleared
input. The quartic invariants used are I=12ae-3bd+c^2 and
J=72ace+9bcd-27ad^2-27b^2e-2c^3. The discriminant expression
(4I^3-J^2)/27 factors exactly as k^4*(l^2-4k)*F(l,k,t).
F has 1,898 nonzero rational coefficients. The full invariant and
factor arrays are in the certificate, not truncated previews.

The attempted sufficient certificate used L=t*l,
S=t^2*(l^2-4k)>0, and z=36*t-9 in [0,1]. After substitution,
t^20*F is a polynomial in L,S,z. For each power of S its z-polynomial
was expressed in the Bernstein basis on [0,1], leaving coefficients
that are univariate polynomials in unrestricted L. Nonnegativity of
every such coefficient polynomial would suffice for nonnegativity of
F; it is not necessary. The Bernstein reconstruction is checked as
a complete exact polynomial identity.

This particular certificate fails: seven of its 197 coefficient
polynomials are negative at L=0. In particular the coefficient of
S^17 at the endpoint z=1 is -5036661/128. This value was checked
independently by extracting the l^0*k^17 terms of the original F
and substituting k=-S/(4*t^2), t=5/18, with the t^20 prefactor.
The complete seven failing values and every algebra-check flag were
inspected with the shared JSON inspector. All five algebra checks
pass; seven sign conditions for the proposed certificate fail.

These negative coefficients are not negative values of F. The
representation also does not use the full Delta<0 and M>0 constraints.
Thus it does not prove a negative discriminant anywhere admissible,
and does not exclude other positivity representations. Even a strictly
positive quartic discriminant would still require distinguishing four
real roots from zero real roots; neither case nor any discriminant-zero
or H(0)=0 boundary was resolved. No witness, count theorem or new lemma
is claimed. Full matching Mathlib coverage is unchecked.

Outcome EXPLORATION: this is the second mathematical exploration since
the informative fourfold-family stop1471. Reassess the collision method
instead of repeating an expanded-discriminant coefficient test. The
concrete continuation within the unchanged approved target is a direct
sign comparison: use R=(1+l*x+k*x^2)^2 and J=T R, and test whether
ordered real zeros of J supply two negative H values separated by a
positive H value. Such a strict pattern, with the positive leading
coefficient, would force four distinct real roots of H. The product-rule
evaluation of T(RQ) at J zeros must be derived and its signs certified;
shared zeros, repeated J roots, H(0)=0 and all equality cases remain
part of the test. A counterexample to this sufficient sign pattern
would reject that comparison, not the sextic target. No interlacing,
global deformation or composition theorem is assumed.

This is a materially different sign-evaluation test from the failed
global coefficient representation; its success is unestablished.
The main RH gap and the independent actual-factor assumptions remain.
There is still no justified central creative nomination without a
testable actual-data loss mechanism and actual-factor applicability.
