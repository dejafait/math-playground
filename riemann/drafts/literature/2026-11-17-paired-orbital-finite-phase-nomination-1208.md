# Two-level finite-phase response — coverage approval1209

TARGET: Determine whether an absolute C bounds |E_(k,b)(x)|<=C*x*b^2 for D_b=diag(a+i*b,a-i*b,r,...,r), finite n>=2, 0<=k<n, a,r,x>0 and real b with x*|b|<=1/4, using C030m's definitions and separate normalizers; prove an explicit uniform C or a rigorously unbounded family without extending to unequal backgrounds or Xi.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Approval1209 reuses broader finite-phase exact-defect searches and theorem comparisons in assessments1203/1204 and drafts/working/2026-11-16-paired-orbital-source-review-1204.md; a scoped local orbital/HCIZ duplicate search found no completed finite-phase bound. No repeated web discovery search or novelty claim; reopened primary domains for this exact restricted target.
SOURCE_EVIDENCE: Reopened McSwiggen arXiv1712.03995v4 https://arxiv.org/pdf/1712.03995v4 Theorem1 p4/(2) p2/continuation after(24) p10; Novak arXiv2203.10746v1 https://arxiv.org/pdf/2203.10746v1 Theorem1.2 p6/domain pp2-3/Theorem4.7 nonvanishing reduction p34. Reuse1204's GGN2014 https://www.numdam.org/article/AMBP_2014__21_1_71_0.pdf Theorem5.1 pp84-86/Section5.2 pp86-87 and corrected Guionnet--Maida https://perso.ens-lyon.fr/aguionne/rgfend.pdf Theorem4 p5. Read relevant C030m definitions, branch proof and audited scope, and C030l comparison hypotheses/qualifications; no independent reaudit claimed.
COMPARISON: Prior searches addressed a broader finite-phase defect including this common-background subfamily. C030m supplies positivity on the proposed window but only a pointwise infinitesimal derivative bound. Exact complex identities, bounded-field small-coupling nonvanishing and low-rank asymptotics do not state the required finite-n adjacent-rank bound at unrestricted real contrast. Adequate coverage permits a bounded attempt, not import or a novelty claim.
GAP: A parameter-uniform finite-phase bound on the logarithmic derivative, or a rigorous violating family, remains unproved; a pointwise O(b^4) expansion and a positive partition function do not provide it. General backgrounds, pair summation, actual-Xi scales and all-degree positivity remain independent.
REASON: Separate approval1209 confirms adequate coverage for exactly TARGET using1204's broader search and the audited local inputs; no essential unread source is required for this restricted direct test. A later mathematical turn may seek an explicit absolute C or an unbounded normalized-defect family. Neither is derived or mathematically approved here.
SCOPE: Normalized Haar on U(n); exactly one conjugate pair with equal real part and one common positive background rate; repeated projection eigenvalues, both signs of a-r, a=r, n=2, k=0,n-1 and b=0 included. Full matching Mathlib coverage unchecked. No cross-notebook input.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED target changes the pointwise coefficient to a finite-window uniform estimate, expressly outside1206's audit scope. This turn supplies separate comparison and approval using1203/1204 rather than repeating their searches; no additional literature turn is proposed.

## Proposed test and existing inputs

The nomination text below records the state at1208. Completed
approval1209 at the end supersedes its pending-review language,
preserving TARGET and every mathematical obligation.

Use Z_(j,b), G_(j,b) and E_(k,b) exactly as defined in C030m;
the x derivative holds a,r,b fixed. Each rank retains its own Haar
normalizer. C030m's equation (3) already gives a positive real quotient
on the stated window. This nomination does not require another proof
of that branch or assume a common partition function. The audited
coefficient bound is a necessary local check, not a uniform remainder
estimate. At b=0 the proposed inequality has the removable equality.

Essential local inputs are C030m and C030l's full real tilted-array
comparison, including weak rows and arbitrary fixed real fields.
Its source scope is Sra author v3 Lemma C.7/Theorem C.8, printed
pp25-27, https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf,
and Olshanski2013 Corollary3.2 p1017,
https://www.heldermann-verlag.de/jlt/jlt23/olshla2e.pdf,
whose uniform orbital-law statement requires strict top rows.
The local weak-row extension is justified in C030l; it is not imported
from Olshanski's strict-row statement. Complex stochastic order is
not an established input. No general orbital theory should be reproved.

Main gap: actual-Xi all-degree positivity in L030-L032/C032a.
Plausible downstream use: a paid signed perturbation of the finite
real reference. Even a positive result here supplies neither a sum
over many pairs nor a rate/degree/time match for actual Xi. A rigorous
unbounded family would stop this uniform finite-phase proposal, not
RH or all signed comparisons. The bounded decision is an explicit
absolute C with complete parameter control, or a rigorous family whose
normalized defect is unbounded. A finite numerical sample or another
fixed-parameter Taylor formula does not settle that test.

