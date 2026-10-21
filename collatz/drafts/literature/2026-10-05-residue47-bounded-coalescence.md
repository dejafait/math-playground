# Bounded coalescence on a surviving least-root cylinder: source assessment

TARGET: Determine whether there exist integers L>=1 and N>=1 such that every n=47+243k>N, k>=0, has a positive c<n with c=20 modulo 27 and T^s(c)=T^t(n) for some 0<=s,t<=L, retaining actual parities on both paths.
CHECKED: 2026-10-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Eleven focused exact-statement, bounded-coalescence, merging-trajectory and obstruction queries were executed; queries, inspected sources and unread leads are distinguished below. No matching uniform theorem was established by this bounded search.
SOURCE_EVIDENCE: Read Sodelin's B-S20-ANCESTOR-DEPTH-OBSTRUCTION-001 statement and proof cases at lines 8–74 and 94–114; L4 sections 1–5; corrected L5 sections 1–7; AB_mersenne_inverse_word_no_go sections 2–6; Rozier (2019), Lemma 1 and proof, pp. 2–3; LaDue arXiv:1709.02979v3, sections 3–4, Theorems 3.2 and 4.1 and both proof cases, pp. 3–5. Exact links and qualifications follow.
COMPARISON: The ancestor theorem and its simultaneous extension exclude two alternative one-path certificates, not a common later iterate. The Mersenne theorem excludes unrefined whole-parameter-family certificates, not arbitrary parameter-dependent companions on the ternary cylinder. Known guarded finite-word semantics and adjacent-pair identities supply machinery but neither the requested cover nor an all-L obstruction.
GAP: Decide the exact two-path cover with uniform L,N, actual parities, positive residue-20 companion and order against the original n; no existence, nonexistence or finite base convergence is assumed.
REASON: Complete the changed-target review separately from mathematics; allow one bounded attempt with inspected guard semantics instead of repeating Attempt 011's ancestor-only search. No novelty conclusion follows from the search.
SCOPE: The exact TARGET, including both empty paths, parameter refinement and choices of words depending on n; known unrefined-family completeness and no-go theorems may be used only within their stated narrower hypotheses. An exact finite-clock test or an analytical all-L obstruction is within this review; an infinite coalescence or recursive-rank theorem is outside it.

## Hypotheses

Use the positive-integer shortcut map T of foundations, not the odd-only map. Both clocks count shortcut steps. Essential local context is L013's visitation and L014–L018's same-original-root restrictions. Their relevant statements and L014's convergence-transfer proof were checked; the existing ancestor assessment and Attempt 011 were compared. The supplied overview records that 47+243k survives those necessary conditions.

