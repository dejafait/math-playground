# Source comparison: angular Gram bound with the actual pole residues

TARGET: Assess whether known Gram-matrix results cover E_0/D>=c^2*n^2*exp(-n/16) for the fixed L703 family while retaining its exact signed pole residues.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 211 reused the Moitra/Danchenko--Semin readings and searched Hardy/Szego Gram conditioning, prescribed-residue rational norms and Takenaka--Malmquist orthogonalization. Inspected the primary statements below and scoped local stops, including common-sign and bulk-pairing failures. No inspected theorem bounds the actual signed vector at TARGET; unsuccessful searches do not certify novelty.
SOURCE_EVIDENCE: Gorkin--McCarthy--Pott--Wick, arXiv:1404.3088v2 (5 July 2014), Section 2 Proposition 2.1/Theorem 2.2 and (2.1), Lemma 3.4 and Theorem 3.5 proof, printed pp.2--5; Heuberger--de Hoog--van den Hof--Wahlberg, SIAM J. Control Optim. 42 (2003), 1347--1373, notation p.1349 and Section 2.1 Proposition 2.1/(2.2), p.1350. Precise links, reading limits and applicability below; older sampling/Parseval readings reused.
COMPARISON: Interpolating-kernel Gram estimates require quantitative separation/interpolation constants and concern normalized kernel coefficients, not original D. Takenaka--Malmquist gives exact orthogonal coordinates without such separation, but no lower bound for the actual coordinates. L666 quadrature and L725 interior limsup still supply no angular coercivity; C645p's unaudited ambient evaluation cost is only a contrast.
GAP: Estimate the complete signed common-interior-pole principal part of c_0 relative to the original D, retaining its actual residue vector and all cross correlations. Neither a suitable interpolation constant, a favorable actual-vector energy rate nor the displayed E_0/D bound has been established.
REASON: Essential theorem-level comparison is complete for one bounded joint-residue energy attempt. No matching coercivity theorem was found; the new work would be the actual-vector estimate, not orthogonalization or Parseval. This new continuation scope needs separate next-turn approval; the completed L725 audit is preserved.
LITERATURE_REASON: The observable changes from a pointwise zero-moment limsup to its full angular signed-energy ratio, with actual interior-pole residue correlations as the proposed extra information; reuse the old sampling and pole-cost readings and investigate only this uncovered bridge.
SCOPE: Fixed original L703/L708 profile, n=12q+3, M=n/3, all unit original masses, anchor, j=0 factor, inverse angle, endpoints and moments; E_0 and D are exactly L666's normalized angular quantities. Seek a fixed c>0 along an unbounded subsequence, with no assumption of eventual nonvanishing, positive complex cross terms or Xi realization.
COVERED_TARGET: Test whether the complete negative-angular projection of c_0 for the fixed L703 family satisfies ||P_-c_0||_2^2/D>=c^2*n^2*exp(-n/16) along an unbounded subsequence.

## Relevance and bounded decision

The main gap remains actual-Xi all-degree mixed positivity. This proposed
intermediate test concerns the unpaid angular observation for the existing
finite family. L666 already explains how the displayed ratio would imply
H>=(log D)/2-n/32+log n+log c. That is only a conditional downstream
use: full support, Xi realization and signs would remain independent.

Essential local inputs are L666 (definitions and exact rational sampling),
L703/L708 (fixed actual profile), and newly audited L725 (interior rate).
C645p and the recorded angular stops are comparisons, not assumed
coercivity inputs. C645p's statement still carries an unaudited label;
any new mathematical use of its formulas must justify that interface.
No cross-notebook theorem is proposed.

The candidate idea is to use the actual joint pole residues of the signed
sum when examining its angular Gram form. It is not enough to bound each
residue separately, assume an arbitrary vector is admissible, clear poles
and pay their ambient evaluation cost, or infer positive cross terms from
positive quadrature weights. The source review must compare this proposed
information with the old sampling and Gram obstructions before deciding
whether there is a materially different mechanism. L725 supplies a new
exact constraint at u_*, but does not itself establish improved angular
conditioning or a quantitative norm ratio.

