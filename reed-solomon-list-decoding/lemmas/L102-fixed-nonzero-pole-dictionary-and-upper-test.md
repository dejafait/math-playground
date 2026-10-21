# L102 — Fixed nonzero-pole dictionary and one upper test

## Hypotheses

Use C012a's Q=65537, E=F_Q, H=<19139> of order n=1024,
F=F_(Q^28), k=64, epsilon*=2^(-128), and m>=1. Message rows
are in F[X] of degree strictly less than 64. Use the closed
simultaneous-column list model in
[foundations/02](../foundations/02-pinned-list-model.md).
Put Z=X-3, T=Q^28/2^128. For a,b in E and c in E^*, define

\[
 Y_{a,b,c}(x)=((Z(x)^{67}+aZ(x)^2+bZ(x)+c)/Z(x)^3,0,\ldots,0).
\]

For each 67-subset S of H put g_S(X)=product_(x in S)(X-x),
and let N(a,b,c) count those S satisfying

\[
 g_S(Z+3)\equiv c+bZ+aZ^2\pmod {Z^3}.                 \tag{1}
\]

## Conclusion

The entire list with at least 67 simultaneous agreements consists
of the distinct tuples (f_S,0,...,0) indexed by (1), where

\[
 f_S(X)=\frac{Z^{67}+aZ^2+bZ+c-g_S(X)}{Z^3}.           \tag{2}
\]

Each f_S is in E[X], has degree at most 63 and agrees exactly on S.
The list size is N(a,b,c) for every m. No claim that every label
occurs is made.

Here is one uniform upper allowance, including all character types.
Set D=(Q-1)Q², C=binomial(1024,67), B=769 and
E_0=binomial(835,67). For d=2^a, 1<=a<=16, define rational
coefficients h_(d,0)=1 and

\[
 h_{d,k}=\frac1k\sum_{j=1}^k b_{d,j}h_{d,k-j},\qquad
 b_{d,j}=\begin{cases}1024&d\mid j,\\769&d\nmid j.\end{cases}
                                                               \tag{3}
\]

Then, for all the stated labels,

\[
 N(a,b,c)\le\lfloor U\rfloor,\quad
 U=\frac CD+(1-Q^{-2})E_0+
                  \frac1D\sum_{a=1}^{16}2^{a-1}h_{2^a,67},
 \qquad 4780<\frac UT<4781.                            \tag{4}
\]

This single upper test is insufficient for family exclusion. It is
not a lower bound on any fiber. Neither arbitrary-center safety,
an unsafe list, nor any improvement of the 955–957 bracket follows.
The dictionary and finite test are REPRODUCTION of the assessed
general tools; no progress beyond the inspected methods or novelty
is claimed. The separate critical audit of 2026-10-20 retains this
restricted result; its full scope and independent evidence are below.

## Proof

