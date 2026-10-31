# Saturation: global polynomial approximation feasibility

TARGET: Test whether, for some fixed A>=0, real polynomials p_T of degree d_T can satisfy sup_{0<=x<=B_T}|p_T(x)-x/((log T)^A+x)|<=1/8 and J_T log(2J_T)=o(T) along an unbounded sequence, where N=floor(T^(1/24)), M=floor(sqrt(T/(2pi))), B_T=(sum_{n<=N}n^(-1/2))^6 and J_T=M N^(3d_T).
CHECKED: 2026-10-29
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact bounded/rational resonator searches and a stronger-result search for best uniform approximation of reciprocals; inspected Kraus--Vassilevski--Zikatanov v3 Theorem 2.1 and Appendix A, plus the classical Markov statement. Reused the completed bounded-correlation review and L481's primary mean-square/saddle comparison. Targeted local uniform-polynomial/Markov searches found no completed duplicate of this implementation test.
SOURCE_EVIDENCE: Kraus--Vassilevski--Zikatanov arXiv:1002.1859v3, Section 2/(2.1)--(2.3), Theorem 2.1 p. 3, degree-zero case p. 4 and Appendix A pp. 20--22; Shadrin author-hosted draft Section 1.1/(1.1), PDF pp. 1--2; Heap--Soundararajan 2007.13154v1 Section 5/(14), reused as L481 (3)--(4). Direct URLs and qualifications are below.
COMPARISON: Best reciprocal approximation and Markov's inequality are known results; the proposed change of interval/normalization and comparison with the explicitly defined formal product-length budget are routine specializations. No signed saturation theorem is available from these citations. This test concerns approximation over a deterministic envelope, not the smaller set of amplitudes actually visited on [T,2T].
GAP: Establish the correct degree requirement with all constants needed for tolerance 1/8, justify the envelope and the stated budget's relation to L481's finite-polynomial interface, and decide simultaneous feasibility for each fixed A. No specialized bound or feasibility conclusion has been derived. No exceptional-set, coefficient-norm or full correlation theorem is approved by this assessment.
REASON: Essential source coverage is complete for one deterministic implementation test. Import the known approximation result or Markov inequality rather than reprove it; only specialize and compare lengths. The newly written ready assessment requires separate next-turn approval. This is established-method calculation, not a new central sign mechanism or proof of RH.
SCOPE: Fixed A>=0; arbitrary real T tending to infinity along a sequence; d_T nonnegative integer; real coefficients allowed to depend on T without positivity assumptions; the entire interval [0,B_T]; the stated formal budget only. No RH, independent phases, Haar replacement, coefficient cancellation or weighted-tail disposal.

## Relevance and precise bounded test

The main gap remains actual-Xi all-degree positivity. The intermediate
obligation is a necessary feasibility check for one implementation of
the bounded dual certificate proposed in the completed
[source review](2026-10-29-bounded-short-resonator-dual-correlation.md).
An eventual o(1) uniform approximation would in particular have to
meet the fixed tolerance 1/8. This tolerance alone is not asserted
sufficient for any positive residual correlation.

B_T specifies a triangle-inequality envelope for |F_T|^6, not its
actual finite-height range. J_T is a proposed ungrouped one-sided
product-length budget for applying the retained finite mean-square
method after polynomial substitution. Check that interpretation rather
than treating it as a universal necessary condition for all methods.
In particular, J_T log(2J_T)=o(T) controls only the relative length
factor in the cited mean-square estimate, not all coefficient norms
or the full signed approximation error.

## Known results to import, not reproduce

**Kraus--Vassilevski--Zikatanov, _Polynomial of best uniform
approximation to x^(-1) and smoothing in two-level methods_,
arXiv:1002.1859v3, 23 May 2012.**
[Primary version](https://arxiv.org/pdf/1002.1859v3#page=3).
Section 2 assumes 0<lambda_min<lambda_max<infinity and maps that
interval affinely to [-1,1]. Theorem 2.1: for a>1, integer m>=1,
the best degree-at-most-m uniform approximation error to 1/(t+a)
on [-1,1] is delta^m/(a^2-1), delta=a-sqrt(a^2-1).
Read (2.1)--(2.3), the full theorem, the separate degree-zero case
in Theorem 2.3's proof, and Appendix A's reflection/equivalent-form
argument from Meinardus (1967), p. 33, (4.25). This is a classical
optimal-approximation theorem, not a new resonator bound. The appendix
is a derivation from that prior result, not a fresh proof of its
optimality. Its application here must check scaling, constant shifts,
degree zero, growing degree and the allowed T-dependent parameters.
No specialization to our saturation has been performed in this turn.

**Markov's classical inequality.**
[Shadrin, _Twelve Proofs of the Markov Inequality_, author-hosted
undated draft, Section 1.1/(1.1), PDF pp. 1--2](https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/markov.pdf#page=1):
for real p of degree at most d, ||p'||_[-1,1]<=d^2||p||_[-1,1].
This may supply a simpler sufficient obstruction instead of evaluating
the exact optimal error. If that bound decides the test, there is no
need to reprove the stronger optimal theorem. Affine interval scaling
and the ordinary mean-value theorem are the allowed elementary tools.

**Finite-height method, retained scope.**
[Heap--Soundararajan v1, p. 9/(14)](https://arxiv.org/pdf/2007.13154v1#page=9)
for arbitrary finite coefficients z_j and length J gives the integral
on [T,2T] as (T+O(J log J)) sum |z_j|^2. L481 (3)--(4) retains
the small-J qualification and bilinear form; its Sections 2 and 4
retain the complete chirped term and endpoints. The new degree budget
is to be justified, not imported as an established L481 conclusion.

## Continuation/abandonment criterion and remaining obligations

Decide whether uniform approximation and the formal length budget can
coexist. A rigorous incompatibility stops only this global-envelope
polynomial implementation. It would leave the actual saturation
correlation, approximation on measured ranges, nonpolynomial methods,
and even L477's L1 defect threshold unresolved. Do not claim failure
for any of those from failure on the larger deterministic interval.

If feasible, report the actual degree, interval and complete error
requirements before proposing signed polynomial evaluation: both U
and Re(exp(2i theta)V), coefficient-dependent errors and endpoint
kernels must still be controlled. Do not infer positivity from
component signs or use L477's unweighted transfer with an unbounded
polynomial. If infeasible, preserve the obstruction and require a
materially changed implementation before repeating the test.

One bounded analytic calculation is sufficient; no numerical search
or mathematical script is needed. Any new lemma must state the
implementation's exact hypotheses and Mathlib status; no new lemma is
required merely to record a known approximation obstruction.

Mathlib: full matching approximation/length compatibility was not
checked; supporting standard inequalities may exist. No absence claim.
Expected classification is REPRODUCTION under SPECIALIZE. Creative
central-gap proof work remains blocked by the missing actual-height
joint signed input, so this calculation must not be labeled creative.