First reuse the precise theorem statements and comparisons in the older
sampling assessment. Search only the missing exact-residue/Gram interface
and its known obstructions. Continue only if the review identifies a
matching theorem or a concrete bounded specialization retaining original
D and all signed cross terms. Otherwise record the overlap or obstruction
and select an independently testable mechanism through bounded discovery;
do not rerun ambient pole-clearing or bounded-coefficient propagation.

The nomination above records the invocation-start gate. The completed
comparison follows. This turn derives no new norm identity, asymptotic,
inequality or lemma, and changes no mathematical script.

## Completed comparison — 3 November 2026, step 211

### Reuse, duplicates and failures

Read L666 Sections 1--4 for the exact rational product, original D and
zeroth energy, C645p Sections 1--3 for its actual projection convention
and ambient extremizer qualification, and L703/L708/L725 hypotheses
and conclusions for the fixed-profile and interior-rate scope. The
existing sampling assessment's primary statements and applicability
comparison are reused, without reopening their general proofs.

Moitra's Theorems 2.2--2.3 concern separated unit-circle exponential
columns; no exact representation with the requisite observation budget
for these rational W_a has been supplied. Danchenko--Semin Theorem 2
permits complex sums and gives exact positive observation weights, but
does not compare that sum to the diagonal of its summands. L666 already
specializes this theorem; repeating quadrature is not the missing step.

The low-moment origin closure repeats C645p's pole-clearing loss.
The bounded-coefficient angular stop discards the common algebraic
relations; it is not an admissible actual-residue counterexample.
The inner-annulus anchor and two-arc complement records do not pay the
unit-circle energy relative to D. L700's audited common-sign failure
and L701's audited single-bulk-pole pairing failure exclude those
sufficient mechanisms in their stated scopes, not a complete quadratic
form with mixed signs. They are contrasts, not additional assumptions.
No historical stop is treated as a global ban on joint residue analysis.

### Newly inspected primary statements and their limits

