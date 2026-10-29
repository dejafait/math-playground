# L147 — Complete images at 3 and 5, Selmer witnesses and a rank bound

## Hypotheses

Use L138's smooth proper genus-two curve B, its Jacobian J, odd model
Y²=G(X)=(X−r)H(X), r=9075, and specified algebra Q[X]/G=Q×K:

    H=X⁴−67760X³+1581228000X²−15306287040000X+52615361700000000,
    K=Q(alpha), alpha⁴+64alpha³+150alpha²−32500alpha−109375=0,
    eta=−907500/(alpha−50), X ↦ (r,eta).

Use L135's audited maximal order O with basis (1,alpha,beta,gamma),
beta=(alpha²+14alpha+25)/50,
gamma=(alpha³+239alpha²+4475alpha+19375)/18750, its multiplication
table and complete prime lists. Use L139's supported product norm kernel
V, c=dim Cl(O[1/330])/2<=2, dim V=11+c and dim J(Q)[2]=1.
Use L140/L141's complete images at infinity and 11, and L145's complete
dyadic image and resulting filtered subspace V_old with dim V_old<=6+c.
Keep their exact ordered 39 supported witnesses and all duplicates.

No global basis, class-group equality, global independence of the 39
columns, GRH, finiteness of Sha, or pairing value is assumed. All local
maps below are the full odd-degree maps, with no scalar quotient.

## Conclusion

Use two bits (valuation parity, nonsquare normalized residue) for each
local field. Order the product components as the rational coordinate,
then primes P_27,P_28 over 3, or P_29,P_30,P_31 over 5, using L135's
zero-based order. Encode bits by their binary integer. Uniformizers are

| Place/prime | Uniformizer in O | Ramification index | Residue field |
|---|---|---|---|
| 3, P_27 | 1+gamma | 3 | F_3 |
| 3, P_28 | 3alpha | 1 | F_3 |
| 5, P_29 | beta+2gamma | 1 | F_5 |
| 5, P_30 | 1+gamma | 1 | F_5 |
| 5, P_31 | 1+4gamma | 2 | F_5 |

The complete images are

    im(delta_3)=span_F2{7,13},       dimension 2,
    im(delta_5)=span_F2{102,19,68},  dimension 3.

The formal coefficient space of the fixed witnesses surviving infinity,
11 and 2 has dimension 34. Imposing 3 and 5 leaves dimension 31.
These are coefficient dimensions, not global square-class dimensions.
The additional quotient map on this old coefficient kernel has rank
three, witnessed below. Consequently

    dim Sel²(J/Q) <= 3+c,
    rank J(Q) <= 2+c <= 4.

Two globally independent classes in Sel²(J/Q), specified by masks 165
and 132102 in the fixed zero-based 39-column order, are

    epsilon=(1/2405700000000000000,
             458232+67632alpha+251664beta−472680gamma),
    eta_class=(1/26730000000000,
               −73548−2988alpha−56376beta+138360gamma).

The symbol eta_class denotes a Selmer class, not the field generator eta.
For each displayed representative q*N(b)=1 exactly. This supplies one
eligible pair, not a nonzero pairing. The bound four misses the sufficient
bound one by three. There is no rank lower bound, full Selmer group,
point classification, integer recovery or Beal resolution. The arithmetic
replay passes; the separate critical mathematical audit of 2026-10-28
accepts these statements without a mathematical correction, as detailed below.
This is a known-method specialization, not a claim beyond the sources.

## Proof

