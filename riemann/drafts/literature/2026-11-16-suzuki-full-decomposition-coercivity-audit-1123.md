# Suzuki full decomposition and coercivity — audit coverage1123

TARGET: Audit Suzuki's full three-term decomposition and small-window coercivity for arbitrary complex L2 tests using C618a and consistently defined contour and gamma constants.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse completed comparison1122/step1123, assessment1121 and the November1 screw screen. Exact erratum, article-title/correction and C0/gamma searches found no inspected correction; no originality inference is drawn. Local C618a covers the two form bounds; the parameter-family and square-order records are distinct stops, not duplicate full-decomposition audits.
SOURCE_EVIDENCE: Suzuki, Aspects of the screw function corresponding to the Riemann zeta-function, JLMS108(2023),1448-1487, DOI10.1112/jlms.12785; controlling arXiv2206.03682v4 PDF internal31May2023, Section2.1/(2.1)-(2.5), p6, Theorem4.2/(4.2)-(4.11), pp12-15. Complete relevant source proof cases and HTML conjugations compared in1123. NIST DLMF5.2(i)/(5.2.2),5.11(i)/(5.11.2) inspected. C618a's full proof read; its Tao Plancherel citation is reused.
COMPARISON: The source claims positive definiteness for all nonzero complex L2 tests on sufficiently small windows; this is known mathematics. A full local audit is justified because its printed contour-line constant, later gamma normalization, lower-band convention and inequality direction need reconciliation. C618a supplies the shifted-form and low-frequency bounds but not the three-term identity or their assembly.
GAP: Verify the source identity, domain/integrability cases and corrected constant bookkeeping, or identify an exact unresolved step or rigorous counterexample. Establishing these claims would be reproduction of the cited local theorem, not a new arithmetic sign theorem, effective onset or RH advance beyond the sources.
REASON: Specific suspect source passages and arbitrary-complex-test applicability justify a bounded reproof. All essential source statements are accessible in the controlling PDF; publisher comparison timeout does not block this audit. No additional discovery or repeated general literature screen is needed for this exact scope.
SCOPE: One conceptual audit of Theorem4.2's complete decomposition and existential small-window coercivity on complex L2(-a,a); use C618a without reproving it. Excludes Theorem4.3 Fourier tails, numeric onset, all-support positivity, removed-zero tails, parameter descent and Xi/common-graph realization. Proposed completed classification REPRODUCTION.

## Exact object and source inputs

Use the source's g=-Psi and G_g(t,u)=g(t-u)-g(t)-g(-u)+g(0),
with form integral G_g(t,u)phi(u)conjugate(phi(t))du dt on
[-a,a]^2. Phi(phi,z)=(hat(phi)(z)-hat(phi)(0))/z has the
removable value and positive-exponent transform in C618a.
Do not impose mean zero, parity, reality or extra smoothness.

Controlling source: [Suzuki v4 PDF](https://arxiv.org/pdf/2206.03682v4),
with [HTML conjugations](https://arxiv.org/html/2206.03682v4#S4.SS3).
The PDF numbering/date controls. The exact comparison and primary
transform cases are recorded in
[completed assessment1122](2026-11-16-suzuki-coercivity-source-scope-1122.md).
The asserted source decomposition is Q=I0+I1+Iinfinity, equations
(4.5)-(4.8); verify its identity, not merely a bound on an
unidentified form. Section2.1 supplies the three component transforms,
including the full digamma-series case, without assuming RH.

Import the standard digamma expansion
[NIST DLMF5.11.2](https://dlmf.nist.gov/5.11#E2) only in its stated
sector |arg(w)|<=pi-delta, fixed delta>0, as |w| tends to infinity.
[DLMF5.2(i),5.2.2](https://dlmf.nist.gov/5.2#E2) supplies the
gamma/psi pole and nonvanishing facts. These apply to the positive
real parts in the source contour strip; justify that specialization
and all remaining estimates rather than assume contour convergence
from pole-freeness alone. Standard Fourier inversion and Cauchy's
integral theorem may be used with their domains and limiting
hypotheses checked. C618a already contains the Plancherel convention
and primitive for non-mean-zero tests; its canonical proof must be
used rather than replaced by a pointwise kernel-order argument.

## One bounded audit and its obligations

Fix a1>0 and c>1; all constants must be independent of phi and
0<a<=a1, except the final threshold limiting a. The printed
constants are not automatically valid audit inputs. Required
conditions for replacement constants are:

- A finite multiplier bound M for both P(s)=1/(s-1)+1/s and
  Z(s)=zeta'(s)/zeta(s) on the actual line Re(s)=1/2+c.
  Check the absolute Dirichlet-series domain and use the absolute
  form estimates to obtain the direction needed in (4.11).
- The real-axis multiplier is exactly
  W(r)=Re[(1/2)psi(1/4-ir/2)-(1/2)log(pi)]. For the chosen
  positive tail level C, the threshold T must concern W itself.
- A nonnegative finite D must satisfy W(r)>=-D on |r|<=T.
  The printed maximum of a differently normalized expression
  is not an established substitute. Existence and sufficiency
  of the replacement choices remain proof obligations.

These conditions specify what to audit; no new bound or successful
choice of constants is asserted by this assessment. Audit the
pole/prime inversions for both spatial signs, the gamma contour
shift with all vertical edges and the removable point z=0,
absolute Fubini for the full complex L2 test class, and convergence
of the gamma-weighted real-axis integrals. If smooth approximation
is used, justify passage to the actual form and each integral.

Use C618a's C2=exp(2ca1) and C3=2T/pi for the two already
audited comparisons. Then check the source's lower-bound assembly
and small-a coefficient with the consistent constants. Do not
declare strict positivity until E0(phi)>0 for every nonzero phi
has also been justified. The desired conclusion is the source's
existential, uniform small-window coercivity relative to E0;
it is not a positive lower bound relative to the L2 norm of phi.

Continue if every identity and limit is justified and the resulting
coefficient is strictly positive on one uniform small-a interval.
Otherwise record the exact remaining assumption or a fully proved
violating test. A source-display mismatch or numerical sample is
not a counterexample to Theorem4.2. One bounded attempt precedes
reassessment; unchanged flags do not justify another literature turn.

## Relevance and limits

Main gap: L030/L032/C032a require actual-Xi all-degree signs.
This audit's plausible use is reliable analytic control for later
arithmetic/complement comparisons. It supplies no missing signed
prime mechanism, low-mode coupling or common-graph realization.
Only C618a is a local mathematical input; the main-gap IDs are
context, and the older source stops are contrasts. No cross-notebook
input is authorized. Matching Mathlib coverage remains unchecked;
no Lean verification is claimed. This is reproduction, not creative
work; no justified new central signed mechanism is currently nominated.

This ready continuation was written in step1123. The supervisor owns
its separate approval before mathematical invocation; no mathematics
on this extended scope was performed in the literature turn.
