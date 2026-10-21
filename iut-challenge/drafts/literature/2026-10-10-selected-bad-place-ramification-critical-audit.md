# Selected bad-place ramification — separate audit source coverage

TARGET: Critically audit L041's selected bad-place divisibility ell | e(D_w/Q_p), checking normalized valuation transfer, full local torsion-field identification, finite inertia order and ramification in nonsplit cases under Dupuy–Hilado arXiv:2004.13228v1.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the predecessor's documented exact/stronger Tate-torsion searches and nonsplit proof review; compared all three proof sections of L041 with that coverage and ATTEMPTS/022,025,026. Targeted author-PDF searches for ANT Theorem 7.38, completion generation preceding 8.1, and EC2 geometric torsion located explicit supporting statements; no duplicate new ramification theorem is proposed.
SOURCE_EVIDENCE: Reuse the predecessor's inspected Dupuy–Hilado arXiv:2004.13228v1 sections 2.4.2,3.2, Definition 5.3.1(2),(4),(5), complete Lemma 5.4.1 proof, Definition 5.5.1, Milne EC2 III.3 (24)–(26), ANT v3.08 7.42,7.43,7.58(a),8.10–8.11; additionally read ANT 7.38 with complete proof (p.123), opening of chapter 8 through 8.1 (pp.135–136), and EC2 II.6.3 with characteristic-zero proof case and III.3.12–3.13 (pp.70–71,98).
COMPARISON: Known full-torsion inertia and local-field theorems cover the audit's external inputs; explicit completeness and geometric torsion citations supplement the prior coverage. Their applicability to L041's embedded coordinate field and normalized tower still needs an independent mathematical audit, not a reproof of Tate theory.
GAP: Independently audit the specialization, especially the all-coordinate completion identification and nonsplit inertia application; source readiness does not verify those steps or the divisibility conclusion. No original finite B>=A, native applicability or sufficient admissibility is supplied.
REASON: Exact source scope is now approved by reuse plus narrowly necessary primary citation completion; the completed proof attempt is preserved, and the next turn defaults to its independent mathematical audit.
SCOPE: Exactly TARGET under L041's unchanged F_0,v,u,w,H_0,H,D,N and prime-to-ell hypotheses; permits citation clarification in that audit, but no exact-field specialization, tensor extension, altered initial data or new ramification mechanism.

LITERATURE_REASON: The supervisor requires separate approval of this newly named critical audit; its full completed-coordinate-field check exposed essential completeness and geometric torsion-count citations not explicit in the predecessor. Unchanged Tate and inertia coverage is reused.

## Retained audit obligations

Essential canonical input: L041. Its proof imports named external results,
with no previous local lemma as a mathematical premise. The prior
assessment is
`drafts/literature/2026-10-10-tate-division-field-ramification-prerequisite.md`.
Reuse that ready coverage rather than repeat unchanged browsing.

Retain F_0=Q(j_E), v in S, H_0=F_{0,v}, u=w restricted to F,
H=F_u, D=F(E[ell]), N=D_w, p odd, ell>=5, ell!=p,
ell prime to ord_v(q_v) and [F:F_0], and F/F_0 Galois.
The audit must check the geometric integer q-series and its leading
term, the local decomposition degree, valuation restriction, all full
local torsion coordinates after completion, finite Galois faithfulness,
absolute-to-finite inertia inclusion, exact order ell, |I|=e and the
tower to Q_p. In particular the audit cannot assume split reduction
over H, identify a cyclic subgroup field with D_w, assume D_w/Q_p
Galois, or silently discard the global degree condition.

Continuation test: approve only the exact independent audit scope if
the already inspected primary coverage is adequate, or name essential
missing coverage before mathematical audit. A later audit passes only
if every stated hypothesis and essential identification holds; repair
or narrow on failure. Full matching Mathlib coverage remains unchecked.

Downstream use is a necessary ramification screen for future local
packets. The original finite B>=A, actual/native input/action, global
data, marked pilot transport and essentiality remain unresolved.
L039/L040 and ATTEMPTS/022,025,026 remain prior stops and supply no
premises to L041. No exact-field specialization or tensor-component
extension is proposed in this continuation.

## Completed source-scope comparison — 2026-10-10

The predecessor assessment is adequate for the unchanged geometric
parameter, Galois degree, selected full division field and transvection
inputs. Its recorded versioned-PDF reading includes both split and
nonsplit cases of Dupuy–Hilado Lemma 5.4.1. Reuse that coverage rather
than require the inaccessible original Silverman chapter. A targeted
check of the [versioned HTML theorem statement](https://arxiv.org/html/2004.13228v1#S5.SS4)
also retains normalized ord_L(j_E)<0 and the prime-to-ell condition;
the predecessor's PDF pagination remains authoritative. The theorem
allows a nonsplit curve over the unchanged local base. Its subsequent
canonical-subspace discussion is outside this audit's imports.

### Explicit completion coverage

[Milne ANT v3.08](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
Theorem 7.38, printed p.123, covers a finite separable extension of a
field complete for a discrete absolute value. It gives a unique
extended absolute value and completeness. The full proof was read,
including its final basis-coordinate Cauchy argument. The opening of
chapter 8, p.135, preceding Proposition 8.1 (p.136), explicitly
identifies a completed simple finite separable extension with the
field generated over the completed base by its embedded generator.
These supply precise sources for L041's topology step; 7.42–7.43
alone should not be its completeness citation. The later audit must
check finiteness, separability and the restricted topology for the
actual coordinate field, and the use of density/closedness. This
review does not prove that identification.

### Explicit full geometric torsion coverage

[Milne EC2 (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
Proposition II.6.3, printed pp.70–71, states that geometric m-torsion
is free of rank two over Z/mZ when m is prime to the field
characteristic. Its characteristic-zero proof case was read, together
with Theorem III.3.12 and Proposition III.3.13 and their proofs on
p.98. The latter states invariance of torsion under extensions of
algebraically closed fields. This covers the point-count fact needed
in both characteristic-zero algebraic closures. The audit must still
check injective embedding, distinctness, preservation of the group
equations and all coordinates. A point-count citation suffices for
that obligation; scheme-theoretic etaleness need not be an additional
unproved premise. No changed torsion hypothesis or reproof is proposed.

### Decision and limits

SPECIALIZE authorizes exactly the saved critical audit. Normalized
valuation transfer uses the already inspected ANT 7.42–7.43 and
8.10. The nonsplit transvection import uses the complete prior
Lemma 5.4.1 coverage. The finite faithful action, exact-order check
and absolute-to-finite inertia inclusion remain audit obligations;
the inspected ANT 7.58(a) and 8.10–8.11 supply the external
ramification inputs. This is a comparison of coverage, not a
verification of L041's argument or conclusion. Any citation
clarifications belong in the canonical lemma during that audit.

No new theorem search is needed for the unchanged elementary finite
Galois and group-order steps, and no lattice calculation is proposed.
The predecessor's documented exact/stronger searches and the three
preserved realization stops give no competing local result requiring
a new proof here. An adequate citation is imported; no originality
or discovery beyond the sources checked is claimed. Mathlib coverage
remains unchecked.

Continue with the independent audit only under the retained full
hypotheses. Repair or narrow if any normalization, full-field,
nonsplit or inertia application fails. Passing supplies only a
necessary bad-place screen, useful before selecting future packets;
it leaves original finite B>=A and all actual/native, global,
marked-pilot and essentiality bridges open. No lemma, mathematical
script, DAG or argument overview was modified in this literature turn.