### Imported theory and exact applicability

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-28-pair-cassels-tate-test.md`, including its
reused support and local-image assessments. Import Michael Stoll,
*Implementing 2-descent for Jacobians of hyperelliptic curves*, Acta
Arith. 98 (2001), 245–277,
[DOI 10.4064/aa98-3-4, publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83397),
Lemmas 4.1,4.3–4.4 and Proposition 4.2, pp.250–251, Proposition 4.6
and Corollary 4.7, pp.252–253, and Section 6, pp.267–272. These give
the injective odd-model cohomological norm-kernel representation, Selmer
membership by actual local images, branch/point evaluation, image dimension
m−1 at an odd place with m factors, and the sufficient outside-support
valuation condition. Authenticated images attaining m−1 prove completeness.

L138 verifies monicity, integrality, squarefreeness, genus two, a rational
odd infinity and the exact field identification. Its sufficient support is
infinity,2,3,5,11. Every odd place outside this support has discriminant
valuation zero. Thus the cited outside-support condition applies to every
supported class here; none of those places requires a point search.
The image-dimension formula includes bad reduction at 3 and 5.

Reuse the odd-residue square criterion cited in L141/L145: Pete L. Clark,
*Algebraic Number Theory II: Valuations, Local Fields and Adeles*,
[161-page author notes, Proposition 2.20 p.72 and Theorem 2.24/proof
p.73](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
accessed in the prior assessment. Over a finite extension of Q_p with
p odd, valuation parity and normalized unit residue square class are
complete square-class coordinates. This applies also to the wild cubic
at 3. No unramified or tame assumption is used.

### All local factors, uniformizers and exact square-class arithmetic

L135 enumerates every maximal ideal of O/pO, giving exactly two primes
above 3 and three above 5, all norm p. Since O is the maximal order,
these give every completion of K, with residue degree one. L138's inverse
formula alpha=50−907500/eta shows that eta generates the full local algebra;
therefore the full quintic has m=3 at 3 and m=4 at 5, including its separate
rational factor. This is not factorization in a nonmaximal power order.

Here are the exact arithmetic certificates used for the table and images.
For a prime P, construct P^n by multiplying every pair of lattice basis
vectors for P^(n−1) and P in the audited multiplication table. Integer
row reduction records both containments between that generated lattice
and the saved basis. Its determinant is p^n. The replay verifies every
forward integer combination, every reverse containment by rational
Gaussian coordinates, and every determinant. Thus each saved lattice
is exactly P^n, inductively, rather than a sublattice of the same purported
ideal. Depth at most six suffices for all calculations here.

The displayed pi_P satisfies pi_P in P but not P², proved by these exact
lattice memberships. Since O_P is a DVR this makes it a uniformizer in
the completion. Applying the same test to p gives valuations (3,1) at 3
and (1,1,2) at 5. Their sums are four, consistent with the complete prime
lists and residue degrees. L135 supplies maximality and completeness;
the valuation sum is not substituted for those hypotheses.

For integral nonzero a, determine v by a in P^v and a not in P^(v+1).
There is a unique t in {1,...,p−1} with

    a−t*pi_P^v in P^(v+1).

Indeed the quotient is the one-dimensional residue field F_p and pi_P^v
has nonzero image. This t is exactly the residue of a/pi_P^v. The two
bits are (v mod 2, nonsquare(t)). Every such membership and residue used
in the output is independently replayed, not inferred from a numerical
p-adic approximation.

For a general b in K*, clear all rational O-coordinate denominators:
a=D*b in O, D>0. Write D=p^d*u with p not dividing u. The class of b is
the class of a minus d times the locally computed class of p and minus
the unit class of u mod p. These subtractions are XOR in characteristic
two. This retains ramification in the class of p; division by p is not
treated as division by the chosen uniformizer. The rational component
uses the identical valuation/unit criterion with uniformizer p.

This proves that the reported bits are complete local square-class
coordinates and multiplicative homomorphisms, not merely tests on the
sample pool. The rational component occupies bits 0,1 and the successive
quartic-completion components occupy bits 2,3, then 4,5, and at 5 also
6,7. No coordinate is removed by a scalar quotient or a norm shortcut.

### Actual divisor images saturate the required dimensions

The rational branch divisor D_r=[(r,0)−infinity] evaluates by the imported
formula to (H(r),r−eta), where H(r)=73990352390625. In the O basis,
r−eta=−8085−220alpha+440beta−1320gamma. Its mask is 7 at 3 and 102
at 5. The complete rational component and all quartic components of
these evaluations are saved, including their exact normalized residues.

The remaining generators come from genuine Q_p points, with finite
nonbranch X-values as follows:

| p | X | G(X) | v_p(G(X)) | Unit residue | Kummer mask |
|---|---|---|---|---|---|
| 3 | 6 | −476336355067224210384 | 4 | 1 | 13 |
| 5 | 10 | −475572171659352250000 | 6 | 1 | 19 |
| 5 | 100 | −458626786603600000000 | 8 | 4 | 68 |

Each valuation is even and each residue is a nonzero square. The imported
Hensel square criterion supplies Y in Q_p with Y²=G(X), so the divisors
[(X,Y)−infinity] are actual local Jacobian classes. Their evaluations
are precisely (X−r,X−eta). These masks are checked in all components.
The signs of the displayed rational G(X) values impose no p-adic issue.

At 3 the masks 7,13 are independent. At 5 the masks 102,19,68 have rank
three. Their spans lie in the actual images and attain respectively
m−1=2 and m−1=3. Therefore they are the full images, including all divisor
classes and exceptional fibers. Rational curve points alone are not being
assumed to generate; the imported dimension theorem supplies completeness.

### The fixed witness space and the three additional conditions

Let F=F_2^39 and let phi:F→V send a coefficient vector to the product of
the fixed L140/L145 witnesses (q_j,b_j). Each is supported and q_j*N(b_j)=1;
L140's complete support proof applies to all 39 including the appended
rational elements. No injectivity of phi is needed.

Use linear normal-form reduction modulo each complete local image.
The previous real/11/2 quotient columns have rank five. Their kernel
F_old has dimension 34 and maps into V_old. Reducing the new masks at
3 and 5, and concatenating the six-bit 3-part with the eight-bit 5-part,
gives a linear quotient map on F_old of rank three. Three explicit
coefficient masks, with their entire new quotient masks, are

    22 ↦ 9058,    34 ↦ 674,    1038 ↦ 881.

Each mask on the left has zero previous quotient. The three masks on
the right are independent: the first has highest bit 13, the second
has highest bit 9, and the XOR of the last two is 467 with highest bit
8. The full replay checks every coordinate and the complete elimination,
not just these leading bits. Simultaneously imposing all five local
conditions has coefficient rank eight, leaving a full kernel of dimension
31. All 31 saved independent kernel vectors are checked as actual zero
combinations of the 39 quotient columns.

Let R:V_old→(L_3*/L_3*²)/im(delta_3) ×
(L_5*/L_5*²)/im(delta_5) be restriction followed by quotient. The preceding
three coefficient witnesses give three independent images under R∘phi.
Consequently rank R>=3, regardless of any dependencies of the global
witnesses. Rank-nullity and L145 give

    dim ker R <= dim V_old−3 <= (6+c)−3=3+c.

Every Selmer class lies in ker R by the exact local conditions. Subtracting
the rational two-torsion dimension one from its upper dimension gives
rank J(Q)<=2+c<=4. This uses only an upper bound on the full Selmer
dimension; the witness space need not exhaust it. The detected quotient
rank is exactly three on F_old, but only a lower bound three on V_old.
There is no assertion of exact ambient codimension or exact rank.

### The one selected Selmer pair and its qualifications

Masks 165 and 132102 select columns {0,2,5,7} and {1,2,10,17} respectively.
Multiplying their exact saved representatives in O gives the displayed
epsilon and eta_class. The replay checks all four O coordinates, the
rational components and the signed field norms by independent determinant
expansion. Each product has exact product norm one, so no unspecified
norm square root is required in this odd-degree representation.

Both masks belong to the complete 31-dimensional coefficient kernel.
Thus their restrictions lie in the actual images at infinity,2,3,5,11.
Their support gives the required conditions at every other place by the
imported Stoll support results. Proposition 4.2 therefore identifies them
with actual classes of Sel²(J/Q), not just supported norm-square classes.

Concatenating their full local masks (before quotient) in the bit ranges
real 0–4, 11-adic 5–8, dyadic 9–17, 3-adic 18–23, 5-adic 24–31 gives
1713291454 and 1713217696. They are nonzero and distinct; hence they are
independent over F_2. A global square class has zero localization at
every place. Independence of these localization tuples therefore proves
independence of the global classes. This does not prove independence of
any of the remaining formal kernel basis vectors.

No Cassels–Tate value is asserted. A subsequent bounded raw covering-form
test did not reach certified standard models; its unfinished calculations
and precise stop are in `drafts/2026-10-28-cassels-tate-membership-attempt.md`
and `scripts/pair-genus-two/pair-cover-gate-certificate.json`. That separate
model failure is not an input to any statement proved above and is not a
nonexistence proof for rational covering or Kummer points.

### Complete evidence, replay and scope

Reproduce the local calculation with
`python3 scripts/pair-genus-two/odd_membership_35.py`, then
`python3 scripts/pair-genus-two/verify_odd_membership_35.py`.
Full evidence is in `scripts/pair-genus-two/odd-membership-35-certificate.json`
and `scripts/pair-genus-two/odd-membership-35-verification.json`.
The replay passes 316044 checks with no failures. It uses Gaussian
coordinates instead of triangular membership, permutation determinants
instead of the producer's lattice determinant, low-bit instead of
high-bit binary elimination, and direct power evaluation instead of
Horner evaluation. It verifies all source hashes, ideal span identities,
residues, accepted/rejected square tests, generator ranks, 78 witness
localizations, all coefficient kernels and the two exact selected products.
It imports no producer arithmetic. Both still use Python fractions and
the same audited input table; this is not a formal proof or separate
critical mathematical audit by itself.

The tests are 134/200000 at 3 and 924/200000 at 5. Maximum ideal depth
is 6/64 at each place. Observed rational coefficient size is 116/8192
bits in both scripts. The full fixed domain has 39 columns; there is no
enumeration of 2^39 vectors. The initial input-schema KeyError is preserved
in `scripts/pair-genus-two/odd-membership-35-initial-schema-failure.json`;
the corrected producer recognizes L138's status field. No mathematical
failure is suppressed. No backend, external service or conditional class
calculation was used.

This advances the local descent and rank upper bound using known methods.
It leaves a three-dimension sufficient-rank shortfall in the worst allowed
case, full global generation, actual rank, point control, marked/integer
recovery and every other residual Beal signature unresolved.

### Separate critical mathematical audit — 2026-10-28

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-28-pair-three-five-membership-audit.md`.
This separate audit accepts the complete local images, the three-condition
rank deduction and the two independent Selmer classes without correction.
It reuses the precise Stoll and Clark imports above; no general descent
theorem is reproved and no claim beyond the checked sources is made.

