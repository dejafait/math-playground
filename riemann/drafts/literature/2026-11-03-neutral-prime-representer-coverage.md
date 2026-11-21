# Neutral prime representer: completed source coverage, step 235

TARGET: Assess paper 18/v3's identity Q(u)=⟨q,u⟩ for fixed neutral complex u, with q(y)=log(2pi)-{y}+(1/2)log(1-y^(-2)), including every contour boundary limit.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the existing neutral arithmetic/density and dyadic/sqrt(N) assessments for representer, contour, zero and q; they exclude this input. External exact-title and representer/fractional-log searches located paper 18 itself; standard-input searches located DLMF and Trudgian's primary strip argument. No priority claim follows.
SOURCE_EVIDENCE: Inspected paper 18, displayed v3, fixed-probe hypotheses and complete (21)--(28), plus DLMF 1.14.35, 25.5.5, 25.4.1--2, 25.2.4, 25.6.1/11, 5.11.2/9 and Trudgian arXiv:1010.4596 Section 4 Lemmas 1--3, (8)--(14), pp. 5--6.
COMPARISON: The manuscript states a stronger fixed-generator identity C_m=<q,rho_m> for every integer m>=2; the saved target asks only its finite complex neutral specialization. L729 supplies the absolute prime functional and L730 the conditional endpoint, but neither supplies the representer contour. A separate replay is warranted for this unreviewed input.
GAP: Essential proof passages and standard analytic hypotheses are now accessible; independent verification of Mellin inversion, strip/left-boundary estimates, all residues, ordered limits, q in H and conjugations remains. Full norms, saturation and a new complementary-residual mechanism remain outside scope.
REASON: Coverage now supports a bounded conceptual audit instead of dependent projection work. Source comparison alone establishes no identity or new mathematics and does not reopen the paid-tail cutoff or full-update stops.
SCOPE: Completed literature-only review. The separately nominated audit in 2026-11-03-neutral-prime-representer-audit.md requires next-turn approval; no derivation or lemma is made in step 235.

The exact proposed input uses H, rho_m, K_m, T_m, A, B and Q from
L729, with u a fixed finite complex combination satisfying A(u)=B(u)=0.
The inner product is linear in its first entry, so Q and ⟨q,u⟩ are
conjugate-linear in u. Source: bramble_trace, *Fixed and growing neutral
gradients of the anchored Selberg–Möbius approximant*, paper 18, displayed
v3, 22 October 2026, https://rstation.ai/problems/riemann_hypothesis/papers/18 .

Reuse drafts/literature/2026-11-03-neutral-arithmetic-tail-audit.md and
drafts/literature/2026-11-03-constructive-neutral-density-audit.md for
their established scopes. Begin with the primary theorem hypotheses,
then inspect the representer proof's essential cases and precise cited
analytic inputs. Do not infer global contour validity from the endpoint
calculation in L730 or from a formal cancellation of nontrivial zeros.
Do not identify the arithmetic span with all step functions.

Original continuation test: coverage must specify justified contours, all pole
cases, convergence of the residue series and the actual order of
limits, and address q∈H near 1 and infinity. If an essential source
estimate is inaccessible or missing, record that blocker and park its
dependent application. No RH, simple-zero, whole-space density or
unconditional saturation assumption is allowed. No new creative
complementary-residual mechanism is justified merely by this identity.

## What was actually inspected

The HTML source above was labeled v3, dated 22 October 2026, inspected
3 November 2026. Read the fixed-probe theorem and its definitions before
the full section **An elementary representer of the complete fixed
gradient**, including its four subsections. Equation numbers below
refer to that version. This is source coverage, not an independent
verification of the manuscript's claims.

The source identifies the prime sum S_m with a Mellin integral in (22).
Its claimed transform (21) has fundamental strip 1<Re(s)<2; inversion
uses the narrower line 1<c<3/2. The proof gives both endpoints of K_m,
continuity, integrability on that vertical line, and the absolute
Dirichlet-series condition needed for Fubini. In particular it does not
invert the merely conditionally convergent transform of f_m directly.

Equation (23) rewrites the product of the logarithmic derivative and
zeta(1-s) as -chi(1-s)zeta'(s). Its stated local argument covers an
arbitrary multiplicity r, with order r-1, rather than simple zeros
only. The text then supplies a three-case strip estimate on [-A,c],
including both adjoining edges. After the quadratic denominator its
horizontal bound is T^(c-5/2+epsilon), with
0<epsilon<3/2-c. These are exact source bounds for the later audit;
their exponents and edge uniformity have not been reproduced here.

The source specifies odd A>=3 for the left vertical line, so it avoids
the negative even poles. It estimates the log derivative there using
the reflected absolutely convergent series, a bounded cotangent and a
uniform digamma estimate. Equation (24) claims an absolute left-edge
integral O((1+log A)/(m A)). It explicitly takes T→infinity at each
fixed A before odd A→infinity. There is no asserted joint bound in A,T
and no exchange of an infinite nontrivial-zero residue sum.

