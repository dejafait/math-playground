# Combined flowed Ward-response literature assessment

TARGET: Compute the g^2 log(sqrt(tau)/a) coefficient of the remaining response Cov(O_i, V_a S_g - J_3 - J_6) for L010's two Wilson-flow probes, including action, measure, and flow corrections.
CHECKED: 2026-09-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searches for gradient-flow translation Ward identities, one-loop lattice energy-momentum matching, generator renormalization, and fixed-boundary counterterms led to the primary texts listed below; references from Del Debbio–Patella–Rago and Giusti–Pepe were followed to flow renormalizability and general-SU(N_c) matching.
SOURCE_EVIDENCE: Read https://arxiv.org/pdf/1306.1173v1 sec. 3.1 and 6, eqs. (6.1)–(6.17); https://arxiv.org/pdf/1101.0963v2 sec. 7 and 8.2; https://arxiv.org/pdf/1006.4518v3 eqs. (2.28)–(2.33); https://arxiv.org/html/1304.0533v6 sec. 2–3; https://arxiv.org/html/1503.07042v2 sec. III; https://inspirehep.net/files/8597677d931595baa34d5f59b02a2fb6 sec. 3 and 5.2, Table 1; https://arxiv.org/pdf/hep-lat/9207009v1 sec. 2.5. Versions and scopes follow.
COMPARISON: Known perturbative flow finiteness, finite translation-generator renormalization, and general-SU(N_c) clover stress matching cover substantial bulk inputs; no inspected statement evaluates the exact remaining covariance for L010's bare-normalized probes, endpoint-averaged generator, plaquette triplet, and all-face fixed boundary.
GAP: Justify the use of those inputs for the specified insertion and boundary conditions, retain the bare 1/g^2 probe factors and all order-g^2 corrections, and determine the two leading cutoff-log coefficients with control of the remaining cutoff dependence.
REASON: Reuse the established bulk results by citation and investigate only their stated applicability differences; the existing literature does not justify assigning a coefficient, especially zero, to this covariance without that work.

## Scope and relevance

The exact saved target is preserved. In its notation, g is L010's **bare** coupling, O_i is its centered nonlinear Wilson-flow probe, and J_3,J_6 are its unflowed nonlinear insertions. The setting stays SU(2), D = (-4,4)^4, relative boundary conditions from fixed links, a = 8/N with even N, the specified compact displacement, and tau = 1/16. Neither a new probe normalization nor a different infrared regulator is substituted.

The gap is the interacting Ward response after the isolated Haar term. A logarithmic coefficient would diagnose the ultraviolet behavior of the two-channel normalization and help decide what matching remains necessary. Even a vanishing coefficient would leave finite matching, an interacting remainder along a specified coupling trajectory, and the reflected-error threshold **c_box/2** unproved. Full limiting field content, reflection positivity, infrared control, and finite positive mass remain separate gaps.

The [official target audit](../../foundations/01-target-and-scope.md) is reused: its same-day check records the unchanged Jaffe–Witten statement. The earlier [normalization](../../foundations/04-perturbative-curvature-renormalization.md) and [lattice-matching](../../foundations/05-lattice-stress-tensor-matching.md) audits are retained; the new readings below address the combined-response target rather than repeat those audits.

## Search record

Queries run on the checked date included:

- `Yang Mills gradient flow translation Ward identities lattice Z delta one loop renormalization 1306.1173`
- `Luscher Weisz perturbative analysis gradient flow non abelian gauge theories boundary counterterms 1101.0963`
- `lattice energy momentum tensor one loop finite renormalization Wilson action SU N Caracciolo Menotti Pelissetto 1990`
- `"gradient flow" "translation" "one-loop" "Z" renormalization`
- `"lattice" "gradient flow" "translation" "Haar" divergence`
- `"gradient flow" "fixed boundary" "Ward"`
- `"Schrödinger functional" "renormalizable" "boundary" Yang Mills Luscher Narayanan Weisz Wolff`
- `"One-loop analytic computation" site:cds.cern.ch` and the corresponding INSPIRE/title/PDF searches.

The broad searches located the flow and matching papers; the exact generator/boundary searches supplied no full matching statement. That search outcome is not a novelty claim. Publisher references led to the 2020 independent one-loop calculation, which removes the need to infer general color dependence from an SU(3) example.

## Inspected primary statements

### Flowed translation identities and the generator

