# Complete even inverse — boundary exit-potential comparison839

TARGET: Assess whether the killed-reference exit-time potential yields an explicit constant C_boundary for C759k's complete-even shift32 inverse with |u(x)| <= C_boundary ||g||_infinity / sqrt(log(e/(1-|x|))) almost everywhere on (-1,1), without sign or isolation assumptions.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step839 searched geometric-stable interval exit-time, explicit logarithmic barrier and exact Suprema of Levy processes terminology; inspected GRv1 Proposition3.5 and its upper-bound proof, KMRv3 Theorem4.4 and its complete proof, Proposition2.1/2.3 and normalization passages; narrowly compared L513, C759k, assessment828 and stops829/831. Queries and primary citations follow; no novelty inferred.
SOURCE_EVIDENCE: GR1107.0745v1 Section3, Proposition3.5, printed p7, gives an exit-time upper coefficient1 in normalized renewal functions. Kwasnicki-Malecki-Ryznar1103.0935v3 Theorem4.4, reprint p14, gives the global renewal upper coefficient5. Their Section3 and Section4 normalizations agree; C759k Proof1-5 and L513's existing half-speed normalization are reused.
COMPARISON: Effective reference inputs are available, rather than merely an unspecified qualitative boundary constant. Neither paper states the complete signed Weil-operator estimate: the remaining application must combine these cited bounds with C759k's compatible equation and verify the global logarithmic-weight conversion. No C_boundary or new lemma is derived in this literature step.
GAP: Specify and prove the finite numerical full-operator constant, including interval translation, half-speed normalization, signed forcing domination, almost-everywhere identification and the entire endpoint regime; retain both poles and all five prime shifts. This is now a covered known-method specialization, not missing essential literature.
REASON: Continue this independently testable bounded-forcing boundary ingredient using the effective cited estimates; no sign or spectral-isolation premise is needed in those estimates. Weighted positive trial margin, complete isolation, parity and actual-Xi realization remain independent gaps.
LITERATURE_REASON: The exact boundary weight and effective exit-potential constant are outside the ready unsigned unweighted scope. C759k resolves the full-operator boundedness premise missing in stop829, but the necessary quantitative reference coverage remains unread.
SCOPE: Completed source review for I=(-1,1), real even essentially bounded g, u=(A_e+32I)^(-1)g and the complete C759a form. Known effective reference bounds cover a subsequent unsigned almost-everywhere specialization; no boundary estimate, sign, continuous representative or eigenfunction certificate has been proved here.

The original nomination below is preserved as historical scope and stopping
criteria. Its statements about unread exit-time/renewal coverage are superseded
by the completed comparison839 at the end. The separate proposed application
is recorded in `2026-11-13-even-boundary-exit-specialization-839.md` and requires
its own next-turn approval; it is not performed in this source review.

## Recovery comparison and selected mechanism

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The completed step838 is solely the conceptual audit of
C759k. It is not a derivation or approval of this new target. The
following comparison selects one future source review, without
testing additional mathematics in that completed turn.

1. Further unsigned norm optimization or a repeated source approval
   would revisit a completed target. C759k has passed at the required
   fixed shift; no residual application currently requires a sharper
   constant. Close that sequence and preserve its stalled history.
2. A pole-free rank-one secular isolation test would address another
   gap, but assessment791 records the missing controlled background
   and arithmetic numerator. The new unsigned inverse does not
   provide either, or a full spectral count. A generic secular
   identity alone is therefore not a justified reopening.
3. A reference exit-potential bound would address the independent
   boundary error gap. C759k supplies both actual-Q boundedness
   and the compatible equation u=R_0(g+Ku). Its full K acts on
   bounded data. The selected question is whether precise known
   killed-reference estimates can now give an effective boundary
   bound for this equation, with arbitrary signed forcing.

