# Finite distant-left allowance: reproduction nomination1648

TARGET: Reproduce Kawano v1's distant-left allowance T_farleft(p)<=10^(-4) L^(9/2)/r for the S(p)-normalized absolute full-theta integral on 1<=Re(u)<=Re(u_0)-1 in C048c's full closed sector.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse review1648's exact-side local duplicate/failure search, L803/history533 mismatch and primary-target queries in 2026-11-19-mellin-distant-left-source-notes-1648.md; no matching canonical inequality or novelty inference.
SOURCE_EVIDENCE: Kawano Preprints.org202611.0383v1, posted4November2026, DOI10.20944/preprints202611.0383.v1, https://www.preprints.org/manuscript/202611.0383/v1 , Section5.2(28)/Lemma5.1(i)/complete horizontal phase proof(31), AppendixB finite-band definitions/C_f/B_f/both full-mode inequalities and proof explanation, AppendixC full-sector geometry/distant-tail allocation and 10^(-4) threshold, read19November2026; reuse inspected Devroye(1986) VII.2.6 pp299-300 tangent method and DLMF5.9.1 positive Gaussian-moment hypotheses from the ready local assessments.
COMPARISON: The source gives a full-sector distant-tail allowance and an all-t>0 weighted-theta envelope, supporting this finite integral-of-moduli specialization; its finite-band cell constants and C048h's t>2/3/2 envelope cannot be extended here. L803 has different saddle, height, endpoints, normalization and modulus placement.
GAP: Verify the complete normalized absolute integrand, x>=1 phase and small-parameter full-mode envelope, then the explicit uniform 10^(-4) coefficient on all closed boundaries and unbounded L; no source quantitative claim is a premise.
REASON: Citation alone does not establish this operational absolute specialization or certify a quantitative preprint estimate; a separate known-method reproduction with exact constant checks is justified by accessible complete source cases.
SCOPE: Newly written ready continuation for separate approval next turn; REPRODUCTION only. No origin continuation, global contour equality, zero count, inversion or actual-Xi sign implication is covered.

Use precisely assessment1647's observable, without changing F or moving
the contour. For C048c's r,L,w,u_0,h_p,K,A_0,S(p), put x_0=Re u_0
and use C048h's normally convergent full theta factor F. The target is

    T_farleft(p)=integral_{1-x_0}^{-1}
       |K(s)F(u_0+s)exp(h_p(u_0+s)-h_p(u_0))| ds
                                          /|sqrt(pi/A_0)|
       <=10^(-4)L^(9/2)/r.

Follow source-notes1648's full applicability and boundary checklist.
Prospective direct inputs are C048c's geometry and exact normalization
and L799's general strip convergence/factorization. C048h's phase proof
may be reused only with explicit verification of its x>=1 scope;
its near-left amplitude conclusion is not a far-left input. L803 and
L802 are method comparisons, not direct inequality premises. All direct
mathematical uses must be represented in the local DAG if a result is
eventually written. Do not assume the source's C_f, B_f or AppendixC
constant as an established local inequality.

Check every mode and the lower-power mode1 term for all real t>0,
the 2/u and saddle-ratio amplitude, principal square root and S(p),
left phase in both Re p cases, real p and conjugation, L=12, closed
angular endpoints and unbounded L. A rigorous certificate, if needed,
must verify a proved scalar reduction, not sample the sector. Standard
Gaussian moments are cited using DLMF5.9.1 with positive real parameter;
do not reprove that known formula. The integral need not reach zero.

Continue only if this explicit bound is proved uniformly or a rigorous
obstruction to the selected sufficient majorant changes the decision.
Failure of a majorant does not disprove the target or RH. Preserve the
global-import stop and unfinished work; no origin/global assembly is a
premise. A possible downstream use is a separate full Mellin remainder.
The main gap is L030-L032/C032a actual-Xi all-degree positivity; zero
counts, inversion and a sufficient sign bridge remain independent.
This is an established-method specialization, not creative research.