The residues section distinguishes the double pole at 1, the pole at
0, and simple trivial zeros -2k. It states the residue at -2k as
R_m(1+2k)/(2k), with R_m given by (25), and an absolute O(1/(m k²))
bound for their series. The zero of m^(s-1)-m^(-1) at s=0 is retained;
it does not by itself remove that pole. Formula (26) records the
resulting sum. The recovery section uses the conditional finite part
(27), finite endpoint (28), and termwise integration of the logarithmic
series against bounded rho_m, with an integrable logarithmic majorant
at 1. All these cases are now available for replay.

The fixed-probe theorem asserts q∈H, not that the original
prime-discrepancy function belongs to H. The audit must check the
square-integrable logarithm at 1 and bounded behavior at infinity.
For the complex neutral specialization it must retain the source
coordinate formula C_m=T_m(1)-2 gamma a_m-S_m and the first-entry-linear
inner product. No PNT remainder is needed for the neutral contour
identity itself; the manuscript's separate fixed-gradient asymptotic
uses such an input and is not nominated here.

## Standard analytic coverage and its limits

The following references were opened at their relevant statements;
they support a later applicability check, not a new proof this turn.

- [DLMF 25.5.5](https://dlmf.nist.gov/25.5#E5), citing Titchmarsh,
  *The Theory of the Riemann Zeta-Function*, 2nd ed., (2.1.6), p. 15:
  the centered fractional-part integral is stated for -1<Re(z)<0.
  The source's substitution z=1-s lies in exactly that strip. Its
  improper integral must retain the bounded-primitive interpretation.
- [DLMF 1.14.35](https://dlmf.nist.gov/1.14#E35): Mellin inversion
  requires continuity of f and integrability of its Mellin transform
  along the selected vertical line, in its convergence strip.
- [DLMF 25.4.1--2](https://dlmf.nist.gov/25.4): the two reflected
  functional equations, with their exceptional points 0 and 1 treated
  separately; [25.2.4](https://dlmf.nist.gov/25.2#E4) gives the Laurent
  expansion at 1. [25.6.1](https://dlmf.nist.gov/25.6#E1) and
  [25.6.11](https://dlmf.nist.gov/25.6#E11) give zeta(0) and zeta'(0).
  These cover the standard values required by the pole expansions.
- [DLMF 5.11.2](https://dlmf.nist.gov/5.11#E2) gives the digamma
  expansion uniformly within a closed sector |arg z|<=pi-delta;
  5.11.9 gives the gamma modulus on vertical lines, and Section 5.11(ii)
  supplies remainder qualifications. The source's growing left line
  has Re(1-s)>=4, within a sector away from the negative real axis.
- T. S. Trudgian, *A modest improvement on the function S(T)*,
  [displayed arXiv:1010.4596 PDF](https://arxiv.org/pdf/1010.4596),
  Section 4, pp. 5--6: Lemma 1 states polynomial-bound interpolation
  for a holomorphic strip function with growth
  |f(s)|<C exp(exp(k|t|)), 0<k<pi/(b-a), -Q<=a, and boundary
  exponents alpha>=beta. Equations (8)--(9) give the right/left
  zeta bounds, and the proof explicitly removes the pole with
  (s-1)zeta(s) when the strip crosses 1. Lemmas 2--3 and (14)
  document its zeta application. Only qualitative classical
  convexity is needed here; no explicit decimal constant or
  subconvexity estimate is imported. Cauchy's derivative estimate
  is a standard named input; the later audit must check its circles
  stay away from 1 at large height and pay their exponent enlargement.

The Rutgers Titchmarsh PDF timed out twice; the AMS journal PDF was
403; a TIFR URL was inaccessible. The primary Trudgian PDF and DLMF
statements above were accessible alternatives. Rademacher's original
article was located bibliographically, but its notice/secondary
quotations do not count as inspecting Theorem 4. No essential estimate
is being imported from those unread leads. The Markdown download of
paper 18 was unsupported by the web reader; its complete relevant HTML
proof was accessible. Shell DNS failure is recorded without treating
it as a global source blocker.

## Duplicate and failure comparison; mathematical status

Reused the arithmetic, density, dyadic-contraction and sqrt(N)
assessments. They approve other scopes and expressly leave this
representer unverified. The recorded full-update obstruction and
`ATTEMPTS/2026-11-03-signed-neutral-tail-gram-dual-source-stop.md`
concern unpaid whole residual or growing-unit-ball estimates. The
representer identity supplies neither estimate and does not overturn
their evidence. Exact-title and formula/standard-terminology searches
did not locate an independently inspected stronger result replacing
this contour audit; that is not evidence of novelty.

The source statement covers the requested finite neutral target, so
SPECIALIZE is appropriate. An independent audit is justified by the
unreviewed source, multiplicity and boundary-limit sensitivity, and
the complex convention. There is no mathematical result to put in a
canonical lemma or in PROOF.md at this stage. Full matching Mathlib
coverage remains unchecked. Supporting coverage was inspected:
[`mellinInv_mellin_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/MellinInversion.html#mellinInv_mellin_eq)
requires MellinConvergent, VerticalIntegrable and ContinuousAt at x>0.
Its exact hypotheses support inversion only; they do not prove the
representer, contour estimates or residue calculation.
