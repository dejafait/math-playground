# Global normal-summand Chern test — working checkpoint

2026-10-17. Approved target: Test whether L114's smooth ASD extension
preserves L108's normal splitting and forces |Z|<=800 via L111's Chern budget.
Use the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-17-equality-normal-summand-global-chern-bound.md`.

The precise universal gap is primitive rational Hodge realization. This
step only tests a conditional necessary bound on the equality-kernel recipe;
it neither supplies F nor a lower bound on the split set. A later independent
constraint on that set could use the bound. Stop this application if the
actual projector/connection comparison or restricted HE hypothesis fails.

Inspected L108's actual algebraic projector, metric complement, extension
and separate audit; L111's hypotheses, canonical M=E and corrected Chern
budget; and L114's specific smooth extension, tangent connection comparison
and separate audit. The targeted duplicate search found no completed bound
in L108--L114 or history/325--329. ATTEMPTS/063/066/067 are preserved:
none covers the new smooth-connection input with the actual KS data.

Provisional reasoning for canonical write-up: L108 gives P=ir, kernel N,
image i(T_B), parallel and orthogonal for the actual connection on U.
L114 extends that same connection and positive metric on M=E, so the smooth
tensors nabla_End(P) and G(Pv,w)-G(v,Pw) vanish by density on all B.
Thus the actual N is invariant. Its induced connection has the inherited
(0,1) operator, is unitary and hence is its Chern connection. Its curvature
is the restriction of the full ASD curvature, without a second-fundamental
correction because P is parallel. ASD gives Lambda_omega F_N=0 at the
unchanged real metric. Perego Theorem 4.21 gives polystability; Corollary
6.42 in dimension two, rank 48 and c_1=0 gives
-96(800-|Z|)<=0. Thus the requested upper threshold should follow.

Completed: the full specialization and exact citations are canonical in
`lemmas/L115-equality-global-normal-connection-and-chern-bound.md`; the
ID-only DAG, argument overview and checkpoint are updated. The separate
critical-audit proposal has REVIEW_REQUIRED coverage. The application gives
the conditional upper bound, without an equality-case strengthening or a
mathematical script. This file preserves the preliminary reasoning above;
PROGRESS.md alone records the current next action.
