# Singleton all-F-place q-order — completed source assessment

TARGET: Test Definition 3.1(c)'s q-order coprimality at every F-place above rho(w), using the retained E_0,F and native F_mod without computing F_mod.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped L045,L048,L051,L060 and selected-place/ramification assessments leave this obligation open; exact GenEll/Definition 3.3/local-height and exact-title searches located the primary author text and journal repository. Complete load-bearing author passages and IUT place clauses were read; details below.
SOURCE_EVIDENCE: IUT I May 2020 Definition 3.1(b)-(c), pp.61-62, and bibliography p.185, read in the retained 186-page reproduction; Mochizuki Arithmetic Elliptic Curves in General Position, author-listed 2009-02-17 text, local setup pp.14-15, Definition 3.3 p.15, Remark 3.3.1 p.16, read completely for normalization; Milne ANT v3.08 Theorem 3.34 pp.59-60, statement and full Galois proof case read, with earlier inspected valuation/completion coverage reused.
COMPARISON: GenEll uses the surjective integer valuation of the local base field; IUT tests every F-place over the selected moduli subset. Known ramification restriction and Galois prime-factorization results cover the needed transport mechanism; L045,L048,L051,L060 supply the retained arithmetic inputs, but their uniform native application has not been carried out here.
GAP: Specialize the cited definitions and ramification results to the same curve and every F-place over rho(w), explicitly distinguishing absolute v_3, integer ord_(F_t), and ord_N; compute the coprimality verdict next turn.
REASON: Essential normalization coverage is now inspected and sufficient for exactly TARGET; no new theorem or reproof is needed. The remaining work is a bounded known-method application, not completed mathematics in this literature-only turn.
LITERATURE_REASON: Changed target from section/cusp auditing to the all-F-place q-order predicate, with essential unread GenEll Definition 3.3 normalization.

SCOPE: Exactly TARGET with the retained curve, fields, singleton and conditional native inclusion below; no F_mod computation, field enlargement, new cover, full initial-data claim or numerical IUT comparison.

This completed assessment supersedes the pending review only as source
coverage. Its newly changed ready status is subject to the supervisor's
separate approval; no mathematical application is performed here.

Retain L045,L048,L051,L060 and their hypotheses: unchanged E_0/Q,
F=Q(zeta_60,E_0[30]), K_glob=F(E_0[7]), u,w,H subset N, full
30-torsion, M>=max(M_tors,31), fixed pointed Tate isomorphism,
changed q_0 in Q_3 with v_3(q_0)=30 and v_3(3)=1, and native
Q subset F_mod subset F with rho the restriction of places. Keep the
same singleton {rho(w)}, full section, U,Q and all retained local maps.
Do not identify F_mod with Q, K_glob with N or q_0 with 3^30.

## Inspected native scope and bibliography

[IUT I, May 2020 author source](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf),
Definition 3.1(b)-(c), printed pp.61-62, was read through the retained
[reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf).
Clause (b) defines V(F)^bad as the full inverse image of V_mod^bad;
(c) requires ell prime to its residue characteristics and the q-orders
at those F-places. It does not test only the section's K_glob-place.
The bibliography, printed p.185, identifies GenEll as S. Mochizuki,
Arithmetic Elliptic Curves in General Position, Math. J. Okayama Univ.
52 (2010), 1-28. Reproduction/author byte identity and journal-version
equivalence remain unverified; no stronger version claim is made.

## Inspected normalization and its hypotheses

The [author's paper list](https://www.kurims.kyoto-u.ac.jp/~motizuki/papers-english.html)
dates its [GenEll text](https://www.kurims.kyoto-u.ac.jp/~motizuki/Arithmetic%20Elliptic%20Curves%20in%20General%20Position.pdf)
2009-02-17. This is a 25-page author version. Its local setup, printed
pp.14-15, assumes a finite K/Q_p and a surjective v_K:K^times -> Z.
The semi-abelian scheme has proper generic fiber and special fiber G_m.
Definition 3.3, p.15, defines local height as v_K(q_E), a positive
integer. The preceding paragraph identifies q_E with the Tate parameter
and its ideal with the pulled-back moduli boundary divisor. Thus this
is neither a point's canonical local height nor a logarithmic degree.
Remark 3.3.1, p.16, extends the definition to potentially multiplicative
reduction by dividing the height after extension by the ramification
index. The next application uses L051's stronger split case.

The [journal repository PDF](https://ousar.lib.okayama-u.ac.jp/files/public/3/33503/20160528030421647295/fulltext.pdf)
identified the 2010 publication; a search extract displayed Definition
3.3, but attempts to retrieve its precise interior range failed. That
extract is corroboration only. Coverage rests on the complete author
setup, definition and remark read above, not on journal pagination or
an unread theorem. No proof of a height inequality is needed or imported.

## Transport coverage reused and specialization boundary

Reuse `2026-10-12-native-all-places-above-three.md` for Milne ANT
v3.08 (19 July 2020), Theorem 3.34 and its Galois proof, completion
interpretation in chapter 8, and Kedlaya's Tate Theorems 1-2. L051's
all-completion proof explicitly transports the Q-defined coefficients,
origin and pointed Tate isomorphism over Q_3. Reuse
`2026-10-10-selected-bad-place-ramification-critical-audit.md` for
Milne 7.42-7.43 and 8.10 on integer valuation restriction by ramification
index; its earlier full source inspection is adequate and unchanged.

[Milne ANT](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Theorem
3.34, printed pp.59-60, was also checked directly: finite separability
over a Dedekind domain gives sum e_i f_i=[L:K]; in the Galois case
the common indices satisfy efg=[L:K]. The full Galois proof, including
prime transitivity, was read. This supplies a degree-based route for
controlling ramification factors, without computing their exact values.
General valuation restriction is imported, not reproved.

The later attempt must identify the actual place fiber using the
conditional Q subset F_mod subset F, retain the same pointed curve at
each completion, convert its absolute parameter valuation using the
integer normalization, and apply L045's global degree divisibility.
These are application obligations, not conclusions of this review.
Do not borrow the order in N or require explicit F_mod. No numerical
local order or coprimality verdict has been established in this turn.

## Relevance, duplicates and stopping test

Queries included `site.kurims.kyoto-u.ac.jp Mochizuki "GenEll" "3.3"`,
`"Mochizuki" "Definition 3.3" "local height"`, and the exact GenEll
title with valuation/pdf terms. The native bibliography, rather than
a secondary interpretation, fixed the reference. Local selected-place
assessments and L045,L048,L051,L060 separate this pending test from
their established conclusions. ATTEMPTS/030,031 stop other cover or
coordinate mechanisms and are preserved; neither is an obstruction
to this different, independently testable arithmetic condition.

The main gap remains original finite B>=A and actual input/action/pilot/
essentiality. A verified coprimality result could remove one independent
native-data admissibility gap. Continue to a mathematical specialization
only on the exact covered hypotheses. Its discriminating test is the
required gcd(ell,h_t)=1 for every t above rho(w), with h_t the native
integer local height; a failing place stops this singleton application.
An unverified normalization/transport premise instead keeps that
application incomplete. Other initial-data conditions remain separate.
Full matching Mathlib coverage is not checked. No novelty is claimed.
