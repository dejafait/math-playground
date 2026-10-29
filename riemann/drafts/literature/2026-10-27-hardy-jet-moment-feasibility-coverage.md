# Complete Hardy-jet moment feasibility: completed source comparison

TARGET: Assess whether complete fixed-order second and fourth Hardy-jet moments admit a finite-atomic law with nonvanishing normalized first-Laguerre negative mass.
CHECKED: 2026-10-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Compared L410's full construction, L414's full construction through atomic replacement, L416's full construction and normalization audit, and L419's hypotheses, conclusion and relevant support/moment proof; searched Hardy joint fourth moments, Laguerre negative mass, truncated moment and finite-atomic law terminology. No inspected source supplies the requested clipped-quadratic law; no novelty is inferred.
SOURCE_EVIDENCE: Directly inspected Bui--Hall arXiv:2304.05178v1, definition, (1), Theorem 3, Corollary 1, Proposition 3 and the complete Section 7 deduction; checked the PDF's first page and Theorem 3 against HTML. Directly inspected Bayer--Teichmann arXiv:math/0502473v2, Corollary 2 and proof, pp. 3--4. Reused the October-15 duality comparison and October-27 filtered-Laguerre comparison, with their qualifications.
COMPARISON: Known sources cover every fixed second/fourth ordinary-jet coefficient and its error, and conditional atomic replacement. L410/L416/L419 do not assert positive mass for (xz-y^2)_+; their response-weighted constraints and support conclusions are different. L414's rare-measure mechanism is relevant reusable work, not a new mechanism or a completed proof of this target.
GAP: Simultaneous feasibility with a uniform positive clipped-mass coefficient remains undecided by inspected results. A later attempt must retain six second entries and all fifteen quartic entries, including odd derivative-order errors; no law, separator, coefficient calculation or actual-Xi negative value is established here.
REASON: The changed scope now has essential source coverage for one bounded feasibility attempt. Sources do not directly decide it; EXPLORE authorizes only that finite-moment test after the supervisor's separate approval, with no claim of originality or actual-zeta realization.
LITERATURE_REASON: The target changed from a pair-divided majorant and response-dependent joint signs to all ordinary second/fourth jet moments and a clipped first-Laguerre statistic; the supplied assessment lacked this essential theorem-level comparison.
SCOPE: Exactly six raw degree-two and fifteen raw degree-four moments of ordinary Hardy jets of orders 0,1,2, with the errors specified below and ell=log H fixed on [H,2H]; real H tending to infinity and abstract H-dependent probability laws. No first/cubic constraints, response requirements, RH, simplicity, quotient estimate or global analytic realization is imported.
COVERED_TARGET: Assess whether complete fixed-order second and fourth Hardy-jet moments admit a finite-atomic law with nonvanishing normalized first-Laguerre negative mass.

## Bounded test and relevance

The main gap remains actual-Xi initial signs at unbounded heights and
all-degree mixed positivity. A proposed independent intermediate test
asks what *all* covered second and fourth moments can force about the
first sign, rather than applying another pair-by-pair moment bound.

For a future comparison use ell=log H and the three real coordinates

    x=Z(t), y=Z'(t)/ell, z=Z''(t)/ell^2, t in [H,2H].

The prospective abstract target is a family of finite-atomic probability
laws mu_H matching every raw degree-two and degree-four leading moment
of this triple, with the source errors justified coordinate by coordinate,
and satisfying

    E_mu_H (xz-y^2)_+ >= epsilon ell

for one fixed epsilon>0 and all sufficiently large H. Odd total
derivative orders and their error bounds must also be retained; they
must not be silently dropped. Atom sizes, probability normalization,
onset, error uniformity and any constraints actually imported from the
local laws must be explicit. No such law is constructed in this turn.
The exact source formulas and admissible errors are specified below.
No finite-dimensional construction is carried out in this review.

