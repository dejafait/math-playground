# Rational cubic units and the dyadic condition — source comparison

TARGET: Determine whether the norm-one unit square classes of Q[X]/(g), mapped into L069's D, contain a class whose rational two-adic localization is outside L070's H.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the recorded Simon/BPT comparison and local audit; checked L069, L070, ATTEMPTS/032 and histories 214,217,220; searched exact cubic, norm-one unit, dyadic Kummer and certified-unit variants; inspected Bruin–Stoll, official PARI documentation, Stacks 0BD2 and two exact-curve leads, with scope and queries below.
SOURCE_EVIDENCE: Simon 2002 Section 1.1–1.2 p.8; BPT arXiv:2001.02263v3 Lemma 1.3 and Remark 1.4 p.4, with L070's Theorems 1.8/1.11 coverage reused; Bruin–Stoll 14 March 2008 Section 2/Remark 2.1 p.3 and Section 4/Lemma 4.4 plus complete algorithm/proof cases pp.6–10; official PARI stable catalogue bnfcertify/bnfinit/bnfisunit/nfeltnorm/nfislocalpower; Stacks Lemma 31.18.6 tag 0BD2, statement and proof; Li author PDF Assumption 2.1 pp.4–5 and Example 5.3 p.19; Chung–Li 2014 Section 3.2 pp.50–51.
COMPARISON: Known exact unit-certification and full local-image methods cover the tools for a finite subfield test, but neither the recorded local index nor the inspected exact-curve examples decide this global-local comparison; Li's square-free-discriminant Selmer theorem has incompatible hypotheses.
GAP: The source gate is complete for the delimited test; exact representatives, norm-one quotient bookkeeping, transport to V, complete local membership evidence and survival as nonsquares in D remain mathematical obligations, with no answer derived here.
REASON: Apply inspected known methods to this specified cubic and rational place; the only authorized derivation is their exact applicability and certificate comparison, not a reproof of the local index or a new global rank theorem.
SCOPE: This exact subfield witness/completeness test, including necessary field/coordinate, unit, norm/base-change and dyadic square-class certificates; no full degree-36 unit computation, Selmer dimension, class-group calculation for K/D, rank bound, subgroup index or integer exclusion.

Here g=X³−4X²−160X−1264, K is the degree-twelve field of L033,
D=K[X]/(g) is L069's entire cubic extension of K, and H is exactly
L070's full Kummer image over Q2 in A=Q2[X]/(g). The proposed map
from Q[X]/(g) sends X to the same distinguished generator of D;
localization uses L046's rational place and retains the entire cubic
algebra. Norm-one means norm to Q equals 1; the quotient is by squares
of norm-one units. Whether a candidate survives as a nonsquare in D
must be justified, never assumed from its nonsquareness in the subfield.
No cross-notebook input is proposed.

The main gap is primitive integer emptiness. The intermediate goal is
one certified global unit direction removed by the accepted local
condition. A positive answer needs an exact unit/inverse and norm
certificate, justified membership in L069's V, and proved local
nonmembership in H. A negative answer for this target needs coverage
of all norm-one unit square classes of the rational cubic subfield;
an unsuccessful bounded candidate search would not suffice. Neither
answer controls the full degree-36 unit group or supplies a rank bound.

The sources below approve a separate mathematical attempt at the exact
saved target. Reuse L070's index theorem and Simon's unit/Kummer
framework; do not reprove the index or infer global surjectivity from
it. No new units, local images, specialized norm identities or global
dimension claims have been derived in this literature turn.

Continue this subfield route only if a finite exact test is justified;
if all its norm-one unit classes are certified inside H, park this
subfield witness mechanism while preserving the possibility of other
global units. If essential sources remain persistently blocked, choose
an independently testable mechanism. ATTEMPTS/032 concerns the bare
unfiltered upper space and remains intact. Full class coverage, other
places, rank below twelve, subgroup indices/cosets, other classes and
primitive integer lifting remain unresolved. Mathlib coverage for the
new comparison is not checked.

## Inspected primary inputs and their limits

