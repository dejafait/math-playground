# L131 — No extra rational involution on the actual genus-two quotient

## Hypotheses

Let B be L110's audited smooth proper genus-two curve over Q, with exact
affine equation

    W²=f(T)=11(T²−4)(7+52T−6T²−64T³−25T⁴).

Use its squarefree sextic and full proper model, including the infinity
chart V²=−275 at h=0. An involution means a Q-automorphism of exact order
two. Write h_B for the hyperelliptic involution (T,W)↦(T,−W).

## Conclusion

B has no Q-defined involution other than h_B. Thus the extra-involution
degree-two elliptic-subcover mechanism is unavailable for this Q-model.
This does not determine geometric automorphisms, higher-degree elliptic
covers, Jac(B)'s rank or B(Q), and gives no Beal signature exclusion.

## Proof

### Imported automorphism facts and rational branch points

Import Lercier–Ritzenthaler–Sijsling, *Fast computation of isomorphisms
of hyperelliptic curves and explicit Galois descent*, Open Book Series
1 (2013), 463–486, DOI [10.2140/obs.2013.1.463](https://doi.org/10.2140/obs.2013.1.463),
Sections 2A–2B, pp.465–468, Definition 2.1, Lemma 2.2, equations (1)–(2),
and Section 2E1, p.474. In characteristic zero and genus at least two,
the hyperelliptic involution is central; every Q-automorphism is represented
on the function field by

    T↦(aT+b)/(cT+d),  W↦eW/(cT+d)³,
    M=[a,b;c,d] in GL2(Q), e in Q*, F(M(X,Z))=e²F(X,Z),

where F(X,Z)=Z⁶f(X/Z). Its reduced action preserves the geometric branch
set. The kernel of this action is {1,h_B}. These hypotheses hold by
L110; no scalar normalization or coordinate change over an extension
is used here.

Import Shaska–Völklein, *Elliptic subfields and automorphisms of genus 2
function fields*, [arXiv:math/0107142v1](https://arxiv.org/pdf/math/0107142v1),
19 July 2001, Section 3.1, Lemma 2(a) and both proof cases, p.7.
Over an algebraically closed field of characteristic different from two,
a nontrivial reduced involution has order-two lifts precisely when it
fixes no branch point; if it fixes two, its lifts have order four.
Apply this over Qbar to an asserted Q-involution: base extension retains
its order, so its reduced action fixes no geometric branch point.
This imports the geometric criterion, not a rational-descent conclusion.

Let Q4=7+52T−6T²−64T³−25T⁴. The rational-root theorem exhausts its
possible reduced rational roots as ±m/n with m in {1,7}, n in {1,5,25}.
Here are all exact residuals; none is zero:

| m/n | Q4(−m/n) | Q4(m/n) |
| --- | --- | --- |
| 1 | −12 | −36 |
| 1/5 | −396/125 | 2076/125 |
| 1/25 | 76788/15625 | 28332/3125 |
| 7 | −38724 | −81900 |
| 7/5 | 252/125 | −25452/125 |
| 7/25 | −105924/15625 | 305172/15625 |

The rational branch set is therefore exactly {−2,2}. Infinity is not
a branch value: F(1,0)=−275 is nonzero, consistently with L110's two
unramified geometric infinity points. The complete divisor and residual
certificate is saved at the path below; no bounded-height root search
replaces the rational-root theorem.

### Complete projective parameter family

Suppose σ is an involution different from h_B. Its reduced action m
is nonidentity and of order two, since the kernel is {1,h_B}. It fixes
no branch point by the imported criterion. A Q-defined Mobius map sends
rational branch points to rational branch points, so m exchanges 2 and −2.
For a representative [a,b;c,d] the denominators at these finite images
are nonzero. The two equations are

    2a+b=−4c−2d,       −2a+b=−4c+2d.

They give d=−a and b=−4c. Hence every candidate is

    M(a,c)=[a,−4c;c,−a],    (a:c) in P¹(Q), a²−4c²≠0.

Conversely each nonsingular matrix in this family exchanges the points
and squares to (a²−4c²)I. This establishes completeness before solving
any coefficient equations. Both charts c=1 and c=0 must be included;
no assumption on rational fixed points of m is made.

### Exhaustive full-sextic identity

Write the ascending coefficients of F as

    (f0,...,f6)=(−308,−2288,341,3388,1034,−704,−275).

In the c=1 chart set a=r and expand

    F(rX−4Z,X−rZ)=sum_(j=0)^6 g_j(r) X^j Z^(6−j).

Every coefficient is specified without omission by the finite formula

    g_j(r)=sum_(0≤i≤6, 0≤p≤i, 0≤q≤6−i, p+q=j)
      f_i binom(i,p)(−4)^(i−p) binom(6−i,q)(−1)^(6−i−q)
      r^(p+6−i−q).

Since f0≠0, proportionality to the full F is equivalent to all six
equations E_j=f0*g_j−f_j*g_0=0, j=1,...,6. The exact gcd is r²−4.
For a compact checkable certificate, the first two equations are

    E1=−2799239168−2006749184r+528450560r²+584362240r³
          +48477440r⁴−20668736r⁵−1409408r⁶,
    E2=302573568+323017728r+61843584r²−57243648r³
          −34371744r⁴−5877696r⁵.

The following complete polynomial identity is checked by multiplication:

    U E1 + V E2 = 25169101816320000 (r²−4),
    U=−3239283069−2031198576r−566459916r²,
    V=−30300744744−7927201174r+1684682352r²+135830968r³.

Every E_j is divisible by r²−4: for r=2 or −2 the numerator and
denominator linear forms satisfy N=rD, and F(N,D)=D⁶f(r)=0 identically.
This also follows from the saved exact quotient for each of the six
equations. The displayed Bezout identity supplies the reverse divisibility
for their common gcd. Consequently the only possible rational parameters
are r=±2. Both have determinant 4−r²=0; their entire transformed sextic
is zero. They are singular matrices, not automorphisms or lifts with
zero multiplier.

The remaining projective chart c=0 has representative [1,0;0,−1].
Its full transformed sextic has coefficients

    (−308,2288,341,−3388,1034,704,−275).

The constant coefficient forces multiplier 1, but its residual against
F is (0,4576,0,−6776,0,1408,0), which is nonzero. This chart fails.
All projective parameters have thus been exhausted, and no nonsingular
branch-preserving candidate exists for σ.

### Twist, lifts, proper scope and reproducibility

The identity used the entire F including 11. For a nonsingular family
member with M²=kI, k=a²−4c², a surviving multiplier λ would need a
rational e with e²=λ. Squaring the displayed field map then sends
W to (λ/k³)W; an order-two lift would require λ=k³. Here there are no
nonsingular survivors, so rational-square and order-two survivor tests
are vacuous. No twist was replaced and no geometric normal form was
used to infer rational existence.

Every putative proper automorphism restricts to the field map already
excluded. The homogeneous identity treats finite values mapping to
infinity as well as all branch values. L110 supplies the full smooth
proper model; no affine denominator exclusion can create an omitted
proper automorphism. No new proper extension assertion is required
for a nonexistent survivor.

Reproduce with

    python3 scripts/pair-genus-two/involution_eligibility.py
    python3 scripts/pair-genus-two/verify_involution_eligibility.py

Full producer evidence is
`scripts/pair-genus-two/involution-eligibility-certificate.json`;
independent replay evidence is
`scripts/pair-genus-two/involution-eligibility-verification.json`.
The replay imports no producer arithmetic. It checks all seven binary
coefficient polynomials at seven distinct rational parameter values,
which proves their identities because their degrees are at most six;
it also checks every equation, quotient, the full Bezout identity,
all rational-root candidates, both singular exceptions and the remaining
chart. All 45 checks pass with no failures. The full budget ledger is
`scripts/pair-genus-two/involution-eligibility-ledger.json`: including
producer, replay and selected certificate inspections, 20/10000 divisor
trials and 2541/200000 charged operations/nodes, maximum degree 8/64
and rational bit length 84/4096. Charges measure public polynomial
operations, candidate tests, matrix/coefficient checks and certificate
nodes, not library-internal elementary operations. Repeated executions
charge the same persistent caps cumulatively and may eventually stop.

This is the exact-instance reproduction/specialization approved in
`drafts/literature/2026-10-25-pair-genus-two-involution-eligibility.md`,
not a new automorphism theorem or a novelty claim. It supplies informative
negative evidence for this mechanism. Numerical upper ranks and point
control, marked lifts, degree-nine recovery, both L095 systems, the
minus-eleven alternative and other residual signatures remain unresolved.

## Mathlib

Full matching automorphism/elliptic-subcover coverage and supporting APIs
have not been checked. No absence or Lean-verification claim is made.
The general criteria are imported by the precise primary citations above;
the instance difference is certified by rational polynomial identities.