Select3. Stop829 concerned a combined effective eigenfunction
enclosure and full isolation, and lacked actual-Q boundedness. This
target removes the eigenfunction/isolation demand and adds the
now-verified full-Q bounded forcing input. It asks only for a
weighted inverse estimate and does not reuse Hopf positivity to
prove a sign. Stop831's unrestricted L2 residual remains excluded;
the forcing norm here is L-infinity. C759i's complete-operator
order obstruction remains in force; only the killed reference has
the positivity needed in the proposed source mechanism.

## Exact source question and decision test

Set delta(x)=1-|x| and b_delta(x)=1/sqrt(log(e/delta(x))) on I.
These merely define the desired weight; no comparison estimate
is asserted. C_boundary must be a specified finite numerical upper
bound, or a completely specified evaluable expression whose finiteness
and bounds can be certified in one covered specialization. An
unspecified existence constant does not meet this target.

Use the reference process of exponent half log(1+t²), killed on
exit from I, rather than Brownian subordination after killing.
Inspect primary theorem hypotheses and essential proof cases for
its expected exit time or discounted occupation potential. Determine
whether their constants, normalization, interval size and endpoint
regime support the displayed weight globally on I. A half-line
asymptotic with an unquantified onset or an unnormalized renewal
function does not by itself give the requested constant.