**Actual field and complete prime lists.** L135's accepted exceptional
maximal-ideal enumeration has space IDs [185,208] at 3 and [990,997,1066]
at 5. The current full prime records, with zero-based indices [27,28]
and [29,30,31], agree with that accepted certificate, whose hash agrees
with its critical audit. Every residue degree is one. The basis and all
64 multiplication constants are the same as L138's transported maximal
order. The model certificate is also bound to its accepted audit. Thus
the counts concern the actual quartic field, not its nonmaximal power
order. The quintic has one additional rational factor and is squarefree;
the inverse formula for alpha shows that eta generates each complete
local algebra. There are exactly three and four local factors.

Both implementations were read in full. The independent replay consumes
every saved prime-power lattice. The supplement checks that every row
and every forward coefficient is integral, with exactly four basis rows
and four (at levels zero and one) or sixteen (at higher levels) generator
coefficients. Combined with the replay's two containments, these identify
the exact product ideals inductively. The determinant is p^n in each
case. No finite-precision approximation is used for these memberships.
The five printed uniformizers have valuation one, and the valuations of
rational p are respectively (3,1) and (1,1,2). The full prime enumeration,
rather than merely their degree sum, supplies completeness.

**Normalization and full local images.** The quotient P^v/P^(v+1) is
one-dimensional over O/P=F_p. Since pi^v has exact valuation v, the
recorded nonzero residue t is uniquely the residue of a/pi^v in O_P.
This proves the asserted residue normalization even for the wildly
ramified cubic at 3. For b=a/D, D=p^d*u, the denominator's square class
is d[p]+[u], where [p] is the actual two-bit class of rational p in the
completion and [u] has valuation zero and residue u mod p. Therefore
XOR subtraction used by both programs is exactly multiplication by D^-1.
It does not replace p by pi or forget the residue of p/pi^e. The standard
odd-residue Hensel square criterion makes these two bits complete and
multiplicative on the entire local field; no tame hypothesis is needed.

