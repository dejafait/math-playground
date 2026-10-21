# Exact auxiliary field — all-place local-height source assessment

TARGET: Determine whether L078's unchanged E_L/G has multiplicative reduction at every place v above 3 with native integer local height h_v=30e(G_v/Q_3) prime to seven, without assuming G/Q normal.
CHECKED: 2026-10-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the two singleton-height assessments, exact-G semistability coverage and L073,L077,L078,L081; checked ATTEMPTS/027,034 and history/317,329. Targeted nonsplit Tate and ramification-tower searches located Silverman C.14.1(d), Milne Exercise 4-2 with its solution, and the accessible GenEll journal text; full relevant statements/cases were inspected below.
SOURCE_EVIDENCE: Mochizuki, Math. J. Okayama Univ. 52 (2010), 1–28, local setup pp.16–17, Definition 3.3 and Remark 3.3.1 p.17; Silverman AEC second edition (2009), VII.5.4(b) pp.197–198 including proof and C.14.1(b,d) p.445; Milne ANT v3.08 Exercise 4-2 p.83 and solution p.155, 7.42–7.43 p.124, and reused 3.34 pp.59–60/8.1–8.2 pp.135–136; Kedlaya fall 2004 Tate Theorems 1–2 pp.3–4 and (3) p.2.
COMPARISON: Known results cover finite local bases, geometric Tate-parameter uniqueness, persistence of good/multiplicative reduction, nonsplit height normalization and ramification towers without normality of G/Q; L061 itself applies only to the earlier witness. No source already states the unchanged exact-G all-place specialization.
GAP: Apply those results to every actual G-place above 3, transport the geometric curve/parameter through the corresponding F'-completion, and check ramification in both towers through F' rather than using divisibility by nonnormal [G:Q]; the requested height and coprimality verdict remains unproved.
REASON: The essential source omissions are resolved; this is a bounded reproduction/specialization of known methods, with no need for a new general lemma or reproof. The newly ready assessment requires separate supervisor approval before mathematics.
LITERATURE_REASON: Changed curve/base and potentially nonsplit places were outside the prior split-height application; essential unread nonsplit normalization and tower coverage required this literature-only turn.
SCOPE: Exactly TARGET with the same auxiliary witness, D,s,t,iota, G subset F'=F_aux(s), and embedded H,N; no normal closure, new curve, global normality verdict or sufficient-initial-data claim.

This completes source comparison, not the mathematical specialization.
The exact TARGET is preserved for separate approval and a later attempt.

Main gap: original finite B>=A. The proposed intermediate target would
test the local-height and residue-characteristic prerequisites for a
possible selected moduli place above 3. A positive answer would leave
normality, complete selected data and the original numerical comparison
independent. A negative answer would identify a precise obstruction to
this unchanged auxiliary instance; it would not refute IUT.

Essential inputs are L073's same auxiliary Q-curve, its
changed Tate parameter valuation and Galois F_aux degree divisibility;
L077's actual quadratic extension and complete pointed comparison;
L078's literal G subset F'; and L081's semistability over this G.
L061 is a method/source comparison, not a result about this witness.
If connecting all v above 3 to a native moduli-place fiber, check L079's
actual F_mod identification separately and retain its exact hypotheses.
No selected section or sufficient initial data is assumed.

## Inspected primary coverage

The earlier assessments remain adequate for IUT I May 2020 Definition
3.1(b)–(c), pp.61–62, read in the recorded reproduction: its bad-place
test uses the whole base-field place fiber. Their reproduction/author
byte identity remains unverified. This target tests all places above 3
directly and does not assert a complete native instance.

