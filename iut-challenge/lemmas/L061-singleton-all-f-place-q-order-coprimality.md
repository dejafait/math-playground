# L061 — Singleton all-F-place q-order coprimality

## Hypotheses

Retain L045,L048,L051,L060 with the same reselected E_0/Q,
F=Q(zeta_60,E_0[30]), K_glob=F(E_0[7]), u,w and fixed pointed
Tate isomorphism. In particular F/Q is finite Galois with degree
dividing 2^14*3^3*5, and E_0 over Q_3 is the pointed Tate curve
of the changed q_0 in Q_3 with v_3(q_0)=30, v_3(3)=1.
The precision remains M>=max(M_tors,31). No equality q_0=3^30
is assumed.

Condition on the native inclusions Q subset F_mod subset F subset
K_glob and restriction map rho on places. Retain L060's v_*=rho(w)
and proposed selected bad subset {v_*}. Write

    T_*={t in V(F): t restricts to v_* on F_mod}.

Use the May 2020 IUT I Definition 3.1(b)-(c) interpretation and
source-version qualifications in the pre-invocation assessment
`drafts/literature/2026-10-14-singleton-all-f-place-q-order.md`.
Here ell=7. No other unverified initial-data clause is assumed true.

## Conclusion

T_* is nonempty and consists of finite F-places above 3. For every
finite F-place t above 3, hence in particular every t in T_*, the
native integer local height is

    h_t=ord_(F_t)(q_0)=30 e_t,
    e_t=e(F_t/Q_3),
    gcd(7,h_t)=1.

Also 7 is prime to their residue characteristic 3. Thus the
q-order and residue-characteristic coprimality tests of the cited
Definition 3.1(c) pass for this proposed singleton. This is a
conditional known-method application validated by the separate critical
audit below, not sufficient initial Theta-data or an essential IUT flaw.

## Proof

### Imported definitions and transport results

Reuse the saved SPECIALIZE assessment above. In
[IUT I, May 2020 author text](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf),
Definition 3.1(b)-(c), printed pp.61-62, the tested F-place set is
the full inverse image of the selected moduli-place subset. It is
not merely the place selected by the section of K_glob-places.
As in the assessment, inspection used the 186-page reproduction;
byte identity with the author file and journal-version equivalence
remain unverified.

