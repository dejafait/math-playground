# Newly activated prime: logarithmic collar allocation — review1141

TARGET: Assess whether the newly activated n=97 term under dilation from radius 9/4 to log(101)/2 admits an absolute bound by one eighth of the fixed logarithmic reference energy on the entire complex form domain.
CHECKED: 2026-11-16
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1141 searched logarithmic boundary Hardy/explicit constants, logarithmic Fourier small-set concentration, Beckner/Pitt uncertainty, sharp interval variants, and exact97/correlation/logarithmic combinations; compared the inspected primary statements below and local cusp/nodal/half-Beckner stops. No exact one-eighth theorem or recorded duplicate was located in this bounded search; no novelty inference.
SOURCE_EVIDENCE: Reused1131/1134 and C750f/C750g; read paper162/v1(2) and Section2's34-active-term statement; Laptev-Weth revised2020(1.2), Corollary2.4/proof and dimension-one discussion; Dyda-Jarohs-Sk2411.11181v3 Theorem1.2, Theorem5.1 hypotheses/proof, Remark5.2, Proposition5.3/proof, Corollaries5.4/5.10 and their proofs; Beckner math/0612486v2 Corollaries1-2/(9)-(10), Fourier convention and differentiation justification.
COMPARISON: Boundary Hardy gives domain-dependent constants and an additive norm term; its explicit half-space constants are available but are not a proved J-allocation. Beckner supplies an explicit one-center logarithmic uncertainty estimate, not a two-collar overlap bound. Laptev-Weth admits interval characteristic functions, supporting an effective real-pulse falsification test of the all-complex claim. None of these sources signs the fixed allocation.
GAP: No full-domain bound or violating witness is established. Next quantify the exact97 correlation and full-frequency J for the single prescribed endpoint-pulse pair below; source coverage suffices for that bounded necessary test, not for assuming a sharp Hardy constant or generalizing passing samples.
REASON: Essential theorem-level comparison for this bounded test is complete. Investigate the fixed threshold once by an admissible explicit witness calculation, without a spectral floor or eigenvector premise; no source theorem is reproved. Separate approval of this newly ready continuation belongs to the next turn.
SCOPE: Exact fixed-endpoint allocation on the stated complex domain, with no derivative, nullvector, neutrality, parity or positivity premise. Ready mathematical scope is the one real endpoint-pulse test below, including domain, exact activation/overlap, rigorous full-frequency integral and tail bounds. A full-domain proof by additional unassessed machinery requires separate coverage; no mathematics was performed in this literature turn.

Main gap: L030-L032/C032a actual-Xi all-degree positivity. The proposed
intermediate target prices one activation in a support comparison.
Its possible downstream use is one term of a later complete budget;
it cannot itself extend positivity or imply RH.

Set a0=9/4, b=log(101)/2, and let f be a complex L2 function on
(-a0,a0), extended by zero, with

    J[f]=(1/(2pi))*integral_R log(2+|t|)*|F_f(t)|² dt < infinity,
    F_f(t)=integral_R f(x)*exp(-itx) dx,
    (U_b f)(x)=sqrt(a0/b)*f(a0*x/b),
    C_g(s)=integral_R g(x+s)*conj(g(x)) dx.

The proposed allocation, not a derived inequality, is

    (2log(97)/sqrt(97))*|C_(U_b f)(log(97))| <= J[f]/8

for every such f. The constant1/8 is an explicit resource-allocation
test, not a claimed optimal constant or a full-form positivity margin.
Use the coefficient from paper162(2); verify which prime powers newly
activate and the exact overlap at both endpoints before any estimate.
The baseline's other terms must not be silently charged to J.

Continue only if an applicable effective theorem supports a bounded
proof-or-counterexample attempt at this fixed threshold. A subsequent
attempt may prove the inequality on the entire stated domain or give
a rigorously admissible witness violating it. An unknown constant,
eigenvector-only asymptotic, finite passing sample or qualitative
compactness does not decide it. If the allocation fails, preserve the
witness and park this allocation; do not just enlarge the denominator.

Relevant contrasts: L523 and its October30 nodal stop; the October30
prime-shift cusp coverage; C750g's separate-channel stop. They are not
global bans. Essential local inputs are C750f/C750g for conventions,
not their sign conclusion. Effective boundary concentration, complex
scope and any required closure argument remain unresolved. All
old-shift defects, digamma/pole changes, both-sector complete budgets,
comparison of J with the baseline energy and actual-Xi realization
remain independent gaps. Mathlib matching coverage is unchecked;
no cross-notebook input or new mathematical result is claimed.

## Completed source comparison1141 — 16 November2026

The nomination above is preserved as the unproved research target.
This review produces no allocation estimate, numerical evaluation,
new lemma, or change to the main argument.

### Primary hypotheses and applicability

