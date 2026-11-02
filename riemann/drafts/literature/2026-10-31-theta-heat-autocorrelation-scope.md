# Theta-specific heat-equation/autocorrelation — completed source comparison

TARGET: Assess whether theta heat-equation integration by parts supplies a noncircular autocorrelation decomposition of the complete actual-theta first associated kernel, with all boundary and residual terms retained.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed exact-object/stronger-result searches and scoped local heat/modular/autocorrelation duplicate checks; read L019, L233, L239 and the named finite/parity/reflected stops. Reused the September 27 lattice assessment. No inspected theorem supplies the requested complete decomposition; this bounded finding makes no novelty claim. Queries and reading limits below.
SOURCE_EVIDENCE: NIST DLMF v1.2.8 (2026-09-15), 20.1, 20.2(i)-(ii), 20.7.32 and 20.13.1-2; exact domains, constants and principal square root inspected. Csordas arXiv:1309.0055v2, printed pp.11-13, Theorems 4.5-4.6/Open Problem 4.7 reused; newly compared (4.9)-(4.10) and Proposition 4.9 with the requested Jacobi heat mechanism.
COMPARISON: Jacobi heat differentiation uses elliptic z and lattice tau, whereas actual k varies tau=i exp(2u). The separate Xi heat deformation also gives no physical-space square decomposition. Neither inspected statement supplies a signed complete residual; modularity at z=0 does not grant the same decay to auxiliary z derivatives.
GAP: A noncircular complete decomposition and independent all-frequency compensation remain unavailable. Before proposing a square from the Jacobi heat derivative, one fixed full-line profile integrability test is justified; its answer and any corrected profile are unproved.
REASON: Finish the saved comparison without deriving an identity or asserting positivity. Nominate only the concrete source-covered integrability discriminator below; do not invoke an unspecified creative sign argument, repeat the theta grid, or infer factorization from the desired spectrum.
SCOPE: Completed literature comparison of one complete-kernel heat/IBP mechanism. Only supporting identities are available; no new sign lemma, source reproof, mathematical script or full-target theorem import.
LITERATURE_REASON: The invocation's target had REVIEW_REQUIRED coverage; the Jacobi heat-variable and modular derivative interface had not been assessed. Existing Fourier and lattice coverage does not cover it.

## Gap, target and decision test

The main gap is actual-Xi all-degree positivity at unbounded heights.
The reviewed intermediate target was a physical-space decomposition of
L233's complete A(t)=C_g(2t)+t^2 C_k(2t), g(u)=u k(u), into
ordinary autocorrelations plus an independently controlled residual.
It could address the first spectral sign; all higher signs remain
independent. No such identity was asserted or derived this turn.

Continue toward a sign argument only with an explicit complete identity
and an independent compensation threshold. In a proposed A=P+R with
nonnegative spectrum of P, the required bound is Rhat>=-Phat at every
frequency, including zeros of Phat. Abandon an implementation that just
renames the first-sign inequality or factorizes by assuming Ahat>=0.
No inspected source supplies this threshold. Thus an unspecified
creative identity attempt is not yet justified.

## Local comparison and prior failures

Read L019 and L233 in full and L239's complete relevant proof. L239's
strip evenness and decay concern actual one-variable k, not an elliptic
lift. Reused `2026-09-27-first-associated-theta-lattice.md` for its exact
addition, weighted Poisson and first-sign comparison. Read:

- ATTEMPTS/2026-09-23-first-associated-autocorrelation-test.md;
- ATTEMPTS/2026-10-03-complete-parity-positive-definiteness-test.md;
- ATTEMPTS/2026-10-31-associated-theta-reflected-majorant-bounded-test.md;
- ATTEMPTS/2026-10-31-real-zero-to-reflected-implication-stop.md.

These retain the signed generic remainder, modular cancellation between
parity blocks, stopped finite grid and audited L599 comparison. They
stop their stated implementations, not a different full-theta identity.
L599 is a contrast, not a premise for an actual-theta sign. No
cross-notebook input was read. No existing unfinished work was discarded.

The initial broad notebook search returned unrelated matches and was
truncated; subsequent searches were restricted to theta assessments,
attempts and exact lift terminology. No conclusion depends on omitted
preview content. Exact searches for theta_3/vartheta/theta3, Jacobi or
heat lift, auxiliary elliptic variable and elliptic derivative in those
records found no completed test of the next fixed profile. This is a
bounded duplicate check, not certified originality.

