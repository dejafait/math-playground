# Retained native field and radical dictionary — completed source comparison

TARGET: Compare IUT I Definition 3.1 and Example 3.2(iv) with the retained global division field and selected place to determine the exact hypotheses for identifying native K_w with N and the native pilot-root coset with L069's roots, without marked transport or all-image claims.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the 2026-10-13 EtTh base-field application/audit and definition assessments; checked relevant native Definition 3.1/tensor assessments, foundations/05, L045,L048,L054,L060,L069 and ATTEMPTS/027,031,032. No completed IUT global-field/root-coset application was located; L054 already covers the distinct EtTh local dictionary. Direct retrieval resolves this definitional target; no novelty follows from the search.
SOURCE_EVIDENCE: Mochizuki, IUT I, May 2020, 186-page text: Definition 3.1(a)-(f), printed pp.61-63; Example 3.2 opening and (i)-(iv), pp.69-71, read continuously through the reproduction linked below. Author endpoint supplied version/indexed text but subsequent retrieval timed out; byte identity and journal-version equivalence are unverified. Reused EtTh December 2008 pp.10,12,16 and Kedlaya Theorem 2(a),(b), p.4, as assessed on 2026-10-13; reused foundations/05 for IUT IV April 2020 Theorem 1.10 hypotheses/(iv),(v), pp.22,26-28.
COMPARISON: Native K is defined by the full ell-torsion kernel, not a selected cyclic cover. The source's q_v belongs to the underlying base elliptic curve; bold_q_v is a 2ell-th root with mu_(2ell) ambiguity. These definitions cover a conditional assignment to the retained division-field completion and L069 root set; they do not choose a theta marking or certify initial data. L054's completed EtTh application needs no reproof.
GAP: A later application must document the same-curve/full-coordinate kernel, embedded completion, selected place and base parameter, then compare root sets. Full initial Theta-data and IUT IV's additional global hypotheses remain unproved; marked transport and all-image factorization are outside this dictionary.
REASON: Missing IUT defining clauses are now inspected. Only a bounded conditional specialization remains, using audited inputs and known definitions, with no new radical/torsion theorem or reproof of theta evaluation.

LITERATURE_REASON: The ready L069 audit covers radical membership, while this target requires the IUT global-kernel and selected-place/root-coset clauses; further EtTh membership browsing was unnecessary.
SCOPE: Source comparison only; the later application is limited by its separate ready assessment. No retained-packet specialization, theta normalization or all-image assertion is established here.

## Primary definitions and hypotheses inspected

Primary source: [Mochizuki, IUT I, May 2020 author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf).
Continuous passages actually read came from the
[186-page reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf).
References use printed pages. Subsequent author-PDF find/open requests
failed; shell download failed at DNS resolution, and screenshot retrieval
failed. None of those failures is verification evidence. Essential text
was accessible in the reproduction; byte identity with the author or
journal version remains unverified.

Definition 3.1(a)-(b), pp.61-62, requires a number field containing a
square root of -1, an algebraic closure, a once-punctured elliptic curve
with everywhere stable reduction, its native field of moduli, a nonempty
selected bad subset of odd residue characteristic, and multiplicative
reduction at all F-places above that subset. It also requires F/F_mod
Galois of degree prime to ell and rational full 6-torsion. Clause (c),
p.62, requires ell>=5 prime, torsion image containing SL_2(F_ell), and
coprimality with the selected residue characteristics and integer local
q-orders. It defines K by the kernel of the full torsion representation.
This is the field definition to compare with L045's full coordinate
field; neither a cyclic-point field nor an extra extension is prescribed.

Clause (d), p.62, retains the covering and K-core. Clause (e), pp.62-63,
chooses a section over V(F_mod), defines local notation by base change to
K_v and separately imposes local cover type at selected bad members. It
attributes the EtTh field condition to rational 2-torsion. Clause (f),
p.63, imposes the cusp sign label. The section image is not the whole
fiber over a moduli place. L060 supplies a conditional section through
w, not a verification of every initial-data clause.

Example 3.2 opens on p.69 under initial Theta-data at a selected bad
place. Parts (i)-(ii), pp.69-71, retain the tempered cover and reciprocal
normalized theta function, with root-of-unity and ell*Z covering
indeterminacies. Part (iv), p.71, fixes the underlying elliptic curve's
Tate parameter and states that rational 2-torsion and the definition of
K supply a 2ell-th root in the local field. It identifies the indicated
theta value with such a root, citing EtTh Proposition 1.4(ii), and
specifies mu_(2ell) ambiguity. The subsequent divisor-monoid and
characteristic-splitting construction is additional structure. Import
only the stated root convention; neither theta evaluation nor categorical
transport is reproved or independently verified in this review.

## Conditional dictionary for the later application

Retain L045,L048,L054,L060,L069 and foundations/05, with the same
E_0,F,K_glob=F(E_0[7]), Omega, fixed embedding, u,w,H,N,
M>=max(M_tors,31), full30/full7 torsion, pointed Q_3 Tate isomorphism,
changed q_0 in Q_3 with v_3(q_0)=30, and L060's conditional singleton.

| Native item | Proposed assignment | Check required in the application |
| --- | --- | --- |
| F,X_F,ell | retained F,E_0 minus origin,7 | Same curve and origin; no sufficient initial-data claim. |
| K of 3.1(c) | K_glob | L045's full-coordinate pointwise kernel; do not use the cyclic cover. |
| selected bad v | w through L060's section | Keep the actual restriction to native F_mod and conditional setup. |
| K_v | N | L045's embedded completion, not a degree match or global K=N. |
| E_v,q_v | E_0 over N,q_0 | Reuse L054's base-curve and parameter-uniqueness checks. |
| bold_q_v ambiguity | L069's fourteen-root set | Compare root conventions; do not select a transported marked value. |

The table specifies an application still to be written; it is not its
proof. No different radical degree or all-level radical closure occurs
in the inspected IUT clause. Membership of every root does not identify
a theta-normalized marked value, resolve ell*Z covering choices, or track
a pilot across log-links. A root coset cannot replace the all-image union.

Reuse the exact covered scope of
`2026-10-13-retained-native-base-field-application.md` and
`2026-10-13-retained-native-field-specialization-critical-audit.md`.
L054 already checks the finite p-adic base, original curve and uniqueness
of the changed parameter. The present comparison adds IUT global-kernel,
section and root-convention coverage. Preserve ATTEMPTS/027's exact-curve,
031's marked-coordinate and 032's tensor-objection stops in their own
scopes; this dictionary does not reopen them.

## Relevance and continuation test

The main gap remains original finite B>=A. A conditional dictionary may
remove ancillary field/radical assumptions in L068 and foundations/05;
source-marked all-image factorization, independent initial/global
conditions and essentiality remain unresolved. Continue if the full
kernel, embedding, selected place and base parameter match the unchanged
objects. Otherwise isolate the exact extra predicate and withhold the
identification. Abandon any inference of marked transport or full initial
data from a pass. No essential source remains unread for this narrow
application; no new lemma or mathematical script is needed.

Matching Mathlib coverage for the native dictionary is not checked.
This is local source-readiness progress by imported definitions, not
mathematics beyond the sources checked or evidence of an IUT flaw.
PROOF and DAG do not change in this literature-only step.
