# Actual ind2 group — completed source comparison

TARGET: Assess whether L017's compact involution is compatible with the actual ind2 group definition in Dupuy–Hilado [DH20b], §4, keeping tensor-packet and initial-theta-data realization as separate unresolved requirements.
CHECKED: 2026-10-05
DECISION: IMPORT
SEARCH_EVIDENCE: Searched exact Dupuy–Hilado ind2/log-shell and First Two Indeterminacies terminology and the cited Hoshi Theorem 7.6; inspected versioned primary definitions and the published supporting theorem, with local overlap and parked source blockers checked.
SOURCE_EVIDENCE: Dupuy–Hilado arXiv:2004.13228v1 (2020-04-28), Definition 3.6.3 and §4 opening/§§4.6–4.8, printed pp. 13, 17, 19–23; arXiv split/version record and author's paper list; Hoshi, Introduction to Mono-anabelian Geometry, PMB (2021), pp. 5–44, Definitions 5.1–5.5, Remark 5.5.1, Theorem 7.6 with proof and Corollary 7.7, printed pp. 29–30, 39–40, 43, DOI 10.5802/pmb.42.
COMPARISON: The cited exposition's local tensor-summand lattice condition is compatible with the already proved g(I)=I if its domain and lattice are identified with L017's singleton pair; this supplies no actual tensor realization. Hoshi's full MLF-pair theorem instead has a profinite-unit scalar kernel over fixed G, so it does not certify arbitrary lattice maps as native lifts.
GAP: No realization of (K,I) as an actual tensor summand is supplied, nor a lift of g to the source group-monoid data. Which structure is forgotten in passing to the tensor-shell action remains an obligation; original initial data, ind3 input, pilot, essentiality and normalization are independent gaps.
REASON: The essential cited definition is now read. Import the source comparison rather than redo the orbit proof; test the independently specified full-pair lift restriction next, without equating it to the entire original ind2.
LITERATURE_REASON: The gate-approved actual-ind2 target changed the scope beyond the ready fixed-packet audit and required unread §4 definitions and their cited theorem.
SCOPE: Source comparison only, preserving L017's proved singleton lattice map; no new tensor counterexample, initial theta data, native group membership theorem or IUT conclusion.

## Exact source and version

The [2020 version](https://arxiv.org/pdf/2004.13228v1) is the work denoted [DH20b] in [the numerical paper](https://arxiv.org/pdf/2004.13108v2#page=19); the bibliography labels are paper-local. The [current record](https://arxiv.org/abs/2004.13228) reports a 2025 split; v2 is the initial-data paper. The [author's current list](https://tdupu.github.io/papers.html) lists the separate indeterminacy preprint without a download. No revised indeterminacy definition was inspected or silently substituted.

## Inspected definition and source qualifications

In v1, §4, I_v=log(O_v^times)/(2p_v), I_vecv is their tensor product. Section 4.8 uses the Q_p-linear group on K_vecv preserving I_vecv, with products over summands. Its formula prints containment; its prose requires lattice isomorphisms. L017 already proves equality and involutivity, avoiding that ambiguity. Section 4.6 treats ind1 through procession maps, tensor products and permutations; it is not a restriction of ind2 to factorwise maps. Definition 3.6.3 uses j=1,...,(ell−1)/2, hence j+1 tensor factors. Footnote 13's blanket determinant-one sentence is not imported. No exact determinant-one restriction on g is inferred from it.

For Hoshi, an MLF is a finite extension of Q_p; a model MLF×-pair is Gal(kbar/k) acting on O_kbar^times. Definitions 5.1–5.3 require the full group, monoid and compatible action. Definition 5.5 and Remark 5.5.1 give profinite unit exponentiation. Theorem 7.6(i–ii) says the forgetful map between pair-isomorphism sets and group-isomorphism sets is surjective with Ind-torsor fibers. Corollary 7.7 identifies its automorphism kernel; for × it is Zhat^times. Read the proof: surjectivity uses reconstructed monoids and Kummer poly-isomorphisms; the kernel argument uses their functoriality when alpha_G=id. This theorem supplies no arbitrary-GL lifting statement for an isolated invariant lattice or a tensor packet.

Primary locators: [DH v1 §4.8, printed p. 23](https://arxiv.org/pdf/2004.13228v1#page=23); [Hoshi definitions, printed pp. 29–30](https://www.numdam.org/item/10.5802/pmb.42.pdf#page=26), [Theorem 7.6 and proof, printed pp. 39–40](https://www.numdam.org/item/10.5802/pmb.42.pdf#page=36), [Corollary 7.7, printed p. 43](https://www.numdam.org/item/10.5802/pmb.42.pdf#page=40). The [publication record](https://pmb.centre-mersenne.org/articles/10.5802/pmb.42/) dates online publication to 2022-03-04 in the 2021 volume. The January 2017 RIMS-1868 precursor was read as a version comparison, not identified page-for-page with the published paper.

## Comparison with the existing input

L017 has K=Q_3(pi), pi^27=3, J=log(O_K^times), I=J/6. Its complete-lattice inputs are L015/L016. The Q_3-linear compact map g already satisfies g(I)=I and g^2=id. Thus the lattice-preservation test in the DH definition offers no new exclusion conditional on an exact identification of domain and lattice. This is a comparison of an existing proved property with a definition, not a new membership proof for actual data.

That conditional comparison does not construct a summand K_vecv, a tensor-shell identification or an extension across the source packet. In particular, one factor is not a procession level in Definition 3.6.3. Nor does it lift g through an invariant/torsion quotient to a full MLF×-pair. The Hoshi citation supplies a concrete full-pair kernel test but does not identify that kernel with all transformations of the later forgotten structure. No contradiction between the two sources or exclusion from original IUT is claimed.

The narrow next target tests the full-pair lift over identity G using the already explicit map. It is independently testable without tensor or initial-data construction. Passing would support that particular lift route; failure would abandon only that route and preserve the broad-lattice auxiliary result. Actions with nonidentity G and quotient-only maps remain outside it. See the separately prepared [lift assessment](2026-10-05-degree-27-fixed-galois-lift.md), which must receive supervisor approval before research.

## Search, overlap and stopping evidence

Queries included `"Dupuy" "Hilado" "ind2"`, `"Dupuy" "Hilado" "First Two Indeterminacies" log-shell`, `Yuichiro Hoshi "Introduction to mono-anabelian geometry" "7.6"`, and `"Ind2" "tensor" "log-shell" Dupuy Hilado`. An initial unquoted DH20b query was irrelevant; no result from it is used. Search snippets and secondary discussions supplied no theorem inputs. The published Hoshi PDF at the journal host timed out; its Numdam copy was readable, so there is no persistent blocker for this comparison. PDF screenshots returned no readable image and were not treated as evidence; continuous extracted primary text supplied the inspected definitions and proof cases.

Read L017 fully and the needed L016 coefficient/functional ranges. Local targeted search found no prior actual-ind2 comparison in the recent assessments. Reuse the ready orbit audit and the earlier version/split check. ATTEMPTS/006 and the pilot assessment retain the stopped current-IUT-I/quotient access routes; the unread log-Kummer envelope in the hull-screening assessment remains parked. No failed native-source retrieval was repeated. The official challenge statement was already rechecked today in the full-orbit assessment and is reused without changing the target.

No new lemma, calculation, mathematical script, DAG or argument overview was written. This turn's advance is removal of the essential definition-reading gap and a precise supporting-theorem scope distinction, not new mathematics or progress beyond the cited results. Full matching Mathlib coverage and supporting MLF-pair kernel coverage: **not checked**; unknown availability is not absence.