Reused stops1117/1181/1193/1200/1107 and finite-core overlap884
retain their documented scopes and are not mathematical premises.
The source-review1204 zero examples concern different spectra; do not
treat them as counterexamples here. No independent source blocker
or exhausted mathematical route is being reopened by changing a name.

The next turn is source-scope comparison/approval for exactly TARGET.
If adequate coverage is confirmed, nominate one bounded mathematical
attempt without deriving the finite-phase result in that review turn.
If essential coverage is still missing, identify it precisely. This
REVIEW_REQUIRED nomination does not invalidate the completed C030m
audit and does not claim that the proposed inequality is true.

## Separate source-scope approval1209 (17 November 2026)

One literature comparison only: no response calculation, new lemma,
numerical probe or mathematical script. Completed1204's exact-defect
searches concerned finite phase, arbitrary remaining positive rates
and the same independently normalized defect. Equal remaining rates
restrict that already searched question. The earlier authorization
was only for the infinitesimal diagnostic; this separate review
supplies the missing finite-phase scope decision.

C030m, independently audited1208, now supplies the positive quotient
on the entire proposed window through equation(3). Equations(1)-(2)
bound only its b->0 response; the remainder in the proof of(4) is
explicitly local at fixed parameters. That statement does not answer
TARGET or permit passing a parameter supremum through the limit.
C030l supplies the full real tilted-array comparison including weak
rows, fixed arbitrary real fields and separate normalizers; its scalar
rank bound is not a theorem for complex D_b. No new application or
finite-phase differentiation formula is derived here.

Primary source comparison, retaining the versions and direct URLs in
SOURCE_EVIDENCE:

- Novak, *Topological Expansion of Oscillatory BGW and HCIZ Integrals
  at Strong Coupling*, arXiv2203.10746v1, (1.2) p2, domain pp2-3,
  Theorem1.2 p6: probability Haar, exponent z*N*Tr(AUBU^-1),
  eigenvalue moduli <=1, |z|<=epsilon for an existential epsilon
  in(0,2/27). It gives nonvanishing for every N and uniform large-N
  logarithmic expansions. Theorem4.7 p34 obtains nonvanishing from
  a normalized integral within1 of1 for large N and shrinks the disc
  for finitely many remaining N. No critical-coefficient proof audit
  was performed. Reuse1204's normalization comparison A=-D_b/M,
  B=P_j, z=x*M/n: phase control does not impose that coupling bound.
  Removing a common scalar leaves unrestricted real contrast. This
  excludes direct import, not the desired estimate itself.
- McSwiggen, *A new proof of Harish-Chandra's integral formula*,
  arXiv1712.03995v4, Theorem1 p4, trace formula(2) p2 and continuation
  after(24) p10: normalized Haar and complex Cartan variables are
  permitted in the discriminant-multiplied identity. Repeated-spectrum
  quotients require removable limits. The identity states neither
  nonvanishing nor the required adjacent-rank derivative inequality.
  No general HCIZ reproof is justified or needed.

Reuse1203/1204's GGN2014 conditional zero-free-disc convergence and
arithmetic-progression zero case, and Guionnet--Maida's beta=1 rank-one
complex asymptotics, with their precise hypotheses. They were not
reread here. Their statements neither cover TARGET nor refute this
small-phase paired/projection family. Two-projection Jacobi and
rank-deficient contour formulas remain unread optional leads, not
premises of this direct C030m/C030l test. Any later load-bearing use
requires checking that theorem's exact hypotheses first.

The local search was confined to orbital/HCIZ-named files in
drafts/literature, drafts/working, ATTEMPTS and history. The older
2026-11-01-vandermonde-spectral-derivative-hciz-review.md concerns a
different arithmetic insertion, not a uniform phase defect. Read
stops1193/1200 narrowly: missing signed degree/time and heat-block
inputs do not refute this finite family. Reuse1204's scoped1117/1181/
1107 and overlap884 comparison. Finite signed-smoothing factor budgets
and actual-Xi transfer remain unpaid. Stops are context, not premises
or global bans. No cross-notebook mathematical input is used.

Decision: ready EXPLORE for exactly TARGET in a later research turn.
Seek complete parameter control yielding an explicit absolute C, or
stop this universal proposal with a rigorous unbounded |E|/(x*b^2)
family. If neither is achieved in one attempt, preserve the precise
remaining estimate and report the partial outcome honestly. Pointwise
Taylor expansions, positive partition functions and finite samples
alone are not decisive. Retain both contrast signs, a=r, n=2, b=0,
k=0,n-1, and x differentiation at fixed a,r,b.

Recommended routing: proof_attempt/development, deep_research/xhigh.
This develops the audited response mechanism. Essential local inputs
are C030m and its full comparison input C030l, relative to the cited
orbital law. Unequal backgrounds, pair summation, actual-Xi scales,
all-degree positivity and graph realization stay open. Full matching
Mathlib coverage remains unchecked. No new theorem, originality claim,
complete candidate or RH conclusion is established in this review.
