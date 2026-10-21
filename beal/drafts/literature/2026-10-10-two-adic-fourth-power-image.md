# Two-adic fourth-power image — source assessment

TARGET: Determine whether the primitive fourth-power condition at two strictly shrinks the complete whole-fiber connecting-class image for L033's 54a1 branch.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact fourth-power/X0(11)/54a1 and two-adic fifth-isogeny searches found no inspected matching image comparison; local duplicate checks covered L032-L034, L035/L037's baseline definitions and ATTEMPTS/008,010,012,013. Search failure is not evidence of novelty.
SOURCE_EVIDENCE: Read FNS final June 10, 2019 manuscript Section 7.2 transport, (7.2), Lemma 7.3, Lemma 7.5 statement/proof, Lemma 7.6 hypotheses and relevant proof cases, and Lemma 7.12's entire 54a1 cusp case; read Schaefer-Stoll June 13, 2001 manuscript Lemmas 4.2-4.5 statements/proofs, and Clark's Hensel and Eisenstein/local-integer-ring statements below. Reused foundation 15 and L033-L034's audited interface.
COMPARISON: FNS Lemma 7.6 explicitly excludes the 54a1 cusp domain and concerns a two-descent square class; its conclusion cannot answer this target. Schaefer-Stoll does supply the unrestricted prime-to-residue-characteristic isogeny image theorem, so test that baseline before any disk enumeration. The exact fiber/power comparison still requires a local specialization.
GAP: Certify all factors and residue fields of K tensor Q2, apply the local image theorem with the dual kernel, and decide whether a complete compatible fiber with common primitive even-C/odd-B fourth-power witnesses realizes each baseline class. No factorization, witness, nonemptiness or strictness/equality is proved in this review.
REASON: Essential theorem coverage is now ready for one bounded mathematical attempt on the unchanged target; known prime-to-two isogeny theory is the screening mechanism, with exact local algebra and common-witness verification as the necessary specialization rather than a reproof of descent.
SCOPE: Complete twelve-dimensional algebra, all finite unbranched modular fibers and their isomorphisms, the dual five-isogeny and good-divisor exceptional values, and common primitive two-adic scalar witnesses in L032's 54a1 branch; no global arithmetic or Selmer equality.

The main gap is still unconditional global emptiness of the 54a1 branch,
plus four other twists and infinitely many signatures. The intermediate
target tests whether coupling an entire modular fiber to the original
common primitive cube/fourth/eleventh scalar witnesses at two removes a
connecting class. Use L032's even-C, odd-B branch and retain the full
fourth-power identity. Do not replace the unrestricted whole-fiber
baseline by unrestricted independent points on E0's factors: the latter
can give an inherited restriction with no additional power information,
as recorded in ATTEMPTS/010 and the later five-adic equality.

Exact inputs to assess are L032's branch and Lemma 7.3 application,
L033's K, E0 and normalized dual connecting map, and L034's entire
modular map with its exceptional charts. No cross-notebook input.
The decomposition of K tensor Q2, prime identifications, exact unit
classes and common primitive scalar domain are unresolved. All
whole-fiber isomorphisms, factor embeddings, exceptional evaluations
and class collisions must remain. No global class data, GRH, rank,
Sha, positivity over Q2 or integer lifting is presumed.

## Precise source comparison

