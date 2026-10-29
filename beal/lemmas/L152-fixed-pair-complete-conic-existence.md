# L152 — Complete branch-pair conic existence for the fixed classes

## Hypotheses

Use L138's actual monic odd model G=(X−9075)H, its root map
theta=−907500/(alpha−50), and L135's maximal order of K=Q(alpha), where

    A(X)=X^4+64X^3+150X^2−32500X−109375.

Use the full Q×K representatives of eta_class and nu from L147/L149,
with masks 132102 and 3109, respectively, without a scalar quotient.
Their quartic components b are exactly those in L150/L151. In particular
their valuations are even at every K-prime outside 2,3,5,11. Retain the
conic convention and completed local evidence of L150/L151:

    C_ij: b_j u²−b_i v²+(theta_j−theta_i)w²=0

for two distinct quartic branches, with the appropriate rational
component q at the rational branch. The ordered distinct quartic pairs
have the single degree-twelve field M proved in L151. No assertion of
goodness, explicit global solution, pairing value or rationality of a
Selmer class is assumed.

## Conclusion

For each fixed class every quartic-pair conic has a point at every
completion of M, and hence an M-rational point. Together with L150,
every branch-pair orbit conic has a point over its actual root-pair
field. Each also has an affine point with w=1.

The separate conceptual audit below accepts this existence statement.
It also clarifies its source-level consequence: both classes satisfy
Shukla's existential good-element condition, by choosing points in the
orbit fields and transporting them. The choices can have uv!=0 in the
affine chart. Explicit global coordinates and their checked transport
are not provided, so the constructive certificate remains unfinished.
No Cassels–Tate value, rank improvement, point control or Beal resolution
is asserted. This is a specialization of known methods, not a new
general conic or pairing theorem.

## Proof

### Known inputs and local convention

