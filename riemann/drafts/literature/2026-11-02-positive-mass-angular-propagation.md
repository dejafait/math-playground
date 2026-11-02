# Positive mass and angular propagation — bounded source assessment

TARGET: Assess whether mass-sensitive noncancellation results for positive atomic exponential sums can prove E_n>=c exp(-n/16)D_single,n for the saved angular family, including a uniform transfer to its exact Blaschke weights.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: On 2026-11-02 searched Turan/Nazarov local propagation, pure power sums, positive residues and inverse Blaschke sums; compared C645g/o/x/y/z, L647/L648 and scoped angular drafts/attempts/history. Primary statements and proof portions actually read are identified below; no exact-family match was found in this bounded search and no novelty follows.
SOURCE_EVIDENCE: Read Biro, An improved estimate in a power sum problem of Turan (2000), unnumbered Theorem p.344, Newton-Girard formulas pp.344-345 and (14) p.351, and Section 4 pp.355-357; also Friedland-Yomdin arXiv:1107.0039v3 Theorems 1.1/1.2, Definition 1.1 and the full proof of Theorem 1.2/Lemma 2.1, PDF pp.1-5. Reuse the earlier angular Fourier/residue assessment; no theorem is imported into the RH argument here.
COMPARISON: Biro supplies a uniform pure-power noncancellation constant with an anchor node and repetitions allowed, but not the exact rational weights. Friedland-Yomdin propagates a scalar exponential polynomial with an absolute unspecified constant and degree/measure or metric-span losses, not our rational sum. No inspected result proves the full-energy comparison or a uniform cancellation-sensitive transfer. L647/L648 do not refute that comparison; C645y already stops initial-prefix shortcuts.
GAP: The complete exact weighted spatial coefficient sequence has not been related to a pure-power or exponential sum with a controlled inverse transfer. Any transfer must retain original integer mass, full n-factor weights, the full signed sum and D_single,n, with squared loss at most 1/16 uniformly without separation. That is mathematical work, not an available source specialization.
REASON: The bounded review finds a relevant known mass-counted theorem and a precise functional mismatch, sufficient to test one exact representation/transfer mechanism under EXPLORE, without claiming applicability, originality or a lower bound. Further generic browsing is not the next step. Original Nazarov-source access is nonessential to this exact-algebra test and is parked below.
LITERATURE_REASON: This invocation began with missing essential coverage for positive-mass noncancellation and nonlinear-weight transfer; the earlier Fourier/Nehari assessment did not inspect those hypotheses. This review supplies comparison coverage, not the missing transfer.
SCOPE: One bounded exact Newton-Girard/pure-power transfer attempt for the unchanged family and squared-energy comparison below, using Biro only within his stated hypotheses and the reused Fourier/residue inputs. No approximation by exponentials, new source-dependent theorem, initial-prefix substitution or general propagation theorem for rational functions is preapproved.
COVERED_TARGET: Test an exact Newton-Girard/pure-power representation of the full weighted spatial coefficient sequence for the saved angular family, seeking a uniform transfer that proves E_n>=c exp(-n/16)D_single,n without truncating the n-factor weights or spatial modes.

## Preserved family and intended use