The [MathPrize statement](https://mathprize.net/posts/collatz-conjecture/), page dated 2021-07-07, was rechecked on 2026-10-05: every positive integer under the unshortened map must eventually reach 1. This is unchanged. Prize terms are not mathematical inputs.

## Conclusion

EXPLORE approves the unchanged target for a separate mathematical turn. The review supplies no new lemma, cover, obstruction or convergence result. Its outcome is EXPLORATION, classification NOVELTY_UNCHECKED. Source comparison supplies actionable coverage, not progress beyond the checked sources. There is no essential source-access blocker.

## Proof

This section records source statements and applicability limits, not a derivation of the target.

### Ancestor obstruction and the positive n-side clock

Sodelin, *An unbounded-depth obstruction for residue-20 ancestor covers*, node `B-S20-ANCESTOR-DEPTH-OBSTRUCTION-001`, [statement and proof, lines 8–41; simultaneous case and scope, lines 56–74](https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/lemmas/Bounded_Ancestor_Depth_Obstruction.md), uses precisely the local shortcut map and S={positive integers 20 mod27}. For every L,a>=0, r=47+3^(L+3)a has no smaller S ancestor at time <=L. Its proof transfers admissible inverse words to anchor 47, preserves the modulo-27 guards, and uses the fact that 20's forward orbit misses 47.

The simultaneous theorem prescribes independently a forward horizon H and ancestor horizon L, both >=1. Its CRT roots satisfy r=47 mod3^(L+3) and r=-1 mod2^(H+1); they defeat direct descent through H and ancestors through L together. Lines 94–114 give a second simultaneous construction on the source's q5 cylinder. Neither theorem asserts that an inverse path from a later forward iterate cannot end below r. Lines 67 and 114 explicitly leave general coalescence available. Thus their stated conclusions do not settle our t>0 target; extending the anchor proof would be new mathematical work and was not done here. Attempt 011's stop remains valid at t=0.

### Exact machinery and its limits

Reuse the finite-parity assessment in [the 2026-09-26 review](2026-09-26-current-target.md). Rechecked Olivier Rozier, *Parity Sequences of the 3x+1 Map on the 2-adic Integers and Euclidean Embedding*, INTEGERS 19 (2019), A8, [Definition 1, Lemma 1 and proof, pp. 2–3](https://math.colgate.edu/~integers/t8/t8.pdf#page=2). It uses the same T; every finite binary parity word specifies one starting class modulo 2 to its length, and its proof supplies the affine endpoint identity. These statements cover finite positive realizations without probabilistic parity assumptions. They assert neither two-word order nor uniform coverage. No reproof of this arithmetic is warranted.

Sodelin, *L4 — General inverse-word coalescence semantics*, dated 2026-08-23, [sections 1–5, lines 7–179](https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/lemmas/L4_General_Inverse_Word_Coalescence.md), defines inverse E(y)=2y and O(y)=(2y-1)/3, with O allowed only at y=2 mod3. Every intermediate O needs this guard. The theorem compares a uniform forward binary cylinder with a guarded inverse affine family reaching its endpoint. Both a smaller slope and equal slope with a smaller intercept can give a smaller positive companion. A further O can require parameter refinement once all factors of 3 in the leading coefficient are consumed. This supplies neither residue-20 membership nor a cover of our cylinder.

The supporting [corrected L5, sections 1–7, lines 35–268](https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/lemmas/L5_Inverse_Word_Search_Completeness_Bound.md) bounds inverse length by forward time only for uniformly admissible whole-family words on an unrefined binary cylinder. Its proof retains the equal-slope case; section 7 excludes refinement from its completeness claim. It must not prune parameter-dependent inverse words in the full TARGET. Strict-slope-only searches would omit valid certificates.

Read the primary theorem behind ledger F018: [Sodelin, Mersenne inverse-word no-go, sections 2–6, lines 31–252](https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/routes/AB_mersenne_inverse_word_no_go.md). For K>=1, M_K(x)=2^K(x+1)-1, x>=0, and uniform forward time 0<=t<=K, every uniformly admissible whole-family inverse word has slope at least 2^K. Its equality case reconstructs M_K exactly. The proof checks loss of factors of 3 and both slope cases; section 6 expressly allows refinement. Our parameter-dependent cover is outside that unrefined scope. This is a warning against that restricted search class, not a disproof of our target. No extension to a ternary-restricted parameter is imported.

### Known explicit coalescence does not supply this cover

Mark D. LaDue, *Clusters of Integers with Equal Total Stopping Times in the 3x+1 Problem*, [arXiv:1709.02979v3, 2017-11-15, sections 3–4, pp. 3–5](https://arxiv.org/pdf/1709.02979v3#page=3), Theorems 3.2 and 4.1, treats odd m>1 written m=2^p(2q+1)-1, p>=1, q>=0, with p=v_2(m+1). The (p+2)-step shortcut iterates of m and m-1 agree exactly when p and q have the same parity. Read Lemma 3.1's actual trajectories and both Theorem 4.1 proof cases; equality does not assume convergence. Its companion is the specified adjacent integer and its clock depends on p. It provides neither the required S companion nor the uniform bound on every member of 47+243k. It is comparison machinery, not an input establishing the cover. The earlier Andaloro odd-only assessment is reused for scope; no map-time conversion or new specialization is made.

### Relevance, discriminating test and continuation

The main gap is universal eventual descent. The intermediate target is the exact TARGET. A guarded cover could transfer convergence from smaller S companions to a hypothetical least root through the common future state, as contemplated in the startup review; a finite base needs separate proof. Other surviving cylinders and universal descent remain unresolved even if this cover succeeds. No hypothetical least root is asserted to exist.

Approve one bounded mathematical attempt using the inspected finite-word semantics, retaining every intermediate parity, positivity, S membership, offset and original-root comparison. Parameter refinements and equal-slope/smaller-intercept cases must be kept. A complete finite-clock cover with explicit L,N, or an all-L obstruction with an unbounded counterfamily in this cylinder, is decisive route evidence. A fixed-L miss is only a bounded diagnostic; raising L without a new mechanism does not meet the continuation test. Neither F018 nor the ancestor anchor theorem licenses an all-L conclusion for the two-path target.

No mathematical exploration turn is spent here. Bounded-coalescence has one literature EXPLORATION and zero mathematical turns. Attempts 009–013 and their separate stops or parked gaps are preserved; none is reopened.

### Search and provenance

Queries actually executed:

- `Collatz "bounded coalescence" residue`
- `Collatz "47" "243" "coalescence"`
- `Collatz smaller integer merging trajectories bounded time theorem`
- `site:github.com/Sodelin/Collatz-Conjecture-Work "simultaneous" "coalescence"`
- `Collatz "bounded coalescence" theorem`
- `site:github.com/Sodelin/Collatz-Conjecture-Work "Bounded" "cover" "OOEO"`
- `Collatz "47+243k" coalescence bounded`
- `Collatz "20 modulo 27" coalescence`
- `Collatz "bounded" "coalescence" "smaller"`
- `site:github.com/Sodelin/Collatz-Conjecture-Work "Mersenne" "inverse" "L5"`
- `Collatz "bounded coalescence" "47"`

Search snippets led to the primary notes above; the atlas served only to locate L5 and the Mersenne theorem. The failure ledger F015–F018 supplied scope warnings, followed to the primary statements rather than imported as proofs. Local paired-state coalescence and Attempt 011 were duplicate checks; neither settles the changed target. L024 remains a distinct single-coordinate budget obstruction, not a coalescence theorem.

[arXiv:2005.09456](https://arxiv.org/abs/2005.09456) was a discovery hit whose abstract preview identifies a numerical coalescence study; the landing page was opened, but no theorem or full-text assessment was made. It is not imported. The bilateral workbench note remains an unread theorem lead, as recorded in the old ancestor review. Other claimed resolutions and newer synchronized-coalescence search hits were not assessed. They are not evidence of a universal theorem or of novelty.

The Sodelin notes were read from live main on 2026-10-05; no immutable revision was obtained. They are informal public mathematical inputs, with the full no-go and completeness formalizations pending. No external checker or Lean build was run. The published Rozier and versioned LaDue papers anchor the standard finite-word and coalescence comparisons.

## Mathlib

Full matching bounded residue-20 coalescence cover or obstruction: **not checked**. Supporting congruence, iteration and affine arithmetic: **not checked**. External partial Lean claims do not establish Mathlib coverage, and unknown availability is not absence.
