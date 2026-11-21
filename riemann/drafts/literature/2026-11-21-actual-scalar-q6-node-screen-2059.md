# Prescribed actual scalar Q_6 — fixed input-condition screen

TARGET: Certify whether the prescribed actual scalar Q_6 has at least four distinct real zeros, retaining all odd coefficients and N=6's own Jensen weights.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed partial-biorthogonality review2059 reused auxiliary-review2058 and scoped November20–21 Pollaczek/Jensen failure/duplicate coverage. No exact Q_6 root certificate was located there. The proposed finite input condition differs from the recorded U_6 output-index, metric, residue and cross-degree tests; no novelty claim.
SOURCE_EVIDENCE: Direct primary source https://doi.org/10.4153/CMB-2008-055-0 (publisher PDF linked in recovery2060 below), Kuznetsov2008 Proposition4.1 p567 fixes scalar weights; equations(4)/(13) pp563/566 and weighted family pp568–569 fix coefficients. C029n Section1 records exact N=6 data and actual degree; C029q Hypotheses fixes A_(N,k). Musin https://arxiv.org/pdf/0903.1908v2 Theorem1 p4 supplies the general partial-orthogonality count source; full citations/hypotheses and DLMF matching in completed assessment2058.
COMPARISON: This is a fixed algebraic input-premise test for a known-result specialization, not an output Hermite count or an all-N sign mechanism. Classical Sturm root counting, square-free separation and rigorous coefficient enclosures can certify the distinct real count without assuming RH or the transform identity. That analytic specialization remains separate.
GAP: Exact Q_6 distinct-real-root count is uncomputed. Its coefficients involve pi and sqrt(2), so floating approximations or an unverified Sturm sequence cannot certify the count. The full-real-parameter moment identity, Chebyshev applicability and uniform Q_N condition remain open.
REASON: Screen the independent scalar premise before spending work on the conditional analytic specialization. At least four distinct real zeros passes only this finite premise; fewer than four parks this N=6 baseline. Do not sweep degrees or infer failure of the eventual index bound or RH.
SCOPE: One fixed N=6 scalar input-condition screen only, after separate approval of this newly saved assessment. No U_N output-root/inertia calculation, beta alteration, odd-term deletion, higher N, auxiliary coefficient inversion or new analytic transfer proof is included.

Define the prescribed polynomial exactly as in nomination2058:

    Q_6(x)=sum_(k=0)^6 [(2k+1)!!/(2k)!!] A_(6,k) x^k,
    A_(6,k)=[6!/((6-k)!6^k)] beta_k/S,
    S=sin(pi/8)/sqrt(2)>0.

Use C029m's beta formula with u_0,...,u_8, including all odd entries;
C029n's exact reduction to Q(sqrt(2))[pi] and its rational enclosures
may be reused. C029q's definition agrees at N=6. Independent positive
normalization of Q_6 is allowed only with explicit root invariance.
Do not import N=7's weights or infer uniform degree from C029n.

The sole threshold is four distinct real zeros on R, not four zeros
counted with multiplicity and not four numerical approximations.
Certify degree and root separation/nondegeneracy as needed for the
chosen method. A rigorous interval Sturm chain with all necessary
nonzero signs, or isolating sign brackets plus a rigorous upper count,
is acceptable. Record exact constructions, enclosure bounds, failures
and full certificate under scripts/pollaczek/; print only bounded
results, actual/required count, certificate path and replay command.
If the bounds cannot decide this fixed screen, save the unresolved
sign/degeneracy and stop; do not launch a precision/degree sweep.

Downstream use is conditional: completed review2059 locates Musin's
general count theorem but does not prove the prescribed bilateral
moment identity. A passing Q_6 screen would leave that applicability
proof, all-N input control, initialization, degree drops, weighted
convergence qualifications and Xi transfer unresolved. Failing this
finite baseline cannot reject an eventual-only bound.

Essential inputs: C029m family, C029n Section1 coefficient/degree
conventions, C029q finite normalization, and completed assessment2058
source comparison2059. Preserve auxiliary-review2058 and all recorded
C029q/r/s/t/v/w/x/stops. No cross-notebook theorem; Mathlib matching
unchecked. This is standard calculation/specialization, not creative
research. Any subsequent transfer proof or changed polynomial requires
its own matching review.

## Source-URL recovery2060 (2026-11-21)

LITERATURE_REASON: Supervisor reported that this ready assessment lacked
its own direct source URL. Repair that evidence field for the unchanged
fixed Q_6 target; reuse completed comparison2059, without reopening
transform research or computing roots.

Direct sources inspected in this repair:

- Alexey Kuznetsov, *Expansion of the Riemann Xi Function in
  Meixner–Pollaczek Polynomials*, Canad. Math. Bull. 51(4) (2008),
  561–569, [publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FD79D70DF68748CCEC70097E3FB9F2FA/S0008439500012492a.pdf/expansion-of-the-riemann-function-in-meixnerpollaczek-polynomials.pdf).
  Proposition4.1 p567 is a sufficient all-real-input to all-real-output
  statement with scalar weights (2k+1)!!/(2k)!!. It does not give the
  proposed partial-root transfer. The degree-dependent Jensen weights
  and weighted family appear on pp568–569. Those passages were read;
  their numerical output observations do not certify scalar Q_6 roots.
- Oleg R. Musin, *Chebyshev systems and zeros of a function on a convex
  curve*, [arXiv:0903.1908v2](https://arxiv.org/pdf/0903.1908v2),
  27 April 2009, Section2 definitions pp2–3, Theorem1 p4.
  The statement requires continuous functions, a Chebyshev system,
  continuous constant-sign weight, orthogonality and nonzero f*rho.
  It counts sign changes of f. Definitions and theorem were reread;
  the proof assessment is reused from completed comparison2059.

For the finite scalar calculation, the local exact coefficient inputs
remain C029m, C029n Section1 and C029q Hypotheses. No transform theorem
is assumed to count scalar roots. Use classical Sturm's theorem with
certified signs and distinct-root handling as already specified above;
no new algorithm, root certificate or analytic specialization is supplied
here. No change to TARGET, DECISION or SCOPE. No source blocker remains
for this finite screen. All previously listed analytic/uniform gaps and
Mathlib-unchecked qualification remain. This is a process repair with
unchanged mathematical evidence, hence STALLED rather than ADVANCE.
