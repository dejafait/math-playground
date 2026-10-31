# Uniform transformed-test seminorms — source comparison

TARGET: Audit family 003's uniform transformed-test seminorm estimate for Vsharp used in L541, retaining L548's Mellin formula and checking logarithmic derivatives, finite input seminorms and constants independent of the moving arithmetic data.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Targeted local searches of L541/L548, family003 terminal-energy, Mellin and internal-Fourier assessments and their relevant source/audit histories locate retained contracts, not a completed standalone uniform-kernel audit. Exact web queries for Vsharp/reflection-test-seminorm and the source paragraph title locate the same manuscript; a Mellin/gamma-quotient/Schwartz query yields general transform leads, none needed to replace its exact statement. Search failure is not a novelty claim; inspected and unread results are distinguished below.
SOURCE_EVIDENCE: Pinned OpenAI family003 build/paper.tex, commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a: prop:completed-reflection hypotheses/transform 1559–1629, full seminorm statements 1727–1755 and complete uniform-estimates proof 2261–2314; pointwise Mellin hypotheses 1073–1091 and proof 1157–1171. DLMF 5.2(i), paragraph after 5.2.1, and 5.11.9 including bounded-real-part uniformity were inspected. L541 Hypothesis 1 and (11)–(12), L548 hypotheses and (6) were compared.
COMPARISON: The exact source already claims this kernel estimate on L548's full test class, with finite input norms, all fixed logarithmic derivative orders, both endpoint weights and constants free of arithmetic labels. A later local verification must check the stated contour/seminorm interface rather than reproduce it as new mathematics. Its one-variable annular bound does not certify L541's joint common-density operation, lattice-tail aggregation or arithmetic estimates.
GAP: Source coverage for this bounded kernel audit is complete; independent local verification of the gamma quotient, horizontal joins, derivative orders, endpoint combination and norm-twist cost remains. Common profiles, marked expansion, arithmetic uniformity, global closure and actual-Xi signs remain separate.
REASON: SPECIALIZE permits a REPRODUCTION audit of an explicit retained source contract, needed to remove this particular conditional input from L541. Mere citation identifies the known bound but does not accomplish the requested independent verification; no stronger estimate or novelty is proposed. This literature turn does not carry out that verification.
SCOPE: Exactly the V-to-Vsharp kernel, fixed logarithmic derivative orders, weighted finite input seminorms, one-variable fixed-annulus Fourier bound and pure imaginary norm twists. Retain L548's formula/test class and its conditional arithmetic reflection. Exclude joint common-profile/Minkowski verification, lattice-tail aggregation, marked expansion, coefficient/Gauss bounds, global closure and Xi positivity. No cross-notebook input.

## Primary source and exact interface

Use L548's transform (6) and L541 Hypothesis 1 as the local interface.
The conditional raw theta, coefficient and finite Gauss inputs of L548
remain in force for reflection. They are not uniformity estimates for
the kernel. The latter is the same explicit integral for every branch.

