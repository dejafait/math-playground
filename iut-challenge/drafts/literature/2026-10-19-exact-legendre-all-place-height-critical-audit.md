# Exact-G all-place height — critical-audit source coverage

TARGET: Critically audit L084's all-place multiplicative reduction and prime-to-seven integer height over unchanged G, checking arbitrary-place pointed transport, nonsplit normalization and both ramification towers.
CHECKED: 2026-10-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step332 compared full L084 with the ready all-place application assessment, the relevant canonical statements of L073,L077,L078,L081, histories 330–331 and ATTEMPTS/027,034; reused the application's exact-statement, stronger-result and obstruction searches. No changed general theorem hypothesis calls for fresh external retrieval.
SOURCE_EVIDENCE: Reused inspected primary coverage: GenEll published journal local setup pp.16–17, Definition 3.3/Remark 3.3.1 p.17; Silverman AEC second edition (2009) VII.5.4(b) pp.197–198 including the relevant proof case and C.14.1(b,d) p.445; Kedlaya Tate fall 2004 Theorems 1–2 pp.3–4 and (3) p.2; Milne ANT v3.08 (19 July 2020) 3.34 pp.59–60, Exercise 4-2 p.83 and its solution p.155, 7.42–7.43 p.124 and section 8 pp.135–136. These were not newly retrieved in step332.
COMPARISON: The recorded primary hypotheses cover the finite local extensions, pointed base change, split Tate parameter, semistable reduction alternatives, extension-normalized height and separate ramification towers used by L084. Its all-place and exact-field assertions remain application obligations for the independent audit, rather than conclusions imported wholesale from a source.
GAP: Source scope for the exact audit is ready; the independent mathematical audit of full L084 remains undone, with no verdict about its correctness or the original IUT claim.
REASON: Complete the saved REVIEW_REQUIRED audit-scope comparison using adequate unchanged source coverage; next perform the bounded mathematical audit rather than repeat retrieval or reprove the general inputs.
SCOPE: Exactly TARGET for unchanged full L084 and L073,L077,L078,L081 with the same D,s,t,iota,F',G; no new curve, normal closure, global normality verdict or sufficient-initial-data claim.
LITERATURE_REASON: The saved critical-audit target was REVIEW_REQUIRED and distinct from the ready application target; this turn supplies its required source-scope comparison, not additional searching on the ready application.

## Source-scope comparison — step332

The reusable assessment is
`drafts/literature/2026-10-19-exact-legendre-all-place-q-order.md`.
Its recorded primary readings, not model recollection or search previews,
supply the following coverage. Links identify those recorded versions;
no source was freshly retrieved in this turn.

- [Silverman, AEC, second edition](https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf),
  VII.5.4(b), pp.197–198, covers persistence of good and multiplicative
  reduction over finite extensions. The inspected multiplicative proof
  case has no restriction excluding residue characteristic three.
  C.14.1(b,d), p.445, covers the Tate curve for nonintegral j and the
  quadratic splitting description, unramified in the multiplicative
  case. These statements permit checking reduction descent using
  L081's semistability; they do not identify every G-completion with H
  or assert splitness downstairs.
- [Kedlaya, Tate curve, fall 2004](https://kskedlaya.org/18.727/tate-curve.pdf),
  Theorems 1–2, pp.3–4, and (3), p.2, cover the finite-Q_p-extension
  construction, parameter uniqueness and j-series used in L084.
  L077's explicit complete pointed maps, and their base changes at
  arbitrary places, are local application checks rather than a new
  uniformization theorem. L073 supplies the same Q-defined curve
  and its changed parameter of valuation 30, not q=3^30.
- [Mochizuki, GenEll, published journal version](https://www.math.okayama-u.ac.jp/mjou/mjou52/_01_mochizuki.pdf),
  Math. J. Okayama Univ. 52 (2010), local setup pp.16–17, Definition
  3.3 and complete Remark 3.3.1 p.17, covers the surjective integer
  valuation and extension-normalized potentially multiplicative
  height. The audit must check that its chosen extension provides the
  split setup, and must retain the division by its ramification
  index. This is not a canonical height of a point. The accessible
  journal passage resolves the prior access issue; equivalence of
  entire author/journal texts is not claimed.
- [Milne, ANT v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
  Exercise 4-2 p.83 and solution p.155 cover ramification towers without
  normality. Corollary 7.42/Remark 7.43 p.124 cover local degree ef
  and integer-valuation restriction; 3.34 pp.59–60 supplies the
  Galois ramification divisor, and section 8 pp.135–136 supplies
  induced completions. These cover the two separate towers through
  F_aux and G. The later audit must check every field inclusion,
  place restriction and local quadratic-degree hypothesis; it may
  not replace them with divisibility by nonnormal [G:Q].

The full L084 contains no additional general mechanism outside this
scope. L073's canonical conclusion supplies Galois F_aux and its
degree divisor; L077 supplies the actual quadratic adjunction and
pointed comparison; L078 supplies the literal G inclusion; L081
supplies semistability, allowing nonsplit nodes. Their recorded
separate audits are available, but the later audit should read the
proof passages needed for these uses, rather than treating the
overview's old pending-audit wording as a current verdict.

Duplicate and failure comparison reuses the scoped application search:
L061 concerns a different witness and is not a proof of this statement.
ATTEMPTS/027 stops exact rational-parameter globalization, whereas
L084 uses the changed auxiliary curve. ATTEMPTS/034 stops the cyclic
normality separator; the proposed audit needs no normality of G/Q.
Neither stop is reopened. No novelty inference follows from these
checks. No essential missing source was found in this scope comparison.

This is approval of coverage only. No new lemma, proof derivation,
mathematical script or audit verdict is supplied. It adds no new
mathematical/source evidence beyond the reusable application coverage;
the checkpoint therefore reports STALLED honestly while routing to
the now-covered independent audit. Mathematical exploration usage
remains zero. Full matching Mathlib coverage is unchecked; the
supporting abstract tower theorem and its qualifications remain those
recorded in the application assessment.

## Invocation-start proposal retained for provenance

The proposal below is superseded only as to its pending source-scope
status. Its mathematical audit, continuation test and limitations
remain pending and unchanged.

The main gap remains original finite B>=A. The proposed audit would
make the new local prerequisite reliable before downstream use. Its
input is full L084, not the old-witness L061. Reuse the application
assessment where adequate; no new search is requested merely because
this is an audit. Compare its inspected hypotheses against the exact
proof and approve only the covered scope.

The later audit must check arbitrary v|3 extending to z of F',
restriction to F_aux, the two complete pointed maps over F'_z, and
the same Q-defined curve/changed q_aux at every place. Check the
semistable good-versus-multiplicative descent and the exact nonsplit
height convention before integer normalization. Check the Galois
degree divisor for F_aux, the local quadratic bound, and tower
multiplicativity through F_aux and G separately. No local index may
be assumed to divide nonnormal [G:Q].

Continue if all exact hypotheses and conclusions survive; otherwise
isolate the failing assertion and repair or narrow it without
changing the witness. The native moduli-fiber identification,
G/Q normality, mixed radical/15-torsion information, independent
initial data, native input/action, all-image factorization, pilot
transport, essentiality and finite B>=A remain unresolved. Retain
the recorded IUT reproduction/author source-version qualification.

Full matching Mathlib coverage is unchecked. Supporting abstract
ramification-tower coverage is recorded in the application assessment;
it is not a formalization of L084.