The precise primary lead is Grzywny-Ryznar,
*Potential theory of one-dimensional geometric stable processes*,
[arXiv:1107.0745v1](https://arxiv.org/html/1107.0745v1).
Only its Section2 process definitions are already covered for this
task. Retrieve the relevant interval/exit-time/renewal theorem before
larger passages. Reuse assessment828's inspected comparison with
[Hernandez-Santamaria, Lopez Rios and Saldana, arXiv:2401.18033v2](https://arxiv.org/html/2401.18033v2),
Theorem1.1 and Section4; do not simply reread the qualitative boundary
theorem or treat its different symbol as the present one. Reopening
any source access issue needs an essential exact passage, not a
repeat of the closed FOT/Engel-Nagel retrieval sequence.

Continue only if the source review supplies effective applicable
coverage, or specifies one explicit reference barrier/occupation
calculation with all essential source premises available. Otherwise
record the exact unpaid constant or hypothesis and park this
quantitative target. No mathematical estimate is established in
this nomination. Any subsequent specialization receives its own
approval; merely finding a known qualitative boundary exponent is
not success at this threshold.

Essential local mathematical input is C759k, including its audit
Proof5 and reference equation(12); C759a(1),(5)-(6), C759h's pole
action, L741's exact remainder and L515's reference identify its
operator. C759i/j and stop829 are comparison evidence, not positivity
premises. No cross-notebook input is proposed. Full matching Mathlib
coverage is unchecked. Even a successful bound would leave the
weighted positive trial margin, lowest-even isolation, parity
ordering and actual-Xi/global assembly unproved.

This is source comparison for a known-method development, not a
creative proof claim. Discovery priority was considered; no concrete
new signed arithmetic/Xi mechanism or controlled pole-free spectral
input is available from this audit. The boundary test is selected
for its independently checkable missing estimate, not a quota.

## Completed comparison839 — 13 November2026

### Primary effective inputs and their exact scope

Grzywny and Ryznar, *Potential theory of one-dimensional geometric stable
processes*, [arXiv:1107.0745v1, 4 July2011](https://arxiv.org/pdf/1107.0745v1),
Section3, Proposition3.5 and the upper-bound proof, printed p7, state

\[
 E^y\tau_{(0,R)}\le V(\min(y,R-y))V(R),\qquad 0<y<R.
\]

The standing assumptions are a symmetric non-compound-Poisson Levy process
and ladder normalization kappa(z,0)=sqrt(z). The proof's upper part uses the
nonnegative occupation identity quoted from Bertoin, *Levy Processes*,
ChapterVI, Theorem20, p176, and interval-to-half-line domination. It does
not use the unspecified C1 in the lower estimate. That book proof was not
newly inspected; its role and previous import are already explicit in L513.
This is an interval bound at every interior starting point, not an
asymptotic or a sign statement about the complete operator.

Kwasnicki, Malecki and Ryznar, *Suprema of Levy processes*, Annals of
Probability41(3B)(2013),2047-2065, DOI10.1214/11-AOP719,
[arXiv:1103.0935v3, 8 July2013](https://arxiv.org/pdf/1103.0935v3),
Theorem4.4 and proof, electronic-reprint p14, state

\[
 \frac{1}{5\sqrt{\Psi(1/x)}}\le V(x)
 \le\frac{5}{\sqrt{\Psi(1/x)}},\qquad x>0.
\]

Hypotheses: symmetry, not compound Poisson, and both Psi(xi) and
xi^2/Psi(xi) increasing for xi>0. Section3 equation(3.1), reprint p7,
chooses local-time constant1; Section4 immediately before Proposition4.3
identifies the same kappa through its log-Psi integral. Read the complete
Theorem4.4 proof: its upper bound uses Proposition2.1's explicit Catalan
constant comparison and Proposition2.3's monotone Laplace bound; its lower
bound uses subadditivity and Proposition2.2. No regular-variation onset is
required for either bound. These auxiliary statements and the upper
comparison proofs were inspected, not reconstructed as new theorems.

### Applicability and the specialization still to do

For the reference, Psi(xi)=half log(1+xi^2). Symmetry, infinite Levy
measure and the precise killed realization are already C759k Proof1/5.
The required monotonicities follow from the increasing concave Bernstein
function psi(s)=half log(1+s), with psi(0)=0; KMR Remark4.7 records this
subordinate-Brownian applicability. Thus the slowly varying endpoint
case is included. The factors are for the source-normalized renewal
function, not an arbitrary multiple. L513 Proof's normalization passage
already checks the half-speed change V=sqrt(2)V_GR and the occupation
factor2. That existing argument is reused, not reproved here. The KMR
bound can instead be applied directly to the half-speed exponent.

For a future application translate the interval to (0,2), use the
reference killed occupation potential to dominate the discounted
reference potential, and use C759k(12)'s compatible equation on bounded
signed data. C759k(1),(9) supply the full forcing budget. The application
must justify those representations for equivalence classes and convert
the source's global weight involving Psi(1/delta) to the requested
log(e/delta) weight on every 0<delta<=1. These are explicit remaining
checks, not estimates claimed in this review. No full-operator order
preservation, eigenfunction sign, spectral count or boundary point value
is supplied by either cited theorem. No reproof of their general results
is justified or proposed.

### Duplicate/failure comparison and decision

L513 already contains the normalized half-line occupation bound and an
exact endpoint asymptotic; neither that asymptotic nor assessment828's
qualitative different-symbol theorem provides an effective global
constant. The newly inspected KMR theorem supplies the explicit uniform
renewal factor that this source question lacked. This is local source
progress using known results, with no beyond-source discovery claim.
C759k supplies actual-Q boundedness that stop829 lacked. Stop831 is
about unrestricted L2 residuals; this target keeps L-infinity forcing.
C759i/j's recorded order/norm stops remain intact. Relevant existing
renewal, boundary and November13 even assessments were searched for the
exact KMR identifier and effective-constant target; no duplicate complete
boundary certificate was found in those paths.

Searches included `"geometric stable" "exit time" "interval" Grzywny Ryznar`,
`"geometric stable" "explicit" "barrier" boundary log`, and the exact
title `"Suprema of Levy processes"` with the authors. Search snippets
were used only to locate primary papers. The more general unimodal-barrier
and bounded-interval-exit papers were screened as leads and not imported;
no essential theorem from them is needed after these two effective inputs.
The half-line spectral-analysis paper was opened as a lead, not used.
Full matching Mathlib coverage is unchecked; no Mathlib theorem is claimed.

The continuation test is met at the source level: explicit global renewal
and interval occupation constants are available with compatible
normalizations. A full numerical C_boundary is still unproved. Select a
single known-method specialization, subject to separate approval next
turn; do not browse these unchanged sources again merely to repeat the
decision. No concrete new signed arithmetic/Xi mechanism is yet specified
well enough for a protected creative attempt. Its missing central bridge
is a discovery blocker, not a reason to relabel this routine specialization.
