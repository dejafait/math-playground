# Unused S_0 versus Q and D_6 — step 231

Ready assessment: `drafts/literature/2026-10-14-cyclic-family-alternating-kernel.md`.
Main gap: exclusion of sixteen compatible errors. This bounded attempt
tests whether S_0 supplies an independent restriction on L092/L093's
reconstructed seeds. Continue on an independent restriction; abandon
this gate if its remainder follows identically from Q and D_6. The
subgroup seed restriction, full kernel, actual-error application,
arbitrary families and challenge qualifications remain unresolved.

Inputs read: L089–L093, the saved D_6 diagnostic and attempt, and
ATTEMPTS/020,029,031,032. L089 is audited; L090–L093 are not.
The ready coverage is reused; no new external input or literature turn.
No H-label sweep or rank sampling is proposed.

Saved before calculation: use exactly L093's c,d,e,g,j,k,X,Y,M,N,O,Z,W
and Q. L091 at t=0 gives, after b=infinity,p=0,f=1 normalization,

    Y(d-X)/(X(d-Y))
      +(d-c)(z-j)(X-g)/((d-g)(d-j)(z-c))=1.

The first factor involving h(0)=infinity cancels projectively; all
remaining differences divided by are nonzero at any bijective extension.
Substituting z=Z/W and clearing the nonzero denominators gives

    P=d(Y-X)(d-g)(d-j)(Z-cW)
       +(d-c)(Z-jW)(X-g)X(d-Y).

Here degree P<=5. Reduce it to sigma_0+sigma_1 X modulo Q and
compare with rho_0+rho_1 X. In the rho_1!=0 branch a necessary
compatibility equation is rho_1 sigma_0-rho_0 sigma_1=0.
The both-zero rho branch must instead retain the full sigma equation
with Q. No independence, seed feasibility or exclusion has yet been
established. All L092/L093 poles, transformed H-membership and collisions
remain gates.

Completed: [L094](../lemmas/L094-cyclic-joint-seed-gates.md) is the
canonical proof. The new linear residual supplies Psi=Xi=0, with all
rho/sigma-zero branches retained. A symbolic slice c=2,d=3,e=4 gives
an exact distinct-label witness over F_(97^13) satisfying the nine
used D-gates, S_8, Q and E, but failing S_0. The complete independent
direct-gate replay checks every label and 130 nonzero gates. This
proves independence only on the enlarged algebraic seed domain, not
on transformed H seeds or F_(97^20); no rank test or H sweep occurs.

The preliminary rational specialization g=20 had X=g and was rejected
as an independence witness on the distinct-label domain. It was not
used as a valid labeling. Algebraic factor extraction on the single
symbolic slice supplied the displayed pole-free distinct-label witness.
Both full certificates are under `scripts/cyclic-shared-gates/s0-residual-*.json`.
The producer and direct verifier pass, actual deg P=5 against at most
five and residual degree one against at most one. This is local progress
on the assessed target, not certified originality or subgroup exclusion.

Route decision: the unused gate is not redundant in the enlarged
domain, but another unconstrained nonidentity would not address the
remaining finite seed gap. The next bounded mathematical test should
seek a uniform factorization of Delta and Psi forcing a collision or
pole on actual transformed H seeds, retaining all-zero residuals.
If only further generic nonidentities emerge, stop that elimination
mechanism and reassess. L090–L094 remain unaudited; uniform rank,
actual-error applicability and the global interval remain unchanged.
Zero mathematical EXPLORATION turns used or carried forward.
