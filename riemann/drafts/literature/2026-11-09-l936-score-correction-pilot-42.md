# Fixed-witness test of a low-degree theta-score correction

TARGET: Test the fixed L936-witness degree-eleven score-correction feasibility at lambda=1/10240 with eight constants in [-16,16], certifying a nonnegative complete half-line residual or rigorous coefficient infeasibility.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse step42's first-panel score comparison and exact theta/score/polynomial/contact and density-operator/cumulant searches, together with step176's polynomial-dual comparison. No inspected theorem provides this finite feasibility result; no novelty inference follows.
SOURCE_EVIDENCE: Ley-Swan ECP18(2013), paper7, Definition2.1/Theorem2.2 pp2-3 https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/2578/2199.pdf ; Fantuzzi-Goluskin-Huang-Chernyshenko arXiv:1512.05599v2 Section4(4.2)-(4.10)/Proposition3 pp8-9 https://arxiv.org/pdf/1512.05599v2 . Reuse inspected hypotheses/proof cases from step176, as specified in 2026-11-09-actual-theta-score-contact-41.md. L874's audited polynomial/score domination and L936's accepted exact witness are local inputs.
COMPARISON: The density-operator identity and auxiliary-function template motivate a future sufficient certificate at genuine contacts; they neither guarantee a multiplier nor turn fake moments into actual expectations. This tests necessary feasibility of one proposed uniform-relaxation certificate on a fixed algebraic member, with exact actual score. The old degree-one high-time pilot stopped for empty actual domain, not coefficient infeasibility; this algebraic domain is nonempty and the degree cap excludes uR.
GAP: Decide this eight-coefficient pointwise feasibility with complete K/K' and the exact witness root retained. No multiplier, residual sign, coefficient obstruction, realization or genuine-contact theorem is established. Success leaves extension over actual contacts unpaid.
REASON: L936 rules out a purely finite-moment sign implication. This independently testable score-sensitive screening step can reject or provisionally retain a different sufficient certificate without assuming an actual contact or retrying blocked correlation sources.
SCOPE: Newly written ready nomination awaiting separate supervisor approval before research. One fixed parameter, unchanged L936 witness and this degree/box only. No new moments, altered root, sweep, quadrature refinement, coefficient enlargement, derivation or mathematical script in step42.

## Exact proposed test, not an established inequality

Essential input IDs: L019, L058, L874, L917, L936. No cross-notebook
input. Use L936's exact algebraic root alpha in its certified bracket,
fixed raw moments/common mass, y7 and normalized exact c. Do not replace
alpha by a midpoint or c by an approximate null vector. Reuse the
accepted step41 audit; no repeat witness audit is needed.

Fix lambda0=1/10240. Form the finite polynomial from the witness data:

    g_w(z)=sum_(j=0)^6 (-1)^j y_j z^(2j)/(2j)!,
    R_w(u)=-sum_(n=2)^6 n b_n [z^(2n)] cos(zu)/g_w(z),
    b_n=sum_(i+j=n-2) c_i c_j.

The inverse is formal at zero and has constant term one. This is
L874's finite prescription on algebraic data, not an assertion that
g_w is an actual characteristic function. Coefficients through z^12
are determined by the accepted data. Retain y7 as part of the witness;
it does not enter R_w.

Choose once eight real constants (a0,...,a5,alpha0,beta0) in [-16,16]^8,
independent of u. The proposed odd multiplier and residual are

    P(u)=c2^2 sum_(j=0)^5 a_j u^(2j+1),
    W(u)=u*(K'(u)/K(u))*R_w(u)
          +P'(u)+(2lambda0*u+K'(u)/K(u))*P(u)
          +alpha0*R_w(u)+beta0*u*R_w'(u).

Ask whether W(u)>=0 for every u>=0, using L019's full exact K.
P has degree at most eleven, whereas uR_w has degree thirteen;
that tautological correction is outside this class. No sign,
asymptotic estimate or residual coefficients are derived here.

## Purpose, evidence and stopping test

Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
Plausible use: a uniform analogue over the first-panel contact
relaxation might yield the genuine contact score sign after a
separately justified density-operator application. One accepted member
is a necessary screening test for that stronger certificate, not its
proof. Uniform extension remains an independent gap on success.

For feasibility, give explicit coefficients and a rigorous nonnegative
half-line residual: u=0, every compact interval used and the complete
infinite tail. Justify any claimed density identity's integrability
and endpoints. The general operator identity is the cited input.
K positivity permits multiplication of W by K for verification, but
a finite theta truncation or a mesh is not a sign certificate.

For infeasibility, finitely many necessary point inequalities with full
score enclosures suffice only with a rigorous certificate excluding
every coefficient tuple in the box. One failed tuple, sampled negative
value for that tuple, optimizer status or unresolved interval does not
establish infeasibility. Exact linear separation is optional; verify
every algebraic/interval coefficient and sign used. No particular
solver or transcendental SOS theorem is assumed.

The witness need not be actual moments at lambda0. Thus E_actual R_w=0
and E_actual[uR_w']=0 must NOT be assumed. A full W>=0 certificate
here alone yields no actual flux conclusion. Failure at these data
rejects only this proposed certificate uniform over a relaxation
containing them, not the actual-theta sign or RH.

End at proved feasibility, certified coefficient infeasibility, or the
first essential unresolved term after one coherent attempt. In the
last case save that term honestly and reassess; no degree/box/parameter/
witness-family enlargement. Initialization, tangency/equality, actual
realization, uniform extension, other panels/degrees and global
continuation remain open. No complete candidate. Full/supporting
Mathlib coverage is unchecked, not asserted absent.
