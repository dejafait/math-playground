# Retained degree-seven formal extension — source review

Literature-only step 195; no retained-object extension is proved here.
Target: the exact Next action in the saved extension assessment.
Main gap remains original finite B>=A and actual input/action/pilot/essentiality.
The intermediate target could support native graph comparison; a changed
generic map or essential enlargement of N withholds the requested conclusion.

Inputs inspected: L053's actual rank-one isogeny and point-group statement;
L055's hypotheses, node/marking and ramified-pullback charts. Preserve
ATTEMPTS/027 (old exact rational Tate curve) and /030 (full multiplication);
neither decides this rank-one formal extension. No cross-notebook read.

## Inspected primary construction

[Brian Conrad, *Arithmetic moduli of generalized elliptic curves*](https://math.stanford.edu/~conrad/papers/kmpaper.pdf),
author PDF dated July 18, 2006, 49 pages. Publication: J. Inst. Math.
Jussieu 6 (2007), 209–278, DOI 10.1017/S1474748006000089;
theorem/page references below are to the inspected author version.
Journal byte identity and numbering were not verified.

Read Definition 2.1.2 and polygon construction, pp.4–5; Corollaries
2.2.3–2.2.4 and proofs, pp.8–9; section 2.5, pp.16–18, including
Example 2.5.1 and Theorem 2.5.2's proof; Theorem 3.2.4 and proof and
Corollary 3.2.5, pp.24–25. Essential source hypotheses and conclusions:

- DR curves are proper, flat, finitely presented genus-one curves with
  geometrically connected semistable fibers and trivial fiber dualizing sheaf.
- Corollary 2.2.3 needs an ample smooth Cartier group divisor acting on
  the curve, trivially on Pic^0; it supplies the unique group structure.
- Corollary 2.2.4 algebraizes compatible generalized elliptic curves
  over powers of an ideal in an adic noetherian ring, with fixed polygon size.
- Section 2.5 glues annuli XY=r, with r topologically nilpotent in
  an adic noetherian ring. Rotation quotients are finite etale, including
  the separate one-gon construction. Theorem 2.5.2 identifies the generic
  fiber with Tate_1(q), where r=q^(1/n), compatibly at the formal origin.
- Example 2.5.1 supplies the degree-m power isogeny, with kernel mu_m.
- Theorem 3.2.4 extends generic isomorphisms over normal bases when
  singular fibers have matching polygon sizes.

These are known inputs, not new results. In Theorem 2.5.2 the notation
q^(1/n) denotes the formal base variable. For the proposed application,
use r=q_0, n=7, and compare the generic source with Tate_1(q_0^7);
do not substitute a seventh root of q_0 or silently change the base.
Example 2.5.1 is the opposite-direction power isogeny, not the desired
rotation quotient. Its kernel is relevant to matching L053's alpha;
the corresponding factor psi must still be matched as an algebraic map.

The proof cases actually read matter: algebraization uses an ample
torsion divisor and formal GAGA, rather than properness of the smooth
locus. Generic Tate identification uses contraction of nonidentity
components and [DR, VII, 1.14]. Theorem 3.2.4 first treats smooth
closed fibers via Neron models, then equal-sized singular polygons via
contraction and finite level-structure Isom schemes. Its proof uses
extensions for verification; its stated conclusion is over the original
normal base. It is not an existence theorem requiring a changed field.
The unpointed Stacks stable-reduction uniqueness lead is unnecessary:
its genus-at-least-two setting should not replace this pointed-genus-one
comparison. The canonical-curves normalization lead was not imported.

## Log and native sources

Reuse the ready F. Kato 1994 chart/pullback assessment in
`drafts/2026-10-13-retained-stable-log-source-notes.md`.
Primary text reinspection of [alg-geom/9406004v3](https://arxiv.org/pdf/alg-geom/9406004v3),
Definitions 3.1 and Lemmas 3.2–3.4, pp.6–7, confirms strictness,
ghost comparison and the fs-product qualification. Proposition 3.8
states the strict **log-smooth** equivalence; it is not cited as a
printed log-etale theorem.

A new accessible primary endpoint resolves the narrow log-etale input:
[Martin C. Olsson, *Logarithmic geometry and algebraic stacks*,
Ann. Sci. ENS (4) 36 (2003), 747–791](https://www.numdam.org/item/10.1016/j.ansens.2002.11.001.pdf).
Inspected Proposition 3.19 and proof, pp.764–765; Definitions 4.1,
4.4–4.5 and Theorem 4.6(i)–(iii), pp.765–767, and its pertinent
proof on pp.767–768. Fine log schemes are required. Proposition
3.19 identifies the strict locus and its open immersion into Log_S;
Theorem 4.6 equates log-etaleness with weak Log-etaleness and with
the unique infinitesimal lifting property plus local finite presentation.
These supply precise coverage for a strict ordinary etale map with
pullback log, to be applied on algebraic models/strict reductions.
No moduli-curve existence theorem from Olsson or Kato-2000 is imported.
The earlier access-failure evidence remains; the specific new Numdam
endpoint succeeds. Kato's 1989 scanned Chicago PDF has no extracted
text here and is an unread, unnecessary lead.

[Mochizuki, EtTh, PRIMS 45 (2009), 227–349](https://ems.press/content/serial-article-files/41069?nt=1),
journal section 1 opening, pp.237–239, was read at the new-target scope.
It assumes a stable-log formal curve of type (1,1) over the closed-point
log base of a finite p-adic field, split singular special fiber and
smooth algebraized generic log fiber. It describes the infinite formal
graph cover and the associated integer quotient. This confirms relevance
of a finite cycle test, without identifying L053's cover. Keep the
author/journal and odd/even-level qualifications in the previous notes;
no theta-cover splitting or later environment theorem is imported.

## Application obligations approved for a separate research turn

The exact retained-object conclusion is not printed in these sources.
SPECIALIZE is appropriate, with REPRODUCTION classification: apply the
known models and check their compatibility with existing objects. A
full new general construction or a reproof of the cited theorems is
unnecessary. The following obligations are within the assessed target:

1. Check Corollary 2.2.3 on L051's unchanged one-pointed cubic and
   its section, then use Theorem 3.2.4 with the pointed Tate isomorphism
   to match the one-gon target to this actual cubic. Check both models'
   geometric singular polygon sizes and the normality of O_N. Do not
   substitute the regular I_n model for the fixed stable cubic.
2. Use the known formal seven-gon rotation construction over O_N at
   r=q_0 and its algebraization. Match its generic curve/map to L053
   by the power-isogeny kernel mu_7 and pointed factorization. Check
   the whole morphism, not only abstract point groups or degrees.
   If composition with the quotient is used, verify it is [7].
3. Transport the target's L055 log structure and take its pullback
   on the cover. Check fs charts, strictness and the cited log-etale
   criterion on all reductions. Check node smoothing parameters,
   all seven smooth marking sections and overlap gluing. No numerical
   node thickness is assumed in advance.
4. Read off and justify the degree-seven cycle map, retaining branch
   and marking data. This does not yet identify native tempered
   quotients, select their generator sign or supply a theta splitting.

Continue if the exact map over unchanged N passes all four checks;
withhold the conclusion and localize the obstruction if changing the
generic map or field is essential. Elementary matching checks are
needed because the target fixes prior objects; they are not a reason
to reprove standard Tate, quotient, algebraization or log theorems.
No application above is claimed completed in this literature turn.

Mathlib: full matching formal Tate polygon, retained isogeny-extension
and log-etale coverage is not checked; no absence assertion is made.

## Discovery, duplicates and limits

Queries included `Tate curve finite etale covering formal model cycle
graph q power Mumford`, `Mochizuki Etale theta function Tate curve
graph covering log etale`, `Tate curve n-gon isogeny generalized`,
and strict/log-etale theorem terminology. Conrad supplied the concrete
new lead. Secondary search hits, van der Put's Mumford-cover paper
and generalized-Tate papers remain unread leads, not evidence of
novelty or dependencies. No repeated blocked graph-theorem retrieval
is needed for this test. Shell PDF download failed DNS; primary web
text furnished the theorem statements and pertinent proof cases.
Screenshots were not returned as readable images; no unverified OCR
overlap formula is being certified. Use the cited gluing construction
and justify any coordinates used in the later specialization.

Narrow duplicate/failure checks used L053,L055, the existing native
source notes and histories 177,178,190,194. No local result already
establishes this exact extension. Historical stops remain local.
The independently missing native tempered comparison, label/splitting,
full selected/theta data and actual input/action/pilot/essentiality
are preserved. The required finite B>=A is still not obtained.

Challenge version: retrieved the [2023-07-07 official announcement](https://zen.ac.jp/news/0ul6zqed9-0)
and [current prize page](https://zen.ac.jp/en/lp/icp) on 2026-10-14.
Their inherent/essential-flaw scope and separate adjudication conditions
agree with foundations/01; this review supplies no prize claim.