By the already established L471 (7)--(9), the corresponding actual
height average of this clipped quadratic is the first-sign negative
mass divided by H ell^2 up to the negligible gauge error. Thus the
prospective positive lower threshold tests whether moment data alone
can imply o(H ell^3). A matching abstract law would obstruct that
inference only; it would give no actual-zeta counterexample or lower
bound for the actual mass. Failure to find one would also not establish
actual positivity. Exceptional heights and higher/mixed signs remain
independent gaps even if a moment method later yields a saving.

## Comparison of mechanisms and stop conditions

1. Pair-divided summation is parked: L471 (3) is unproved and its
   ordinary fourth-moment substitution loses displacement. Preserve
   `ATTEMPTS/2026-10-27-displacement-weighted-negative-mass-test.md`.
2. Scalar height barriers and finite polynomial linear closure have
   their separate retained class obstructions in L469 and L470. Neither
   is reopened by a corrected moment constant or another source read.
3. Select simultaneous Hardy-jet moment feasibility. This tests a
   statistical implication through an explicit law or a separating
   inequality, rather than repeating the failed quotient estimate.
   L410/L416/L419 are possible overlap inputs, not established premises
   of this changed target. Check their exact proofs only as needed.

The duplicate comparison below finds no already-stated conclusion
supplying the requested clipped-quadratic lower bound. The listed
finite constraints, rather than the older response constraints, define
the scope of the next test.
Do not infer feasibility from covariance positivity alone, transplant
the response-dependent forbidden cone, or treat a numerical optimizer
as a rigorous certificate. A source result forcing the opposite
inequality changes the route; a duplicate ends the proposed discovery.
Persistent source obstruction parks this dependent construction.

This source review makes the bounded target ready for separate approval;
it is not a mathematical attempt or a feasible-law result. Full matching
Mathlib coverage is unchecked. No outside-notebook input is used.

## Primary moment input and exact retained constraints