The branch sign is positive H(r) in the rational component and r−eta
in the quartic component, as required by Stoll Lemma 4.3. The displayed
G(6), G(10), G(100), their even valuations and nonzero square unit
residues agree exactly with the saved samples and their full evaluations.
Every component is nonzero. These are genuine Q_p point divisors; the
branch is a genuine rational divisor. There are 37 accepted/97 rejected
tests at 3 and 254 accepted/670 rejected tests at 5, all independently
replayed. Their totals are 134 and 924, with no omitted zero or duplicate
test and no depth/cap stop. Only authentication of the stated generators,
not exhaustiveness of this grid, is used in the proof.

The resulting complete spans are {0,7,10,13} at 3 and
{0,19,34,49,68,87,102,117} at 5. Their dimensions 2 and 3 equal m−1
in Stoll Lemma 4.4, which applies also at these bad odd primes. Inclusion
of the authenticated divisor classes and this dimension equality prove
completeness for the full Jacobian, including nonsampled and exceptional
divisors. Proposition 4.6 is not used at 3 or 5.

**Full witness maps and simultaneous dimension loss.** All 39 complete
ordered source records agree with L145's accepted certificate, including
the rational appended classes and duplicates. Its accepted binding and
L140's support proof cover every outside-S valuation. Every signed norm
and each of the 78 new witness localizations is independently recomputed.
The supplement independently reconstructs the old quotient columns by
enumerating the tiny complete local images at infinity,11,2 and taking
the minimum mask in each coset. It does the same at 3 and 5. These agree
with every stored quotient; all bit ranges are disjoint. All stored
pivots are genuine combinations with the stated leading bit, and all
trace and kernel lengths, coefficient domains, independence and zero
identities are checked. Thus reduction defines the asserted linear
quotient map and no truncated vector list changes the ranks.