Retain n>=5, x=-5/4, R=11/8, U=R^2, eta=1/100 and t_j=j/n.
Let Z be a finite set of distinct common poles with Re(a)=x,
|a|<=R-eta and x in Z, and positive integer original simple-pole
residues r_a with M=sum r_a<=n/3. There is no separation, ordinate
symmetry, or positivity of the complex weighted amplitudes. For |u|=1,

    B_u(v)=product_(j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    q_u(zeta)=sum_a r_a W_a(u)/(R*zeta-a),
    E_n=mean_u ||q_u||_2^2,
    D_single,n=sum_a r_a^2 mean_u |W_a(u)|^2/(U-|a|^2).

Both circles have normalized angular measure. C645g supplies the
spaces and H_q 1=q; C645o supplies the complete signed identity.
L647 and L648 are method contrasts, not lower-bound inputs.
The proposed comparison is E_n>=c exp(-n/16)D_single,n with c>0 and
onset uniform in all admissible data. The anchor gives D_single,n>=64/21,
so that comparison would supply the synthetic angular detector.
Xi layer isolation, other poles, census/clearance, simultaneous
realization, a matching upper bound and signs remain independent gaps.

## Specific comparison to perform

Inspect primary hypotheses and the essential proof cases of any
candidate positive atomic Laplace/Fourier-sum estimate before importing
it. Distinguish dependence on total integer mass, number of atoms,
diameter, minimum spacing, coefficient ratios, and angular-arc size.
An estimate for arbitrary complex coefficients or a fixed exponential
polynomial does not by itself provide the required uniform constants.
If a theorem uses separation, lattice exponents, variable fractional
weights, or an evaluation outside the controlled domain, record that
as a difference rather than adding it to this family.

The exact W_a are rational functions of u with correlated inside and
outside poles. An exponential approximation in the pole ordinate can
have small termwise relative error and still fail after cancellation.
Any claimed transfer must therefore control the complete signed sum
at the required scale. No such approximation or transfer is proved in
this nomination. The original mass bound and integrality must remain
visible; the prior fractional-mixture obstruction is relevant contrast.

The bounded review should either identify an applicable theorem and
the exact remaining specialization, or document a quantitative mismatch
and nominate a genuinely testable continuation. An unread lead, a
generic Parseval citation or an unassessed transfer is insufficient.
No novelty is inferred from the earlier scoped searches. Full matching
Mathlib coverage for this proposed comparison is not checked.

## Completed review, 2 November 2026

### Search record and inspected primary results

Queries included `Nazarov local estimates exponential polynomials applications
inequalities uncertainty principle 1994 pdf`, `Turan power sum positive integer
coefficients first main theorem lower bound power sums`, `Remez inequality
rational functions poles degree explicit Borwein Erdelyi`, `"positive residues"
"Blaschke" "lower bound"`, `"inverse Blaschke" "sum" noncancellation`, and
`"rational functions" "positive residues" "power sums"`. Discovery results
are leads, not theorem evidence. The following two primary papers supply the
inspected comparisons.

**Pure power sums.** A. Biro, *An improved estimate in a power sum problem
of Turan*, Indagationes Mathematicae (N.S.) 11(3) (25 September 2000),
343-358, [author-hosted published PDF](https://users.renyi.hu/~biroand/pdfs/Turan1.pdf),
[DOI](https://doi.org/10.1016/S0019-3577(00)80003-8).
The unnumbered Theorem, p.344, states that an effectively computable absolute
q_*>1/2 exists such that, for any N complex numbers with z_1=1,

    max_(1<=j<=N) |sum_(k=1)^N z_k^j| > q_*.

No spacing or modulus restriction on the other nodes is imposed; repetitions
are allowed. The paper does not compute a numerical q_*.
Read the theorem, the Newton-Girard setup (3)-(4), pp.344-345,
the summed identities (14), p.351, and Section 4, pp.355-357.
The final contradiction splits indices into H_c and its complement, combines
near alignment with (3), and then fixes alpha close to pi/4 and q close to
1/2. The auxiliary lemmas have not received an independent proof audit here.
This is a cited known result, not a result to reprove.

**Propagation.** O. Friedland and Y. Yomdin, *An observation on the
Turan-Nazarov inequality*, [arXiv:1107.0039v3](https://arxiv.org/pdf/1107.0039v3),
7 August 2013. Read Theorem 1.1, p.1; Definition 1.1 and Theorem 1.2,
p.3; and the full proof of Theorem 1.2 including Lemma 2.1, pp.4-5.
For p(t)=sum_(k=0)^m c_k exp(lambda_k t), c_k,lambda_k complex,
a finite real interval B and measurable Omega subset B of positive measure,
their cited Theorem 1.1 gives

    sup_B |p| <= exp(|B| max_k |Re lambda_k|)
                 *(C |B|/|Omega|)^m *sup_Omega |p|,

with absolute C, not numerically specified there. Their own Theorem 1.2
replaces measure by positive metric span omega_D(Omega); D includes degree,
maximal imaginary frequency and interval length. Its proof bounds sublevel
components, compares covering numbers with measure, then invokes Theorem 1.1.
The proof is not a positivity or integer-mass argument. Discrete sampling
requires the span condition; it is not unconditional sampling. No propagation
theorem is imported for our rational functions.

### Applicability and quantitative threshold

Integer residue multiplicities are compatible with repetitions in a pure
power-sum model: the count would be total mass, not just distinct support.
This is why Biro is a more specific lead than an arbitrary-coefficient
propagation estimate. But the actual weighted amplitudes r_a W_a(u) are
complex and depend on angle. Repeating a node does not remove W_a(u).
No identity making the complete response a pure-power sum has been
established. The anchor normalization alone does not establish one.

For the exponential-polynomial route, the missing items are an exact
parameterization, a controlled normalization value, and the inverse transfer
for the complete sum. The inspected propagation constants also do not
evaluate a loss at the required rate. We have NOT established that their
best possible loss exceeds 1/16: there is no valid specialization on which
to perform that comparison. A bound for a surrogate, or a small relative
error on each summand, does not certify the relative full-energy inequality.

The comparison is with D_single,n, not just a nonzero unweighted moment or
an absolute lower bound. The saved constant-input formula from C645o retains
all spatial modes. Neither source supplies the required inequality
E_n/D_single,n >= c exp(-n/16), a uniform onset, or an admissible
countersequence violating it. The source review therefore completes
coverage for a bounded EXPLORE attempt, not a SPECIALIZE or IMPORT decision.

### Duplicates, failures and boundary of the proposed test

Scoped text searches found no Turan/Nazarov or pure-power application in the
angular assessments, C645 files, L646-L648 or their 2 November records.
This is not a comprehensive novelty search. Relevant local statements and
needed proof ranges were inspected:

- C645g already uses positive integer residue mass after exact cancellation
  by B_n on a contour, (19)-(21). Its sparse census is stronger than M<=n/3;
  this is not permission to repeat that conclusion at the larger census.
- C645o retains all cross terms and has a negative cross entry. Weighted
  coefficients cannot be declared positive from positive original residues.
- C645x's fractional lattice is outside the present integer/census family.
  It stops the stated universal dual, not every mass-sensitive mechanism.
- C645y already has P'/P, degree M and the exact retained-grid square
  decomposition. Its initial-prefix obstruction includes the first M grid
  coefficients and extends through ceil(n/2). Merely writing P'/P or using
  only that prefix is duplicate work or a recorded failure.
- C645z's polynomial maximum-to-mean bound does not establish a large angle.
  L647 has subexponential relative loss and exponentially growing absolute
  energy; L648 stops one input. Neither decides the present exponential ratio.

The proposed test must add an exact, quantitatively controlled connection
between the full weighted coefficient sequence and the mass-counted pure
powers. The Biro theorem must remain a citation; only this connection, if
possible, needs proof. No new representation, estimate or script was derived
in this literature turn. C645y/z remain separately unaudited and are recorded
as contrasts here; no new argument is allowed to silently depend on them.

### Unread leads, access limits and Mathlib

Nazarov's original *Local estimates for exponential polynomials and their
applications to inequalities of the uncertainty principle type*, Algebra i
Analiz 5(4) (1993), 3-66; English translation St. Petersburg Math. J. 5(4)
(1994), 663-717, was identified through
[MathNet](https://www.mathnet.ru/eng/aa397). Its PDF initially exposed front
matter, but attempts to retrieve the theorem/proof pages timed out; the
author's PostScript endpoint was unsupported. Thus the original theorem and
proof were not inspected. The statement reproduced by Friedland-Yomdin does
not count as an inspection of that original proof. Further access attempts
are parked; the proposed exact-algebra test does not rely on it.

Cheer-Goldston (1996) was an abstract/introduction lead; its AMS PDF returned
403. Andersson, arXiv:math/0607238v2, pp.1-3, was screened for primary
theorem scope: its explicit minimax results use unit/exterior nodes and
prime-power hypotheses and are not replacements for this family. Neither
paper is an essential dependency. The rational Remez/Bernstein search
returned derivative inequalities, not an inspected matching lower bound.
The inverse-Hankel and scalar Hardy-mean leads are not imported. Their
unread status does not block a test using only Biro and the ready local
Fourier/residue inputs. Any later reliance requires its own source review.

Full matching Mathlib coverage for either source theorem or the proposed
exact transfer has not been checked. The earlier assessment's supporting
Fourier coverage is reused; unknown coverage is not absence.

### Continuation and abandonment test

Coverage permits one exact Newton-Girard/pure-power transfer attempt for
the covered target above. Continue if it produces a uniform complete-sum
transfer at squared rate at most 1/16 (including any polynomial losses),
or a precise intermediate identity with a bounded, independently testable
remaining cost. Abandon this mechanism if its exact inverse-transfer cost
is proved to miss that threshold, or if it reduces only to the already
stopped prefix/termwise replacement. An unevaluated formal representation
or failed search is not an informative negative bound. A genuinely new
unassessed analytic theorem requires another source gate.

Essential starting inputs are C645g's spaces and C645o's complete signed
identity. Biro is available only for genuine pure sums satisfying his
anchor hypothesis. The exact representation, transfer, uniform constants,
and all Xi-realization/sign steps remain unresolved. Newly completed ready
coverage is saved for the separate next invocation; no mathematical attempt
on it occurs in this turn.
