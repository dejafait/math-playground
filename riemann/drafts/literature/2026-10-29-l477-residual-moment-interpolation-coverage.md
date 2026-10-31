# Full-residual moment interpolation: completed source comparison

TARGET: Test whether second/fourth moment interpolation for L477's complete residual certifies integral_T^(2T)|R_T(t)|dt>=c T(log T)^3 for some fixed c>0 along an unbounded sequence.
CHECKED: 2026-10-29
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact-residual, Riemann--Siegel moment, finite Dirichlet-polynomial mean-value, Holder interpolation and oscillatory-integral searches on 2026-10-29; read the primary statements/proof cases below and reused the local Hardy-norm assessment and stationary-involution stop. No matching full-residual moment estimate was established; no novelty is inferred.
SOURCE_EVIDENCE: Tao, 245C Notes 1 (30 March 2009), Lemma 9 and its Holder proof, https://terrytao.wordpress.com/2009/03/30/245c-notes-1-interpolation-of-lp-spaces/ ; Tao, 247B Notes 8, Section 2, Lemmas 2.4--2.5 and proofs, printed p. 5, https://www.damtp.cam.ac.uk/user/gold/pdfs/teaching/notes8.pdf ; Bui--Hall arXiv:2304.05178v1, Theorem 3, Proposition 3 and Section 7, https://arxiv.org/html/2304.05178v1 ; Montgomery--Vaughan (1974), Theorem 2/Corollaries 2--3 and Section 4, https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf , with unread-display qualification below; supplementary comparison Weber arXiv:0907.4931v3, Proposition 6/(37)--(41), https://arxiv.org/pdf/0907.4931v3 . Retain L477 (1)--(5) and its Section 5 audit.
COMPARISON: Interpolation is a standard known input, not a new lemma. The inspected moment theorems do not estimate the complete residual with its fixed cutoff and chirped cross terms. Readable interval integral estimates cover a direct finite-sum diagnostic, including stationary cases; they do not provide a summed error or a lower bound. L471's ordinary-moment loss, L472/L473's abstract-law limitations and the prior Hardy-transfer stop remain intact.
GAP: Prove a lower bound for the full I_2 and an upper bound for the full I_4 with sufficient uniform constants, then compare the certified quotient to T(log T)^3. Coincident frequencies, near coincidences, stationary terms and product lengths remain explicit calculation obligations; no needed residual estimate is being assumed as an input.
REASON: Source scope now supports one bounded finite-expansion/integral-estimate test of the unchanged target under EXPLORE. No moments, lower bound, obstruction theorem or new mathematical specialization were derived in this literature-only step. The changed ready assessment is subject to separate next-turn approval before mathematical invocation; no further generic source search is needed for this limited scope.
LITERATURE_REASON: Essential unread coverage is the finite-interval second/fourth moment comparison for the full residual with growing cutoff and actual chirped cross terms; the ready audit and Hardy-space assessments do not cover those hypotheses.
SCOPE: Exact L477 R_T, theta and M on [T,2T], all ordered pairs and both phase sums, real T tending to infinity; no RH, simplicity, zero spacing, external half-plane premise, selected-law realization or independent random phases.

## Original nomination (preserved; unread-source status superseded below)

For k=2,4, denote the proposed moment quantities by

    I_k(T)=integral_T^(2T) |R_T(t)|^k dt.

The candidate interpolation certificate to assess is the quotient
I_2(T)^(3/2)/I_4(T)^(1/2), whenever I_4(T)>0. The intended
threshold is a positive constant times T(log T)^3 along an
unbounded sequence. These are the target quantities, not estimates
derived or assumed in this nomination.

The next source comparison must first identify precise primary
hypotheses for the interpolation and any applicable finite-interval
moment bounds. Account for polynomial lengths after multiplication,
coincident frequencies, the actual interval length, cross terms and
possible stationary phases. Read only the needed theorem statements
and proof cases. Reuse earlier sources where their scope truly matches;
do not retrieve the same Hardy-space sources to repeat their mismatch.
Do not apply an upper bound for one component as a lower bound for the
complete real residual.

Continue to one mathematical test only if coverage supplies a concrete
finite-sum argument or theorem application with its outstanding estimates
identified. Compare certified bounds for the quotient with the stated
threshold. A subthreshold certificate stops that certificate, not the
full lower-bound target; a bound on the quotient itself would need its
own justification. If essential coverage is persistently blocked, park
this diagnostic and select a different independently testable target.

