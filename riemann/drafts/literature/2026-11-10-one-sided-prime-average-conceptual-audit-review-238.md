# One-sided prime average — conceptual audit coverage

TARGET: Audit L984's one-sided prime-degree average implication, including the cutoff transfer, ordinary-Li normalization, arbitrary-multiplicity poles and same-germ Pringsheim contradiction.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step239 reused review235/236 exact Li/Cesaro/partial-sum comparison and recorded L976/step235/L983 stops; inspected L984 for source scope and L980-L982 input contracts; reopened the four primary sources below. No repeated discovery search or novelty claim; target and arithmetic hypotheses unchanged.
SOURCE_EVIDENCE: L981/L982 audited tails and fixed-index limit; L980's Lagarias AIF57(2007) Lemma4.4/(4.6)-(4.8), pp1708-1709 and Thm5.1, pp1712-1713 https://www.numdam.org/item/10.5802/aif.2311.pdf#page=21 ; Voros arXiv1403.4558v2 (31)-(32), p10 https://arxiv.org/pdf/1403.4558v2#page=10 ; Flajolet-Sedgewick 8May2004 ThmIV.3(ii), full proof pp15-16 https://algo.inria.fr/flajolet/Publications/ch4567.pdf#page=23 ; DLMF1.10(i)-(ii) https://dlmf.nist.gov/1.10 . Primary contracts already inspected in review236 and its reused assessments.
COMPARISON: These are the same standard contracts approved for the completed specialization; the new task critically checks that L984 satisfies them. No source supplies the unpaid arithmetic bound, and no individual-coefficient criterion may be silently applied to averages.
GAP: L984's proof has not been independently audited; check its finite cutoff transfer, sign and every-epsilon quantifiers, ordinary cumulative germ, finite positive radius, multiple-zero residue and extension at the same positive-radius point. Hypothesis (H) remains wholly unpaid.
REASON: Step239 separately completed source approval for this unchanged TARGET/SCOPE using inspected primary contracts and reusable comparison. SPECIALIZE is ready for the next mathematical audit; it does not approve L984 correctness or pay hypothesis (H).
SCOPE: Exactly L984, actual Lambda, all full prime-power endpoints, n>=2, X_n=exp(10000*(n+1)^4), a_n=(n-1)^(-1)*sum_(k=2)^n P_k(X_n), and for every epsilon>0 a finite C_epsilon>=0 with a_n<=C_epsilon*exp(epsilon*n) for all n>=2; no lower bound, RH, simplicity or limit interchange.

The main gap remains actual-Xi positivity and independent payment of
the signed arithmetic bound. The audit is useful because a mistaken
normalization, sign, radius claim or continuation would invalidate
the new conditional interface. It is not a complete RH candidate.
Success requires the entire implication on this exact scope; a
failed essential step must be identified and preserved, not hidden
by replacing the premise or importing RH-equivalent positivity.

Essential local inputs are L018, L980, L981 and L982. Only L980's
exact split and unconditional smooth trend are needed, not its
weak-height residual argument. Independently check (5) of L984
from the audited L981 tail and L982 fixed-index limit; the whole
unaudited step235 inverse is not an input. L968 is normalization
comparison and L976 is a distinct-germ contrast, neither a direct
mathematical premise. No cross-notebook input is used.

Load-bearing audit cases: all n>=2 including the initial degree;
finite prefixes in the smooth-term bound; H(0)=1 and the subtraction
of lambda_1*z; existence of a minimal mapped zero in a compact disk;
residue m*w/(1-w)!=0 for arbitrary m>=1; positivity/nonvanishing of
H on [0,1); the correction radius sqrt(R)>R; and equality of the
continued quotient with the original Taylor germ near positive R.
Reproduce the local reasoning, not Pringsheim's general proof.
No mathematical script or fresh external source is currently needed.

The step235 automatic two-sided payment stop and L983 lobe stop
remain preserved. After a successful audit do not extend a chain
of criteria without an independently testable payment mechanism.
No such creative central mechanism has yet been justified in this
focused step; the essential conceptual audit takes precedence.
Full matching Mathlib coverage remains unchecked and unknown.

## Separate source approval — step239, 10 November 2026

This literature-only step approves coverage for the exact saved TARGET,
not the conditional implication itself. Reading L984 here identified
its imported contracts and proposed audit obligations; no inequality,
pole calculation or logical implication was independently certified.
The main gap remains actual-Xi positivity and independent payment of
(H). The intermediate target is a critical audit of the conditional
interface, whose downstream use is to determine whether that interface
can safely guide a later arithmetic payment attempt. Continue only if
the audit checks every essential premise on the stated scope; preserve
a specific failure otherwise.

Reopened Lagarias's published PDF at the direct URL above: Definition
4.3/(4.5), Lemma4.4/(4.6)-(4.8), printed pp1708-1709; Theorem5.1/
(5.1)-(5.4), pp1712-1713, including its unconditional qualifier and
parameter-dependent onset. Reuse L980's previously inspected trivial
GL(1) applicability, N=Q=1, kappa=K=0, self-duality and normalization.
The source split includes delta=1 and the minus sign before S_f.
The audit needs only this split and the fixed-function smooth trend;
it must include finite prefixes and need not import L980's residual
argument, Section6 or the inconsistent alternating remark (4.13).
The exact fixed-index limit and quantitative cutoff remain the local
L982 and L981 interfaces, with their existing separate audits; L982's
whole step235 inverse is unnecessary.

Reopened Voros v2, (31)-(32), printed p10. These distinguish ordinary
Li coefficients from Keiper's divided coefficients and provide the
normalized logarithmic germ based at s=1. Reuse the prior comparison:
this is not an average criterion. No saddle estimate, global logarithm,
zero simplicity, or radius claim for the cumulative observable is
imported. That observable's normalization and singularities remain
mathematical audit obligations.

Reopened Flajolet-Sedgewick's 8May2004 draft, TheoremIV.3 and the full
proof, printed pp15-16 (PDF23-24). Part(i) uses Cauchy estimates;
part(ii) recenters near the positive boundary and rearranges a
nonnegative double series. The imported named theorem requires an
analytic germ, finite positive Taylor radius and nonnegative Taylor
coefficients. It does not provide those hypotheses for L984's corrected
germ. No exponent transcription in the draft proof is used as an
independent estimate; the named theorem is the input.

Reopened DLMF1.10(i)-(ii): Taylor expansion on a holomorphic disk,
zero order through its first nonzero Taylor coefficient, and uniqueness
of continuation on overlap. These support the local analytic audit;
they neither establish the needed mapped-zero residue nor identify
its continued quotient with the original germ. Those checks remain
for the next research turn, including arbitrary positive multiplicity.

The reused duplicate/failure comparison remains adequate: individual
Li bounds do not directly address means; the L976 translated germ
has different geometry; consecutive-mean subtraction supplies no
one-sided estimate; the step235 automatic payment and L983 lobe stops
are preserved. The unread leads in review235 remain unread and are
not essential to this bounded standard-method audit. No source blocker
remains and no new arithmetic premise has been added. Full matching
Mathlib coverage is unchecked/unknown.

Outcome: STALLED, source-approval process completion with no new
mathematical evidence or new theorem-level comparison. No lemma,
mathematical script, PROOF or DAG edit. The exact Next action remains
ready under this assessment; another approval-only turn is unnecessary.
No justified independently payable creative mechanism was identified;
the essential audit precedes discovery rather than manufacturing one.