* [bramble_trace, paper162/v1](https://rstation.ai/problems/riemann_hypothesis/papers/162),
  15November2026, Section2(2), uses exactly -2Lambda(n)/sqrt(n)
  times Re C_f(log n). Its paragraph after(12) states that all34
  active prime powers through89 occur at radius9/4. C750g's explicit
  list at log(101)/2 adds97 and excludes the zero-overlap101 endpoint.
  This is the source/list comparison, not an independent arithmetic
  certificate. Check the exact support inequalities before any later
  calculation. The absolute allocation keeps the entire coefficient;
  a signed real-part estimate would not by itself suffice. Reuse the
  C750f normalization/domain audit and external-certificate limits.

* Ari Laptev and Tobias Weth, *Spectral properties of the logarithmic
  Laplacian*, [revised2020 author PDF](https://www.ma.imperial.ac.uk/~alaptev/Papers/laptev-weth-2020-revised.pdf),
  (1.2), p2, Lemma2.2 and Corollary2.4/proof, pp4-5. For a bounded
  Lipschitz open set, the logarithmic Fourier closure equals the
  zero-extension L2 class with finite truncated difference energy;
  it contains the set's characteristic function. The proof uses
  smooth-core density and equivalent norms. Section4's dimension-one
  discussion, p11, confirms that the abstract's d>=2 emphasis is not
  a ban on these domain statements. This covers interval-pulse test
  functions, not their Rayleigh quotients. Their norm uses log(e+|t|);
  compatibility with J and finite unions/linear combinations must be
  made explicit when importing it. No new domain proof is attempted.

* Bartlomiej Dyda, Sven Jarohs and Firoj Sk, *The Dirichlet problem
  for the logarithmic p-Laplacian*, [arXiv:2411.11181v3](https://arxiv.org/html/2411.11181v3),
  3July2025, Theorem1.2/(5.1): on a bounded Lipschitz set, for
  1<=p<infinity, the boundary-weighted integral
  integral |u|^p log^+(1/dist(x,boundary)) is bounded by a constant
  times the regional |x-y|^(-N) difference energy plus ||u||_p^p.
  Theorem5.1 tracks Whitney-scale/repetition constants; its proof
  retains the norm term. Remark5.2 changes the terminal scale.
  Proposition5.3 and Corollary5.4 give explicit half-space constants,
  including c1(2,1)<6 and c2(2,1)<5; their proof checks scale and
  multiplicity. Corollary5.10 covers Lipschitz sets qualitatively.
  These statements concern the indicated regional energy, not J.
  A complex p=2 application needs the real/imaginary decomposition;
  a half-line application needs zero extension and both endpoints.
  No fixed-interval J constant or one-eighth conclusion is imported.

* William Beckner, *Pitt's inequality with sharp convolution
  estimates*, [arXiv:math/0612486v2](https://arxiv.org/pdf/math/0612486),
  Corollary2/(10), p3, with Corollary1/(9), p2, and Fourier convention
  p1. For Schwartz functions and 1<p<infinity, it gives a logarithmic
  uncertainty lower bound with explicit constant
  D=log2+[psi(n/(2p))+psi(n/(2p'))]/2. The proof differentiates(9)
  where its constant is1 and equality holds at exponent0. At p=2
  the operator is log(sqrt(-Delta)); this is not a two-boundary
  concentration theorem. L746(4) already records the n=1 angular
  normalization. No new conversion or extension to nonsmooth pulses
  is credited here; use the domain source and Plancherel directly
  for their J instead. A sharp one-center constant alone is not the
  proposed allocation.

The AMS1995 primary PDF URL returned403; the accessible later Beckner
paper suffices for the comparison. The retrieved1710.03416v4 HTML
did not expose the searched Hardy appendix; that appendix remains an
unread lead and is not needed after the explicit2025 comparison.
Search hits about positive-order Hardy/logarithmic corrections were
not treated as theorems about a zero-order multiplier. No essential
source blocker remains for the bounded test below. Full matching
Mathlib coverage was not checked; standard Plancherel, translations,
Cauchy--Schwarz and nonnegative-integral arguments are supporting
inputs, not a claim of formal verification.

### Duplicates, failures and decision

Reused the October30 prime-shift-cusp and L523-audit assessments,
and read ATTEMPTS/2026-10-30-weil-nodal-compression-slope-gap.md.
Their conditional eigenvector/slope obligations do not imply this
absolute full-domain estimate. C750g's separate-channel triangle
budget fails for another resource and quantity. L746's Hypotheses,
Conclusion and normalization show that its counterexample uses the
Beckner remainder; L748's corresponding statements add a spatial
compensation. Neither denominator equals J. These stops remain
evidence against their own mechanisms; they do not settle97/8.
Assessment1139's unpaid complete-dilation budget stays parked.

The bounded search found no directly matching overlap theorem.
That is an EXPLORE decision, not a novelty claim or a proof that
all effective bounds fail. The explicit Hardy estimates support
quantitative work but do not supply the requested constant for free.
Use a necessary witness test before attempting further upper budgets.

### Ready bounded continuation, awaiting separate approval

Keep the exact TARGET and the fixed one-eighth threshold. Proposed
test only, not a computed witness: set r=(a0/b)log97 and w=2a0-r,
and take the real function

    f=1_(-a0,-a0+w)+1_(a0-w,a0),

zero extended. First verify 0<w<a0, activation cutoffs, dilation and
the exact correlation from interval intersections. Import interval
membership from Corollary2.4 with its norm comparison, or directly
verify this particular Fourier integral is finite. Evaluate the full
J of this single pair with a rigorous integration/tail enclosure;
keep its interference term. Elementary Fourier integration of the
specified indicator and Plancherel need no new uncertainty theorem.
Do not use a Fourier cutoff value as J or subtract a missing tail.

A certified strict ratio (2log97/sqrt97)|C_(U_b f)(log97)|/J[f]>1/8
would refute this allocation on its stated domain, since a real test
is allowed in the complex claim. Preserve that witness and park the
allocation without retuning its fraction. A ratio at most1/8 or an
enclosure straddling1/8 is inconclusive for the uniform claim: stop
this single-pair test and record its exact information, with no
unbounded width optimization. A uniform proof still requires all
complex tests and a justified closure argument. No value, sign or
success for the proposed test is asserted in this literature turn.

This is routine source-based calculation scope, not a protected
creative mechanism for the central RH gap. No justified new central
mechanism emerged from this review. The independent full-budget,
J-to-baseline comparison, all-support sign and actual-Xi realization
gaps remain; no cross-notebook theorem is used.