**FNS:** Freitas, Naskręcki and Stoll, *The generalized Fermat equation
with exponents 2, 3, n*, Compositio Math. **156** (2020), 77-113,
[DOI](https://doi.org/10.1112/S0010437X19007693),
[final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
internally June 10, 2019. Printed pages, rather than zero-based PDF indices,
are used. Read pp.25-28 and the complete 54a1 case on pp.32-33.
The paragraph following (7.2) states constancy of entire fiber type on
each listed set, excluding the branch scalars. Lemma 7.3 supplies the
54a1 domain. Lemma 7.5 requires its coefficient normalization, a nonzero
linear term, characteristic not dividing the branching degree, and all
stated strict radius bounds; it is not an unconditional precision cutoff.
Lemma 7.6 excludes the cusp domain explicitly. Its other cases use
root-by-root analytic coverage, unique y reconstruction and a valuation
test for square classes; these are not fifth-power conclusions.
The last case of Lemma 7.12 treats both cusp branches and uses expansions
over Q2(2^(1/11)); its elimination also uses the computed global
two-Selmer image. Neither that conditional elimination nor its GRH-based
global data is imported. The expansion field alone is not a certified
factorization of our defining polynomial.

**Schaefer-Stoll:** *How to do a p-descent on an elliptic curve*,
Trans. AMS **356** (2004), 1209-1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X),
[long author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
June 13, 2001, printed pp.6-7, Lemmas 4.2-4.5.
For an isogeny theta:E -> E' with kernel of exponent p, at a finite
place not above p, Lemma 4.5 identifies the connecting image with the
unramified subgroup if neither Tamagawa number is divisible by p.
Lemma 4.2 gives this subgroup's size as #E(K_v)[theta].
Its proof uses the Frobenius-minus-one kernel/cokernel on inertia
invariants. Lemma 4.3 proves unramifiedness through surjectivity on
the prime-to-p formal group and the smooth special fiber over the
maximal unramified extension. Lemma 4.4's quotient-size formula is
cited there to reference [24], Lemma 3.8; that original reference
was not reread. Import the stated theorem, without rederiving it.
For application, use L033's theta:E1 -> E0 and E1[theta]=mu_5,
not E0's constant forward kernel. Check both curves' good reduction
and every actual residue field before asserting any image size.
L033's audited discriminants and foundation 15 provide the existing
interface; this theorem does not itself identify the restricted fiber image.

**Local algebra inputs:** Pete L. Clark, *Algebraic Number Theory II:
Valuations, Local Fields and Adeles*,
[author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
accessible 161-page version, no identified revision date. Read Theorem
1.75 and Corollary 1.77, printed p.57; Theorem 1.79, p.58;
Theorem 2.8, p.64; Proposition 2.9 and Corollary 2.10, p.65.
Over a complete valued field, coprime residue factors of a primitive
integral polynomial lift; a simple residue root lifts. Hensel-Newton
requires |H(a)|<|H'(a)|^2. An Eisenstein monic polynomial over a DVR
is irreducible; its root generates the integral closure, a DVR with
the original residue field and total ramification. These inputs cover
exact factor and residue-field certification if their coefficient
hypotheses are verified. They also cover normalized unit-root equations
over Q2 and its finite extensions. Foundation 17's Hensel-Newton
coverage is reused; no fourth-root simple-derivative assumption at two
is permitted. No local factorization or power surjectivity is derived here.

## Exact mathematical continuation covered

Use L033's polynomial to certify the **entire** algebra A2=K tensor Q2.
Verify local integer rings/residue fields via the cited lifting and
Eisenstein criteria, rather than reading prime data from the nonmaximal
global power order. Apply the cited isogeny image theorem factorwise
using the dual kernel. If it makes the whole connecting image trivial,
do not enumerate disks: verify whether I_pow is nonempty; a single
fully justified whole-fiber/common-witness example then decides the
comparison. If the unrestricted image is nontrivial, the target still
requires a baseline class absent at **all** allowed witnesses and
isomorphisms, or a proof that every baseline class is realized.
This is a conditional test plan, not a conclusion about either image.

Define I_fiber over Q2 exactly as L035's definition over Q5: all finite
s other than 0,1728, every isomorphism of the complete fiber algebra
with A2, and the product connecting class of its tautological point.
Define I_pow using the same data plus one shared nonzero a,b,c in Z2,
at least one a unit, a^3+b^4=c^11, s c^11=1728 a^3, b odd and c even,
with a=7 modulo 8 as required by L032. Do not add positivity over Q2
or the separate three-adic residues. Retain the same c in both
identities. The L032 scalar domain is necessary; sufficiency for these
common witnesses remains a mathematical check. Do not assume every
compatible fiber lies in that domain unless proved or explicitly cited.
L033-L034 retain j(T), the removable x=16 chart and all embeddings.
L035/L037 are definition/encoding precedents, not a transfer of any
five-adic image theorem to two. Equality must handle empty images as
well as nonempty ones; identity of an unrestricted image alone is
insufficient without restricted nonemptiness or baseline emptiness.

The calculations are justified only to screen these hypotheses and
decide this explicit specialization; a reproof of general descent or
a broader two-adic classification is unnecessary. Preserve all class
collisions and exceptional evaluations. No result of this plan is
asserted in the literature turn.

## Search, duplicates and access

Queries included `"X0(11)" "fourth" "2-adic"`,
`"54a1" "5" "descent" local`,
`"five-isogeny" "good reduction" local image`,
`Freitas Naskrecki Stoll "54a1" "fourth"`,
`"X0(11)" "fourth power" descent`,
`"5-isogeny" "unramified subgroup"`,
`"54a1" "2-adic" "fifth"`,
`"primitive" "fourth" "connecting" "X0(11)"`, and
`"54a1" "Q2" field`. Inspected matches were the primary sources
above. No exact comparison theorem was located. The author's paper
on exponents (2,3,25), Cesnavicius's *Selmer groups as flat cohomology
groups*, and general modular-curve notes were indexed leads only,
not theorem inputs; no stronger applicable conclusion is claimed.

Local checks read the needed L032-L034 proofs, L035/L037 definitions,
foundation 15, the existing even-C/local-five assessments and
ATTEMPTS/008,010,012,013. The historical five-adic equality and global
class-data blocker do not decide this target. Repeated verification of
L033 or enlarging the failed witness boxes is not proposed.
Primary PDFs were accessible through the web reader. Shell download
failed DNS resolution; an alternate FNS export endpoint also failed.
Neither blocks the inspected theorem statements and essential cases.
No mathematical scripts ran and no lemmas were changed.

A certified strict subset would justify a separately assessed global
coupling test; equality would retire this extra two-adic power filter.
Neither result by itself excludes integer solutions. A persistent
essential source blocker requires parking dependent work and selecting
a different independently testable target. Mathlib matching coverage
is not checked, rather than asserted absent.
