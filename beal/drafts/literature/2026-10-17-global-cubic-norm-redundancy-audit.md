# Global cubic norm and thirteen-adic redundancy — audit source coverage

TARGET: Critically audit L088's global cubic norm vanishing and thirteen-adic redundancy on L084's T.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L088 with the unchanged ready norm assessment 2026-10-17-thirteen-global-norm-filter.md; checked L074/L077/L082/L084 interfaces and ATTEMPTS/038/039. Reopened Stacks 0BD2 statement and complete proof and Clark Theorem 1.79 statement; reused the previously inspected Stein/Milne/Conrad results without repeating discovery searches.
SOURCE_EVIDENCE: Stein May 2004 Section 5.2 Corollary 5.2.3 p.28; Milne ANT v3.08 Proposition 4.1 pp.68–69, Proposition 8.2 and Corollary 8.4 p.136; Stacks Lemma 31.18.6 tag 0BD2; Milne CFT v4.03 III Proposition 1.2 and Lemmas 1.3–1.5 p.98; Conrad Finite fields Theorem 4.6 pp.9–10; Clark ANT II 161-page notes Theorem 1.79 p.58, accessed 2026-10-17.
COMPARISON: Known norm and lifting theorems cover the general machinery on the unchanged finite separable fields and full completion algebras. They do not certify L088’s field-specific supported-class correction, determinant bound or final containment; these remain the independent audit obligations.
GAP: No essential source-coverage gap remains for the exact audit. Independently verify every supported-class correction, norm factor, square obstruction, determinant term bound and thirteen-adic character implication before accepting the route stop.
REASON: Approve only a later critical audit as a specialization of already assessed machinery; this literature turn neither verifies L088 nor derives a new result.
SCOPE: Only L088's unchanged fields, support, T and certificate; no new filter, enlarged probe family, global class computation or integer-lifting target.

## Intended reuse and exact review obligation

Main gap: positive primitive integer emptiness, including the 54a1
branch. The intermediate target is a trustworthy decision on whether
J13 adds a restriction to T. L088 says it does not. A successful audit
would retire that filter on this exact space and allow a different
independently testable target; a defect should identify the failed
implication and preserve the valid preceding reductions.

Essential local inputs are L064, L069, L074, L077, L082, L084, L086
and L087; the new result is L088. Read the proof and full relevant
certificate fields in `scripts/thirteen-global-norm/norm-certificate.json`.
The determinant has 201 nonzero terms from all 3^11 column choices;
the proof's permutation bound independently covers every term. Review
the basis zeta=pi^5, pi=zeta^9/16; the valuation 27>6; the odd-degree
descent of kappa's square; and the injection of all four supported
norm-square classes into the dyadic square-class group. Do not replace
norm by scalar extension or a square residue by an actual dyadic root.

For arbitrary supported classes, verify the ideal square correction
using class number one in F only, both norm towers, every finite and
infinite factor, and both negative and positive valuations. No class
group vanishing in D or K is assumed. At thirteen use the actual
unramified degree twelve and the finite-field norm character, then
the D/K norm and even valuations to obtain the entire J13 condition.
The two rational eleven-adic restrictions are not needed in L088;
its larger domain must not be confused with imposing an extra condition
at the ramified eleven-adic place.

Unresolved: k_S, the full norm kernel and T, actual loc_11(T), rational
or integer lifting and all other signatures. The bounds 13+k_S and
fourteen do not improve, and T still does not bound full Mordell–Weil
rank. ATTEMPTS/029/038 remain valid. The full/supporting Mathlib
coverage is not checked. This file approves only the stated later audit and no new mechanism.


## Source-scope comparison completed 2026-10-17

LITERATURE_REASON: The saved audit target was REVIEW_REQUIRED; this turn resolves its source applicability once, reusing the ready construction assessment rather than conducting another discovery search.

The primary [Stacks statement and complete proof](https://stacks.math.columbia.edu/tag/0BD2)
were reopened. Its hypothesis is finite locally free of positive degree;
its norm is the determinant of multiplication, compatible with arbitrary
base change. Finite field extensions and their entire completion tensor
algebras have the required finite free structure. This permits checking
L088’s full local determinant, but supplies no particular coefficient,
valuation estimate or selected-factor replacement.

The primary [Clark notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
161 pages, revision date unidentified, printed p.58, Theorem 1.79,
were opened at the exact statement. The hypotheses are a complete valued
field, a polynomial over its valuation ring, an integral starting point,
and the strict inequality |f(a)|<|f'(a)|². The theorem gives a root in
the valuation ring in the specified neighborhood. This is the precise
form needed to test the claimed dyadic square-neighborhood inequality;
no unit derivative at two is required. At thirteen the same theorem
can be tested with a unit derivative and an actual nonzero residual
root. No proof of Theorem 1.79 is displayed at that location; it is
imported as a named theorem, not independently reproved here.

Reuse the Stein, Milne ANT, Milne CFT and Conrad statements and proof
cases actually inspected in the construction assessment, under its
“Primary statements actually inspected” section. The versions, page
numbers and direct author links there remain the canonical source
record. There is no changed field, support or norm map requiring new
discovery. Characteristic zero supplies separability; normality is not
a norm-tower or completion hypothesis. Milne’s ideal norm formula is
about maximal-ring fractional ideals, so the audit must retain negative
valuations and every prime above a base prime. The local unit-norm
reduction diagram requires the actual unramified extension; L064’s
entire degree-twelve completion is the input to check. Conrad’s formula
concerns the residue-field norm, not scalar inclusion. None of these
results by itself implies the claimed redundancy.

The omitted interfaces were compared at their hypotheses/conclusions:
L074 permits supported nonunit classes and specifies square element
norm; L077 supplies the complete rational-cubic supported family;
L082 supplies the fixed entire dyadic algebra, xi and square kappa;
L084 specifies exactly T. These are inputs to audit, not a replacement
for reading their load-bearing proof ranges where L088 uses them.
The audit must check the cited class-number-one and maximal-basis
arguments of L077 and the square-kappa justification in L082 before
using them. L087’s audited ordered image and L064’s full unramified
completion remain the thirteen-adic interfaces. No additional result
from a sibling notebook is imported.

Duplicates and failures: ATTEMPTS/039 records this exact proposed stop
and still explicitly requires critical review. ATTEMPTS/038 concerns a
different, insufficient five-probe eleven-adic certificate; its failure
neither proves nor refutes L088. This approval does not reopen either
mechanism, repeat an arithmetic test, or assess an enlarged filter.
No new lemma, certificate check or norm identity was produced. The
complete certificate must be read and independently checked next turn;
a source-scope comparison does not validate its nine reported checks.

Continue by accepting redundancy only if all stated implications pass
independent audit. Otherwise identify the first failed implication and
preserve valid preceding work. An essential hypothesis absent from the
sources would require a separate coverage review before a repair outside
this scope. The downstream use is a reliable decision to retire J13 on
unchanged T and choose another independently testable mechanism, while
the main integer gap, localized class kernel, eleven-adic independence
and both dimension bounds remain unresolved. Full/supporting Mathlib
coverage is not checked; this source review establishes no originality.
