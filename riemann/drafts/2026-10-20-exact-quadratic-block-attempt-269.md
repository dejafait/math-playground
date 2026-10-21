# Exact three-test covariance repair — step 269 working record

Prior gate: `drafts/literature/2026-10-20-exact-quadratic-block-covariance-repair.md`
(SPECIALIZE, unchanged at invocation). One RESEARCH / REPRODUCTION
proof attempt on that exact target. Main gap: global mixed positivity.
Intermediate use: distinguish a repairable finite occupation block from
an obstruction to the selected-law relaxation, without claiming a trajectory.

Inputs read: L441's full construction and audit; L442's complete transport
polynomials, raw matrix and residuals; L419 exact forms and K. The scoped
histories retain the narrower stops. No duplicate exact repair was found
in the gate's recorded comparison. Remaining checks below are pending.

Take the baseline law of L441. Let s=sin(omega t), W=E_H w,
mu=E_H(ws)/W, h=s-mu. Then E_H(wh)=0 exactly and |h|<=2.
Use only the off-diagonal matrices V12,V13,V23, with an additional
covariance field h(a V12+b V13+c V23). Its 11 entry and integrated
w-weighted matrix are identically zero.

Put C=E_H(e s w h) and D=E_H(A_xy w h), where A_xy is the entire
xy coefficient in L442 (1), including both slow derivatives.
The exact residual map on (a,b,c) is triangular:

    [[2C,0,0],[D,C,0],[0,0,2C]].

Expected conditioning test: C=1/60+o(1) using only the small integrated
mass loss and fixed-frequency integration; D=O(1/log H). Baseline
residuals r=(o(1),o(1),omega/(360 sqrt(2))+o(1)). Exact solution:
a=-r1/(2C), b=-(r2+D a)/C, c=-r3/(2C).
This is not yet a supported-law conclusion. Verify all-real-H Borel
dependence, boundedness, negative trace/support and all preservation
requirements before recording a canonical result. Continue if C is
uniformly positive and all these checks close; abandon the implementation
only for a proved unavoidable incompatibility or unbounded requirement,
not a failure of one trial coefficient space.

All high/intermediate components, m,w,g_H,response and the original
cutoff remain fixed. No derivatives of kernels, probabilities, atoms,
cutoffs or height-dependent coefficients occur. Other occupation tests,
actual/global realization, clipping, capped nondegeneracy, L413's margin
and global mixed positivity remain unresolved.

Completed outcome: ADVANCE in the local selected-law analysis. The full
proof and qualifications are canonical in
`lemmas/L443-exact-three-test-bounded-covariance-repair.md`; this draft
retains the initial reasoning rather than a second proof. The conditioning,
Borel support and all preservation checks close in that proposed result.
No mathematical script or fresh external browsing was needed. A separate
critical audit remains pending, with new coverage marked REVIEW_REQUIRED;
this turn does not approve that changed continuation or claim originality.
