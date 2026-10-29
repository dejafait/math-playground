# Fixed-lattice first moment — proposed mathematical specialization

TARGET: Test a uniform first-moment bound for interval-relevant pole cost on L089's fixed lattice, removing low reduced-height members and fixed exceptions, against L116's budget and the retained full-image count.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step476's completed review in 2026-10-25-average-lattice-pole-cost.md covers exactly this finite-grid, explicit-residue-count and first-moment specialization; no new search or mathematical conclusion is claimed in this continuation record.
SOURCE_EVIDENCE: Moshkovitz https://eccc.weizmann.ac.il/report/2010/096/revision/1/download, ECCC TR10-096 revision 1 (8 July 2010), sections 1–3 pp.1–2, named Schwartz-Zippel lemma/full proof; Cremona–Sadek https://arxiv.org/pdf/2003.08454v3 (18 October 2021), Proposition 3.1/full proof p.11, prelimit residue-block counts; Zywina https://pi.math.cornell.edu/~zywina/papers/MaximalGalois.pdf, 15-page author version, Lemma 5.9/full proof p.8. Direct endpoints and essential passages rechecked in step477; reuse step338 fixed-level coverage and L089,L101,L116.
COMPARISON: Standard zero-count, residue-count and upper-height inputs cover the method, not this joint conclusion. Remaining work is the explicit fixed-lattice specialization, uniform moving-prime errors, actual reduced-height control and same-member counting; no independence of image and divisibility conditions is imported.
GAP: No averaged pole bound, negligible low-height count, joint passing survivor or selected integral prime has been proved. Every inequality in the bounded test remains to be established before any conclusion is recorded.
REASON: Step477 separately reviewed the saved continuation and repaired its missing direct primary URLs, rechecking the essential source passages without extending scope. SPECIALIZE is retained for one later known-method proof attempt; neither this review nor step476 establishes the specialized estimate.
LITERATURE_REASON: Supervisor recovery requires direct source URLs in this ready assessment; this turn repairs that specific omission and checks source scope, reusing the preceding search and fixed-level assessment rather than repeating discovery.
SCOPE: L089's unchanged rectangle R/2<=A<=R, |B|<=R, B odd on its fixed affine lattice; constants c,h,d_*,e_*,a,b,D fixed before R grows. Retain full images at 120 and seven, all original local conditions/domains, fixed finite exceptions, literal F=G_o, d=6, delta=3317760 and L101's original P1+ interval/P2/P3. No effective R, uniformity in lattice index, L105 assertion for the new prime, field change or IUT resolution is covered.

Main gap: original finite B>=A. Intermediate target: TARGET. Downstream
use: a passing actual member with T<=M(H) would allow L116's conditional
selection and hence supply L098's additional integrality premise. Neither
that member nor a new prime is claimed here.

Use the complete preceding source assessment, with its precise citations,
rather than repeat browsing. Import the general theorems. Any local
proof should explain why it is the required application, not a reproof
of a known general result. Classification for a successful known-method
application is REPRODUCTION; no certified novelty is asserted.

One coherent proposed test is:

1. Prove a uniform box envelope U(H)<=Y(R) with
   Y(R)=O(sqrt(log R) log log R), using the actual rational height and
   the cited upper-height input. Treat numerator cancellation by correct
   inequality direction when replacing poles by polynomial divisors.
2. Apply the named zero bound and explicit residue counts to estimate the
   first moment of W_R=sum_(p<=Y(R), p divides 4A^3+27B^2) log p on the
   actual lattice. Show all moving-modulus errors; handle fixed exceptional
   primes separately. Do not assume the density O-constant is uniform.
3. Test whether the slice H>=(log R)/8 loses negligibly few pairs, using
   L101's reduced-denominator formula, enumeration of rational invariants
   and L089's per-j fiber cap. Also remove the fixed finite parameter
   exceptions before choosing a member. This slice is a proposed threshold,
   not a proven height comparison.
4. Use a first-moment/Markov estimate and exceptional-set subtraction to
   compare the actual joint survivor count with zero, checking the minimum
   of M(H)=3 delta sqrt(H) log(2 delta H)-(delta+2)sqrt(H)-xi on the
   justified height range. Seek a positive count satisfying T<=M(H).

Continue only if the explicit errors, low-height loss and weighted loss
fit inside L089's quadratic count after its full-image exceptions. Stop
or narrow this mechanism upon a failure of the required comparison,
without inferring actual nonexistence or reopening the scalar cap.
Do not replace the actual H by coefficient height or assume statistical
independence. No new general sieve theorem is in scope.

Essential inputs: L089,L090,L098,L100,L101,L116. A later proof must keep
the member and its six actual parameters consistent. Full (a)–(c)/initial
data/III/P7, directed (*), generation/full repair, factor-four excess,
action/factorization/pilot, authentication/def=, essentiality and finite
B>=A remain unresolved; L105 retention is outside this test. No U/B
descent, full B[ell] rationality or global theta splitting is assumed.
Mathlib matching/supporting coverage is unchecked. STATUS remains
IN_PROGRESS; no candidate resolution is supplied.

## Separate source approval — step477, 2026-10-25

All three direct primary PDF endpoints above were accessible. Read
Moshkovitz's complete two-page argument, Cremona–Sadek's Proposition 3.1
and complete proof on printed p.11, and Zywina's Lemma 5.9 and complete
proof on printed p.8, together with its definition of B_k(x) on p.1.
The version and numbering agree with step476's source record. Reused
the inspected step338 composite-level theorem assessment, including
its full Proposition 5.7 proof cases; no change to level or field is
proposed. No new general theorem is proved or imported beyond that scope.

The zero bound requires a nonzero polynomial over the finite field;
the proof's substantive case is positive degree smaller than the field
size. The later application must check reduction on the affine lattice
and handle the exceptional primes. Proposition 3.1 permits any subset
of residues modulo a fixed positive M and positive box weights. Its
asymptotic error constant may depend on M and the residue subset, so
only its explicit prelimit block counts support the proposed moving-prime
test. Translated rectangles and the fixed lattice still need their
application argument. Lemma 5.9 assumes integral nonsingular short
coefficients in a norm box over a fixed number field; it supplies an
upper logarithmic height estimate for large boxes, not a reduced-height
lower bound. No uniformity in a growing lattice modulus is imported.

The prior exact-target searches and duplicate checks in the completed
step476 assessment are reused unchanged. ATTEMPTS/036's scalar-cap
failure remains controlling evidence, and ATTEMPTS/035's authentication
route remains parked. This review establishes no new weighted estimate,
height-slice count or joint passing member. Its outcome is a process
repair with no new mathematical evidence (STALLED), not an advance or
an informative negative result. Mathlib coverage remains unchecked.
The exact TARGET and continuation/abandonment test above are unchanged;
coverage is ready for the separate mathematical invocation.
