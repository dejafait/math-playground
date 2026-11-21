# Signed coprime covariance: source review2080

Completed source review, literature only. No bound or new mathematical identity
is established here. The exact target remains assessment2079's TARGET.
Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
Possible use: pay the low primitive term, retaining the high complement
and the independent detection/normalization/transfer obligations.

## Exact primary interface inspected

Leonard van Hemert, *Exact Zero Detection and Compact Arithmetic
Realizations for the Riemann Xi Function*, v1.0.0, 11 October2026,
DOI10.5281/zenodo.23295277,
[tagged source](https://raw.githubusercontent.com/LeonardSEO/riemann-xi-zero-detection/refs/tags/v1.0.0/paper/paper.tex).
Read FB1-FB3, FB4-FB8 and the complete fixed-band theorem proof,
GC12-GC18 and the primitive-remainder proof. These are manuscript
statements, not independently audited local theorem imports.

For q>1, Q=log q, h in E=L2(R,exp(-y/2)dy), f=J_E(Phi*h),
C_h(r)=integral f(y)conj(f(y+r))dy, and
rho(M)=zeta(2)^(-1) product_(p|M) p/(p+1), GC12 specifies

\[
 M_H=\sum_{\substack{a,b\le H\\(a,b)=1}}
 \frac{\mu(a)\mu(b)\rho(ab)}{\sqrt{ab}}
 w_Q(\log(b/a))C_h(\log(b/a)),
\]

where w_Q(r)=integral_(|r|/2)^(Q-|r|/2)
exp(-s/2)(s^2-r^2/4)ds for |r|<Q and zero otherwise.
GC13 requires 1<=H<=X and gives error
O_q(C_h(0)X^(-1/2)H^(3/2)log^2(2H)). GC18 leaves the two
signed primitive terms unbounded. H here is a primitive cutoff;
the fixed-band projection uses a separate band parameter.

The fixed-band proof explicitly uses h=(D^2+1/4)g, D=-i partial,
for any nonzero nonnegative compact smooth g. The selected bump is
within that stated input class; this observation imports no upper bound.
FB7 permits some sufficiently small positive Fourier band; it does not
prescribe the primitive cutoff as that band.

## Reuse and retained failures

Read the relevant part of assessment2078, history2079 and stop2076.
Reuse November9 gcd conditioning/position-sensitive comparisons and
November17 paired-mollifier audit source-notes1399. Those assessments
concern other quadratic forms and do not authorize this target.
C034q's universal positive convolution-inverse obstruction stays intact;
the signed target proposes no such inverse.

## Access record

The tagged source is accessible through web retrieval. A shell download
failed because raw.githubusercontent.com could not be resolved; this is
not a mathematical source blocker while web access remains available.
The Reading repository's beyondhalf4.pdf returned an Anubis denial;
the primary arXiv1512.03758v2 PDF is accessible instead. No blocked
certificate was retried. No mathematical script or lemma was written.

## Primary comparisons: inspected hypotheses, no theorem imports

Olivier Ramaré and Sebastian Zuniga-Alterman, *On a Möbius double sum*,
[arXiv2603.25961v1](https://arxiv.org/pdf/2603.25961v1),
26 March2026, pp1-3, Theorems1.1/1.2 and Lemmas2.5/2.6; also
Section6 equation(19), its nonnegative square expansion. Read those
statements and the coprimality identity, not the full 31-page proof or
computations of constants. Theorem1.1 concerns
S_0(X)=sum_(a,b<=X)mu(a)mu(b)/[a,b], X>0; in particular it states
0<=S_0(X)<=0.4664 for X>=10^33. Theorem1.2 uses exponent
1+epsilon, 0<=epsilon<=1/25, with its own range cases. These signed
upper bounds have neither GC12's coprime mask nor its rho, half-power
denominator and ratio correlation. Their square expansion is for the
lcm kernel. No quadratic-form order relating it to GC12 was found.
Lemma2.5 treats a coprime mu(n)/n sum; Lemma2.6 retains logarithmic
errors and q factors. Neither states the required two-variable estimate.
The HTML has unresolved Sage constants; the primary PDF resolves the
inspected theorem constants. Neither constants nor a specialization are
imported. Dress--Iwaniec--Tenenbaum and Helfgott were located references,
not independently inspected proofs or essential premises for this
nonmatching-kernel comparison.

Ahmadreza Azimifard, *A power-saving asymptotic for a Möbius-weighted
GCD quadratic form*,
[arXiv2611.00525v1](https://arxiv.org/html/2611.00525v1),
31 October2026, Theorem1.1, equations(1)-(9), Lemmas2.1/3.1/3.2
and displayed proofs through the limiting-square sign argument.
Its T(N)=sum mu(a)mu(b)(a,b)^2/(ab) has positive linear main term
and O_epsilon(N^(2/3+epsilon)) error. Its auxiliary coefficient uses
R(r)=product_(p|r)p^3/(p^3+p^2-1), not rho(r), and unrestricted
pairs with denominator ab. This does not refute the M_H upper. Its
condition (d,ab)=1 in a Jordan-totient decomposition is not GC12's
(a,b)=1. The complete asymptotic proof and Section5's claimed Lean
formalization were not audited; no matching Mathlib coverage follows.

Titus Hilberdink, *An arithmetical mapping and applications to
Omega-results for the Riemann zeta function*, Acta Arith.139(2009),
341-367, DOI10.4064/aa139-4-3,
[primary PDF](https://www.impan.pl/shop/publication/transaction/download/product/82846).
Read mapping(0.1), the finite-norm definition, Theorem2.3 statement
p350 and the entire GCD-spectrum comparison pp362-363. This concerns
the largest eigenvalue of ((a,b)^(2alpha)/(ab)^alpha) on arbitrary
unit coefficient vectors. At alpha=1/2 the stated log spectral growth
is comparable to sqrt(log N/loglog N). It is an operator bound in
its own coefficient normalization for the unrestricted positive matrix;
there is no GC12 coprime mask, rho or actual correlation. No transfer
inequality was found. Theorem2.3's full proof was not audited or imported.
The older unread-lead status is discharged only for these passages,
not for Hilberdink's other papers.

Bondarenko--Hilberdink--Seip, *Gál-type GCD sums beyond the critical
line*, [arXiv1512.03758v2](https://arxiv.org/pdf/1512.03758v2),
11 April2016, Theorem2 p3 and proof pp3-4, including the prime-power
case. It bounds the unrestricted natural-prefix GCD matrix on unit
complex vectors by C_alpha N^(1-2alpha), only for 0<alpha<1/2.
This is neither the endpoint nor GC12's signed coprime kernel. Its
proof uses absolute values, not the missing signed cancellation.
No specialization was derived.

## Actual kernel and downstream-use boundary

Read the tagged source's complete theta reconstruction, paper.tex
lines802-838. The full even density is

\[
 \Phi(u)=\sum_{n\ge1}(4\pi^2n^4e^{9|u|/2}
       -6\pi n^2e^{5|u|/2})e^{-\pi n^2e^{2|u|}}.
\]

Its stated transform is Xi(z)=integral Phi(u)exp(izu)du. The
fixed-band proof uses weighted convolution multiplier Xi(u-i/4)
times the transform of J_E h. The Fourier sign convention, weight,
Plancherel normalization and all interchanges remain independent audit
obligations; reading the reconstruction does not certify the source.
The needed named standard tools are Gaussian Poisson summation,
Plancherel/convolution, Bochner absolute Fubini, Hilbert-space
Cauchy--Schwarz, Stieltjes integration by parts and meromorphic
uniqueness. FB6 assumes no primitive-sector arithmetic upper.

Read L030,L031,L032,C032a for local scope: the missing form uses
algebraic squares on actual nodes, so another absolute-square/GCD
positivity does not pay it. An exact-label search for GC12,
log-primitive-remainder and fixed-band-cumulative in local literature,
lemmas, foundations and ATTEMPTS found only assessments2078/2079 and
these new notes, not a canonical local detector import.

## Queries, outcome and continuation

Queries issued: `coprime Möbius quadratic form gcd sums Hilberdink
upper bound`; `"coprime covariance" "theta" van Hemert`;
`Hilberdink "An arithmetical mapping" theorem mobius 2009 pdf`;
`"coprime" "Möbius" "quadratic" sum upper bound rho`;
`"coprime" "Möbius" "two" "Dirichlet series"`;
`"On a Möbius double sum"`; `"coprime" "Mobius" "double sum"
zeta`; `"Gál-type GCD sums beyond the critical" arxiv`.
Only the identified primary sources support comparisons; aggregators,
search snippets and unrelated RH-claim pages are not evidence.

NEGATIVE is limited to the named direct-import shortcuts. The newly
inspected signed lcm/GCD/spectral statements miss GC12's hypotheses,
so the route changes to an independent audit of the fixed-input
detector. This neither refutes the M_H upper nor establishes novelty.
EXPLORE records no adequate match in this bounded search. No usable
signed mechanism with a paid error emerged; unspecified cancellation
does not receive approval.

The next audit is independently testable while both primitive uppers
remain open. Continue only if all FB1-FB8 hypotheses, actual normalization,
pole noncancellation, multiplicity and limsup cases survive checking;
otherwise record the exact failing claim and restrict its use. Success
would verify a known manuscript input, not the arithmetic upper or RH.
Its newly ready assessment receives separate approval next turn.
No creative target is justified yet: the blocker is signed cancellation,
not source access or a historical global ban. Zero mathematical attempts
added or counters reset. No cross-notebook input. Full matching Mathlib
coverage unchecked. No input was imported into the canonical argument;
PROOF.md and DAG.md are unchanged in this step.
