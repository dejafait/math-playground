# Regular-background weighted-flow attempt952 — saved reasoning

Approved target: assessment951's nonzero-H stopped-density uniform
integrability question. Main gap: L030–L032/C032a actual-Xi all-degree
algebraic-square positivity. This attempt can pay only one local
analytic-factor condition. C466q and the complete source comparison950
have been read; their exact scope and stops927/932/941/947/948 remain.

Promising calculation, pending complete write-up: put
F(q)=q^2 exp(-H(q)), h=H'(q), and rho=|q|. Before the first
singularity/escape, dot F=-|S'|^2 F and dot J=overline(S'' J).
Consequently the squared full density has differential upper bound
2(|S''|-|S'|^2)|FJ|^2. Pointwise,

    |S''|-|S'|^2
    <= M2 - 2/rho^2 + 4|h|/rho - |h|^2
    = M2 + |h|^2 - 2(1/rho-|h|)^2
    <= M2 + M1^2.

This would give |W_T(r)| <= exp((M2+M1^2)T)|W_0(r)|
on every surviving trajectory, with
|W_0(r)| <= r^2 exp(-Re H(0)+M1 a). Zero extension preserves
the bound, hence suggests a linear measurable-set modulus.

Still to check before claiming the target: maximal punctured-disk
flow and first-exit conventions agree; survivor sets are Borel and
the fixed-time derivative is the actual smooth ODE derivative; the
estimate is uniform over H sharing the prescribed data, with no
cutoff constant lost at collision. No variable-time derivative,
phase-sign inference, or integral-invariance assertion is involved.
Use a canonical lemma if these checks close; otherwise preserve this
estimate with the precise outstanding issue. No mathematical script
is needed for these symbolic inequalities.

Completed disposition: the lifetime and measurability checks closed.
The full proof and explicit class-uniform linear modulus are now
canonical in C466r. No extra hypotheses or cutoff-dependent constants
were needed. This record preserves the initial reasoning; it is not
a second proof. Independent audit is the nominated continuation.