**Hardy Gram conditioning.** P. Gorkin, J. E. McCarthy, S. Pott and
B. D. Wick, *Thin sequences and the Gram matrix*,
[arXiv:1404.3088v2](https://arxiv.org/pdf/1404.3088v2), 5 July 2014,
Section 2, printed p.2: normalized Szego kernels at a Blaschke sequence
alpha_j; delta=inf_j product_(k!=j)|(alpha_j-alpha_k)/(1-conj(alpha_k)*alpha_j)|.
For an interpolating sequence, Proposition 2.1 bounds both Gram and
inverse norms by the square of the H-infinity interpolation constant.
Theorem 2.2 quotes Earl's bound M(delta)<=((1+sqrt(1-delta^2))/delta)^2.
Read these statements, inverse formula (2.1), Lemma 3.4/proof p.4,
and Theorem 3.5's proof pp.4--5: its thin-tail direction uses separation
constants tending to one. Earl's proof and the original Shapiro--Shields
proof are not independently audited or imported here. The paper's
diagonal matrix D is unrelated to notebook D. Neither finite
distinctness nor positivity of original spatial masses verifies the
needed quantitative constants or the conversion of coefficient norms
to notebook D. No quantitative separation failure is newly proved here;
these statements do not themselves settle the actual-vector target.

**Exact rational orthogonal coordinates.** P. S. C. Heuberger,
T. J. de Hoog, P. M. J. Van den Hof and B. Wahlberg,
*Orthonormal basis functions in time and frequency domain: Hambo
transform theory*, SIAM J. Control Optim. **42** (2003), 1347--1373,
DOI [10.1137/S0363012902405340](https://doi.org/10.1137/S0363012902405340),
[author PDF](https://publications.pvandenhof.nl/Paperfiles/SIAM2003.pdf),
notation p.1349 and Proposition 2.1, (2.1)--(2.2), p.1350.
For poles |xi_k|<1, listed with multiplicity, Gram--Schmidt on the
partial fractions gives

    Phi_k(z)=sqrt(1-|xi_k|^2)/(z-xi_k)
                         *product_(l<k)(1-conj(xi_l)*z)/(z-xi_l).

This is the source theorem's formula, not a new notebook identity.
Its space consists of exterior-analytic rational functions vanishing
at infinity, with normalized circle norm: negative angular modes here.
Finite orthogonality needs no uniform separation or infinite
completeness assertion. The source refers to residue calculus and
historical proofs, without displaying that proof. It supplies coordinates,
not a lower estimate for their actual coefficients or original D.

**Historical follow-through and access limits.** Followed the cited
Takenaka lead to S. Takenaka, *On the Orthogonal Functions and a New
Formula of Interpolation*, Japanese J. Math. **2** (1925), 129--145,
[publisher and PDF link](https://doi.org/10.4099/jjm1924.2.0_129).
The retrieved text exposed pp.129--137, primarily general extremal and
orthogonal-function statements; the later rational-system proof was
not inspected. A targeted later-range request timed out. It is an
unread historical proof lead, not an essential source blocker: the
explicit finite theorem in the 2003 source is the cited input. The
Washington University `wp/mccarthy/...CNPv2.pdf` search lead returned
404 and supplies no evidence. Chalendar--Fricain--Timotin (2003),
Section 2, was screened for conventions only; no result is imported.

The reusable Fourier/Parseval and orthogonal-projection source is
Levitt, *Analyse de Fourier et applications*, Theorem 1.3/Exercise 1.2
and Theorem 1.11/Corollary 1.12, printed pp.6,8, with its completeness
proof previously inspected in the rotation-averaged assessment. The
ordinary residue theorem and simple-pole rule are Howell--Mathews,
*Complex Analysis*, Section 8.1, Theorems 8.1.5/8.1.7, also already
inspected there. Cite these tools; do not reprove them as discoveries.
Full matching Mathlib coverage for the proposed energy estimate and
the rational basis is unchecked; supporting Hilbert-space tools are
not a full matching theorem.

### One bounded mathematical continuation after separate approval

The covered test above concerns P_-c_0, the strictly negative angular
Fourier projection in normalized L2. Use all common interior poles
p_j=t_j*x/U, and their **actual** scalar residues
rho_(j,n)=Res_(u=p_j)c_0(u), with zero for cancellations. These are not
the original spatial masses. The exact residue-vector norm, evaluated
in the source orthonormal coordinates, is the proposed mechanism;
no common sign, arbitrary admissible coefficient vector, polewise
absolute estimate or least-eigenvalue relaxation is authorized.

A later attempt must first justify the scalar projection interface
directly from L666's product and the cited residue/Fourier tools:
all exterior poles stay outside, common poles are simple, cancelled
poles contribute zero, and the holomorphic remainder and constant
mode must be accounted for. C645p's unaudited vector-valued statement
must not be silently imported. The finite basis theorem can then be
cited with these exact poles; no infinite basis theorem is needed.
Retain each signed sum before taking its norm. Computing coordinates
or restating the Gram matrix alone does not establish the target.

The discriminating mathematical task is to estimate the resulting
joint norm against the **unchanged original D** at the covered scale,
with fixed c>0 on one unbounded subsequence n=12q+3. Success would
give a sufficient route to the original E_0/D test by orthogonal
projection contraction, then the existing L666 H bridge. Its new
content would be this quantitative actual-vector estimate, not the
standard contraction or basis theorem. L725 supplies no projection
coefficient at the unit circle and does not certify this estimate.
Independent angular/global charge, H/support, realization and signs
remain open even after a successful test.

Continue only with that bound or a paid intermediate estimate that
specifies the remaining exponential loss. A rigorously inadequate
projection ratio would stop this sufficient subtest, not E_0/D or RH;
a finite numerical dip would not. If one attempt yields only the
ambient evaluation loss, unevaluated coordinates or uncontrolled
absolute sums, save its partial reasoning and stop this mechanism
pending a materially new estimate. No new result is approved in this
literature-only turn. This newly written ready scope is to receive
separate supervisor approval before invocation.

### Executed search record

Queries: `Hardy space reproducing kernels Gram matrix interpolating
sequence product pseudohyperbolic separation Riesz sequence theorem`;
`rational functions prescribed residues lower bound L2 norm Cauchy Gram
matrix common poles cancellation`; `Takenaka Malmquist system rational
functions orthonormal basis formula proof pdf residues`; `Gorkin
McCarthy Pott Wick Thin sequences Gram matrix norm Earl 2014 pdf`;
`"rational" "prescribed residues" "Gram" "lower bound"`;
`"Takenaka" "residues" "norm" "cancellation"`.
The last two returned no usable primary theorem. The first four located
the inspected sources above. Abstracts and search snippets served only
to locate sources. This bounded review does not establish novelty or
the absence of a stronger theorem elsewhere.