## Inspected source hypotheses

[DLMF 20.1](https://dlmf.nist.gov/20.1) fixes Im(tau)>0 and
q=exp(i pi tau). [20.2.3 and 20.2(ii)](https://dlmf.nist.gov/20.2)
give theta_3(z|tau)=1+2 sum_(n>=1) exp(i pi tau n^2) cos(2nz)
and entire dependence on z for fixed tau. These specify the lift's
normalization; they include no limiting assertion at tau=0.

[20.13.1-2](https://dlmf.nist.gov/20.13) give
partial_tau theta=-(i pi/4) partial_z^2 theta; with tau=i x,
x>0, the diffusion coefficient in x is pi/4. This relates two variables,
not a stated heat equation in logarithmic u. Periodicity is in z.
It supplies no associated-kernel Fourier sign.

[20.7.32](https://dlmf.nist.gov/20.7#E32) states, with
tau'=-1/tau and principal square roots,

(-i tau)^(1/2) theta_3(z|tau)
  = exp(i tau' z^2/pi) theta_3(z tau'|tau').

At tau=i exp(2u) it applies for every finite real u. Both the Gaussian
multiplier and transformed elliptic argument must be retained under
z differentiation. L239's cancellation at z=0 cannot be assigned to
these derivatives without checking them. No new derivative identity or
asymptotic coefficient is computed here. The singular endpoint
u -> -infinity is an outstanding integrability issue, not a boundary
value supplied by DLMF. Cite these formulas; no reproof is needed.

Csordas, [*Fourier transforms of positive definite kernels and the
Riemann xi-function*, v2, 21 February 2014](https://arxiv.org/pdf/1309.0055v2),
printed pp.12-13, (4.9)-(4.10), uses
H_lambda(x)=integral_0^infinity exp(lambda s^2) Phi(s) cos(xs) ds
and partial_lambda H_lambda=-partial_x^2 H_lambda. This parameter is
distinct from Jacobi lattice time. Proposition 4.9 concerns multiple
zeros relative to the transition constant, not a first-sign bound at
zero time. No de Bruijn/Newman theorem is imported; its upstream proofs
and historical numerical bounds are not inputs. The already assessed
Theorems 4.5-4.6 and Open Problem 4.7 give admissibility and the sign
interface, without the desired square decomposition. A dated open
problem is not evidence of current nonexistence of a theorem.

## Searches and reading limits

New external queries actually used:

- `"Riemann" "associated kernel" "heat"`;
- `theta heat equation Laguerre inequality autocorrelation integration by parts`;
- `site.dlmf.nist.gov theta heat equation modular transformation`;
- `"Riemann" "theta" "heat equation" "Laguerre" "kernel"`;
- `"associated kernel" "integration by parts" Riemann`;
- `"Riemann" "autocorrelation" theta heat`;
- `"Riemann" "Jacobi" "heat" "integration by parts" kernel`;
- `"theta" "associated kernel" autocorrelation heat equation`;
- `"theta" "modular" "second derivative" "20.7.32"`.

Results led to the exact DLMF formulas and the assessed Csordas source.
Uninspected repositories, discussion pages, proof claims, the Simo
Yomgni PDF and the adjacent 2026 theta-block paper remain leads only.
Their snippets are not evidence or essential inputs to the fixed DLMF
specialization. No inaccessible source is being treated as a theorem.
No further survey is needed for that narrowly defined test.

## Continuation and outcome

[The next assessment](2026-10-31-jacobi-heat-profile-integrability.md)
fixes one Jacobi heat derivative profile and tests its full-line L2
membership with every modular contribution retained. This can accept
or reject its use as an ordinary autocorrelation factor. Failure would
not exclude pairings with rapidly decreasing actual k, corrected lifts,
cancellations or the original sign. Success would not prove any sign.

EXPLORATION: an actionable source comparison, no new mathematical
obstruction or advance and no progress beyond checked sources.
Literature work does not spend/reset the mathematical exploration
budget. The main all-degree gap stays open. Creative sign work lacks
a specified independently controlled complete residual; this is not a
historical ban. Newly written continuation coverage requires separate
approval next turn. No lemma, script, DAG or PROOF change was made.

Mathlib: full decomposition and supporting Jacobi heat/modular derivative
coverage not checked; availability unknown. L599's periodization
support does not cover this interface.
