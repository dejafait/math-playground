# October 2026 external zero-free input

Checked: 2026-10-21. This is a citation register, not a locally reproduced proof. The [overlap assessment](../drafts/literature/2026-10-21-openai-quasi-rh-overlap.md) records the notebook comparison and verification limits.

## Exact statements to reuse

OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8*, dated September 30, 2026, Theorem 1.1 (`thm:main`), states nonvanishing for every Dirichlet L-function and every finite-order Hecke L-function over Q(sqrt(-3)), uniformly in conductor and height, in Re(s)>7/8. Zeta is included. A principal-character pole at s=1 is allowed; this is not an assertion of holomorphy there. The boundary Re(s)=7/8 is not excluded. Use the [pinned manuscript source](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex) and its [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf).

The alternate October 5 manuscript, *The Quasi-Riemann Hypothesis (alternate 11/12 proof)*, Theorem 1.1, gives Re(s)>11/12 for the same families. This is weaker, not an additional improvement beyond 7/8. Its Corollary 1.2 states an effective uniform prime-counting error O(x^(11/12) log x) for reduced residue classes and q<=x. That application is outside the family 003 Lean scope note and has not been imported into a local proof. See [source](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex).

Baiying Liu, *Improved zero-free half-planes for the quasi-Riemann hypothesis*, [arXiv:2610.12234v2](https://arxiv.org/html/2610.12234v2), revised October 12, Theorem 27.1 and Section 33, states the stronger boundary

    B_new=(18 xi_new+7)/(18 xi_new+9)=0.874957019420098946...,
    1188 xi_new^3-2160 xi_new^2+171 xi_new+190=0,
    0.38858<xi_new<0.38859.

Its beta_* is the supremum for nontrivial zeros of primitive finite-order Hecke functions over Q(sqrt(-3)); Corollary 14.1 transfers the bound to Dirichlet functions. Nonvanishing is for Re(s)>B_new. Corollary 33.2 gives the convenient exact rational boundary 34998281/40000000=0.874957025. Earlier v1 constants and the earlier algebraic bound 0.874957069799... are not the strongest statement in v2. The claimed optimality is within that paper's specified comparison system, not a barrier to stronger mathematics. The theorem statements and the iteration in Section 33 were inspected; its full analytic proof and claimed Lean formalization were not independently checked here.

For zeta, combining the cited 7/8 theorem with the classical functional equation puts nontrivial zeros in the closed strip 1/8<=Re(s)<=7/8; in this notebook's Xi(z)=xi(1/2+iz) convention this is |Im(z)|<=3/8. With Liu's cited result the corresponding widths are 1-B_new<=Re(s)<=B_new and |Im(z)|<=B_new-1/2. These are the standard reflection/change-of-variable interpretation of the external statements, not reality of Xi zeros. In particular a hypothetical off-line zero inside the remaining strip is not excluded.

OpenAI's separate *Uniform exclusion of Landau–Siegel zeros*, dated October 1, states that an absolute c>0 satisfies (1-beta) log q>=c for every real zero beta in (0,1) of every primitive nonprincipal real Dirichlet L-function of conductor q>=3. It does not exclude every real zero in (0,1). William D. Banks, [arXiv:2610.15483v1](https://arxiv.org/html/2610.15483v1), Theorem 1.1, gives c=0.003 for q>=10^10 and extends it to q>=3 using a cited finite-conductor computation. That computation and the determinant proof have not been reproduced here. This is character-family information; zeta's lack of real zeros in (0,1) was already recorded in L013.

## Formal proof scope and trust status

The pinned [family 003 scope note](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/003.md) lists the zeta, Dirichlet and Hecke 7/8 results and the uniform real-zero gap. Later applications are explicitly outside its scope. The public repository describes results at different stages of verification; do not infer certification from the release count.

Inspected the zeta and Dirichlet comparator statements, zeta comparator JSON, solution module and its immediate final assembly. The comparator files contain `sorry` because they specify challenge statements; they are not the solution proofs. The JSON maps the zeta comparison to `OAI.NumberTheory.DirichletL.Nonvanishing`, permits only `propext`, `Quot.sound`, `Classical.choice`, and has `enable_nanoda: false`. The [solution module](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean) exports `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re` and `OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re`, using `ProbeFinalAssemblyUnconditional`. Its Dirichlet theorem excludes the principal pole explicitly. Lean's totalized zeta value at the pole must not be confused with analytic holomorphy/nonvanishing there.

No local Lean build, complete import-closure audit, comparator run, or independent verification of the entire manuscript was performed in this update. Treat these as precisely cited external results with supplied formal artifacts, not a newly established local theorem or a locally verified RH proof. Any load-bearing application must retain the source/version and check its exact hypotheses. The source repository may change: pinned links above use commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.

## Reuse boundaries

- Reuse the fixed half-plane result instead of rediscovering a constant zero-free strip no stronger than these bounds. Full RH remains open.
- Nonvanishing does not extend the domain of absolute convergence of the Euler prime logarithm or reciprocal Dirichlet series in L001/L005/L010. Analytic continuation and an absolutely convergent positive prime representation are different assertions.
- No all-degree mixed positivity, critical-line nonvanishing, zero simplicity, common-zero density estimate, clipped joint-sign lower bound, or jet-law realization follows merely by citing the half-plane statement.
- A fixed zero-free half-plane is new information for L330/L331. Quantitative logarithmic-derivative and reciprocal bounds on their exact moving domains require a fresh theorem-level comparison. Do not infer their desired little-o bound from nonvanishing alone, or repeat their old-envelope test as though no new input existed.
- The result concerns actual undeformed L-functions. It is not a uniform theorem for the heat-deformed theta family, Gaussian-regulated transforms, arbitrary prime-phase assignments, or generic comparison kernels.
