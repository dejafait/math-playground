# Direct quartic-algebra pairing mechanism: source comparison

TARGET: Assess a direct quartic-algebra Cassels–Tate evaluation for the audited pair eta_class,nu, testing whether the rational branch removes the need for ATTEMPTS/065's raw covering models.
CHECKED: 2026-10-29
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the saved Fisher–Yan comparison and ATTEMPTS/065–066; searched Shukla Stoll Cassels Tate pairing hyperelliptic odd degree explicit formula, Cassels Tate pairing genus 2 rational Weierstrass point quartic algebra formula, and exact phrase Cassels-Tate quartic algebra. Retrieved Shukla's complete 2024 thesis, published in the Bayreuth repository in 2025; the previously unread odd-degree lead now has theorem-level coverage.
SOURCE_EVIDENCE: H. Shukla, On computation of the Cassels-Tate pairing, DOI 10.15495/EPub_UBT_00008348, published thesis.pdf, 165 PDF pages: Chapter 4 setup pp.85–86; Section 4.2 and Theorem 4.2.1 with its orbit/corestriction proof pp.88–89; Proposition 4.3.13/Corollary 4.3.14 with proofs pp.97–98; Section 4.3.3/Proposition 4.3.15/equation (4.3.7) pp.99–100; Lemma 4.3.19/Corollary 4.3.20 with proof pp.105–106; Algorithm 1 pp.106–107; Section 4.4 through Proposition 4.4.4 with complete proof pp.107–111; Remark 4.5.1/Algorithm 2 pp.113–114. Reuse Fisher–Yan and Stoll only within the existing assessment's scope.
COMPARISON: Shukla supplies an odd-model method avoiding explicit torsor equations and full rational two-torsion. The simpler construction is conditional on equivariant branch-pair conic solutions (Assumption 4.4.3), not on the existence of a rational branch alone. The 1+4 algebra permits orbitwise computation over Q and K, but does not remove the quartic orbit, the conic conditions, local halves or auxiliary-cochain support.
GAP: No good-element test, cochain construction, lifted local evaluation or pairing value has been computed for eta_class,nu. Complete branch-pair conic solubility is an independently testable gate for the simpler method; a passing test is not a pairing certificate or a rank improvement.
REASON: A primary constructive replacement changes the route beyond ATTEMPTS/065's raw-model box. Prepare a separately approved finite conic-condition test by standard specialization; do not claim a new formula or justify a creative label merely by this source import.
SCOPE: Exactly TARGET on L138's Jacobian and the audited L147/L149 masks 132102 and 3109; no new witnesses, enlarged searches, class-group computation or cross-notebook input.

## Relevance, inputs and discriminating source test

The main gap remains point control at rank <=2+c<=4 and then marked/integer
recovery and residual signatures. A certified pairing value on these two
classes could constrain rational Kummer and strengthen rank control; three
Selmer classes alone do neither. No nonzero value or sufficient final
bound is assumed. The rational branch makes the actual descent algebra
Q×K with K quartic. The proposed mechanism asks whether that factorization
permits a direct evaluation through quartic norm equations and local
Hilbert symbols instead of the previous raw six-dimensional model search.
Applicability of the simpler construction to these classes remains conditional.

Essential inputs are L138/L139/L147/L148/L149, their exact full-product
representatives, complete local images at infinity,2,3,5,11 and accepted
support. The pair masks are 132102 and 3109; their sum is represented by
XOR products only modulo componentwise squares. Epsilon is the known
rational radical and is not one of the proposed two pairing arguments.
Rationality of either new argument is unknown; a computed zero value
would not establish rationality. No global generation or Sha finiteness
is presumed. Full matching Mathlib coverage is not checked.

The 2026-10-29 source review below completes this literature-only gate.
No new mathematical result, class computation or pairing was performed.

## Primary source and exact interface

