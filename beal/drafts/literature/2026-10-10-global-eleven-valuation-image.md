# Global K(S,5) valuation image — completed source assessment

TARGET: Determine the image of K(S,5) under the three eleven-adic valuations modulo five and intersect it with L044's two-vector set.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused foundation 15 and the five-isogeny/primitive-eleven assessments; compared ATTEMPTS/008-009,012 and history/111; searched K(S,p) valuation image/class-group exact sequences, S-unit exact sequences, the exact field polynomial/54a1 class data, and PARI unconditional certification. No inspected source supplies this exact projected image; failed searches do not establish novelty.
SOURCE_EVIDENCE: Inspected Schaefer-Stoll June 13, 2001 manuscript Section 5, printed pp.8-9, and Theorem 8.1 hypotheses/proof, pp.20-21; Sharifi Iwasawa Theory Chapter 1, Notation 1.1.1, Remark 1.1.2, Definition 1.3.19, Proposition 1.4.5 and proof; official PARI stable manual entries bnfinit, bnfcertify, bnfisprincipal and bnfsunit, accessed 2026-10-10.
COMPARISON: Known ideal/class and Kummer inputs support a projected ideal-class test and a fully certified arithmetic implementation; the CM dimension theorem is not applicable to K. Full K(S,5) generators and local unit images are stronger tasks than this valuation-only target. No exact-field class data or image is imported.
GAP: The field-specific ideal criterion, all S-prime identifications, unconditional ideal/class certificates or sufficient exact witnesses, and the resulting projection/intersection still require a separate mathematical attempt; practical completion is not guaranteed.
REASON: Essential theorem and certification coverage is now available for the unchanged target; approve one bounded specialization, without claiming its criterion or image has been proved or calculated in this literature turn.
SCOPE: Exactly TARGET for L033's degree-12 K and every prime above 5 and 11, with L041's ordered normalized valuations and audited L044; permit an ideal-class reduction or exact global witnesses, but no full Selmer/point-class equality or other signature claim.
LITERATURE_REASON: The new global projection falls outside ready local coverage; its essential ideal/class comparison and unconditional certification interface were unread at invocation start.

The main gap remains global emptiness in the 54a1 branch of ordered
(3,4,11), alongside four other twists and infinitely many signatures.
The proposed intermediate target is only the projected valuation image,
not a full Selmer calculation. The downstream test is whether its
intersection with {(0,2,0),(2,0,0)} is empty, smaller, or unchanged.
An empty intersection would obstruct this branch; a nonempty one would
not supply an integer solution. No mathematical claim about that
intersection is made here.

Essential local inputs are L033's exact K and S and class containment,
L041's ordered places and valuation normalization, and the audited L044.
L034 supplies the inherited norm constraint if the assessment calls for
it. Any use of the known five-adic factorization must cite and verify
L038 locally; no cross-notebook input is proposed. Missing global
ideal/class data, unconditional certification and effects of primes over
5 remain unresolved. Do not assume GRH, a computed class group, rank,
Sha, or equality of Selmer and global point classes.

## Primary results actually inspected

Edward F. Schaefer and Michael Stoll, *How to do a p-descent on an
elliptic curve*, Trans. AMS **356** (2004), 1209-1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X);
locators here refer to the [June 13, 2001 long manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf), not presumed published numbering.
Section 5, printed p.8, gives the S-unit/S-class p-torsion exact sequence;
pp.8-9 describe construction and restriction of its classes. The proof of
Theorem 8.1, p.21, explicitly uses the kernel of the map from ideals
supported above p, modulo p, to the ordinary class group modulo p.
Its theorem assumes a CM elliptic curve over Q and a split odd p; those
hypotheses are not available here, so its dimension bounds are excluded.
Its ideal-map calculation is a methodological comparison, not a theorem
computing our projection. Foundation 15's general descent applicability
is reused. No general descent reproof is justified.

Romyar Sharifi, [*Iwasawa Theory*, Chapter 1](https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch01.html), live author HTML,
accessed 2026-10-10; no revision date identified. Notation 1.1.1 and
Remark 1.1.2 display the principal-ideal/class exact sequence and finiteness
for any number field. Definition 1.3.19 defines the S-class quotient and
S-integers. Proposition 1.4.5, with S containing every place over n and
the infinite places, gives the S-unit/Kummer/S-class n-torsion sequence.
Its proof uses surjectivity of the nth-power map in the maximal
S-ramified extension and the cohomology exact sequence; it does not
require F to contain mu_n. The root-of-unity hypothesis in the following
Lemma 1.4.6 is not transferred to Proposition 1.4.5. For our intended
use, n=5 and the infinite places may be included without an odd-power
sign condition. This source supplies general inputs, not our ideal data.