By L477 (4), a successful full-scale lower bound would reject this fixed
square as a little-o approximation. Failure to certify one proves no
little-o estimate. Either outcome leaves mean negative-mass saving,
individual-height signs and all-degree mixed positivity unresolved.
Full matching Mathlib coverage is unchecked. No new lemma, mathematical
script, moment calculation or independent analytic-input audit is part
of this source nomination.

## Completed review, 29 October 2026

The main gap remains all-degree actual-Xi mixed positivity. This target
tests a norm certificate for the exact residual in L477 (1)--(2). Its
possible downstream use is precisely L477 (4): a full-scale lower bound
would reject this fixed square as a little-o approximation. Neither
outcome would establish mean negative-mass saving, individual-height
signs or RH. Those independent gaps stay open.

### Inspected statements and proof cases

1. **Tao, 245C Notes 1, Lemma 9, Section 2, 30 March 2009.**
   The [author's notes](https://terrytao.wordpress.com/2009/03/30/245c-notes-1-interpolation-of-lp-spaces/)
   state log-convexity on an arbitrary measure space: for
   0<p_0<p_1<=infinity and f in both spaces,
   ||f||_(p_theta)<=||f||_(p_0)^(1-theta)||f||_(p_1)^theta,
   where 1/p_theta=(1-theta)/p_0+theta/p_1.
   Read the finite-exponent Holder proof immediately below the statement.
   The proposed 1,2,4 quotient is within this standard theorem's scope;
   use Lebesgue measure dt on the actual interval, consistently without
   normalized/infinite-time means. L477 defines a continuous finite sum
   there, so finite-norm hypotheses present no source obstacle. Treat a
   zero denominator separately. This source supplies no moment estimate.
   Cite the theorem and check the exponent specialization in the research
   turn; a fresh interpolation proof has no purpose here.

2. **Tao, 247B Lecture Notes 8, Section 2, Lemmas 2.4--2.5,
   printed p. 5 (PDF page 5).** The
   [primary lecture notes](https://www.damtp.cam.ac.uk/user/gold/pdfs/teaching/notes8.pdf)
   define I(lambda)=integral_J exp(i lambda phi(x))dx for a smooth real
   phase on an interval. Lemma 2.4 requires |phi'|>=c>0 and monotone
   phi', and gives O((c lambda)^(-1)). Lemma 2.5 requires
   |phi^(k)|>=c>0, k>=2, and gives O_k((c lambda)^(-1/k)).
   Read both proofs: integration by parts retains the interval boundary;
   the higher-derivative proof isolates a short small-derivative interval
   and applies the lower-order bound outside it. Thus an interior or
   endpoint stationary point is not silently omitted. Constants are
   uniform in the phase subject to these hypotheses. These estimates
   bound individual integrals, not their arithmetic coefficient sum.
   No stationary-phase asymptotic or sign of a stationary term is imported.

3. **Montgomery--Vaughan, _Hilbert's inequality_, JLMS (2) 8
   (1974), 73--82, Theorem 2, Corollaries 2--3, Section 4.**
   The [primary PDF](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
   exposes the distinct-real-frequency hypotheses, local separations,
   finite/infinite qualification and proof reduction: expand the square,
   separate the diagonal and apply Hilbert inequalities to endpoint
   forms. Display extraction still loses the inequalities. Screenshot
   calls returned references without inspectable images; shell download
   failed DNS. No exact constant is newly certified, and this partially
   readable source is not an essential input to the approved direct
   integration alternative. Do not repeat attempts at this same endpoint
   merely to recover an optional constant.

   Supplementary [Weber, arXiv:0907.4931v3](https://arxiv.org/pdf/0907.4931v3),
   Section 3, Proposition 6/(24)--(25), printed p. 8, gives readable
   fixed-frequency mean-square statements and the endpoint expansion.
   Read also (37)--(41), p. 11: raising a length-N polynomial to power nu
   produces length N^nu and a length-dependent mean-value error. The
   short-polynomial simplification requires the displayed relation
   T>=N^nu. These expository restatements are comparison evidence, not
   a recovered independent reading of the 1974 displays or a theorem
   for the chirped residual. In particular an eighth-degree polynomial
   envelope cannot simply reuse the original square-root length; any
   resulting M^4 length must be compared with T. Proposition 8/Theorem 9,
   pp. 12--13, require fixed linear frequencies; the latter uses
   nonnegative coefficients and a centered interval. They supply no
   shifted-interval lower bound for the complete real chirped sum.

4. **Bui--Hall, _On the derivatives of Hardy's function Z(t)_,
   arXiv:2304.05178v1, 11 April 2023, Theorem 3, Proposition 3,
   Sections 4.2 and 7.** Read these
   [primary passages](https://arxiv.org/html/2304.05178v1#S4.SS2).
   For fixed nonnegative derivative orders their fourth-jet integral
   has main term HARDY(k,l,m,n)T(log T)^(k+l+m+n+4)/pi^2 and an
   error one logarithm smaller. Proposition 3 treats two zeta factors
   at +it and two at -it, shifts O(1/log T), on [T,2T], with uniform
   O(T(log T)^3) error. Section 7 applies fixed differential operators
   to this shifted formula; Section 4.2 omits its proof, referring to
   the preceding derivation. No independent manuscript audit is claimed.
   This scope includes genuine fourth jets but does not include mixed
   terms with L477's prescribed finite square, or a full eighth-jet
   moment. L477's L1 transfer error is not a stated L2/L4 transfer error.
   Accordingly this theorem alone cannot be cited as the desired I_2
   or I_4 estimate. No new residual specialization is made here.

### Comparison with local failures and search record

Read the previous fixed-square and Hardy-L1 assessments, L477 through
its finite proof, the audit history, and
`ATTEMPTS/2026-09-24-actual-phase-poisson-ratio-test.md`. Reuse the first
audit's conclusion; do not repeat it. The stationary-involution stop
concerns signing a transformed block and remains valid. Estimating
the complete residual's finite moments is a different test, but merely
exhibiting stationary terms or repeating that unsigned transform would
not be progress. L317's fourth-order pointwise dominance stop and L471's
zero-weighted ordinary-moment loss are not the present norm estimate.
L472/L473's laws do not give actual-arithmetic lower bounds. The previous
Hardy-space comparison still blocks automatic Haar-to-height transfer.

Queries included: Montgomery Vaughan Hilbert inequality 1974 mean value
Dirichlet polynomial theorem 2 corollary pdf; Riemann Siegel polynomial
fourth eighth moment finite interval derivatives Hardy Z moments;
Dirichlet polynomials Holder fourth moment lower bound L1; van der
Corput second derivative test integral; Riemann Siegel residual fourth
moment square; Dirichlet polynomial P_0 P_2 P_1 moment; Hardy Z Wronskian
moments. Exact/stronger-result searches did not establish a matching
estimate. This bounded result is not evidence of novelty or nonexistence.
New filtered-fourth-moment search hits were not inspected or imported:
their displayed subject does not itself cover the complete residual's
mixed finite-square and fourth-residual moments. No result from another
notebook is used. Full matching Mathlib coverage remains unchecked.

### Bounded mathematical scope after separate approval

Keep exactly the saved TARGET. Use L477 (1)--(5), retaining L317 (1),
L316's analytic phase and L471 (7)/curvature as qualified inputs. This
is a finite residual calculation, not another derivative-AFE audit.
There is no RH, simplicity, zero-spacing, external half-plane or random
phase assumption. Ready source coverage is for the following test:

- Expand both full even powers, retaining every ratio/product cross
  term, and check grouping of equal frequencies before using separation.
  A convenient candidate kernel family is integral exp(i(2q theta(t)
  +t log r))dt for integer q and positive rational r; establishing the
  exact index ranges, coefficients and complete representation is work
  for the research turn, not an identity proved in this source review.
- Classify constant phases, nonzero linear phases and phases retaining
  theta. For the last class, verify the first- or second-derivative
  hypotheses from the retained phase input on the full closed interval;
  use the second-derivative bound at stationary points. Include every
  endpoint and near-coincidence cost. Finite expansions allow this test
  without a general theorem for chirped Dirichlet-polynomial moments.
- Obtain a lower estimate for the **complete** I_2 and an upper estimate
  for the **complete** I_4, or record the precise obstructing sum. A
  component lower bound cannot survive unspecified cross cancellation.
  Component upper bounds may be combined only by a cited norm inequality
  with every factor and length retained. The interpolation quotient
  needs both directions of evidence, not two moment upper bounds.

Compare the resulting certified quotient with c T(log T)^3 for a fixed
c>0 along an unbounded sequence. A successful certificate would settle
only this lower-bound test. A subthreshold lower certificate stops that
certificate, not the true quotient or lower-bound target. A rigorous
upper bound on the quotient is a different conclusion requiring proof.
If this bounded pass supplies neither adequate bounds nor a materially
refined, independently testable sum, save its evidence and reassess;
do not continue by repeating generic mean-value or Hardy-norm searches.
Uncovered techniques or stronger theorem applications require their
own separate assessment. No moment calculation, new lemma or script
was performed during this review.
