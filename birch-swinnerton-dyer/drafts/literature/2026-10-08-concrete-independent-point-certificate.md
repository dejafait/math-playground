# Independent-point source assessment for the fixed curve

TARGET: Certify two independent rational points on E=[0,1,1,-2,0] and apply L004 with audited L033, without assuming complex order or Sha finiteness.
CHECKED: 2026-10-08
DECISION: IMPORT
SEARCH_EVIDENCE: Searched “Cremona 389a1 generators independent 0 0 1 0” and “Cremona elliptic curve database generators proven independent allgens documentation”; located and inspected Cremona's corrected book Table 2, its interpretation, current allgens row and arithmetic verification account, rather than relying on search snippets or a rank label.
SOURCE_EVIDENCE: Cremona, Algorithms for Modular Elliptic Curves, corrected online second edition (1997), Chapter 4 p.105 and Table 2 p.257 row 389A1, gives (0,0),(1,0) as Mordell–Weil generators modulo torsion; the author's ecdata TABLE TWO identifies the exact model [0,1,1,-2,0] and checked generators, with matching allgens row; the ANTS VII account §§2.3–2.4,3.4 describes arithmetic verification and qualifications.
COMPARISON: The published basis result is stronger than the two independent images required by L004. Import its independence consequence only; use existing L030 for the model/non-CM premise and audited L033 for good ordinary p=7 and the nonzero quadratic coefficient. No height recomputation, saturation proof, complex-order claim or Sha hypothesis is needed for this source import.
GAP: Essential source coverage for this fixed target is ready; a later research turn must place the precise imported point statement and its model identification in a canonical file and explicitly check the L004 application. The original descent/height execution certificate has not been replayed here; uniform point production and complex-order comparison remain open.
REASON: A previously uncovered arithmetic input is now covered by a precise published fixed-curve basis result, so the next mathematical step should import it rather than reprove known independence or repeat coefficient audits.
SCOPE: Only the exact TARGET, points P=(0,0), Q=(1,0) on E=[0,1,1,-2,0], their source-backed independence modulo torsion, and the existing L004 application with k=n=2 at p=7 using audited L033; no independent certificate algorithm or larger family is approved.

Essential inputs are L004, L030 and audited L033; their normalization
ultimately uses L027/L028/L031/L032 and foundations/05. This is a
literature-only approval, not the mathematical application of L004.

The intermediate threshold is two independent images in E(Q) tensor Q;
a full Mordell--Weil basis is unnecessary for L004. Continue by importing
the published basis result after matching the equation and coordinates.
Abandon that application if the source result is withdrawn or the model,
point convention, primitive series or ordinary-prime hypotheses fail to
match. A rank label, distinct points or an unqualified floating-point
height determinant alone still fails the threshold.

This would test the arithmetic side of the already-produced coefficient
certificate on one curve. It would not produce rational points uniformly
from complex order >=2 or resolve the general Clay rank assertion.
No mathematical exploration on this target occurred in this source review.

## Inspected primary evidence

1. **Published fixed-curve result.** J. E. Cremona, *Algorithms for Modular
   Elliptic Curves*, second edition, CUP 1997, corrected online edition:
   [Chapter 4, p.105, Table 2 description](https://johncremona.github.io/book/fulltext/chapter4.pdf#page=2)
   defines the entries as generators modulo torsion. The two-point entry
   [Table 2, p.257, 389A1](https://johncremona.github.io/book/fulltext/table2.pdf#page=3)
   is P=(0,0), Q=(1,0). This is the arithmetic group statement being
   imported, not Table 4's numerical BSD data. The
   [second-edition errata dated 26 September 2003](https://johncremona.github.io/book/errata.pdf)
   was read in full; it gives no correction to this entry.

2. **Exact model and present source data.** The author's
   [ecdata, TABLE TWO: GENERATORS](https://johncremona.github.io/ecdata/)
   explicitly explains this very example, including [0,1,1,-2,0], rank
   two, trivial torsion and the two projective points. Its general
   description says the listed generators have been checked. The exact
   [allgens.00000-09999 row](https://raw.githubusercontent.com/JohnCremona/ecdata/master/allgens/allgens.00000-09999)
   read on 2026-10-08 is `389 a 1 [0,1,1,-2,0] 2 [] [0:0:1] [1:0:1]`.
   This is a matching transcription, not an independent second proof.
   The site reports update 2020-11-27; the raw master file is cited as
   accessed, with no unverified immutable revision claimed. At conductor
   389 the historical capital A becomes a; no other label change applies.

3. **Verification and its qualifications.** Cremona, *The elliptic curve
   database for conductors to 130000*, ANTS VII, LNCS 4076 (2006),
   [§§2.3–2.4, PDF pp.5–6, and §3.4, PDF pp.13–15](https://johncremona.github.io/papers/ecdb_ants.pdf)
   describes point search, 2-descent and saturation. It reports arithmetic
   rank verification for rank-two and rank-three entries. Some generator
   subgroups in the larger database had only finite index certified;
   this is a saturation qualification, distinct from independence.
   Section 2.3 also acknowledges possible software/data-processing
   errors. We import the corrected published computational result with
   that provenance; no execution transcript or independently replayed
   descent certificate has been inspected in this turn.

4. **Independence method comparison.** The same book's
   [§§3.4–3.5, pp.71,75–77](https://johncremona.github.io/book/fulltext/chapter3.pdf#page=10)
   explains canonical heights and the point-processing cases: adding an
   independent direction, recognizing an integral combination, or
   enlarging a sublattice when a multiple lies in the previous span.
   Rank lower bounds and saturation are separate tasks. These inspected
   sections explain what the basis assertion means; their algorithms
   were not executed, and a printed regulator is not substituted for a
   certified determinant. Silverman's general height theory, cited there,
   is an unread lead and is not essential to the direct table import.

## Local comparison, scope and next application

The relevant local search and reads covered L004's full hypotheses and
conclusion, foundations/05, drafts/2026-09-25-point-coefficient-certificate.md,
history/004 and history/083–086, the statements of L030/L033, and
ATTEMPTS/022–023. The existing certificate is conditional on independent
points; none of these records supplies this fixed pair. The previous
production stops concern missing symbol/calibration inputs and are
preserved. This point input is a distinct gap, not a reopening of those
conditional-audit loops. The source search establishes coverage, not
novelty.

For a later application, use precisely the minimal equation already
certified in L030 and the ordinary p=7 series of L033, including total
minimal real period, trivial Teichmuller branch and kappa(gamma)=8.
L033 supplies the strict coefficient enclosure with b=13/256, N=1 and
v_7(b)=0. L004 already covers Kato divisibility without a residual
surjectivity hypothesis in this scope. It also records exactly which
finite 7-primary Sha and cyclotomic consequences follow once k=n=2
is justified; these are conclusions to check next turn, not premises.
No complex order or finiteness of full Sha is imported from the tables.
The known basis result suffices by citation; a local reproof of its
descent or numerical height algorithm would add no needed hypothesis.

Full matching Mathlib coverage for this fixed basis result or L004's
arithmetic application: **not checked**. No absence claim is made.