The assessed method is Shukla, *On computation of the Cassels–Tate
pairing*, Bayreuth thesis (2024, repository publication 2025), DOI
[10.15495/EPub_UBT_00008348](https://doi.org/10.15495/EPub_UBT_00008348),
Section 4.4, Assumption 4.4.3 and Proposition 4.4.4, printed pp.109–111,
and Algorithm 2, pp.113–114, in the
[published primary thesis](https://epub.uni-bayreuth.de/id/eprint/8348/1/thesis.pdf).
We specialize only its defining conics. The prior SPECIALIZE assessment
is `drafts/literature/2026-10-29-shukla-good-element-conics.md`.
No additional general pairing construction is derived or invoked here.

Import the standard named Hasse–Minkowski theorem over number fields:
a nondegenerate quadratic form is isotropic over the number field iff
it is isotropic over every completion. The standard odd local quaternion
criterion, with its sign convention reproduced in L150, is sufficient
for all new places. In a complete discretely valued field of odd residue
characteristic, a unit with square residue is a square by simple Hensel
lifting. For a uniformizer varpi and residue quadratic character chi,

    (varpi^m u,varpi^n v)=chi(−1)^(mn) chi(u)^n chi(v)^m.

In particular both even valuations imply splitting, regardless of the
unit residues or residue degree. These are imports/short reproductions
of the known conic method, not new general results.

Multiplying the two quaternion entries b_i/b_j and
(theta_i−theta_j)/b_j by the square b_j² gives the convenient entries

    a=b_i*b_j, c=(theta_i−theta_j)*b_j.                 (1)

Indeed U=b_j*u, V=v gives U²−a V²=c w². Thus a square suffices for
solubility, as does the even-valuation criterion. Reversal exchanges u,v
and negates the original equation, so tests cover reversed pairs too.

The new producer rebuilds both entire representatives from the fixed
39-column order and compares them coefficientwise to L150's full
products. The replay does so independently in the integral basis.
No masks are treated as coefficients, and no scalar normalization is
used to change the conics.

### Every remaining pair above three

L135/L150 give K tensor Q_3=Q_3×F, with F totally ramified of degree
three and residue field F_3. The Q_3 branch is the simple root alpha=2
modulo three. Since A mod 3=(X−2)(X−1)³, all three roots of the cubic
local factor reduce to one;
the exact maximal-order prime certificate checks v_F(alpha−1)>0.
Normalize v_F(3)=3 and extend this valuation, with this normalization,
to an algebraic closure. Fractional values are allowed in this paragraph.
L150 already covers pairs between the simple branch and a cubic branch.

Fix a cubic branch alpha_i, put Z=alpha_j−alpha_i, and deflate:

    A(alpha_i+Z)/Z
      =A'(alpha_i)+(6alpha_i²+192alpha_i+150)Z
        +(4alpha_i+64)Z²+Z³.

The four coefficient valuations, in ascending powers, are exactly
(5,3,0,0). These are certified by maximal-order ideal membership at
L135's zero-based prime index 27, including leading residues and
nonmembership in the next ideal power. If alpha_j is another cubic
branch, t=v_F(Z)>0. The four term valuations are

    5, 3+t, 2t, 3t.

If 0<t<5/2, 2t is the unique minimum; if t>5/2, 5 is the unique
minimum. Neither permits a zero sum in a valued field. Thus t=5/2
for every distinct within-cubic pair. This uses only the ultrametric
inequality, not an assumption about a Galois group or completion count.

Write b(alpha_i+Z)−b(alpha_i)=b_1 Z+b_2 Z²+b_3 Z³. Exact coefficients
are the usual Taylor coefficients b_k=sum_(j>=k) binom(j,k)b_j
alpha_i^(j−k); no derivative denominators are omitted. The certificates
give the following valuations in the same normalization:

| Class | v_F(b_i) | v_F(b_1),v_F(b_2),v_F(b_3) | Lower bound on v_F(b_j−b_i) |
|---|---:|---|---:|
| eta_class | 3 | 2,0,0 | 9/2 |
| nu | 4 | 2,0,0 | 9/2 |

Thus b_j/b_i has residue one in every actual pair completion. Since
three is odd it is a square there. Consequently a=b_i²(b_j/b_i) is
a square, and every remaining conic above three splits. This argument
covers all extensions containing the pairs; no untested component of
M tensor Q_3 is discarded.

### Every remaining pair above five

The complete local decomposition from L135/L150 is Q_5×Q_5×F_2,
where F_2/Q_5 is a ramified quadratic extension with residue F_5.
The first rational branch alpha_0 is the simple root alpha_0=1 mod 5.
The other rational branch is alpha_1=50+125x, where

    A(50+125X)/390625
       =625X^4+1320X³+990X²+308X+33.

This polynomial has the simple root x=4 mod 5 (derivative 3 mod 5).
Coefficientwise substitution authenticates the displayed identity.
For both root polynomials all 23 Hensel digit steps are saved and replayed,
yielding root precision 24; alpha_1 has precision 27 after scaling.
Exact membership of alpha−alpha_k(approx) to the claimed depth identifies
the two rational completions as prime indices 30 and 29, respectively.
Both have ramification one. After the inverse affine change the actual
root in the indicated completion lies in the simple Hensel disk, so
uniqueness identifies it with the lifted Q_5 root.

L150 tested alpha_0 against alpha_1 and against F_2. Reversals are
equivalent conics. The sole new mixed type is alpha_1 against F_2,
at prime index 31, whose normalization is v_F_2(5)=2. Using the saved
approximation t to alpha_1, the exact rational-polynomial arithmetic gives

    a_t=b(t)/b(alpha), c_t=(theta(t)−theta(alpha))/b(alpha).

For both classes their respective (valuation, square-class mask) pairs
are ((5,1),(1,1)). Here mask=m mod 2+2*(nonsquare residue bit), in
L150's fixed prime uniformizer. In particular both normalized unit
residues are squares. The odd Hilbert formula gives +1 because
chi_5(−1)=+1. The independent replay checks the full coefficient
identities after multiplication by b(alpha), and each ideal-power
valuation/leading-residue certificate, not merely these masks.

The exact coefficients have the same leading classes as these
approximations. For h=b or theta the polynomial difference error in
F_2 is at least

    2*(27+min_k v_5(h_k))−v_F_2(b(alpha))=45.

This is strictly above both computed valuations 5 and 1. Thus both
actual mixed conics split. No approximate point or approximate symbol
is used as a substitute for a stability proof.

It remains to pair the two quadratic roots. They both belong to F_2;
this exhausts this type because a quadratic extension is normal. In
both classes v_F_2(b_i)=v_F_2(b_j)=1. Their sum is the quadratic
local trace of b, computable by removing the two rational contributions
from the global trace. The exact global power traces are

    Tr(1),Tr(alpha),Tr(alpha²),Tr(alpha³)=4,−64,3796,−135844.

The producer obtains these from multiplication traces in the power
basis; the replay uses the maximal-order multiplication table. Subtract
b(alpha_0(approx))+b(alpha_1(approx)) from Tr_K/Q(b). The resulting
rational approximation has F_2-valuation 2 for eta_class and 4 for nu.
The exact trace differs from it by valuation at least 40, since the
smaller of the two root precisions is 24, the minimum b-coefficient
valuation is −4, and v_F_2(5)=2. Both actual trace valuations are
therefore strictly greater than one.

It follows that (b_i+b_j)/b_i lies in the maximal ideal, so b_j/b_i
has residue −1=4 in F_5. This is a square residue (2²=4), hence a
square in F_2. Equation (1) has square a and the remaining conics split.
The local decomposition lists all four roots: pairs of the two rational
roots, pairs between a rational root and a quadratic root, and the two
quadratic roots exhaust every possibility, with reversals as above.

### Every pair above eleven

There is just one K-prime above eleven, totally ramified of degree four
with residue F_11. Normalize v_F(11)=4. For a fixed root alpha_i the
same deflated difference polynomial has coefficient valuations
(3,2,1,0), certified at prime index 1. If t=v_F(alpha_j−alpha_i),
the term valuations are 3,2+t,1+2t,3t. All roots are integral. For
t<1 the last term is uniquely minimal; for t>1 the first is uniquely
minimal. Thus every distinct root difference has t=1. This remains
valid at every pair completion, with the extended normalization.

Every conjugate alpha_i−50 has valuation one, since there is one
K-prime. The exact root map gives

    theta_i−theta_j
      =907500*(alpha_i−alpha_j)/((alpha_i−50)(alpha_j−50)),

so its valuation is 4*v_11(907500)+1−1−1=7. For eta_class every
conjugate b_i has valuation one. Equation (1) therefore has valuations
v_F(a)=2 and v_F(c)=8. In an actual completion of M these are multiplied
by an integer ramification index, and hence are both even. Its odd
Hilbert symbol is +1, whatever the residue extension.

For nu every b_i has valuation zero, and the three Taylor coefficient
valuations are (0,0,4). Since each root difference has valuation one,
v_F(b_j−b_i)>=1>0. Thus b_j/b_i is a principal unit and a is a
square. These two arguments cover every root pair and every completion
above eleven without assuming the residual cubic splits in K_F.

### Every place outside the support, and local-global assembly

L138's exact discriminant and resultant identity gives

    disc(H)=2^32*3^11*5^15*11^21,
    disc(G)=disc(H)*H(9075)²,
    H(9075)=3^5*5^6*11^7.

For any finite M-prime above p outside 2,3,5,11, each theta_i is
integral because H is monic integral. In a splitting field the product
of all six squared quartic root differences is disc(H), a unit at p.
Each factor has nonnegative valuation, so every difference is a unit.
Restriction to M retains that conclusion for the selected pair.

Full supportedness of the two representatives, as proved in L147/L149,
means v_P(b) is even at every K-prime outside the support, not merely
that N(b) has even valuation. Each embedding of b into M therefore has
even valuation, by restriction of valuations and an integer ramification
index. Equation (1) has even valuations for both entries. The odd
Hilbert criterion gives splitting at every such place. This argument
does not require a maximal order or a discriminant computation for M.

The sections above cover all places of M above 3,5,11. L151 covers its
entire dyadic part, and L150 covers every real ordered pair. These are
all archimedean places: any embedding sends both alpha roots to real
roots of A; complex places, if present, would in any event split.
Thus each conic over M is soluble at every completion. Its three
diagonal coefficients are nonzero, so it is nondegenerate.
Hasse–Minkowski supplies an M-point. L150 already proves the analogous
global existence for the rational/quartic orbit. Over either infinite
number field a smooth conic with a point has infinitely many points by
projection from that point, while w=0 contains at most two; hence each
also has a point with w=1.

This existence proof does not furnish the explicit field coordinates
required by the approved constructive certificate. Constructing and
checking coordinates remains future work. The conceptual audit below
settles the existential compatibility distinction; no pairing follows
from conic existence.

### Certificates, failed runs and reproducibility

Run `python3 scripts/pair-genus-two/shukla_odd_pair_conics.py`, then
`python3 scripts/pair-genus-two/verify_shukla_odd_pair_conics.py`.
Full evidence is in
`scripts/pair-genus-two/shukla-odd-pair-conics-certificate.json`;
the independent O-basis replay is
`scripts/pair-genus-two/shukla-odd-pair-conics-verification.json`.
The producer passes 84 checks. The replay passes 756 direct and
123280 helper checks, including every saved ideal-power forward and
reverse containment, determinant, full coefficient, residue and Hensel
digit. Both new mixed symbols are +1. Its scope is the fixed two masks.

The two simple root lifts use exactly 46/46 digit steps, precision
24/24. Maximum ideal depth is 28/64. The producer's full saved rational
size is 4874/8192 bits; the replay helper's observed arithmetic size is
230/8192 bits (a helper statistic, not a bound on all saved evidence).
No conic point search or external number-field backend is used.
The initial input-schema and string-resultant parsing failures are
preserved as `shukla-odd-pair-conics-initial-*-failure.json` in the same
directory. Neither was mathematical evidence; both were corrected
before the passing replay. No completed rational-row or dyadic test was
regenerated. The local progress is a standard arithmetic specialization,
not a claim of progress beyond the cited general methods.

### Separate conceptual audit — 2026-10-29

The gate is
`drafts/literature/2026-10-29-complete-conic-existence-audit.md`.
The full L150–L152 proofs, four complete independent replay programs
and their arithmetic interfaces were reviewed. All four replays pass;
the new odd-pair replay has 756 direct and 123280 helper checks, no
failures, 46/46 root-lift steps, precision 24/24 and ideal depth 28/64.
It checks the complete lattice witnesses, coefficients, valuations,
leading residues and all lift digits. L150 and L151 record the other
three replay counts and their conceptual acceptance. The original
certificate flags `good=null`/`full_goodness_decided=false` are retained:
those finite arithmetic programs did not prove the global transport
assertion. The present prose supplies its mathematical justification.

**All embeddings and places.** L138 authenticates the same monic
quintic, quartic factor and inverse root maps. L147/L149 authenticate
the actual masks and supported products, including every prime rather
than norm parity alone. The conic coefficients agree exactly after
multiplication by b_j; square normalization and reversal are invertible.
No rational scalar quotient was substituted for the full Q×K tuple.

Above three the local factor degrees 1+3 exhaust all four roots. The
simple/cubic pairs were covered by L150. In the cubic cluster the
deflated coefficients have valuations (5,3,0,0). For a positive root-gap
valuation t, the only possible minimum attained twice is at t=5/2.
The Taylor lower bound 9/2 is strictly greater than each b-valuation
3 and 4. Thus the ratio is a principal unit in every pair completion,
even when its valuation relative to the cubic field is fractional.
Rescaling to that completion's integer normalization preserves this
strict inequality. Odd Hensel lifting proves it square there.

Above five the two rational branches and the ramified quadratic give
all types. The exact root-membership certificates identify the lifted
rational branches with indices 30 and 29, not merely roots with similar
residues. For the new mixed type the error bound 45 exceeds both 5 and
1. The residue signs and chi_5(−1)=1 give splitting. In the quadratic
pair the nontrivial local automorphism preserves valuation, so both
b-values have valuation one. Removing the two rational components
from the trace gives valuations 2 and 4 with error >=40, strictly
larger than those values. The ratio has residue −1, a square in F_5;
quadratic normality accounts for the entire remaining pair type.

At eleven, the sole quartic place makes the coefficient valuations
uniform across all embeddings. The deflated polynomial forces every
distinct root gap to have valuation one in the stated normalization.
The denominator valuations in the root map are both one, yielding
theta-gap valuation seven. For eta_class the two symbol valuations
2 and 8 stay even after multiplication by the integer ramification
index of any pair completion. For nu the Taylor bound makes the ratio
a principal unit. Neither argument assumes a single M-place above
eleven or concludes squareness from a norm.

At primes outside the support, integrality and the unit discriminant
make every root difference a unit in a splitting-field completion.
Restricting to M preserves this, while extending each even K-valuation
of b multiplies it by an integer. Both entries in (1) therefore have
even valuation in every M-completion outside 2,3,5,11. This holds for
arbitrary residue degree by Voight's odd local criterion cited in
L150. L151 supplies the unique dyadic completion; the exhaustive real
root pairs in L150 supply all real embeddings. These arguments cover
every place, without a maximal-order computation for M.

Each orbit conic is a nondegenerate ternary form over the actual
number field K or M: its b-values and distinct root gap are nonzero.
Voight, *Quaternion Algebras*, GTM 288 (2021),
[Theorem 14.6.9](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_14)
therefore applies over each field separately. The all-place conclusion
is accepted without an arithmetic correction. This remains an
existence theorem, not a saved coordinate solution.

**Existential goodness and the constructive boundary.** Shukla's
Section 4.4, printed p.109, explicitly transports a point in an orbit
field; Assumption 4.4.3 on p.110 requires the resulting equivariance.
The terminology following Proposition 4.4.4 on p.111 is existential.
Algorithm 2 on p.113 additionally asks for nonzero coordinate products.
These precise interfaces were checked in the
[published thesis](https://epub.uni-bayreuth.de/id/eprint/8348/1/thesis.pdf).

Here the ordered off-diagonal pairs have three orbits: (r,theta_i),
(theta_i,r), and (theta_i,theta_j), i!=j, of sizes 4,4,12. Their
stabilizer fields are K,K,M. Choose a point in each representative
field, whose existence has just been proved. In a splitting field,
an element fixing the ordered pair fixes its entire field and hence
the point's coordinates. Transporting that point by any automorphism
carrying the representative to a given ordered pair is consequently
independent of the chosen automorphism. This defines equivariant
choices on every orbit; restricting to a fixed first root gives
exactly the source's condition over that root field.

There is no additional simultaneous reversal-swap constraint in that
condition. In the quartic-pair orbit a reversed point is obtained by
the relevant field embedding; the solubility proof's variable-swap
argument does not require that this conjugate equal the variable swap
of the initially chosen point. For the two different rational/quartic
orbits either independently chosen points or reversed choices suffice.

A smooth conic with a field point over an infinite field is rational
by projection and has infinitely many field points. None of the three
coordinate lines contains it; each removes at most two geometric
points. We may therefore choose points with uvw!=0 and set w=1.
Conjugation preserves this condition. Both fixed Selmer classes thus
are good in the source's existential sense, even with this nonvanishing
requirement. This corrects any reading of the earlier constructive
qualification as an extra unknown existence or compatibility obstacle.

No coordinates, cochain, auxiliary pairing-place support, local halves
or pairing value have been computed here. Those tasks must check their
own conventions and equations; the printed algorithm's variable and
guard cautions remain. Rational Kummer membership, generation, the
rank-one threshold, marked/integer recovery and other Beal signatures
remain unresolved. The audit establishes a relevant known-method input
and repairs its boundary statement; it claims no general novelty.

## Mathlib

Full matching coverage for these instance conics, all their local
arithmetic and Shukla's good-element construction was not checked.
The standard Hasse–Minkowski, Hensel and quaternion inputs are named
mathematical imports; no matching Lean theorem or formal verification
of the scripts is asserted. Unknown coverage is not evidence of absence.