The exact source lead is OpenAI, *The Quasi-Riemann Hypothesis*,
30 September 2026,
[pinned build/paper.tex](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
Proposition `prop:completed-reflection`, specifically
`eq:reflection-kernel`, `eq:reflection-annular-fourier` and
`eq:reflection-test-seminorm`, lines 1727–1755. The full proof portion
is lines 2261–2314. The hypotheses at 1600–1604 require smooth V on
(0,infinity), with every Euler derivative rapidly decreasing in powers
at both endpoints. This is precisely L548's class, including its
noncompact Gaussian; compact support of V is not required.

For D=x d/dx, A>=0 and integer B>=0, the source defines

\[
 \mathfrak M_{A,B}(V)=\sup_{-A\le\eta\le1/4}
       \int_{\mathbb R}(1+|u|)^B|\widehat V(\eta+iu)|\,du.
\]

Its three claimed bounds, transcribed here as source statements and
not proved in this review, are:

\[
 |D^j V^\sharp(x)|\ll_{A,j}
 \min\{x^{1/4},(1+x)^{-A}\}
 \mathfrak M_{A,\lceil4A\rceil+j+2}(V),\qquad j\ge0;
\]

\[
 \int_{\mathbb R}(1+|u|)^J
 \left|\int_0^\infty\chi(y)V^\sharp(Yy)y^{-iu}\frac{dy}{y}\right|du
 \ll_{A,J,\chi}\min\{Y^{1/4},(1+Y)^{-A}\}
 \mathfrak M_{A,\lceil4A\rceil+J+4}(V);
\]

\[
 \mathfrak M_{A,B}(V)\ll_{A,B}
 \int_0^\infty(1+x^{-A}+x^{1/4})
       (|V(x)|+|D^{B+2}V(x)|)\frac{dx}{x}.
\]

Here x,Y>0, j,J are nonnegative integers, and chi is one fixed
C_c^infinity cutoff in (0,infinity). The source additionally states
M_(A,B)(x^(iu_0)V)<= (1+|u_0|)^B M_(A,B)(V) for real u_0.
Orders and the annular cutoff are fixed before demanding uniformity;
no constant independent of A,j,J,chi is claimed. The displayed input
norms must remain explicit for a moving family of V. Fixed-data
admissibility alone does not give a uniform bound for such a family.

## Proof coverage actually read

The paragraph at 2261–2314 supplies every proof case used for these
claims. It locates the first numerator pole at t=-5/6, treats the
denominator through entire reciprocal gamma functions, and states
|R(sigma+iu)|<<_A(1+|u|)^(4sigma) for -1/4<=sigma<=A,
including bounded u. It invokes the pointwise Mellin estimate for
rectangular contour joins, then differentiates under the integral.
The lines -1/4,0,A supply the three separate endpoint estimates before
they are combined. This includes A=0; a later audit must retain that
case rather than assume a positive decay exponent.

For the annular bound the proof sets f_Y(v)=chi(e^v)Vsharp(Ye^v),
uses compact support in v and J+2 Fourier integrations by parts,
then applies Leibniz and the kernel estimate. For the input seminorm
it treats |u|>=1 with B+2 Mellin integrations by parts, and |u|<=1
with the undifferentiated integral, uniformly over -A<=eta<=1/4.
The final pure-twist assertion uses translation in the Mellin variable.
These are descriptions of the source proof; their local verification
is reserved for the mathematical audit.

The supporting `eq:pointwise-mellin-tail` requires finite weighted
Euler-derivative integrals and vanishing integration-by-parts boundary
terms, uniformly on a compact real strip. Its proof at 1157–1171 was
read, including |T|<1. Its second example (smooth at zero, Schwartz at
infinity) only licenses positive strips; that weaker example must not
replace L548's two-endpoint rapid class on [-A,1/4].

The reusable gamma input is NIST DLMF
[5.11.9](https://dlmf.nist.gov/5.11.E9), read with the sentence asserting
uniformity for bounded real parts and both signs of the imaginary
part. [5.2(i)](https://dlmf.nist.gov/5.2#i), immediately after 5.2.1,
states the poles at nonpositive integers, absence of gamma zeros and
entireness of its reciprocal. These cover the analytic facts needed
by this kernel review; the earlier Bessel inputs are not new kernel
dependencies. DLMF version is reused from the preceding assessment
(1.2.8, 15 September 2026); these two live sections were rechecked.

## Comparison, duplicates and limits

L548 (6) has the same K, R and Mellin sign as this source. Its fixed
arithmetic continuation constants are not being declared uniform.
The kernel statement, in contrast, contains no modulus, prime set,
cusp, coefficient or ray character. Thus the source's claimed constant
dependencies match the requested kernel portion of L541. Its j=0
large-argument claim is the kernel premise quoted in L541 (12).
L541 (11) additionally needs a joint compact-profile construction and
one common row measure: those remain imported contracts, not outcomes
of this one-variable source review. L535/L536's Poisson kernel bounds
are a different transform and do not duplicate this estimate.

Targeted searches used the terms `Vsharp`, `uniform`, `seminorm`,
`reflection-kernel`, `reflection-test-seminorm`, `4A`, and `norm-twist`
in the terminal/Mellin source notes, relevant histories and family003
assessments. The previous Mellin review explicitly stopped before
uniformity; the terminal assessments retain it. No matching completed
local kernel verification or target-specific refutation was located
in those paths. The retained zero-line warning remains: moving an
individual kernel contour does not authorize interchanging the full
dual Dirichlet series with its integral on Re(t)=0.

External queries were `"V^\\sharp" "reflection-test-seminorm"`,
`"Quasi-Riemann" "Uniform estimates for the transformed test"`, and
`"Mellin" "gamma quotient" "Schwartz" Hankel transform estimates`.
The first two locate copies of the same source, not independent
confirmation. General results on local integral transforms are unread
leads, not imported theorems. Only the pinned primary source and DLMF
support this comparison. Shell retrieval failed DNS resolution, but
the web tool retrieved the necessary primary text; no source blocker
remains. Full matching Mathlib coverage is unchecked, not absent.

## Bounded continuation and decision

The main gap is actual-Xi all-degree positivity. The intermediate
target is the exact known uniform kernel interface above, whose
downstream use is L541's conditional reflected-energy argument.
Independent marked, arithmetic, common-measure and global closure
obligations remain even if this interface passes.

Coverage is now ready for a separate REPRODUCTION audit under
SPECIALIZE. That verification is justified by the notebook's explicit
source-audit objective, not by novelty or the need for another lemma.
It must check the gamma bound including denominator zeros, dominated
differentiation, horizontal joins, all fixed derivative orders, A=0,
both endpoint weights, finite input orders and pure-twist dependence.
Pass only with constants depending on the displayed analytic orders
and cutoff, never on moving arithmetic labels. Any missing case must
be recorded and the interface narrowed or parked. A successful audit
supplies this kernel contract only. This turn writes no proof,
lemma or mathematical script and does not certify the estimate.
