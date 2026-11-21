# Two real parts: orbital response assessment1216, review1217

TARGET: Test whether an absolute C bounds |E_k(x)|<=C*x*(b_1^2+b_2^2) for every n>=4, 0<=k<n and D=diag(a_1+i*b_1,a_1-i*b_1,a_2+i*b_2,a_2-i*b_2,r,...,r), where a_1,a_2,r,x>0, b_1,b_2 are real, x*(|b_1|+|b_2|)<=1/4, and E_k is the adjacent-rank physical logarithmic-response defect from the separately normalized zero-phase reference; obtain a uniform bound or a rigorous family with unbounded |E_k|/[x*(b_1^2+b_2^2)].
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1217 searched HCIZ/orbital imaginary perturbation, arbitrary real-field covariance/Hessian, logarithmic derivative, conjugate-pair and matrix-Bingham terminology; exact queries and scoped duplicate/failure checks are in drafts/working/2026-11-17-two-real-part-orbital-source-review-1217.md. Reuse unchanged coverage1213. No matching bound or source counterexample was located; this is not a novelty claim.
SOURCE_EVIDENCE: Read Leake--McSwiggen--Vishnoi, STOC2021, author proceedings PDF https://cs.yale.edu/homes/vishnoi/HCIZ.pdf Problem1.2/Thms1.3-1.4 p2, Prop2.2 and repeated-spectrum qualification p3, Thm2.3 and full proof p4; rechecked Novak2203.10746v1 (1.2),domain,Thm1.2 pp2,5-6 https://arxiv.org/pdf/2203.10746v1 . Reuse1213's Collins--Sniady Cor2.4/(9)-(12)/Prop2.5 pp4-6, Olshanski2013 Cor3.2 pp1015-17 and McSwiggen1712.03995v4 (2),Thm1,after(24) pp2-4,10; precise read qualifications are in working1217.
COMPARISON: C030o covers a_1=a_2 with a whole-block real invariance; C030n does not authorize complex-law addition. The inspected sampling/pushforward results allow arbitrary Hermitian real fields and repeated spectra but supply no uniform joint imaginary-response bound. Novak's bounded-coupling/eigenvalue polydisc does not cover unrestricted real contrast from the phase hypothesis alone. Exact orbital identities and Haar moments remain usable inputs, not TARGET.
GAP: The absolute two-pair physical-response bound, or a rigorous divergent normalized-defect family, remains unproved. Required reality/nonvanishing on the closed window and joint derivative control must be justified; no complex order, block independence, common normalizer or Xi realization may be assumed. No essential source is blocked for a direct bounded test.
REASON: The changed-real-part source comparison is sufficient for one bounded mathematical attempt on this smallest heterogeneous family. A uniform result could pay a finite-reference perturbation input; a divergent-ratio family would stop this particular extension. No result is derived or approved as mathematics in this literature turn.
SCOPE: Exactly the saved two-pair common-background TARGET, including n=4, endpoint ranks, zero phases, either contrast sign, coincident real parts and separate normalizers; one absolute-bound or divergent-family attempt is covered. No arbitrary backgrounds, all-pair unequal-real-part theorem, unread theorem application or actual-Xi transfer is approved; full matching Mathlib coverage unchecked.
LITERATURE_REASON: a_1!=a_2 changes the essential whole-block invariance hypothesis; coverage1213 is reused for unchanged Haar/real-array inputs rather than re-reviewed without cause.

## Exact observable and bounded test

For probability Haar V in U(n), P_j any rank-j orthogonal projection,
and the D specified in TARGET, define

    Z_(j,b)(x)=integral exp(-x*tr(D*V*P_j*V*))dV,
    G_(j,b)(x)=-Z'_(j,b)(x)/Z_(j,b)(x),
    E_k(x)=(G_(k+1,b)-G_(k,b))-(G_(k+1,0)-G_(k,0)).

The zero-phase matrix retains two entries a_1, two entries a_2 and
all remaining entries r. The derivative fixes a_1,a_2,r,b_1,b_2.
Each rank and each reference has its own partition function. Any
proposed response bound must first justify the required nonvanishing
and reality throughout the closed phase window. No such result for
the changed family is proved in this review. At n=4, r is absent.
The divergent-ratio alternative concerns b_1^2+b_2^2>0; the zero-phase
case must be handled separately rather than dividing by zero.

The prior audit inputs are C030l and C030o, with C030n a comparison
only. Review1217 searched the exact finite-family statement, stronger
complex-orbital perturbation results and known obstructions, reusing
coverage1213 where its hypotheses continue to apply. The primary
statements, essential real repeated-spectrum case, applicability and
unread-lead qualifications are recorded in
[working1217](../working/2026-11-17-two-real-part-orbital-source-review-1217.md).
No disjoint-corner independence, common normalizer or complex stochastic
order is available. No calculation or proof of TARGET has occurred.

Continue after adequate coverage to one bounded uniform-bound or
divergent-family test; a bound whose constant grows with n or the
real contrasts is inconclusive for TARGET. Source overlap may instead
make a precise import sufficient. Stops1117/1181/1193/1200/1107 and
overlap884 retain their scopes. Actual-Xi phase and degree/time budgets,
finite-reference and signed-complement hypotheses, all-degree positivity,
theta signing and realization remain unresolved regardless of this test.
Full matching Mathlib coverage is unchecked; no cross-notebook input.

Review1217 completes this changed-hypothesis comparison. No inspected
theorem supplies the response estimate, and no essential source blocks
a direct bounded test. EXPLORE covers one later attempt, not a result
or certified originality. Next routing is proof_attempt/creative,
deep_research/max: test the exact absolute-C or divergent-ratio
alternative at the joint-phase obstruction left by unequal real parts.
Its downstream use is one heterogeneous finite-reference perturbation
payment toward actual-Xi all-degree positivity. The supervisor owns
separate approval of this updated assessment before the attempt.
