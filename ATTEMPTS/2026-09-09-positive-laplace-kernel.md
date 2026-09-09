# Attempt: positive Laplace kernel forces zero-freeness

Date: 2026-09-09

Outcome: failed; the valid η representation and an exact obstruction are retained as Lemmas 12–15 in PROOF.md.

The alternating series proves η(s)/s=∫_0^∞w(e^u)e^{-su}du for Re(s)>0, where w is a bounded indicator. Pairing terms proves η(σ)>0 for real σ>0. The attempted step was to conclude zero-freeness for nonreal s from the kernel's nonnegativity.

A counterexample with the same nonnegative bounded indicator property is v=1_[0,1]∪[2,4]. Its transform is H(s)=(1-e^{-s})(1+e^{-2s}+e^{-3s})/s, with a removable value at 0. The polynomial 1+z²+z³ has one real root r∈(-2,-1) and two conjugate nonreal roots with |z|²=-1/r∈(1/2,1). Thus s=-Log z is a zero of H with 0<Re(s)<(log 2)/2<1, although H is positive on the entire real axis.

**WHY IT FAILS.** A positive kernel controls the integral for real arguments but does not prevent cancellation of complex phases e^{-itu}. The explicit indicator counterexample has a holomorphic transform and genuine nonreal zeros inside the critical strip. It does not have the specific arithmetic interval pattern of η, so it is not a counterexample to a stronger theorem exploiting that pattern; no such stronger theorem was proved. Positivity alone cannot supply the missing zero-free assertion.

Next lemma: obtain the theta/Mellin representation of ξ with explicit convergence estimates and study which additional structure it supplies.
