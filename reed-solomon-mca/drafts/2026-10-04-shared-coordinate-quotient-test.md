# Shared-coordinate quotient of the saved triple

Date: 2026-10-04. One mathematical attempt on the unchanged actual-pencil
COVERED_TARGET in the [ready SPECIALIZE assessment](literature/2026-10-03-nonpersistent-resultant-equality.md).
The assessment and its standard resultant, squarefree and exact-field
ingredients are reused; no additional source review is needed.

## Gap, intermediate target and stopping test

The pinned four-omission count remains between eleven and sixteen, with
fifteen allowed. The saved triple has four-error supports
A0={1,8,12,18}, A1={1,8,22,27}, A2={1,33,47,50} at parameters 0,1,2.
Its compulsory polynomial zero-syndrome kernel made every previous fourth
determinant vanish. This step removes that kernel before testing full
weights. It is a different branch of the same covered actual-pencil
target, rather than another one-dimensional determinant-root sample.

Continue if the quotient produces genuine candidates passing L010/L014,
or a restriction valid over the full extension field. An equality witness
would decide unsafety for this pinned cell. A uniform restriction on this
triple would narrow the remaining support geometry. If neither occurs,
record the tested branch and change mechanism within the exploration
budget. Arbitrary support triples, the global fifteen bound and July
correspondence remain unresolved.

## Saved unfinished reasoning

Let U=A0 union A1 union A2 and let c be the degree-seven codeword
Q(X)=product_(x in H minus U)(X-x), evaluated on H. By the minimum
weight nine and dimension-one shortening on U, the relation between
the three errors is -e0+2e1-e2=lambda*c. Full weights at coordinates
unique to a support require lambda nonzero; rescale all moments to
lambda=1. Write e0(1)=p, e1(1)=q, e0(8)=z. The remaining weights are

    e0(12)=-c12, e0(18)=-c18;
    e1(8)=(z+c8)/2, e1(22)=c22/2, e1(27)=c27/2;
    e2(1)=-p+2q-c1, e2(33)=-c33, e2(47)=-c47, e2(50)=-c50.

Thus the full-weight triple is exactly the three-parameter family
with p*q*z*(z+c8)*(-p+2q-c1) nonzero. Let vx=(x,...,x^8).
Its syndrome at t is

    s(t)=(p+t*(q-p))*v1 + (1-t/2)*z*v8 + h0+t*h1,
    h0=-c12*v12-c18*v18,
    h1=c8*v8/2+c12*v12+c18*v18+c22*v22/2+c27*v27/2.

For a fourth support K, apply its four recurrence functionals F_K.
Outside t=0,1,2, introduce r=p+t*(q-p), w=(1-t/2)*z.
Membership is the four-by-three system

    F_K(v1)*r + F_K(v8)*w + F_K(h0+t*h1)=0.

The first two columns are constant. Their rank is the number of
coordinates in {1,8} absent from K: F_K(vx)=f_K(x)*(x,...,x^4).
Projecting the last column to their cokernel gives only affine equations
in t. Their common gcd either excludes K, specifies one base-field t,
or vanishes identically. This replaces the blind four-by-four determinant
by smaller minors while retaining arbitrary extension-field p,q,z,t.
Universal branches and full fourth weights must still be treated, and
no bound or retained candidate is asserted before the calculation.

## Mathlib

Full quotient and full-weight triple classification: **not checked**.
Supporting resultant product and specialization coverage is **present**
in the previously read [Resultant.Basic](https://github.com/leanprover-community/mathlib4/blob/300d0e535721bc098547106fc297d8ba2a63f6bb/Mathlib/RingTheory/Polynomial/Resultant/Basic.lean),
including `Polynomial.resultant_prod_left` and
`Polynomial.resultant_map_map`. These do not match the quotient target.
Supporting shortening, kernel and recurrence coverage elsewhere is
**not checked**. No new library lookup or Lean verification is claimed.

## Completed quotient test

[L016](../lemmas/L016-shared-coordinate-triple-quotient.md) gives the
full normalization, quotient proof and exact-certificate qualifications.
The [script](../scripts/coefficient-feasibility/shared_quotient.py) exhausts
all 1817 other fourth supports; [the certificate](../scripts/coefficient-feasibility/shared-quotient-result.json)
retains their equations and independently recomputed smaller-minor gcds.
The result is 1610 inconsistent systems, 190 isolated at original
parameters, three forcing the forbidden z=0, thirteen admissible isolated
systems and one universal system. All nonoriginal isolated systems have
four nonzero fixed weights. Every solvable infinity system is tested
before any full-weight rejection, leaving only the universal support.
Thus lower-weight parameters are not silently lost in the filtering.

The thirteen isolated constraints have distinct z-values except three
at z=11. Those three lie on r=88+67t, whose value at 2 equals c1=28;
any two would cancel the third error's required weight at 1. Hence a
full-triple pencil satisfies at most one isolated constraint. The universal
support {12,18,22,27} contributes at most one projective parameter,
t=2z/(z-c8), with its infinity case retained when z=c8=72. Including
the three prescribed parameters, this fixed class has at most five sparse
parameters over every extension. The numerical classification, rather
than sampling input weights, is the finite dependence of that bound.

The full-triple pencil p=5,q=85,z=11 attains five at {0,1,2,6,81}.
Its actual moments and locator, original event on all 2517 supports in
two charts, affine recurrences, complete fourth-power/equality conditions
and exact F_(97^20) root checks all agree. All five bad parameters are
already in F_97; lower weights are excluded. The normalized resultant
has degree 64 and fails the fourth-power condition. Five is below the
existing eleven-count witness, so the main interval remains 11/q–16/q.

Outcome: NEGATIVE; STEP_KIND: RESEARCH; STEP_CLASSIFICATION: REPRODUCTION.
This is an informative exclusion of the saved branch using the covered
moment/MDS framework and imported algebraic audit tools. No certified
originality or progress beyond the checked literature is claimed. Stop
the common-coordinate triple as a sixteen-count generator. Other triples,
arbitrary extension inputs and the global fifteen bound remain open;
July/four-block and other historical stops remain preserved.

The next direction within the same ready actual-pencil target is the
previously unsearched quadratic/quartic fourth-support roots for the saved
disjoint triple. No calculation on that next branch is performed here.
Consecutive uninformative mathematical turns used: zero after this
informative negative; resultant-target mathematical attempts: five.
