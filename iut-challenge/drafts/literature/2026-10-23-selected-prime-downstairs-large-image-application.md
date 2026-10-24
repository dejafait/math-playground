# Same-selected-prime downstairs occurrence — application coverage

TARGET: Fix the source P4 exceptional set before the L101 choice, apply P4-P6 to its same E_o/G_o and selected ell>=7, and then apply L104 over C_o.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step419's exact-target search and duplicate/failure screen in 2026-10-23-selected-prime-downstairs-large-image-source-scope.md; no second search or mathematical application is claimed.
SOURCE_EVIDENCE: IV April 2020 reproduction https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf pp.45-46 (P4-P6); GenEll February 2009 author version https://www.kurims.kyoto-u.ac.jp/~motizuki/Arithmetic%20Elliptic%20Curves%20in%20General%20Position.pdf Example 1.3 pp.5-6, Lemma 3.1(iii) p.14, local setup/Lemma 3.2 pp.14-15, Proposition 3.4/Lemma 3.5 p.17, Lemma 3.7(b) pp.18-19 and Theorem 3.8(b)/proof pp.19-20; July 2016 comments https://www.kurims.kyoto-u.ac.jp/~motizuki/Arithmetic%20Elliptic%20Curves%20in%20General%20Position%20(comments).pdf pp.1-2. Full passage coverage is recorded in step419; URLs reopened in step420 and P4-P6/Theorem 3.8(b) located. Optional split/nonsplit input reuses Dupuy-Hilado https://arxiv.org/abs/2004.13228v1 Lemma 5.4.1 pp.27-28 via the existing assessment.
COMPARISON: The cited method needs no normality of G_o/Q and precedes P7; L101 allows the required exception to be fixed before member selection. It does not justify enlarging exceptions after selecting an arbitrary witness. Only the known method's exact-field specialization and L104 application are proposed.
GAP: Check finite parameter exceptions, actual G_o semistability/height hypotheses, same selected prime, full representation and the L104 premises; no occurrence or transfer application has been carried out by this assessment.
REASON: Essential source coverage is complete; a general large-image reproof or another prime-selection construction is unnecessary. This newly written ready continuation is subject to separate approval next turn.
SCOPE: L089 fixed family/domains/closure, d=6, epsilon_d=1, one ordering, L090 full-coordinate G_o, L092 normal closure C_o of relative degree four, L101 simultaneous ell>=7 and unchanged H; include the P4 exception before the existential construction and keep its resulting member and prime throughout.

Use the completed source comparison for precise links, hypotheses,
proof-case readings and version qualifications. It is source evidence,
not an additional mathematical lemma. Import the cited height,
isogeny, transvection and finite-group statements; prove only their
necessary applicability to the literal fields. L100's audited local
height calculation is available through L101. If directly using the
stronger GenEll theorem, explicitly verify its moduli-domain and
bounded-degree exception conditions rather than assuming them from
lambda-line terminology.

The main gap remains original finite B>=A. Downstairs occurrence
would discharge the premise of audited L104 and clear one independent
normal-closure repair prerequisite. It would not address the relative
factor-four excess or supply native initial theta-data/III.

Continuation test: all finite exceptions must precede the choice;
the actual E_o/G_o, prime ell and H must then stay fixed through the
full-coordinate image calculation and L104. Stop or narrow if any
exception, local height or representation hypothesis fails. A new
curve or a different prime after selection is outside this target.

Essential IDs: L089,L090,L092,L100,L101,L104. Unresolved assumptions:
native data/III, P7, exact generation/full repair, relative excess,
native input/action/factorization/pilot, authentication/def=
qualifications, essentiality and finite B>=A. Ell-integrality is
unused, full matching Mathlib coverage is unchecked, and no complete
flaw candidate is claimed. Any successful specialization is known
mathematics (REPRODUCTION), not a result beyond the checked sources.

## Source-link recovery — 2026-10-23, step420

The direct source URLs are now present in SOURCE_EVIDENCE. The three
PDFs reopened successfully: IV identifies April 2020 and 87 pages;
GenEll identifies February 2009 and 25 pages; the comments identify
July 2016 and two pages. A targeted source lookup located P4-P6 on
printed pp.45-46 and Theorem 3.8(b) on printed p.19, with its proof
on p.20. This repairs traceability, reusing step419's inspected
hypotheses and essential proof cases; it is not an independent
reproof, new theorem comparison, or mathematical application.

SPECIALIZE and the exact TARGET remain unchanged. This separate
review approves the existing continuation's source coverage. The
exception-order, actual-field and same-prime checks in GAP remain
obligations of that attempt. The reproduction's authentication and
L091's def= qualification remain unresolved; neither is certified by
these links. No lemma, mathematical script, DAG or argument change
was made in this recovery step.
