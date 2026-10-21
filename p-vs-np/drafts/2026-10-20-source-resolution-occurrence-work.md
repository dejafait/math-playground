# Step 378 — preserved source-resolution occurrence work checkpoint

Completion: the full informal construction is now canonical in
[L097](../lemmas/L097-source-resolution-occurrence-product-affine-abp-witness.md).
The notes below preserve the reasoning saved before completing it.
No independent audit or implementation was performed in this step.

Approved target: construct the exact L087 occurrence-product witness from
supplied source resolution, in Q=2+M+|F|+|π|. Reuse the unchanged step-377
SPECIALIZE assessment. Main gap: unrestricted SAT decision/separation.
Downstream use: a proof-dependent supplier without a small-core or order
promise. Neither short resolution availability nor W₂ follows.

Preserve Attempts 018/030/031. Targeted comparison of L087, L035/L036,
L049 and the recent occurrence work found no duplicate full transfer.
The source's Boolean-only product passage is not used.

Working construction, not yet a theorem at this checkpoint:

- The split-CNF truth polynomial is exactly f, by separate-order
  multilinear injectivity.
- In an occurrence group z₁,…,zₖ put a=∏(1+zᵢ), b=∏zᵢ. Its exact
  tester polynomial is e=a+b. The ordinary formula “all zero or all one”
  instead has truth polynomial t=a+b+ab. Do not equate e and t formally.
- With A=∏_{i>1}(1+zᵢ), B=∏_{i>1}zᵢ, a correction for ab is
  (1+z₁)W(A,z₁)B+σ₁AB. Telescope group corrections to obtain J(B)=g+g̃.
- From source resolution derive ¬(split-CNF ∧ group-consistency) in
  occurrence-only Frege by replacing each source variable with a chosen
  occurrence. Uniformly complement propositional variables before LTW
  translation, since its tr(x)=x uses the opposite truth convention.
- The desired output is K+fJ, where K(B)=f g̃. LTW's exact MP extraction
  remains applicable; its faulty Booleanity subcase needs L035/L036
  replacement with all independent blocks paid.

Continue only if both formal identities and a fixed Q-polynomial for
every proof/graph/dictionary/time stage can be written. A surviving source
symbol, uncorrected g̃, or uncharged proof unfolding fails the interface.
No mathematical script or finite verification has been run.