[PARI/GP official stable manual, General number fields](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html),
live version accessed 2026-10-10; release number not identified on the
inspected page. The entries `bnfinit`, `bnfcertify`, `bnfisprincipal`,
and `bnfsunit` were read, including failure/flag cases. `bnfinit` alone
is conditional. `bnfcertify(bnf,0)=1` removes GRH for subsequent uses;
it needs fundamental units. Flag 1 certifies only a quotient, not the
full computed group. `bnfisprincipal` returns class coordinates and,
when requested, a principal relation; generator reconstruction can
fail or be expensive. `bnfsunit` gives S-units modulo ordinary units
and S-class data for a supplied complete prime list. These documented
guarantees authorize a certification method, not a claim it succeeds
for K. Preserve the actual version, certification result, ideal relations
and every failure if this implementation is used.

## Exact difference left for mathematics

The next attempt must first formulate and prove the field-specific
ideal-class membership criterion, using unique factorization of fractional
ideals and the cited principal-ideal sequence. Treat it as an outstanding
specialization, not as an established formula in this assessment. It must
allow arbitrary valuations at every prime above 5 before projecting onto
the three primes above 11. An S-unit-only calculation is insufficient
unless its equality with the required projection is proved; do not lose
classes lifting S-class five-torsion. A full unit basis is not a prerequisite
for an alternative proof by complete ideal-class relations or enough
explicit global witnesses, but their sufficiency must be proved.

Identify the two rational eleven-adic places by residues 8 and 2 and the
degree-ten place by residue 10, as in L041. Match global prime ideals to
these places and normalize each uniformizer valuation to one, retaining
ramification index ten at the third place. Work in the maximal integer
ring; reduction in a potentially nonmaximal power order is not a certified
prime decomposition. Any fifth-root principal relation must be checked
as an ideal identity. An uncertified class table cannot prove absence.
Exact elements may prove membership without a class-group certificate,
but lower bounds on an image do not prove its completeness automatically.

The arithmetic threshold is an exact projected image and its intersection
with {(0,2,0),(2,0,0)}. Empty intersection obstructs only this branch;
one surviving vector narrows it; both surviving vectors retire this
projection as an exclusion test. The global image itself need not satisfy
L034's affine norm plane; that plane belongs to compatible connecting
classes. No prospective kernel computation or witness is asserted here.

## Duplicate, feasibility and stopping checks

ATTEMPTS/008 records missing full global arithmetic, rather than a proved
obstruction to this narrower projection. ATTEMPTS/009's constant norm
and ATTEMPTS/012's local-five equality are preserved. This assessment
does not reopen those exhausted tests. L041 supplies local places and
L044 supplies the exact local filter; neither computes a global image.
The reusable FNS field identification remains independent of its adjacent
GRH-dependent Selmer dimensions; those dimensions are not an input.

Queries included `K(S,p) valuation image class group exact sequence
Schaefer Stoll`, `"K(S,p)" "valuation" "class"`, `"S-units" "class
group" "exact sequence"`, `PARI bnfcertify unconditional class group
bnfinit S units bnfsunit`, and exact polynomial/54a1 class searches.
An indexed Stoll verification script for a different signature and a
degree-six 54a1 field is an unread lead, not data for this degree-twelve K.
No adequate exact-field computation was identified in the inspected sources.

Read-only executable checks found no `gp` or `sage` on PATH, no `gp`
at the standard /opt/homebrew, /usr/local or /usr binary locations, and
no importable `cypari2`. No mathematical calculation or installation ran.
This is a practical limitation, not missing theorem coverage: the next
bounded attempt can test exact witnesses or prove the criterion before
deciding whether unavailable arithmetic prevents completion. Do not spend
repeated turns seeking the same unavailable computation. Persistent lack
of necessary certified data parks dependent arithmetic and requires an
independently testable target with separate coverage if uncovered.

Mathlib: full matching projection, class-quotient and certification coverage
not checked; unknown availability is not evidence of absence. No new
lemma, mathematical script, exact image or signature exclusion is produced
by this literature-only approval. The canonical argument and DAG are unchanged.
