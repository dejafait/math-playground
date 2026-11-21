# Common polynomial commutant — source comparison1284

Literature-only step. Main gap: L030-L032/C032a actual-Xi Q>=0 in
every degree. The fixed intermediate question is whether one real
polynomial differential expression of degree at most two can commute
with all four C032f(1)-(3) scalar Hankel components. A successful
joint realization might support an auxiliary relative-output test;
delta, source norm, transport, signing and all-degree assembly remain
independent gaps. No theta differential identity is tested here.

Checkpoint before documentation completion: primary statements and
essential proof/domain passages below have been read. Coverage for a
necessary compact-core rejection test is available; coverage for an
automatic common self-adjoint realization is not. The mathematical
application is deferred. Existing proofs/scripts are preserved.

## Sources, versions and exact coverage

**Yafaev.** D. R. Yafaev, *A commutator method for the diagonalization
of Hankel operators*, Functional Analysis and Its Applications 44
(2010), 295-306, DOI
[10.1007/s10688-010-0040-z](https://doi.org/10.1007/s10688-010-0040-z).
The theorem numbering/page references used here are from the inspected
[arXiv:1009.1391v1](https://arxiv.org/pdf/1009.1391v1), 7 September
2010, not an assertion that the publisher pagination was inspected.
Read (1.6), Section2.1/Theorem2.1 and its complete calculation,
pp2-4; Section2.2, pp4-5; the domain discussion Section3.1/(3.3),
pp5-6; Section4.1's logarithmic transformation and essential
self-adjointness case, p8; and Section5.1, pp12-13, through
Propositions5.1-5.2 and their regular-boundary convention.

The expression is

    L=-(d/dx)((x^2+gamma*x)d/dx)+alpha*x^2+beta*x,
    alpha>=0, gamma>=0, beta real.

For a C2 Hankel kernel k, Theorem2.1 assumes

    -(x+gamma)k''(x)-2k'(x)+(alpha*x+beta)k(x)=0.  (2.3)

Its conditions on a C2 input f are, in the source's notation,

    lim(y->0) (y^2+gamma*y)f(y)=0,
    lim(y->0) (y^2+gamma*y)f'(y)=0,               (2.1)
    lim(y->infinity) k'(x+y)(y^2+gamma*y)f(y)=0,
    lim(y->infinity) k(x+y)(y^2+gamma*y)f'(y)=0  (2.2)

for every x>=0, with the defining integrals/differentiations meaningful.
The calculation before the theorem gives the commutator kernel as
(x-y) times the left side of (2.3) at x+y. The theorem itself states
a sufficient differential-expression commutation condition; do not
call it a general self-adjoint domain theorem or a classification of
all polynomial coefficients. It does not include a purely linear
leading coefficient as stated.

Section2.2 uses additional asymptotics to remove the second independent
ODE solution in (2.8), and uses a self-adjoint realization and spectral
completeness to obtain a spectral transform. It does not infer a
unitary scalar representation merely from a compact-core equality.
In Section3.1, p=x^2+2x on C_c^infinity is explicitly not essentially
self-adjoint: defect indices (1,1). The selected regular extension
requires f in H2_loc, f,Lf in L2, a finite limit of f at zero and
f'(x)=o(x^(-1/2)). Section5.1 retains those endpoint conditions for
the stated regular Whittaker/MacDonald kernels. In contrast,
Section4.1 treats p=x^2 and alpha=1/4: the logarithmic unitary
transformation yields a whole-line Schrödinger operator, and the
source proves essential self-adjointness for that case. Neither
conclusion is a theorem for every nominated polynomial p,q.

**Blower.** Gordon Blower, *Hankel operators that commute with
second-order differential operators*, Journal of Mathematical Analysis
and Applications 342 (2008), 601-614, DOI
[10.1016/j.jmaa.2007.12.028](https://doi.org/10.1016/j.jmaa.2007.12.028).
Use the inspected [arXiv:0712.1013v1](https://arxiv.org/pdf/0712.1013v1),
6 December2007 (manuscript dated7 October2007), printed pp3-6:
Theorem2.1, full proof(2.3)-(2.5), Lemma2.2 and its proof, the
Friedrichs remark, Lemma3.1/Proposition3.2 and proofs. The
[primary HTML](https://arxiv.org/html/0712.1013v1) agrees on the
load-bearing formulas. Also inspected Examples3.3 Q(i)-(v), pp6-7,
to check that the linear-leading-coefficient case is actually included.
No special-function classification is needed as a theorem input.

In source notation Lf=-(a f')'+bf. Theorem2.1 assumes a(0)=0,
a'''=A a', a sum-variable quotient alpha=(a'(x)-a'(y))/(a(x)-a(y)),
and a sum-variable quotient beta=(b(x)-b(y))/(a(x)-a(y)). The kernel
ODE phi''+alpha phi'-beta phi=0 gives commutation on C_c^infinity.
Crucially the proof displays the identity

    (L Gamma-Gamma L)f(x)
      =[phi(x+y)a(y)f'(y)-phi'(x+y)a(y)f(y)]_0^infinity
       + integral_0^infinity Phi(x,y)f(y)dy,                 (2.4)
    Phi(x,y)=(a(y)-a(x))phi''(x+y)
              +(a'(y)-a'(x))phi'(x+y)
              -(b(y)-b(x))phi(x+y).                       (2.3)

The proof explicitly states the iff condition Phi=0 on that core.
Compact support inside the open half-line disposes of both endpoints;
a(0)=0 alone would not dispose of an arbitrary infinite-end bracket.
The necessity statement is used in this compact-core sense, with
ordinary smooth kernels and the source's integration/differentiation
requirements, not as a claim about every possible closed extension.

Lemma3.1/Proposition3.2 explicitly treat

    a(x)=q2*x^2+q1*x+q0,  b(x)=b2*x^2+b1*x+b0,
    -phi''(u)-2*q2/(q2*u+q1)*phi'(u)
        +(b2*u+b1)/(q2*u+q1)*phi(u)=0.                    (3.3)

Here a(0)=0 is retained when invoking Theorem2.1. The coefficient
pair q2,q1 must not both vanish for this divided formula. It is
safer to retain the undivided (2.3)-(2.4) when a quotient could be
undefined. The constant-b case can be handled by (2.3)-(2.4), without
invoking Lemma2.2's nonconstant-b hypothesis. Examples Q(iv)-(v)
expressly include q2=0 and q1 nonzero, including the Airy case.
Thus no limiting argument from Yafaev's monic quadratic is necessary.
Do not copy the source's later translation/rescaling of u as a change
of the fixed notebook kernels or their half-line domain.

The Friedrichs remark assumes a>=0 and b bounded below to assert
existence of an extension. It does not assert invariance of that
extension's domain under Gamma or strong commutation, and is not
blanket coverage when the lower bound on b is absent. The introductory
self-adjoint setting does not justify assuming the notebook scalar c
is real; the necessary identity may be tested first on the two real
a_sigma kernels. A rejection already there would reject a common
operator for all four. Any use of the b_sigma kernels must retain
complex scalars and justify the required linear identity, without
importing an unverified self-adjointness assertion for them.

## Applicability plan and stopping boundary

The notation match is source a=p and b=q, not C032f's a_sigma,b_sigma.
C032f(1)-(5), audit1282, and C032e's full-kernel conventions are the
local inputs. C032e gives holomorphic Psi near every positive real
point; C032f supplies the bounded Hankel realizations. On a compact
input support the test needs local smoothness, rather than a new
global derivative-tail estimate. Checking the formal kernel identity
does not require first constructing a spectral realization. A later
research step must justify this applicability explicitly, retain the
unchanged common p,q, include the linear-p and constant-q cases, and
test the undivided necessary identity exactly for the original kernels.

No theta derivative has been substituted in the imported identities,
no coefficient conditions have been solved, and no exclusion or
compatible p,q is claimed in this turn. A contradiction at the necessary
core test would rule out this fixed class; a formal solution would
leave domain invariance, self-adjoint realization, spectral multiplicity,
relative spectral bounds and the full source metric unpaid. Park
automatic spectral transfer now; do not require an unneeded positive
domain theorem before a possible necessary-condition rejection test.

## Search, duplicates and qualifications

Queries: `Yafaev A commutator method for the diagonalization of Hankel
operators 2010 arxiv`; `Hankel operators commute second order
differential operator quadratic polynomial coefficients necessary kernel
condition linear p`; `Hankel operators commuting differential operators
classification Blower quadratic Yafaev`. No failed search establishes
novelty, and no source asserts the fixed four-theta-kernel conclusion.

Targeted local searches used the title, arXiv identifiers, common
differential commutant and Sturm-Liouville terminology. A follow-up
author/identifier search located existing Blower comparisons in
`drafts/literature/2026-11-12-finite-cosine-displacement-source-notes-675.md`
(Blower paragraph) and
`drafts/literature/2026-11-13-six-pair-audit-source-notes-677.md`
(Blower paragraph). Reuse their Theorem2.1/core-boundary assessment.
They concern finite cosine boundary contrasts, not the fixed common
theta polynomial test. Nomination1283's no-matching-assessment statement
is not a claim that Blower was absent from the notebook. The new
essential read is the polynomial/linear scope and precise comparison
to Yafaev, not a newly discovered general commutator theorem.

Reuse completed1283 for the stopped unweighted scalar-symbol shortcut;
preserve stops1266/1268/1272/1273/1276/1278 and the31October stop.
No pointwise ratio, corona or boundary-cloud witness is restarted.
All sources were accessible as primary text/PDF. Screenshot retrieval
did not provide readable images; no disputed OCR sign supports a new
calculation, and Blower's exact formulas were checked in primary HTML.
Mathlib coverage of the full commutant theorem is unchecked; this is
not evidence of absence. No cross-notebook input or RH candidate.

## Completed decision

Source coverage advances locally: a precise imported necessary-core
test includes the entire nominated polynomial class, including linear
p, without asserting the missing joint spectral theorem. This is
KNOWN_IMPORTED literature progress, not a theta result or mathematics
beyond the inspected sources. A separate ready SPECIALIZE continuation
is prepared for the exact fixed-class test and awaits the supervisor's
separate approval. A central creative attempt remains blocked by the
missing independently signed actual-Xi interface; the finite
specialization is not relabeled creative to meet scheduling targets.