[GenEll, published journal PDF](https://www.math.okayama-u.ac.jp/mjou/mjou52/_01_mochizuki.pdf),
52 (2010), pp.16–17, was read from the finite-local-field setup through
Definition 3.3 and the complete Remark 3.3.1. The valuation is surjective
onto Z; the initial semiabelian special fiber is G_m. Height is the
integer order of the Tate parameter. The remark extends it to potentially
multiplicative curves by dividing the height over an extension with
multiplicative reduction by its ramification index, independently of
that extension. This is not a point's canonical local height. The
journal passage now supplies direct coverage; no equivalence of its
entire text with the earlier 25-page author version is claimed. Author
PDF interior requests and the old repository URL failed this turn;
neither failure blocks this accessible primary journal passage.

[Silverman, AEC, second edition](https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf),
VII.5.4(b), pp.197–198, states persistence of good and multiplicative
reduction under finite extension; its full proof case was inspected.
It uses a general Weierstrass change and the discriminant/c4 criterion,
without the residue-characteristic restriction of the separate (a)
proof. C.14.1(b,d), p.445, was read completely: a nonintegral j admits
a Tate curve over the complete discretely valued base; a nonsplit
curve becomes that curve over a quadratic extension, unramified
exactly in the multiplicative case. These are imports, not new results.
L081 supplies semistability; it must not be read as splitness.

[Kedlaya, Introduction: the Tate curve](https://kskedlaya.org/18.727/tate-curve.pdf),
fall 2004, Theorems 1–2, pp.3–4, and (3), p.2, were rechecked for
the finite-Q_p-extension hypotheses, geometric uniqueness of q and
the integral j-series. Its p.4 proof of 2(a) uses series inversion;
2(b) cites Silverman V.5.3. Only these Tate statements are needed,
not the separate Proposition 3 argument. They cover parameter comparison
after embedding into a common algebraic closure even when the curves
are not isomorphic over G_v itself.

[Milne, ANT v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Exercise 4-2, p.83, and its entire ramification-index solution, p.155,
were inspected: indices multiply in number-field towers, by prime
factorization, with no normality hypothesis. Corollary 7.42 and Remark
7.43, p.124, give local degree ef and integer-valuation restriction;
their displayed proof/formulas were read. Reuse the prior complete
3.34 Galois proof and 8.1–8.2 completion coverage. These results allow
arbitrary v to be extended to F', then restricted to F_aux. They
do not justify a local-index divisibility claim for nonnormal [G:Q].

## Exact specialization obligations and stopping test

A later proof must take arbitrary v|3 of G, extend it to a place z
of F', and use L077's actual map and inverse over F'_z. It must
compare with the base change of L073's same Q-defined E_aux and
its changed q_aux, not q=3^30. Verify geometric parameter transport
and reduction descent using L081 and the cited persistence theorem;
if nonsplit, apply the cited splitting/height convention explicitly.
Do not infer splitness from semistability or reuse the one embedded H
completion for all places. These are pending application checks.

For coprimality, retain the actual tower F'/F_aux/Q and separately
F'/G/Q at z. Check the quadratic local step using s^2=D, the Galois
degree divisor of F_aux from L073, and the tower identities before
concluding anything about e(G_v/Q_3). No ramification or height verdict
for this instance is established by this source review. L079 is not
an input to the all-v|3 statement; it would be needed for a later
identification with the native moduli-place fiber.

Continue if every v satisfies multiplicative reduction and exactly the
requested integer-height/coprimality threshold. A failing place stops
this unchanged instance's local test; an unproved transport or tower
premise leaves the attempt incomplete and requires narrowing. A pass
would clear one prerequisite only, leaving normality and the original
comparison independent. This is a specialization obligation, not an
equivalent formulation offered as a resolution or a claim of novelty.

ATTEMPTS/034's cyclic separator stop remains intact. History/317 records
that the full mixed kernel had no new data; this continuation does not
relabel that same test or claim new kernel information. The local-height
question is independent of deciding G/Q normality. Independent initial
data, retained radical/scalar questions, native input/action, all-image
factorization, pilot transport, essentiality and finite B>=A remain
unresolved. No duplicate all-place exact-G result was found in the
scoped predecessors; no global novelty inference follows from that.

## Mathlib

Full matching height/Tate coverage is unchecked. Supporting
[Ideal.ramificationIdx_tower](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RamificationInertia/Ramification.html#Ideal.ramificationIdx_tower)
was inspected with its commutative algebra/scalar-tower, lies-over and
flatness hypotheses. It covers the abstract index identity, not this
elliptic-curve or native-height application. No formalization is claimed.