The old coefficient kernel has dimension 34. Masks 22,34,1038 are in it
and have the printed quotient images 9058,674,881, of rank three. The
complete new map on this kernel has rank three; the joint coefficient
kernel has dimension 31. Crucially, if any global relation among those
three supported images existed, its localization in the quotient would
be zero, contradicting their independence there. Hence the map R on
the whole V_old has rank at least three. Rank-nullity subtracts this
lower bound from L145's upper bound 6+c; it never substitutes 34 or 31
for a global square-class or Selmer dimension. Every Selmer class lies
in that kernel, so dim Sel²<=3+c and rank J(Q)<=2+c. For c=0,1,2 the
rank bounds are 2,3,4, respectively one,two,three above the sufficient
bound one. No positive rank lower bound follows.

**Products and all places.** The independently rebuilt products for
masks 165 and 132102 equal all the displayed rational and O-coordinates;
their determinant norms give q*N(b)=1 exactly. The full local tuples,
ordered as (infinity,11,2,3,5), are

    165:    (30,5,352,7,102),
    132102: (0,5,208,7,102).

Each coordinate belongs to its complete local image. Every finite prime
outside S is odd with v_p(disc G)=0, by L138's polynomial discriminant,
not merely the field discriminant. Supportedness gives zero valuation
parity there; Stoll Proposition 4.6 identifies that kernel with the
local image. Proposition 4.2 consequently certifies all-place Selmer
membership. The two full localization tuples, before any image quotient,
are nonzero and distinct. Their packed masks agree with the printed
1713291454 and 1713217696, proving global independence in the full
odd-model square-class group. This argument would fail with quotient
masks or a scalar quotient; neither is used. Selmer independence does
not establish independence modulo the rational Kummer subgroup or a
nonzero Cassels–Tate value.

**Evidence and scope.** One fresh run of
`python3 scripts/pair-genus-two/verify_odd_membership_35.py` passes all
316044 checks and is identical in full to the preserved
`scripts/pair-genus-two/odd-membership-35-preaudit-verification.json`.
The fixed-domain supplement
`python3 scripts/pair-genus-two/audit_odd_membership_35.py` passes 3543
checks; full evidence is `scripts/pair-genus-two/odd-membership-35-audit.json`.
It inspects the complete relevant records, not previews. Ideal depth is
6/64 at both places; test counts are 134/200000 and 924/200000; observed
rational coefficient size is 116/8192 bits. The witness domain is 39/39,
kernel dimensions 34 and 31, and new quotient rank 3/3 required. These
are exact Python checks, not formal proofs. The original producer search
and covering experiment were not rerun. ATTEMPTS/065 and all prior
failures remain preserved. No mathematical input or DAG edge changes.

## Mathlib

Full matching Mathlib coverage for these local images, exact supported
Selmer witnesses and rank specialization has not been checked. Unknown
coverage is not evidence of absence. The exact scripts are arithmetic
certificates, not Lean proofs.