**Imported framework and scope.** The unchanged
[SPECIALIZE assessment](../drafts/literature/2026-10-20-fixed-nonzero-pole-three-upper.md)
approves exactly this family and one upper test. Gao,
*Asymptotic distributions of the number of zeros of random polynomials
in Hayes equivalence class over a finite field*,
[arXiv:2203.06729v5](https://arxiv.org/html/2203.06729v5),
2024-01-07, definitions (1)–(2), (5)–(6), Proposition 2 (15)–(16)
and Theorem 3 (17)–(19), give the arbitrary-domain residue-class
framework. Its parameters here are q=Q, monic modulus (X-3)^3,
t=3, ell=0, D_source=H, k_source=64 and j=67. The residual
degree is zero. The required avoidance of the modulus's zero is
proved below. The full group has (Q-1)Q² elements. No generating
identity is reproved and Gao's full-complement quantitative result
is not used on H. The remaining dictionary proof supplies the RS
interpretation and ambient-field completeness, which are not imported.

Li and Wan, *Distance Distribution in Reed-Solomon Codes*,
[arXiv:1806.00152v3, Section 4](https://arxiv.org/html/1806.00152v3#S4),
2019-07-30, Lemma 4.1, printed pp. 9–10, bounds a nonprincipal
unit character's complete degree-one monic sum modulo a monic
degree-d polynomial by (d-1)sqrt(Q), with extension by zero on
nonunits. Its arbitrary-modulus statement covers the nonsquarefree
joint modulus used below, including imprimitive characters. We do
not use the separate cumulative bound requiring triviality on E^*.

Li and Wan, *Counting polynomial subset sums*,
[arXiv:1507.06329v1, Section 2](https://arxiv.org/html/1507.06329v1#S2),
2015-07-22, Theorem 2.1 and Corollary 2.2, printed p. 5, give the
weighted distinct-coordinate sieve for an arbitrary finite domain
and symmetric product weight. The cycle generating identity in the
proof of Lemma 2.6 gives the formal coefficient below. These are
imports, not character-bound or sieve reproofs. L099–L101 are method
comparisons only; their smaller class container and cancellations
are not mathematical inputs here.

**Pole avoidance and dictionary.** C012a proves that 3 has order
65536 in E^*, while every element of H has order dividing 1024.
Thus 3 is not in H and all denominators are nonzero. For a subset
S, put t_x=x-3, P=product t_x, u=sum t_x^(-1), and
v=sum_({x,y} subset S)(t_x t_y)^(-1). All t_x are nonzero and

\[
 g_S(Z+3)=\prod_{x\in S}(Z-t_x)
       \equiv-P(1-uZ+vZ^2)\pmod {Z^3}.
\]

Thus the label is (a,b,c)=(-Pv,Pu,-P), with c nonzero. It is
not asserted that c is in H: translation changes these products.
Equation (1) makes (2) a polynomial over E. Its degree-67 terms
cancel, so the numerator has degree at most 66 and the quotient
has degree at most 63. For x in H, the difference between the first
center row and f_S(x) is g_S(x)/(x-3)^3, vanishing exactly on S.
Other rows are zero. Different supports therefore give distinct
evaluation tuples at this one fixed center, by a point of their
symmetric difference.

Conversely, let (f_1,...,f_m), initially over F, agree simultaneously
on at least 67 columns. The polynomial

\[
 G(X)=(X-3)^{67}+a(X-3)^2+b(X-3)+c-(X-3)^3f_1(X)
\]

is monic of degree 67, since the subtracted term has degree at most
66. L001's factor/root bound implies that its agreeing columns are
exactly a 67-subset S and G=g_S: the monic product of those roots
divides G with the same degree. Reduction at X=3 gives (1), and
(2) forces f_1 into E[X]. Each other row has degree at most 63
and 67 roots, so is identically zero. This proves the entire-list
statement for every m, including empty fibers, with no projection,
tuple exponent or extra-agreement correction.

**Full Fourier normalization.** Let R=E[Z]/Z³ and G=R^*. Every
element is uniquely c(1+uZ+wZ²), c in E^*. Since 2 is invertible,

\[
 c(1+uZ+wZ^2)\longmapsto(c,u,v=w-u^2/2)
\]

is a group isomorphism G -> E^* times (E,+)²: multiplication
adds u and changes w to w+w'+uu', so it adds v as well. The
inverse sends (c,u,v) to c(1+uZ+(v+u²/2)Z²). Hence |G|=D.
As E is prime, its full complex character group consists of

\[
 \chi(c,u,v)=\theta(c)\exp(2\pi i(\alpha u+\beta v)/Q),
 \quad\theta\in\widehat{E^*},\quad\alpha,\beta\in E.   \tag{5}
\]

For x in H, r_x=Z+3-x is a unit. Its coordinates are
(3-x,(3-x)^(-1),-1/(2(3-x)²)). Its subset product is exactly
the residue in (1). For z=c+bZ+aZ² in G and
W_chi=sum_(|S|=67) product_(x in S)chi(r_x), standard finite
abelian character orthogonality gives

\[
 N(z)=D^{-1}\sum_{\chi\in\widehat G}\chi(z)^{-1}W_\chi.
                                                               \tag{6}
\]

This uses the full group even if many labels are empty; no image-size
or surjectivity claim is needed. The principal contribution is C/D.
There are (Q-1)(Q²-1) characters with (alpha,beta) nonzero. The
constant-only characters have (alpha,beta)=(0,0); one is principal
and, since E^* is cyclic of order 2^16, precisely phi(d)=d/2 have
each order d=2,4,...,65536. These counts exhaust all D characters.

**Every cycle, twist and omitted point.** Let A be the annihilator
of H in the character group of E^*. Since H=<3^64>, A has 64
members and 1_H(x)=64^(-1)sum_(eta in A)eta(-x) for x!=0.
The minus sign is harmless because -1 in H by C012a. For
1<=j<=67 define C_j(chi)=sum_(x in H)chi(r_x)^j. The Chinese
remainder theorem for the coprime ideals (X) and ((X-3)^3)
identifies the unit group modulo f=X(X-3)^3 with E^* times G.
On this group define

\[
 \Psi_{j,\eta}(P)=\eta(P(0))\chi(P(Z+3)\bmod Z^3)^j,
\]

and extend it by zero on nonunits. Then

\[
 C_j(\chi)=\frac1{64}\sum_{\eta\in A}
          \sum_{x\in E}\Psi_{j,\eta}(X-x).             \tag{7}
\]

Indeed for x!=0,3 the summand is eta(-x)chi(r_x)^j, so the
indicator recovers H. At x=0 and x=3 it is zero because X-x
is a nonunit of the joint ring. Both points are outside H. These
zeros hold even if a character factor is principal, and are retained
at every positive power; they must not be replaced by 1. The inner
sum ranges over every monic linear polynomial exactly once.

If (alpha,beta) is nonzero, the restriction of chi^j to the additive
factors has parameters (j alpha,j beta), still nonzero since
1<=j<=67<Q. Twisting on the separate CRT factor cannot cancel
that restriction. Thus every Psi_(j,eta) is nonprincipal. Li–Wan's
degree-four bound gives

\[
 |C_j(\chi)|\le(1/64)\,64\cdot3\sqrt Q<769=B,         \tag{8}
\]

where 9Q=589833<591361=769². There is no extra factor 64.

For a nonprincipal constant-only character chi=theta of order d,
if d does not divide j, theta^j is nonprincipal on the second CRT
factor, so the identical argument proves (8) for every eta. If d
divides j, chi(r_x)^j=1 on H, and C_j(chi)=1024 exactly.
These are all principal-power exceptions, not disappearing terms.
For completeness, in this case Psi_(j,eta) is principal exactly
when eta is principal. Its complete sum is Q-2 for that eta and
-eta(-3) for each nonprincipal eta. Since -3 is outside H,
sum_(eta in A)eta(-3)=0; their average is (Q-1)/64=1024,
in agreement with the direct domain calculation. Thus (7) accounts
for all twists and both omitted evaluations even in this exception.

**One sieve bound.** The imported weighted sieve says

\[
 67!W_\chi=\sum_{\sigma\in S_{67}}(-1)^{67-\#\mathrm{cycles}(\sigma)}
                         \prod_{j=1}^{67}C_j(\chi)^{c_j(\sigma)}.
                                                               \tag{9}
\]

The factor 67! converts ordered distinct tuples to unordered subsets.
For a nonconstant character, taking absolute values and using the
imported cycle generating identity bounds |W_chi| by
[t^67]exp(B sum_(j>=1)t^j/j)=binomial(B+66,67)=E_0.
For constant-only order d, use b_(d,j) from (3) instead. The bound
is h_(d,67)=[t^67]exp(sum_(j>=1)b_(d,j)t^j/j); formal
differentiation gives exactly (3). Only j<=67 matters. In particular,
orders exceeding 67 have no exceptional cycle within this coefficient;
they are retained with h_(d,67)=E_0. No old constant-character
vanishing claim is used.

Applying triangle inequality to (6), and dividing the above character
counts by D, gives (4). All character phases have modulus one.
This is a conservative absolute upper allowance, not an exact maximum
or a statement that the error phases can align.

**Exact comparison and meaningful verification.** In reduced form the
allowance U=A_U/d_U is

```text
A_U = 53044746895146418049153132401454442254356973583738869432485950492034551354853198737919018505853426586934259601547817580502080635966595
d_U = 5192455316068781976820312591826944.
```

Exact integer cross multiplication gives

\[
 4780 Q^{28}d_U<2^{128}A_U<4781 Q^{28}d_U,
\]

so even floor(U)>T (in particular, (4780-1)T>1 since T>1).
The nonconstant contribution alone also exceeds T. No retuning of
this estimate was performed after its failure. The failure concerns
the allowance, not an actual list lower bound or the validity of (2).

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/fixed_nonzero_pole.py`.
The full certificate is
`scripts/coefficient-fibers/fixed-nonzero-pole-results.json`.
All 5853 checks pass. The script reconstructs C by factorials and
complete Pascal recursion. For all sixteen character orders it
checks every coefficient 0,...,67 of (3) independently against

\[
 (1-t)^{-769}(1-t^d)^{-255/d},
\]

whose coefficient is expanded using rational rising factorials.
This keeps all exceptional cycle lengths, even when 255/d is not an
integer. Full U, T, the positive failure margin and the constant-only
contribution were inspected. The exact rational comparisons, not a
decimal preview, establish the verdict.

In the proper order-eight subgroup <9> of F_17, pole 3 is outside
the domain. The small test uses k=2 and five agreements. It checks
the translated coefficient signs and whole quotient identity for all
56 five-subsets. It independently enumerates all 289 scalar messages
in the Z basis at every one of the 4624 labels (a,b,c), c!=0.
Every complete list agrees with the dictionary, including all empty
labels. This supports the translated algebra but does not test the
large-domain character estimate or replace the ambient-field proof.

The downstream use is a complete fixed-family dictionary and a precise
stop on this one absolute-sieve certificate. Further methods require
separate assessment. Arbitrary-center 67/68 safety, the main finite
boundary and the ABF-model comparison are still unresolved.

**Separate critical audit, 2026-10-20.** The audit retains (1)–(9)
and their qualifications. It uses the unchanged
[critical-audit assessment](../drafts/literature/2026-10-20-fixed-nonzero-pole-critical-audit.md);
no smaller class group, altered pole, sharper allowance or new theorem
is substituted. The three cited primary inputs were reopened at exactly
their stated definitions, theorem statements and relevant proof cases.
The title of the 2019 Li–Wan citation above is corrected; its version
and theorem are unchanged.

For the dictionary, divisibility is in E[X] on the forward direction
and initially in F[X] on the converse. The leading coefficient is one
even after translation, while Z³f_1 has degree at most 66. Thus a
candidate cannot have more than 67 agreements, and its unique monic
67-root product has coefficients in E. This proves descent without
assuming that an arbitrary ambient polynomial starts over E. Every
other tuple row has 67 distinct zeros and degree at most 63, including
the zero-row case. The symmetric-difference argument proves distinct
evaluation tuples. Empty fibers and m=1 cause no exception.

For the character cases, the inverse logarithmic coordinate map in
(5) proves surjectivity as well as multiplicativity, so there are
exactly D characters. Every nonzero additive pair is protected by the
inverse of j in E, for each of the 67 powers. The CRT factors are
independent: a twist on the X factor cannot cancel a nonprincipal
restriction on (X-3)³. For order d, every primitive exponent is coprime
to d, so the principal-power condition is exactly d|j for all d/2
characters of that order, not just a representative. The principal
joint character occurs exactly when also the index-64 twist is
principal. Nonunits remain zero in all these cases. In particular,
the principal-power complete sums are Q-2 and -eta(-3), rather than
Q and zero. Their exact average is n. The audit retains the full
Fourier denominator, the 1/64 filter and the unordered 67! factor.

Run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/audit_fixed_nonzero_pole.py`.
The complete evidence is
`scripts/coefficient-fibers/fixed-nonzero-pole-critical-audit.json`.
All **147398 independent checks** pass; the constructor also reruns
with its original 5853 checks and reproduces the entire saved file
byte for byte. Its pre-rerun evidence is preserved as
`scripts/coefficient-fibers/fixed-nonzero-pole-critical-source.json`.
The independent audit imports no constructor functions.

The audit reconstructs every coefficient of every order by multiplying
the 67 separate formal factors exp(b_j t^j/j), a third computation
distinct from the constructor's recurrence and two-factor expansion.
It checks all 16 orders, 67 powers and 64 twist decisions, together
with all 67 modular inverses for the symbolic nonconstant case.
Exact arithmetic in Z[zeta_64], using zeta_64^32=-1, checks every
twist residue and the principal-power complete sums. The full primitive
orbit verifies the subgroup filter at every nonzero field point; a
separate pass verifies that precisely 0 and 3 are excluded. These
finite checks support the algebra above; they do not numerically test
or replace the imported Weil bound.

For the small-field check, the independent enumeration uses messages
f_0+f_1 X and solves for c at each evaluation point for every (f,a,b).
Grouping the resulting c values exhausts all 289 messages at each of
the 4624 centers. Every list, including empty ones, agrees with the
saved certificate and with a separate elementary-symmetric expansion
of all 56 root products in X followed by Taylor shift at 3. Complete
polynomial coefficient identities and exact supports are retained.
This is supporting finite evidence; the all-m ambient-extension
conclusion follows from the preceding proof.

Every saved rational contribution, the complete manuscript numerator
and denominator, and both strict cross-multiplication margins agree.
The integer comparison directly checks floor(U)-T>0, not merely U>T.
No load-bearing defect was found. The audit establishes no stronger
bound or actual fiber size and does not reopen the stopped estimate.

## Mathlib

Full translated-pole dictionary and finite upper-test result: **not
checked**. Supporting polynomial, Chinese remainder, unit-character,
Fourier, sieve and finite-field results: **not checked** in Mathlib;
unknown coverage is not absence. The primary links above provide the
imported general theorems. Pinned ArkLib definitions in foundations/02
are **present** and specify the model, not this specialization.