L. Del Debbio, A. Patella, A. Rago, *Space-time symmetries and the Yang–Mills gradient flow*, [arXiv:1306.1173v1](https://arxiv.org/pdf/1306.1173v1), JHEP 11 (2013) 212. Read section 3.1, printed pp. 7–8, and section 6, pp. 13–17, especially (6.1)–(6.17).

Equations (6.11)–(6.13) identify the translation response with a flow-time-zero multiplier insertion and give a finite generator factor Z_delta. The subsequent stress-tensor/residual limit (6.14)–(6.16) additionally assumes continuum translation restoration. Thus the generator statement has stronger independent content than the previous assessment recorded. Equation (6.17) determines ratios of stress factors to Z_delta.

The paragraph following (6.2) treats its lattice transformation as measure preserving. L010's specified generator instead has its recorded nonzero Haar divergence. This prevents copying that finite-lattice Ward formula verbatim; it does not establish an error in the source or a failure of finite renormalization for L010. Its general normalization mechanism is supporting input, not the requested coefficient.

### Perturbative renormalizability of the flow

M. Lüscher, P. Weisz, *Perturbative analysis of the gradient flow in non-abelian gauge theories*, [arXiv:1101.0963v2](https://arxiv.org/pdf/1101.0963v2), 10 February 2011, JHEP 02 (2011) 051. Read sections 7.1–7.4, printed pp. 20–23, equations (7.1)–(7.8), and section 8.2, pp. 24–25.

After ordinary four-dimensional renormalization, their perturbative argument excludes further flow counterterms to all loop orders. Section 8.2 includes gauge-invariant composites at positive flow time. Section 7's boundary is **t = 0 in the additional flow direction**, not a physical face of D. The theory considered is on R^4. Import this result within its perturbative scope; it does not alone cover an unflowed lattice residual or the physical boundaries here.

### Bare versus renormalized flowed observables

M. Lüscher, *Properties and uses of the Wilson flow in lattice QCD*, [arXiv:1006.4518v3](https://arxiv.org/pdf/1006.4518v3), 27 January 2014, JHEP 08 (2010) 071 with its erratum. Read sections 2.5–2.6, printed pp. 6–8, equations (2.26)–(2.33).

The bare-coupling expansion of the flowed energy density has ultraviolet poles in (2.28)–(2.29). Replacing the coupling by (2.30) produces the finite expression (2.32), with its scale logarithm in (2.33). This is a primary worked example showing why flow finiteness must be stated with its coupling convention. It is an energy-density one-point calculation in dimensional regularization, not L010's connected two-insertion response.

### Continuum stress tensor and small flow time

H. Suzuki, *Energy–momentum tensor from the Yang–Mills gradient flow*, [arXiv:1304.0533v6](https://arxiv.org/html/1304.0533v6), PTEP 2013, 083B03 with correction. Rechecked section 2, (2.1)–(2.11), and section 3, (3.5)–(3.11).

The conserved continuum tensor, including its bare 1/g_0^2 normalization, is finite in separated gauge-invariant correlations. The flowed tensor has a small-flow-time expansion into renormalized operators with higher-dimensional O(t) terms. The former supports the protected bulk stress channel already used in L004. The latter cannot be substituted as an exact identity at the fixed tau of this target.

### Lattice stress matching, including general color number

L. Giusti, M. Pepe, *Energy-momentum tensor on the lattice: non-perturbative renormalization in Yang–Mills theory*, [arXiv:1503.07042v2, section III](https://arxiv.org/html/1503.07042v2#S3), Phys. Rev. D 91, 114504 (2015). Rechecked (21)–(28) and the finite-size qualification after (31). Their SU(3) Wilson/clover tensor has finite triplet and sextet factors; (28) supplies one-loop values. The geometry uses shifted temporal and periodic spatial boundaries. These values remain supporting examples, not this notebook's matching constants.

M. Dalla Brida, L. Giusti, M. Pepe, *Non-perturbative definition of the QCD energy-momentum tensor on the lattice*, JHEP 04 (2020) 043, **published version of 7 April 2020**, [article](https://doi.org/10.1007/JHEP04%282020%29043), [full published PDF](https://inspirehep.net/files/8597677d931595baa34d5f59b02a2fb6). Read section 3, (3.1)–(3.12), printed pp. 10–11; section 5.2, (5.4)–(5.21), pp. 17–20; Table 1 and the surrounding extrapolation discussion, pp. 20–21.

This is an independent one-loop calculation for Wilson gluons and a clover tensor with general N_c. Equations (5.7)–(5.8) separate N_c, 1/N_c and N_f contributions; Table 1 reports both channels and compares previous values. Equation (3.12) states finite stress factors. The calculation uses shifted/twisted thermal boundary conditions and numerical evaluation/extrapolation of perturbative lattice sums. It does not provide a rigorous fixed-box error estimate.

**Consequence for reuse:** SU(2) alone is no longer a reason to redo clover matching. The source gives the needed color dependence. L010's triplet is a vertex average of plaquette traces, however, and its generator and flowed covariance are different quantities. Neither clover-channel constants nor extrapolation errors are transferred to them.

### Physical boundary scope

M. Lüscher, R. Narayanan, P. Weisz, U. Wolff, *The Schrödinger functional — a renormalizable probe for non-abelian gauge theories*, [arXiv:hep-lat/9207009v1](https://arxiv.org/pdf/hep-lat/9207009v1), 9 July 1992, Nucl. Phys. B 384 (1992) 168–228. Read section 2.5, printed pp. 10–11.

The paper states one-loop finiteness of the field-dependent effective action after coupling renormalization and gives a symmetry argument against extra gauge boundary counterterms. It explicitly leaves an all-orders rigorous proof outside its scope. This is a Schrödinger-functional slab with periodic spatial directions. It contains neither the flowed mixed response nor a result for the all-face box and its corners. It supports examining boundary renormalization; it does not discharge that examination here.

## Unread leads and access limits

Caracciolo–Menotti–Pelissetto, *One-loop analytic computation of the energy-momentum tensor for lattice gauge theories*, Nucl. Phys. B 375 (1992), 195–239, [publisher record](https://www.sciencedirect.com/science/article/pii/055032139290339D), [institutional record](https://iris.uniroma1.it/handle/11573/75382): **abstract/metadata only**. The institutional record has no attached file; publisher/DOI and INSPIRE searches did not yield readable full text. The abstract advertises a broad discretization class, whose exact hypotheses were not inspected. No equation or full-coverage claim is attributed to that paper here.

It is not an essential unread premise of the screened calculation: the imported statements above are explicit in the inspected texts, and the 2020 work supplies an independent general-color clover comparison. Any later use of the older paper's additional general-discretization formulas requires reading them first. No novelty is inferred from this access limit. Other search results and bibliographic references not listed as inspected are not mathematical inputs.

## Exact comparison and permitted specialization

The following differences delimit the mathematical work still needed; none is resolved by this review.

| Feature of the saved target | Comparison obligation |
| --- | --- |
| Bare g, with 1/g^2 inside both nonlinear probe definitions | Track parameter conversion and probe normalization before interpreting ultraviolet finiteness. Centering is retained. |
| Endpoint-averaged, transported clover generator | Match its flow-time-zero insertion and retain L010's Haar term; do not assume the source's exact finite-a identity. |
| Plaquette-trace triplet and clover-product shear | Establish the needed operator matching for the actual representatives. Their common free limit does not bound their interacting difference. |
| Fixed links on every box face | Control physical boundary contributions and possible corner effects; compact support of the weights does not make a flowed observable local in the initial field. |
| Fixed positive tau and finite box | Keep these limits fixed; neither a small-flow-time expansion nor a thermodynamic extrapolation is a replacement. |
| Remaining connected response | Include action, Haar-density/gauge-quotient measure, insertion, and nonlinear flow/probe corrections. L010's isolated Ward divergence is already separated and must not be counted twice. |

Known flow renormalizability, bulk stress protection, and the cited matching framework should be imported. A fresh proof of those general statements would be redundant. Specialization is justified only for the actual representatives, normalization, and boundary differences above. In particular, this assessment assigns **no value, including zero**, to the requested logarithmic coefficient and proves no new cancellation.

## Redundancy and continuation test

The overview, DAG, L008–L010, histories 010–011, and all four recorded attempts were checked. L010 already bounds the isolated Haar contribution; repeating it would not address the saved target. The beta = 0 reflection collapse, missing MRS positivity, single-factor oriented-plaquette failure, and compact triplet-only obstruction remain relevant. Neither dropping the shear channel nor treating ordinary flowed covariance as a reflected norm is licensed.

The next research step may use this SPECIALIZE assessment for the exact target above. Its discriminating deliverable is the order-g^2 coefficient at fixed mesh followed by a justified identification of its leading log(sqrt(tau)/a) behavior for **both** probes, including the listed corrections. Any claimed bounded remainder must be justified separately; a formal cancellation of selected diagrams is insufficient.

Continue toward finite matching if all unsuppressed logarithms are accounted for and the remaining task is explicitly bounded. If an additional insertion or boundary contribution survives outside the proposed two-channel matching, record that obstruction and reassess the normalization scheme. A nonzero bare logarithm alone is not a disproof of the route: its coupling and operator interpretation must be checked. Failure to resolve an applicability obligation is an unresolved gap, not evidence for a zero coefficient. In every case compare the eventual interacting result with c_box/2, rather than equating a one-loop diagnostic with that required estimate.

This completes one literature step, counted as the first exploration turn since L010. The contribution is a source comparison and a narrower specialization mandate, not a new coefficient, reproduction, or result beyond the inspected literature. The original REVIEW_REQUIRED migration note was resolved by these readings; the interim source-access question is delimited above. Mathematical work is deferred to a later invocation.

## Mathlib

Coverage of the full combined-response statement: **not checked**. Coverage of the supporting perturbative renormalization, Wilson flow, and lattice Ward framework: **not checked**. The named primary statements and direct links above are literature inputs; no Mathlib theorem is asserted to match them.
