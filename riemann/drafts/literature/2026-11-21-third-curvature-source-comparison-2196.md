# Third spatial curvature: completed source comparison2196

21 November2026. Literature only; no derivative computation, sign test,
new lemma or mathematical script. Main gap: L030-L032/C032a actual-Xi
all-degree algebraic mixed positivity. The intermediate question was
whether the proposed third spatial curvature has a source-backed
coefficient consequence beyond the recorded double-Turan conclusion.
That would justify testing it while leaving mixed signs, height,
initialization and actual-Xi realization unresolved. The nomination's
acceptance test fails: the essential iteration source concerns another
operator and supplies no such consequence. Park this proposed calculation.
This is a new source-scope finding, not a disproof of the inequality.

## Primary iteration source and exact hypotheses

Thomas Craven and George Csordas, *Iterated Laguerre and Turan
inequalities*, JIPAM **3**(3), article39 (2002), 18-page author version,
[primary PDF](https://math.hawaii.edu/~tom/mathfiles/iteratedLT.pdf).
Read Definition3.1 and Remarks(a)-(e), printed pp6-7; Proposition3.4
with its complete induction, linear-factor and endpoint cases, pp7-8;
the polynomial-approximation paragraph and Theorem3.5, pp8-9;
Corollary3.6 and Section4 through Theorem4.1's necessity/sufficiency
proof and Corollary4.2, pp9-11; Section5's definitions, Proposition5.1
and Remarks5.2, pp11-13; Lemmas5.3-5.4, Theorem5.5 and its complete
zero-at-origin/nonzero-at-origin/approximation proof cases, and
Remark5.6(a), pp13-16. The printed algebra was read for applicability,
not independently reproduced or certified. No claim in these sections
is installed as a new notebook theorem.

Definition3.1 sets, with derivatives in x,

    T_k^(1)(phi)=(phi^(k))^2-phi^(k-1)phi^(k+1), k>=1,
    T_k^(n)(phi)=(T_k^(n-1)(phi))^2
                  -T_(k-1)^(n-1)(phi)T_(k+1)^(n-1)(phi), k>=n.

This iterates a difference operation in the derivative index k.
The target instead differentiates each newly produced spatial function:
f_0(t)=K(sqrt(t)), f_(j+1)=f_j'^2-f_j f_j''. In particular the target
is f_3>0 on t>0, not the paper's T_k^(3)>=0. Only the initial
first-Laguerre expression is shared by the definitions. No commutation
of differentiation with nonlinear iteration is asserted. As an explicit
interface, the paper itself writes, in Proposition3.4's proof, p8,
for h=g'^2-gg'',

    g'' T_1^(1)(h)=g T_2^(2)(g).

This is a cited identity, not a derivation here. Even that interface
contains extra factors and concerns the second level; it is not an
all-iteration identification for arbitrary spatial kernels.

Theorem3.5 assumes phi is a real entire member of LP+, meaning LP
membership together with nonnegative Taylor coefficients. It gives
T_k^(2)(phi^(j))(x)>=0 for x>=0, k>=2 and integers j>=0. Its proof
uses polynomials with nonpositive real zeros, derivative closure and
compact convergence. The polynomial induction uses those zero locations
and nonnegative derivative factors; it is not a theorem for a positive
smooth density. Remark(c) after Definition3.1 exhibits failure of the second
index iterate for an LP polynomial lacking the additional LP+ premise.
Neither LP+ membership nor its coefficient hypotheses have been
established for f_0, f_1 or f_2 here. LP membership of Xi would itself
be an impermissible way to acquire the missing signs.

Theorem4.1 concerns a positive sequence gamma with a uniform factor
bound gamma_k^2>=c gamma_(k-1)gamma_(k+1), c>=1. For d>=0 its
stated sharp threshold for propagation with factor c+d is
c>=(3+sqrt(5+4d))/2. The proof estimates neighboring entries of a
sequence, not derivatives of a spatial function or theta integrals.
No such uniform strengthened premise for the required local sequence
is supplied by this theorem. Corollary4.2 stays in that sequence setting.
No new application or verification of its printed constants is made.

Theorem5.5, as printed on p15, assumes psi in LP+ and phi=x^2 psi.
Writing psi=sum alpha_k x^k/k!, its coefficient convention is
gamma_0=gamma_1=0 and gamma_k=k(k-1)alpha_(k-2) for k>=2.
Its displayed conclusion is gamma_3^(3)>=0 at x=0. This is the precise
stated conclusion used for scope comparison, rather than extending the
introduction's broader description to all indices or all x. The proof
passes to real-nonpositive-root polynomials and separately treats
psi(0)=0 and psi(0)!=0; in the latter case its positive reciprocal-root
power sums are essential. The factor x^2 changes the coefficient
problem. Remark5.6(a)'s hoped-for removal of that restriction is not a
proved theorem in this source. Nothing supplies the proposed f_3 sign
or a coefficient consequence of that sign for Xi.

## Actual coordinate, strongest relevant conclusion and overlap

Read canonical L019/L021/L030 contracts and proofs. L019 is the full
positive theta kernel, L021 gives its even moments, and L030's square
is algebraic. No truncation, absolute square or model realization
replaces those objects. The formula comparison K(u)=4 Phi(u/2),
already recorded in the September assessment and in
`2026-10-31-actual-theta-quartic-residual-scope.md`, matches
Planat-Sole's displayed (1.1). Thus the squared spatial coordinates
are related by t/4, rather than being spectral differentiation
coordinates. No derivative-scaling calculation is needed or performed:
the cited iteration theorem fails its operator/premise test before
any prospective specialization.

Reuse comparison558 and discovery2195's qualifications for
Planat-Sole, *Second-Level Concavity of the Riemann Xi Kernel*,
[2608.19160v1](https://arxiv.org/html/2608.19160v1). Reopened only
the displayed kernel and Theorem1.1 for normalization and Section7
for the claimed consequence. That source claims strict log-concavity
of s'^2-ss'', where s(t)=Phi(sqrt(t)), and the resulting double-Turan
coefficient inequalities. It does not assert log-concavity of the next
spatial iterate or an all-level transfer theorem. Its certificates
were not replayed, and the existing audit qualifications remain.

The source search also returned Sra's order-four reverse regularity.
Reuse the complete October31 assessment named above: its primary
Theorems1.1/1.4 and complete Fourier proof were already inspected.
Finite spatial Wronskians and integrated Fourier determinants do not
supply the missing pointwise spectral sign. The known fifth-order
failure is retained at its exact scope; it is not asserted to refute
f_3. Do not reopen that stopped direct localization inference.

Kawano, *Logarithmic Inequalities of Arbitrary Order for the Riemann
Xi Coefficients*, [202611.0383v1](https://www.preprints.org/manuscript/202611.0383),
posted4 November2026, was inspected only at Theorems1.1-1.2 and the
coefficient convention, Introduction and Section2 opening. It explicitly
concerns linear differences of log coefficients, not nonlinear spatial
iteration. Its analytic inversion/certification proofs were NOT read
here; its claims are not imported. A local exact-title/URL/author search
located extensive existing Mellin coverage, so this is no new source
mechanism nomination. Liu-Mao's coefficient-iteration paper remains a
search lead here, not inspected proof evidence for the spatial claim.

Reused the ready Section2 downward-order assessment of31October rather
than rebrowsing it. It concerns generalized Laguerre coefficients,
another distinct operator. Read C055a's hypotheses, conclusion and
source application; it obstructs automatic real-zero transfer from
second-level shape for its comparison family only. Read L772's contract:
infinite coefficient-iteration signs do not force its specified order-five
Toeplitz sign; no actual-theta realization is claimed. Neither result
refutes the proposed actual f_3 inequality. Stops1290/1843/2141/2144
were read at their precise WHY IT FAILS contracts and remain preserved.

## Search evidence, decision and next scope

Queries used: `"iterated Laguerre" "log concavity" theta kernel`;
`"Riemann" "third-level" concavity`; `"K" "sqrt" "Laguerre"
"Csordas" iterated`; `"Riemann" "third" "concavity" "kernel"`;
`"squared" "kernel" "iterated Laguerre"`; `"Laguerre" "f'"
"iteration" Craven Csordas log concavity`; `"s'(t)^2" "third"
"kernel" Laguerre`; `"iterated log-concavity" "continuous"
"Riemann"`; `"third-level concavity" theta`. Local searches targeted
the named iteration/curvature assessments and failure files. Search
failure is not evidence of novelty or a proof of nonexistence.

Decision: the exact third-curvature question remains unanswered as a
sign theorem, but its proposed downstream rationale fails this bounded
source test. Park the calculation without asserting a mathematical
counterexample or global impossibility. New evidence is the inspected
operator, LP+ and double-zero mismatch, not a repetition of C055a.
No bound toward L030 is obtained. Mathlib matching is unchecked;
unknown coverage is not absence. No cross-notebook input is used.

No justified creative mechanism survives this review. The next source
question must seek an independent signed spectral remainder rather than
another spatial curvature level. No source access blocker persists.
The sampled L727/C919g/C759n audit candidates are already audited in
their canonical records (226/2173/854); stale PROOF labels do not
authorize repeating them. No proof overview or DAG change is needed.