Denis Simon, *Computing the rank of elliptic curves over number fields*,
LMS J. Comput. Math. **5** (2002), 7–17,
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8FAFF26D93D01A154C51CF897E4BE6CD/S1461157000000668a.pdf/computing_the_rank_of_elliptic_curves_over_number_fields.pdf),
[DOI](https://doi.org/10.1112/S1461157000000668).
Printed p.8, Section 1.1 assumes a monic integral irreducible cubic;
Propositions 1.1–1.2 give the Kummer homomorphism, its exact kernel and
the norm-square target. Section 1.2 recalls the full Dirichlet S-unit
theorem, including roots of unity. These inputs are reused from L069.
They support a finite unit-square-class comparison, but give neither
fundamental units of this cubic nor local nonmembership. The actual
norm-one unit quotient must be justified, rather than silently replaced
by the norm-square kernel. L069 supplies irreducibility and signatures;
the same cubic over Q is the proposed subfield input.

Daniel Barrera Salazar, Ariel Pacetti and Gonzalo Tornaría,
*On 2-Selmer groups and quadratic twists of elliptic curves*,
[arXiv:2001.02263v3](https://arxiv.org/pdf/2001.02263v3),
17 September 2020. L070's audited Theorems 1.8/1.11 application is
reused unchanged. Additionally, Lemma 1.3, printed p.4, states the exact
local-image size as [O:2O] times the cardinality of E(F)[2], for a finite
extension F/Q_p; it cites Brumer–Kramer Lemma 3.1, rather than giving a
new proof. Remark 1.4 uses maximal rings of all local factors. This
cardinality theorem offers a smaller alternative to full image
enumeration: a subgroup generated by certified point images equals H
only after its order is proved equal to the theorem's complete order.
Every local two-torsion point and the abstract exceptional evaluations
must be accounted for. A small sample with no such size certificate is
insufficient. This review establishes no torsion size or generator for
our dyadic specialization. The separate U4 inclusion is unnecessary;
it is not promoted to an equality or a membership criterion.

Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, [author manuscript dated 14 March 2008](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
Math. Comp. **78** (2009), 2347–2370,
[DOI](https://doi.org/10.1090/S0025-5718-09-02255-8).
The theorem/algorithm numbering here refers to that manuscript.
Section 2/Remark 2.1, printed p.3, retains A*/A*² without a scalar
quotient for odd degree and defines the unique infinity value.
Section 4 assumes a characteristic-zero complete discretely valued
local field with finite residue field, a square-free integral polynomial
and its full irreducible factorization. Its general algorithm includes
residue characteristic two and repeated reduction roots; the odd-prime
shortcut in Lemma 4.3 must not be used at two.

Lemma 4.4, printed pp.7–8, requires an irreducible factor h, x0 in O
and e>=0 with the valuation of h(x0+epsilon*pi^e)-h(x0), as a
polynomial in the indeterminate epsilon, strictly exceeding that of
h(x0). It then fixes the factor square class throughout the smaller
disk x0+pi^(e+ord(4))O. Its entire norm/valuation and square-neighborhood
proof was read. SquareClasses and the full correctness/termination
discussion, pp.8–9, check square feasibility and extra dyadic digits;
they prove both exhaustive coverage and actual realization. The linear
root case is absorbed by the separately recorded Weierstrass value.
LocalImage, pp.9–10, also computes the reciprocal chart with
z=1/x, altered polynomial and map z(1-z*theta), and records infinity.
Together these cases return the full image, rather than a residue
sample. A later implementation must save the full terminal-disk and
square-class evidence, including any exceptional charts. No such
specialization or implementation was performed here.

The [official PARI/GP stable General number fields catalogue](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html),
accessed 2026-10-14, supplies precise callable certificate interfaces.
This dynamic page does not print a release identifier; a later run must
record its actual installed version. Its introductory GRH discussion
and full `bnfcertify` entry state that `bnfinit` alone guarantees only
a finite-index unit subgroup, whereas `bnfcertify(bnf,0)=1` certifies
the class/unit computation unconditionally. Flag one is weaker and
does not certify full units. `bnfinit(g,1)` retains exact algebraic unit
data; `bnf.fu` and `bnf.tu` supply fundamental and torsion generators,
and `bnfisunit` gives their exponent decomposition. `nfeltnorm` gives
the absolute norm, and `nfislocalpower(nf,pr,a,2)` tests a square in
the actual completion at a maximal prime. These are supporting
algorithm specifications, not an executed certificate. Units and
inverses should also be checked by exact arithmetic and maximal-ring
coordinates. Checking squares in every factor permits comparison with
the proved complete H, but cannot replace the H computation itself.

[Stacks Project, Lemma 31.18.6, tag 0BD2](https://stacks.math.columbia.edu/tag/0BD2),
statement and entire proof inspected 2026-10-14, gives the canonical
norm for a finite locally free morphism of constant degree at least
one, commuting with arbitrary base change, defined by the determinant
of multiplication. It supplies the named input for transporting the
cubic norm from Q to K and to the rational Q2 place. The future
application must identify D with the entire base-changed cubic,
retain the same generator and check unit/inverse integrality. No
target-specific norm calculation is made in this review.

## Stronger-result and duplicate comparison

Chao Li, *2-Selmer groups, 2-class groups and rational points on
elliptic curves*, [author PDF](https://www.math.columbia.edu/~chaoli/EC4d.pdf),
22-page manuscript checked 2026-10-14; no date/version is printed in
the inspected opening. Assumption 2.1, printed p.4, requires a monic
irreducible integral cubic of negative **square-free** discriminant.
Theorem 1.4/2.18 therefore cannot be invoked on L069's g with its
already recorded discriminant −256*11^5. Section 2's specialized local
claims inherit that assumption. Example 5.3, p.19, does discuss our
exact original curve and reports the cubic field Q[t]/(t³−t²+t+1)
with discriminant −44, but concerns a mod-two Artin/newform congruence,
not explicit unit localization. It provides an optional smaller-model
lead; any use here requires a certified generator isomorphism, not
replacement of g based on the displayed field alone. The example's
assertion that the displayed elliptic model has discriminant −11
conflicts with audited L070's −11^5 and is not imported. No Selmer,
unit-completeness or local-membership conclusion is taken from it.

Ping Ngai Chung and Shiyu Li, *Bounded gaps between products of special
primes*, Mathematics **2** (2014), 37–52,
[DOI](https://doi.org/10.3390/math2010037),
[inspected published PDF mirror](https://pdfs.semanticscholar.org/c3be/cfd40f4e92715bd7c414c8508f379894db9f.pdf),
Section 3.2, printed pp.50–51, uses exactly g. Its conclusion is about
rank-zero **quadratic twists over Q** with prime factors in a specified
Frobenius set; it does not identify ordinary cubic units or their
localization in the untwisted H. The relevant example and references
were read. Ono 1997, Thorne 2008 and Boxer–Diao are references for that
different twisting conclusion, not inspected unit-localization inputs.
Their stronger twist claims are not imported. The publisher page
returned 429, but the complete relevant published passage was accessible
in the mirror; this does not block this comparison.

The local assessments, L069/L070 and ATTEMPTS/032 distinguish the bare
ambient-space stop from this global-local test. They contain no unit
witness or complete negative subfield certificate to duplicate. Other
degree-36 and finite-prime stops in the supplied overview remain routing
context only; no sibling notebook was searched or used.

## Search, applicability work and stopping test

Queries included `cubic number field norm one units 2 descent local
image dyadic Simon computing rank elliptic curves`, `PARI bnfinit
bnfisintnorm bnfisunit bnfcertify fundamental units unconditional`,
`"X^3-4X^2-160X-1264" units`, `"cubic" "11a1" "units" 2 descent`,
`"norm one" "units" "2-descent" cubic`, `"11a1" "2-Selmer"`,
`"160" "1264" "cubic" elliptic units`, `"X0(11)" "cubic field"
"unit"`, `"cubic" "norm-one units" "dyadic"`, and a targeted
Stacks norm/base-change query. Searches found known machinery and the
two inspected exact-curve comparisons; no theorem directly deciding
this norm-one subfield localization was located. This is a bounded
search result, not evidence of novelty or absence of such a theorem.

Specialization is necessary because the unit representatives, exact
inclusion into D and image membership for this g are not supplied by
the known statements. A future research attempt may obtain one exact
norm-one unit and a certified nonmembership witness without computing
all units: that is sufficient for a positive answer. To certify a
negative answer, use fully certified fundamental/torsion units and
prove that the representatives exhaust U_F^1/(U_F^1)^2, where
U_F^1={u in O_F*:N_F/Q(u)=1}. Sign constraints and the distinction
from the norm-square kernel must be treated explicitly. An uncertified
finite-index subgroup, including one of unknown even index, cannot
support that negative answer.

Transport into V must use the specified generator and norm base change.
Nonsquareness in F alone cannot be carried into D without proof: the
extension has even degree over F. The approved positive certificate
must use its nontrivial localization in the whole A, or another exact
square obstruction, to justify survival in D. The complete H may be
certified by LocalImage, or by exact point images plus BPT Lemma 1.3's
matching order with all local two-torsion checked. Either approach must
use exact dyadic square tests with justified precision. No new local
theory or reproof of the index is warranted.

Continue if such a finite certificate yields an excluded global unit;
park only this subfield mechanism if complete class coverage proves
all classes are in H. A failed bounded search or backend failure is
neither outcome. The shell preflight found no `gp` on PATH, and direct
curl had a DNS failure; web primary-source access worked. The PARI
method is available as source coverage, not as a confirmed local
backend. An exact witness approach can proceed without unit-completeness
software; any negative answer still needs genuine completeness evidence.
Save unfinished work and report EXPLORATION if a bounded attempt stops
short of either certificate. No executable was installed and no
mathematical script was written or run in this review.

Mathlib matching and supporting coverage for this comparison: **not
checked**. The sources do not close full global class coverage, rank
below twelve, other-place pruning, point/coset coverage or primitive
integer lifting. This assessment approves the same exact Next action;
it does not assert a mathematical answer or progress beyond the checked
known methods.