H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function Z(t)*,
Bull. Lond. Math. Soc. 55 (2023), 2304--2323,
[DOI 10.1112/blms.12859](https://doi.org/10.1112/blms.12859),
[arXiv:2304.05178v1, 11 April 2023](https://arxiv.org/html/2304.05178v1).
These are unconditional, fixed-order, ordinary derivative statements.
They are imported by citation; no reproof of their arithmetic input is
needed for the abstract test.

For j,k fixed, their Introduction, p. 1, equation (1) states, with
j+k=2s and |j-k|=2d,

    J_jk(T)=integral_0^T Z^(j)(t) Z^(k)(t) dt
      = (-1)^d T Q_(2s+1)(log(T/(2pi)))/(4^s(2s+1))
        + O_(j,k)(T^(3/4)(log T)^(2s+1/2)),

where Q is monic. The immediately preceding display gives
J_jk(T)=O_(j,k)(T^(1/3)) when j+k is odd. For the prospective
X=(x,y,z)=(Z,Z'/ell,Z''/ell^2), the required normalized entries are

    E x^2=ell+O(1), E xy=O(H^(-2/3)ell^(-1)),
    E xz=-ell/12+O(1), E y^2=ell/12+O(1),
    E yz=O(H^(-2/3)ell^(-3)), E z^2=ell/80+O(1).

Here E for actual data means H^(-1) integral_H^(2H). The applicability
operation is the dyadic difference [J_jk(2H)-J_jk(H)]/(H ell^(j+k)).
The monic leading term gives the stated coefficients; lower polynomial
terms and the cited error permit O(1) in even entries, while the odd
primitive bound gives the displayed power-saving errors. L416 checks
these same leading coefficients for a varying log(2+t) divisor. The
future proof must use the fixed ell divisor just specified, rather than
silently identify those two laws or their lower-order terms. No exact
constant terms of the even entries are imposed.

Theorem 3 and its defining asymptotic on p. 4, Corollary 1, and Section 7
give the complete fourth-product input. Write h(k,l,m,n)=HARDY(k,l,m,n)
and S=k+l+m+n. Section 7 explicitly supplies the sharp dyadic formula

    integral_H^(2H) Z^(k) Z^(l) Z^(m) Z^(n) dt
      = h(k,l,m,n) H ell^(S+4)/pi^2 + O_(k,l,m,n)(H ell^(S+3)).

For an unambiguous exact coefficient specification, set

    A=1/2+(u1-u2)u3-u1, B=1/2+(u2-u1)u3-u2,
    C=1/2+(u1-u2)u4-u1, D=1/2+(u2-u1)u4-u2.

Theorem 3 is precisely

    h(k,l,m,n)=3(-1)^(m+n) i^S
      integral_[0,1]^4 (u1-u2)^2 A^k B^l C^m D^n du.

These four affine factors specify a four-linear functional; they must
not be read as four independent copies of one random jet. The i^S and
(-1)^(m+n) factors are essential. Corollary 1 gives h=0 for odd S;
the complete Section 7 parity argument was inspected, not inferred from
an imaginary formal coefficient.

All fifteen constraints are specified without numerical integration as
follows. For each (a,b,c) of nonnegative integers with a+b+c=4, let
(j1,j2,j3,j4) be the sorted list with a zeros, b ones and c twos, and put

    q_abc=h(j1,j2,j3,j4)/pi^2,
    E x^a y^b z^c = q_abc ell^4 + O_abc(ell^3).

The full list is

    x^4, x^3 y, x^3 z, x^2 y^2, x^2 yz, x^2 z^2,
    xy^3, xy^2 z, xyz^2, xz^3, y^4, y^3 z, y^2 z^2, yz^3, z^4.

Odd b means odd S=b+2c: its coefficient is zero and its allowed
remainder is O(ell^3), not an unspecified o(ell^4) or an exact actual
zero. The same O(ell^3) tolerance applies to every even entry. All
orders are fixed, so a common maximum of their finitely many constants
and onsets is allowed; no growing-order uniformity is assumed. This
is a source-coefficient definition, not a newly computed moment table.

Section 7 retains the ordinary-derivative phase expansion and uses
Proposition 3's complex-shift uniformity on O(1/ell) Cauchy contours.
Section 4.2 explicitly omits Proposition 3's proof. This review imports
the published result and checks the required statements and deduction;
it is not an independent audit of that omitted proof or Hall's original
Theorem 3. The direct published moment statements suffice for this
source gate, without RH or a new zero-free-region premise.

## Atomicity and limits of moment duality

Christian Bayer and Josef Teichmann, *The proof of Tchakaloff's Theorem*,
Proc. Amer. Math. Soc. 134 (2006), 3035--3040,
[DOI 10.1090/S0002-9939-06-08249-9](https://doi.org/10.1090/S0002-9939-06-08249-9),
[arXiv:math/0502473v2, Corollary 2 and proof, pp. 3--4](https://arxiv.org/pdf/math/0502473v2).
For a positive measure on a measurable space concentrated on a
measurable set, an integrable measurable map to R^N has its integrals
preserved by at most N positive atoms in that set. Including the
constant coordinate preserves total mass. The corollary's proof pushes
forward by the map, applies Corollary 1, and lifts the selected points;
this covers noncompact state spaces and nonpolynomial coordinates.

The prospective coordinate map here consists of 1, the six second
monomials, fifteen fourth monomials, and (xz-y^2)_+. This is the
appropriate source for atomic replacement *if an integrable feasible
measure has first been supplied*. Integrability of every coordinate
and the retained clipped expectation must be checked in that application.
No uniform atom locations or positive clipped mass follow from the
theorem alone; no feasibility claim is made from covariance positivity.

Reuse the precise Bertsimas--Popescu Theorems 2.1--2.2 comparison in
`2026-10-15-jet-supported-moment-feasibility-review.md`, Section on
primary moment/atomic inputs: pointwise certificates can be integrated,
but strong duality needs additional hypotheses and attainment is not
automatic. No strong duality, flat extension, interiority or numerical
optimizer is needed or imported for the proposed direct construction.
A failed ansatz is not an infeasibility certificate.

## Duplicate, failure and stronger-result comparison

- L410's explicit two-atom proof matches five scalar (Delta,Bcal)
  constraints without a physical triple; it does not match the tensor
  above or assert the desired clipped mass.
- L414's rare weighted pushforward and L416's full eight-state bulk
  proof were read. Their common-sign orientation preserves homogeneous
  quartic products, making the rare-measure method relevant reusable
  work. Their conclusions concern response-dependent joint-sign
  avoidance. L416's bulk has z=-kx, k>0, hence supplies no positive
  (xz-y^2)_+ bulk value. No full matching law with the new lower bound
  is asserted by those proofs. A future specialization must check all
  raw quartic errors at O(ell^3), rather than cite the selected 23
  response-weighted little-o statements as a substitute.
- L419's support and simultaneous-moment proof uses an actual response
  kernel, a six-state negative-Delta bulk and an unresolved rare cubic.
  Its six states and response cone cannot be transplanted to the new
  clipped form. None of its response or cubic hypotheses is silently
  added to this different test.
- Reuse `2026-10-27-actual-xi-negative-part-mean-coverage.md` for the
  already inspected paper 36 v4 Corollary 5 and Theorem 6: positive
  Laguerre/filter-square fourth means do not test an arbitrary nonlinear
  clipped jet expression. These are constraints on the same sourced
  fourth functional, not a theorem of almost-sure first-sign positivity.
  Its larger growing-filter assertions are unnecessary here.
- `ATTEMPTS/2026-10-27-displacement-weighted-negative-mass-test.md`
  retains the loss of displacement and full-scale ordinary-moment
  bound; this review does not reopen that quotient summation.
  `ATTEMPTS/2026-10-15-joint-sign-shrinking-window.md` retains the
  independent regulator-scale obstruction; an abstract law would not
  repair it or provide actual/global realization.

## Search scope, decision and continuation test

Queries actually used included `"Hardy" "joint moments" "Laguerre"
derivatives fourth`, `"Hardy" "moment problem" "derivatives"`,
`"Hardy" "finite-atomic" moments`, `"Hardy" "derivatives" "truncated
moment"`, `"Hardy" "Laguerre" "negative mass"`, and `"Hardy" "jet"
"moments" probability law`, plus Bayer--Teichmann/Tchakaloff terminology.
Hardy-space atomic decompositions and unrelated Laguerre moment problems
were excluded. The Orchard sign proof and other random-matrix or general
moment leads returned by search were not inspected as theorem inputs;
none is used to assert existence, impossibility or novelty.

DECISION EXPLORE concerns the existence/lower-bound target, not the
known moment theorems. After separate approval, test one simultaneous
bulk/rare law using the established finite-moment mechanism. A valid
success must give one fixed epsilon>0, probability normalization,
integrability, all six second errors and all fifteen O(ell^3) fourth
errors on that same family, and E(xz-y^2)_+>=epsilon ell for every
sufficiently large real H. It may cite atomic replacement only after
feasibility and the clipped observable are controlled. Do not impose
unlisted first, cubic, response or global-function constraints.

Continue on a rigorously certified law, or on a genuine error-robust
separator excluding the requested lower bound. Abandon the chosen
ansatz if its covariance correction ceases to be positive, any retained
error exceeds its tolerance, or the clipped coefficient vanishes;
record that limited failure without claiming moment infeasibility.
An unresolved construction is saved as unfinished reasoning. A law
would obstruct an inference of o(H ell^3) from precisely these finite
moments, and would supply no actual negative Xi value, no lower bound
for the actual mass, no exceptional-height control and no RH resolution.