Himanshu Shukla, *On computation of the Cassels-Tate pairing*, doctoral
thesis, University of Bayreuth (2024), repository publication 2025,
[published version](https://epub.uni-bayreuth.de/id/eprint/8348/1/thesis.pdf),
[DOI and version record](https://doi.org/10.15495/EPub_UBT_00008348), accessed
2026-10-29. The repository licenses the thesis CC BY 4.0. Printed page
numbers are used here; printed p.109 is PDF page 109 (zero-based 108).
The 2022 workshop slides were a discovery lead, not the theorem source.

Chapter 4 assumes a number field k and a smooth odd-degree hyperelliptic
curve y²=f(x); f may be taken monic and integral. Write theta_i for its
finite branch roots, T_i=(theta_i,0), and T_0 for rational infinity.
Section 4.1 represents H¹(k,J[2]) by conjugate-compatible values d_i in
k(theta_i)* with square total norm, in the full root algebra modulo
squares. No scalar quotient or full rational two-torsion is assumed.

Theorem 4.2.1 expresses the pairing of actual 2-Selmer classes as a sum
of local Brauer invariants over branch orbits. Its proof constructs the
orbitwise lifts, applies the double-coset formula, and uses compatibility
of invariant maps with corestriction. This is not the Cassels–Tate
pairing of two restricted classes over K: it is the base-field pairing
assembled from individual orbit contributions. In particular, do not
try to recover it by multiplying a pairing after restriction to K by four.

Section 4.3 explicitly avoids equations of the twist. Its general
construction instead needs splitting fields, trivializations of
2-cocycles, Hilbert 90 and local halves. Proposition 4.3.13 and Corollary
4.3.14 remove its intermediate Assumption 4.3.3 for odd-degree models;
this removal does not remove the different Assumption 4.4.3 below.

## The simpler, conditional replacement

Section 4.4, printed p.109, fixes a root theta_1 rational over the
current base field and defines, for j different from 1,

    C_1j: d_j u_j² − d_1 v_j² + theta_j − theta_1 = 0.

Assumption 4.4.3 requires solutions over the corresponding root fields
chosen compatibly with Galois conjugation. For another orbit one first
passes to its representative root field and repeats this construction.
Algorithm 2, pp.113–114, loops over factors of f, then the other roots
over each root field. Thus the global condition involves branch-pair
fields, not just one conic for the Q-rational branch.

The source constructs solutions for orbit representatives and transports
them by conjugation. It then builds p_1j and a cochain using Lemma 4.4.1.
Proposition 4.4.4 supplies the explicit piecewise epsilon_1 with boundary
eta_1. Its complete proof checks permutation compatibility, reduces to
the nontrivial quadratic-character case, and treats both parity cases
of the sign-change subset. The generic semidirect-product calculation
is explicitly restricted to subgroups at p.109; generic full Galois
action is not an extra instance hypothesis. Selmer membership alone
does not verify this stronger good-element condition.

Two transcription cautions matter for future implementation. Algorithm
2 writes its conic with the variables interchanged relative to Section
4.4; fix and verify one convention against the defining equation above.
Its printed line 7 tests M unequal to (0,0) although M was initialized
to (0,0); that is not executable guidance to copy without review. The
proposed test uses the mathematical condition, not literal execution of
that pseudocode. No author implementation was retrieved or executed.

## Local evaluation and all-place obligations

Section 4.3.3 treats both containment and noncontainment of the relevant
quadratic local extension in the first class's splitting field. After
Hilbert 90 it obtains delta_1,v in the local base field by equation
(4.3.7). The associated Brauer invariant is evaluated by the quaternion
Hilbert symbol with the second argument's d'_1. The printed paragraph
occasionally drops a prime on that argument; retain its definition
through the quadratic character and Algorithm 1/2. Raw componentwise
Hilbert products of the two input representatives are not this formula.

Algorithms 1/2 still require actual local Q_v in J(k_v) representing the
first class and compatible halves P_v, adjusted by two-torsion so their
coboundary is the specified cocycle. Accepted local-image membership can
supply inputs but is not itself this lift. Remark 4.5.1 reports that
local-point searches can fail in practice and suggests reusing local
descent images; this is not a termination guarantee.

Lemma 4.3.19 and Corollary 4.3.20 give the finite-place reduction after
epsilon has been constructed: include bad reduction, dyadic and infinite
places, and all primes where any epsilon value is not a unit. The proof
uses unramifiedness and even valuations outside this set, including the
integral, negative-valuation and branch-near divisor-coordinate cases.
The old descent support alone is therefore not a pairing-place
certificate. Include all places above retained base primes in each
orbit field. Normalize the sign-valued convention explicitly against
twice the additive Brauer invariant; an ambiguous printed exponent is
not a value certificate.

## Actual instance, duplicate check and route decision

L138 supplies the monic squarefree quintic, rational infinity, and
Q[X]/G=Q×K required here. L147/L149 give actual Selmer membership and
exact norm-one representatives of eta_class and nu. Transport their
polynomial or integral-basis values through L138's field map; masks
132102 and 3109 are column-product identifiers, not d_i values. This
odd-model method avoids the separate odd-to-sextic transport left
unresolved in ATTEMPTS/065; it does not solve that transport or
contradict the bounded construction failure.

The earlier assessment expressly left the Shukla–Stoll lead unread.
L148 stops the old pair containing epsilon; L149 supplies the different
second argument. No accepted local result already tests these conics.
Fisher's binary-quartic formula found during discovery concerns an
elliptic curve, not this genus-two Jacobian; the word quartic supplies
no genus reduction. Yan's full-rational-two-torsion formula remains
inapplicable. No exact-instance formula or novelty was established.

The source-level replacement is real but conditional. Test the
good-element condition for these two fixed classes over every branch-pair
orbit. Use the standard named Hasse–Minkowski theorem over number fields
and quaternion splitting/Hilbert-symbol criterion for the conics. A
negative local certificate is decisive; positive claims need complete
places, exact solutions and conjugacy checks. This is routine
specialization, not creative theory. The separate continuation assessment
records this finite target for next-turn approval. If neither class is
good, stop this simpler construction on this pair; do not infer that
their pairing vanishes or the general cochain method fails. If a class
is good, its cochain and all-place pairing computation remain separate
work. Full matching Mathlib coverage is not checked.