Mochizuki, *Arithmetic Elliptic Curves in General Position*,
[author text dated 2009-02-17](https://www.kurims.kyoto-u.ac.jp/~motizuki/Arithmetic%20Elliptic%20Curves%20in%20General%20Position.pdf),
local setup pp.14-15 and Definition 3.3 p.15, defines the height
using the surjective integer valuation of the local base field:
h_E=v_K(q_E). Its split semi-abelian setup applies here by L051.
Remark 3.3.1 p.16 concerns the extension to potentially multiplicative
reduction; that extension is unnecessary here. These are definitions,
not a newly proved local-height theorem.

[Milne, Algebraic Number Theory v3.08 (19 July 2020)](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Theorem 3.34 and its Galois case, pp.59-60, gives common ramification
and residue indices and efg=[F:Q]. The integer valuation restriction
and local completion interpretation are the inspected 7.42-7.43
and 8.10, reused through the assessment and its cited ramification
review. Apply these known results; no general theorem needs reproof.

### The actual place fiber

w restricts to u on F, and u lies above 3 by L045. The tower of
restrictions gives u restricted to F_mod equal to v_*. Hence u is
in T_*, proving nonemptiness. Since F_mod contains Q, v_* restricts
to the 3-adic place on Q. For any t in T_*, restriction through
F_mod therefore sends t to that same rational place. Thus t is a
finite place above 3. Conversely we do not assert that every F-place
above 3 restricts to v_*: F_mod may have more than one place above 3.
It suffices to prove the numerical test on the larger set of all
F-places above 3. Neither the section nor its singleton image {w}
replaces this full F-place fiber.

### Same parameter, correct normalization, uniform coprimality

Fix any t above 3. L051's all-completion transport gives a
Q_3-isomorphism F_u -> F_t, obtained from an element of Gal(F/Q).
It fixes the rational coefficients and origin of E_0 and fixes
Q_3 by continuity. Equivalently E_(F_t) is the base change of the
same pointed E_0 over Q_3. The fixed pointed Tate isomorphism of
L048 therefore base changes with the same q_0, and the reduction is
split multiplicative. There is no change of curve or geometric
parameter, and no identification of distinct embedded completions.

Let ord_t:F_t^times -> Z be surjective and positive on the maximal
ideal. Integer valuation restriction gives ord_t(3)=e_t and
ord_t restricted to Q_3^times equal to e_t v_3. Since q_0 belongs
to Q_3, substitution yields

    h_t=ord_t(q_0)=e_t v_3(q_0)=30e_t>0.

This explicitly converts absolute valuation to the native local-base
integer height. In particular the height is not asserted to be 30,
and the integer valuation of N=(K_glob)_w is not used.

Apply Milne 3.34 to the finite Galois extension F/Q at the rational
prime 3. Its efg formula shows that e_t divides [F:Q]. L045 gives
[F:Q] dividing 2^14*3^3*5. Consequently 7 does not divide e_t.
Since 7 also does not divide 30, it does not divide h_t=30e_t;
as 7 is prime, gcd(7,h_t)=1. Every t has residue characteristic 3,
which is likewise prime to 7. The argument holds for arbitrary t
above 3 and hence for every member of T_*.

### Relevance and limitations

The continuation test was a uniform pass at every required F-place;
it passes. The result closes this independent numerical prerequisite
under the conditional native field/place setup without computing
F_mod. The degree divisibility, rather than a degree upper bound,
excludes seven. No computation of an exact e_t is needed.

This does not prove all initial-data hypotheses, the native field
identification, a global theta splitting, actual input/action
realization, pilot transport, essentiality, or original finite B>=A.
The exact-curve and marked-coordinate stops ATTEMPTS/027,030,031
are preserved. The separate audit below checks this application as a
conditional local input. No original mathematical discovery beyond the
checked sources is claimed.

### Separate critical audit — 2026-10-15

**Verdict and scope.** The four specialization bridges pass under the
unchanged pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-15-singleton-q-order-critical-audit.md`.
This verifies the existing conditional conclusion; it neither computes
F_mod nor discharges the native field setup. The IUT reproduction and
GenEll author-version qualifications above remain in force. The known
Tate, valuation and Galois theorems are imported by the precise citations
above, without reproof or a new general height assertion.

**Full fiber.** The place u is the restriction of the retained w to F.
Associativity of restriction in the assumed field tower gives
u restricted to F_mod = w restricted to F_mod = v_*, so u witnesses
nonemptiness. For an arbitrary t in T_*, restriction further to Q is
v_* restricted to Q, which is the 3-adic place since w lies above 3.
Thus t is finite of residue characteristic three. This verifies the
entire inverse image required in the cited clause (b). It uses neither
a transitive action over F_mod nor equality of T_* with all places
above 3. L060's section has just one selected K_glob-place above v_*;
that different singleton supplies no restriction on the size of T_*.

**Pointed parameter and split setup.** For every t above 3 the natural
completion map Q -> F_t extends to Q_3 -> F_t. Base change of the
fixed pointed Q_3-isomorphism in L048 therefore gives an isomorphism
from the same E_0 over F_t to the Tate curve of the image of q_0.
This also verifies the transport in L051: its Galois-induced completion
isomorphism fixes the dense Q, hence Q_3, including q_0. The origin is
preserved throughout. F_t is a finite extension of Q_3 and q_0 has
strictly positive absolute valuation, so the inspected Tate theorem
applies. In particular this is the split multiplicative case required
by GenEll's semi-abelian setup, with split torus special fiber; no
potentially multiplicative extension or division by a further extension
index is needed. The stable nodal compactification is not itself being
substituted for that semi-abelian group scheme. Neither a twist nor the
old rational parameter 3^30 enters this base change.

**Integer normalization.** The local base in GenEll Definition 3.3 is
F_t. For its surjective integer valuation, Milne's valuation restriction
gives ord_t restricted to Q_3 = e_t v_3. In particular ord_t(3)=e_t,
where e_t is the ramification index over Q_3, not over F_mod. Since
q_0 is in Q_3 and v_3(q_0)=30, the imported definition gives exactly
h_t=30e_t. It is a positive integer. The argument would not establish
the asserted test by substituting the absolute value 30 or ord_N(q_0);
N is the completion of a different global field and is not this base.

**Divisibility and uniform quantifier.** L048 applies L045 to the very
same reselected E_0, so F is its actual full 30-torsion/cyclotomic
compositum. L045's faithful torsion representation, CRT and compositum
restriction give [F:Q] dividing 16*(6*48*480)=2^14*3^3*5. The audit
checked that this is divisibility, independent of intersections of the
generating fields, and that F/Q is finite Galois. Apply Milne 3.34
with the Dedekind domain Z and its integral closure O_F at (3).
Its Galois efg formula, with completion interpretation, gives
[F:Q]=e_t f_t g, so e_t divides the displayed seven-free integer.
Hence 7 does not divide 30e_t. Since 7 is prime, this is precisely
gcd(7,h_t)=1, and gcd(7,3)=1 also holds. The argument fixed an arbitrary
t above 3, so it proves the test simultaneously on the possibly smaller
nonempty T_*. No place was omitted and no local degree bound was used
in place of divisibility.

The direct mathematical inputs remain L045,L048,L051,L060; their
inherited hypotheses have not been strengthened or certified anew.
No extra dependency or calculation certificate is required. This is
independent verification of a known-method specialization, with no
new theorem beyond the checked sources, full initial-data assembly,
actual input/action/pilot/essentiality bridge or finite B>=A conclusion.

## Mathlib

Full matching Mathlib coverage of this native singleton application
has not been checked. No absence claim is made. Galois ramification,
valuation restriction and coprimality are supporting known results;
the native predicates are imported by the precise citations above.
No mathematical script or numerical certificate is needed.
