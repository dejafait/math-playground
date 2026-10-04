# Actual affine moments: coefficient feasibility audit

Date: 2026-10-04. One mathematical formulation and audit of the exact
saved COVERED_TARGET in
[the SPECIALIZE assessment](literature/2026-10-03-nonpersistent-resultant-equality.md).
No new literature review is needed for its unchanged hypotheses.

## Gap, relevance and stopping test

For the pinned RS[F_(97^20),H,8] four-omission cell, the proved global
interval is 10/q–16/q and the allowable count is fifteen. The remaining
model-specific question is existence of L010's sixteen-count equality.
The intermediate target is a coefficient system on the actual sixteen
affine moment coefficients, with every splitting, simplicity and
Hankel-nonvanishing condition retained. Its possible use is a supplied
candidate audit or a subsequent structured feasibility test. Deciding
the system, other radius cells and the parked July correspondence remain
separate unresolved steps.

L010 already proves the incidence criterion. L013 stops the prescribed
two-block generator; the 512-pencil search is not a general exclusion.
The full-orbit and source-access failures are preserved. A mere fourth
power, an arbitrary balanced incidence pattern or a failed sample is not
an advance. Continue if this step supplies an exact implementable test or
a useful compatibility restriction; if it supplies only an equivalent
description, record that limitation and do not claim a better bound.

## Reasoning saved before the audit

Write s_j(T)=u_j+T*v_j, j=1,...,8, and obtain L and D from L010's
signed minors. Put R=product_(x in H)L(T,x), c=[T^64]R, and take P
monic of degree sixteen. The prospective direct system is R=c*P^4,
c!=0, all coordinate quartics squarefree, gcd(P,P'*D)=1, and
P dividing T^(97^20)-T. The last condition must be checked in the
specified field; no prime-subfield restriction on u,v is intended.

The top sixteen coefficients of R/c determine the sixteen lower
coefficients of P recursively, dividing only by 4. The remaining
forty-eight coefficients are residual equations. Clearing denominators
can sharply increase symbolic degree, so a short list of equations need
not be an easy solver.

For a supplied bivariate candidate C(T,X)=sum_(j,h=0)^4 C_(j,h)T^h X^j,
the four recurrence identities have degrees at most five in T. Their
twenty-four scalar coefficients give a 24-by-16 matrix N(C) on (u,v):
sum_j C_(j,h)u_(i+j)+C_(j,h-1)v_(i+j)=0 for i=1,...,4 and h=0,...,5,
with out-of-range C coefficients zero. This may detect fabricated
quartics which pass the power/incidence checks but cannot arise from
affine moments. Its sufficiency requires auditing the primitive
coefficient and nonzero-minor conditions, not just rank(N)<16.

Planned controls are existing actual moment pencils, a balanced locator
C=T^4-X^4 with product (T^16-1)^4, and a genuine constant four-support
locator whose moment-compatible line has persistent coordinate roots.
These are algebraic controls, not an equality witness or a search over
all extension-field inputs. No mathematical conclusion is asserted yet.

## Completed formulation and audit

[L014](../lemmas/L014-exact-coefficient-feasibility-and-affine-compatibility.md)
gives a necessary and sufficient direct coefficient system for the
remaining nonpersistent equality case. Its actual moments have sixteen
unknown coefficients, P has sixteen lower coefficients, and the scalar
c supplies one more: 33 unknowns before auxiliary variables for the open
conditions. The 65 product-coefficient equations determine c and the
sixteen P coefficients successively, leaving 48 residual checks. Coordinate
squarefreeness, gcd(P,P'*D)=1 and the sixteen Frobenius-remainder equations
must still hold. No independence or useful codimension is proved.

An alternative uses 25 bivariate locator coefficients. Its product
equations have degree sixteen in those coefficients, rather than degree
64 in the moments. The inverse 24-by-16 matrix gives bilinear equations
with a moment witness. Crucially the witness must have a nonzero actual
Hankel determinant. The other gates make the candidate coefficient
vector primitive in F[T] and of T-degree four; these facts force its
proportionality to the actual minors to be a nonzero constant. Rank
deficiency alone is not asserted sufficient. This gives an implementable
candidate audit, rather than a solved feasibility system.

Eliminating P is not a free simplification: after clearing powers of c,
the last residual can have degree as high as 4096 in the moment variables.
An expanded symbolic solve may therefore be much harder than the small
variable count suggests. The literal polynomial form retains c!=0;
otherwise clearing denominators creates inadmissible solutions.

The command `python3 scripts/coefficient-feasibility/check.py` saves
[the exact control results](../scripts/coefficient-feasibility/result.json):

| Control | Compatibility rank | Result |
| --- | ---: | --- |
| Existing two-block pencil | 15 | One-dimensional kernel recovers actual minors; fourth-power residuals fail |
| Specified dense moments | 15 | Kernel recovers actual minors; resultant degree is 63 |
| Two disjoint four-error points | 15 | Kernel recovers actual minors; resultant degree is 63 |
| Fixed-four-support pencil | 8 | Persistent coordinate roots exclude it despite compatible moments |
| Fabricated product_(alpha in {1,8,64,27})(T-alpha*X) | 16 | All algebraic equality gates and sixteen distinct supports pass, but no affine moments exist |

The last rank rejection also has an exact short proof in L014 valid over
every extension; it is an audit of the previously excluded full-orbit
mechanism, not a new obstruction to arbitrary pencils. The control
R=2*P^4 accepts c=2 although 2 is not a fourth power in F_97. The
squarefree polynomial P=T^16-5 passes the power test but has no roots
in F_(97^20), as checked by the modular Frobenius gcd. These separate
the scalar and exact-field gates from the power identity. The cleared
denominator equations are checked against the unnormalized products.

## Outcome and continuation decision

Outcome: EXPLORATION. This fulfills the formulation/audit target but
gives no equality witness, general obstruction or new count restriction.
The global interval is still 10/q–16/q against an allowable fifteen.
The result reproduces the local L010 criterion with imported standard
algebra; no progress beyond the checked literature is claimed. A full
matching Mathlib theorem is not checked; supporting resultant coverage
and its exact source/declaration links are recorded in L014.

The implementable compatibility and residual gates justify one bounded
feasibility test using the preapproved actual-moment target. Constrain
actual candidates before testing; another unstructured prime-subfield
sample would not decide extension-field feasibility. Failure to obtain a
witness or a useful arbitrary-coefficient restriction must remain an
exploration result. Consecutive uninformative mathematical turns used:
one; total mathematical attempts on the resultant mechanism: two. The
two-block, orbit and July-source stops remain intact. No complete
grand-challenge candidate appeared and STATUS remains IN_PROGRESS.
