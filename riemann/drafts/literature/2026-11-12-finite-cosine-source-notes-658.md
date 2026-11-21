# Source review658: primary evidence and qualifications

Completed literature-only work. The saved target is review657's exact
finite-cosine Carleman assessment; no evaluator, error ledger or new
mathematical result has been derived. The six frozen densities and exact
neutral completion remain unchanged.

Inspected C998a Sections1 and3 for the finite real cosine representation,
parity convention, neutral completion and endpoint subtraction. Inspected
C998b's prescribed work test: its direct nested summation stops only that
prescription, not special-function evaluation. Reused review655's scalar
inclusion assessment; no need to repeat its quadrature literature.

## Search and local comparison

Queries included `site.dlmf.nist.gov sine cosine integrals power series
Ci Si 6.6 6.2`, `site.flintlib.org arb_hypgeom ci si rigorous error bound
algorithm`, and `Johansson Arb efficient arbitrary precision midpoint radius
interval arithmetic 2017 error bounding hypergeometric`. The local search
covered12November Carleman assessments/attempts and separation-seven code,
using Carleman, sici, sine/cosine integral, ci_2f3 and si_1f2. It found no
implemented matching oracle; no claim of originality follows. C998a's
Stieltjes subtraction is already established locally. Review655's Gauss
coverage does not pay a different point oracle. C998b/657 stops its direct
node prescription only. Neither that stop nor the earlier652 stop excludes
frequency evaluation. No sibling notebook or cross-notebook theorem was read.

## Inspected primary inputs

**Definitions and branches.** NIST DLMF, version1.2.8,15September2026,
[6.2.9,11-13](https://dlmf.nist.gov/6.2#ii) defines Si,Ci,Cin;
Si is entire, Ci uses the principal logarithm/cut and Cin is entire.
[6.2.19-20](https://dlmf.nist.gov/6.2#iii) relates Si,Ci to auxiliary f,g.
These cover positive nonzero arguments without crossing a cut. The constant
frequency must be integrated separately, rather than evaluating Ci(0).
They supply primitives for a later finite-interval change of variable and
addition-formula check; no frozen-transform identity was derived here.
The C998a parity convention and exact neutral completion must be retained.

**Convergent representations.** [DLMF6.6.5-6](https://dlmf.nist.gov/6.6)
gives the Si series and Ci's gamma-plus-log-plus-even-power series; these
converge at every finite argument in their branch convention. Convergence
alone does not specify a usable truncation, working precision or error for
a difference. The Cin relation is an available way to separate a logarithm,
not an already implemented cancellation remedy.

**Effective tails and summation.** Johansson, *Computing hypergeometric
functions rigorously*, [arXiv:1606.06977v2](https://arxiv.org/pdf/1606.06977v2),
5July2016: read Sections3.1,4.1 Theorem1 and its full scalar proof,
4.2 through the forward/binary/rectangular summation discussion, and6.5's
transition-cancellation qualification (printed pp5-8,12-13).
For the terms T(k) of(1), with the extra lower parameter b_(q+1)=1,
p<=q+1 and Re(b_i+N)>0, the tail is at most |T(N)|/(1-D) when

    D=|z| product_(i=1)^p(1+|a_i-b_i|/|b_i+N|)
             product_(i=p+1)^(q+1)1/|b_i+N| < 1.

For D>=1 it gives no finite bound. The proof bounds successive ratios by D.
Section4.2 supplies O(N) arithmetic summation for fixed parameters, with
faster alternatives. Parameters, finite N, precision and primitive costs
still need specialization. Section3.1 expressly does not guarantee output
accuracy or precision-doubling convergence. This is not a fixed-data cost
theorem. The displayed S recurrence has a typographic slip; the matrix
recurrence and sum definition specify accumulation. No reproof is needed.

**Asymptotic option, not unchecked infinite summation.** Read
[DLMF6.12.5-8 and its final error paragraph](https://dlmf.nist.gov/6.12#ii),
including the finite geometric-identity explanation of the remainder.
For n>=0 these are exact finite expansions with integral remainders.
In |arg z|<=pi/4 each auxiliary remainder is at most its first omitted
term; on the positive axis it has that term's sign. The stated csc bound
for the adjacent sector is not needed for this real-point scope.
[6.7.13-14](https://dlmf.nist.gov/6.7#iii) supplies the integral
representations used there: their Laplace forms require Re(z)>=0 and,
for g, z!=0. Positive real arguments satisfy these hypotheses. No claim
that increasing the asymptotic order always improves accuracy is made.
The transition range needs convergent series or another covered method.

**Stable implementation cases.** Read the complete Arb2.23.0 files
[si.c](https://raw.githubusercontent.com/flintlib/arb/2.23.0/arb_hypgeom/si.c)
and [ci.c](https://raw.githubusercontent.com/flintlib/arb/2.23.0/arb_hypgeom/ci.c).
The former's lines95-151 implement the convergent sum and geometric tail;
153-249 handle zero/nonfinite input, precision selection, asymptotic choice,
small arguments and input-radius propagation. The derivative bound for a
positive input interval is min(1,1/inf z); the wide-output branch is not an
accuracy guarantee. The latter's lines66-128 implement the convergent
correction plus logarithm and Euler constant;130-220 require finite positive
input and use1/inf z for input-radius propagation. Both files' earlier
asymptotic branches append explicit magnitude errors. Their floating cutoff
heuristics select a method; only resulting radii certify accuracy. This
source inspection is not a verified build or an exhaustive code audit.

The [Arb2.23.0 API](https://arblib.org/arb_hypgeom.html), Si/Ci section,
was checked against those files. The [current FLINT documentation](https://flintlib.org/doc/arb_hypgeom/index.html)
was consulted only as a lead: its October2026 revision notice says some
text was LLM-generated. Stable source and primary mathematics above support
the decision. Initial v3.3.1 separate-file raw URLs returned404; corrected
Arb2.23.0 URLs resolved access. There is no persistent source blocker.

**Elementary calls and finite precision.** Johansson, *Efficient
implementation of elementary functions in the medium-precision range*,
[arXiv:1410.7176v2](https://arxiv.org/pdf/1410.7176v2),9June2015,
Sections2-5, printed pp3-10: read fixed-point error rules, argument reductions,
Algorithm1 and log/sin/cos variants, then the complete top-level error
discussion. Algorithm1's2-ulp claim assumes its actual tables,
0<=X<=2^-4 and2<N<300; it is not a general Si/Ci bound. The detailed
top-level pseudocode is for atan; analogous log/sin/cos error calculations
are delegated to source code. This supports a finite arithmetic design,
not an imported constant for this evaluator. A later proof may use simpler
direct Taylor/rational interval operations rather than reproduce optimized
table code. Count argument reduction, constants and every elementary call;
do not transplant benchmark times or promise requested accuracy.
Reuse review655/comparison656's already inspected Arb inclusion arithmetic.

## Decision and remaining specialization

SPECIALIZE is justified for a separate bounded REPRODUCTION. No source
claims the entire six-density2^-53 result or a batch work bound verbatim.
Missing items are quantitative specialization: finite-transform identity,
both parity signs, zero mode, exact neutral coefficients, positive argument
enclosures, small-argument cancellation, fixed cutoffs/precisions, all error
contributions and scalar work. No such bound or implementation was produced
in this literature turn. A generic adaptive API is insufficient for uniform
finite work; prescribe finite parameters and prove their error, or stop.

In particular, neither a broad t interval passed once to an interval API
nor checks at a few sample points establish a uniform pointwise algorithm.
Narrow argument enclosures must represent each requested t; a later uniform
parameter proof must cover every t in[a*2^-80,a]. Complex-box analyticity
and outer quadrature remain separate obligations, outside this approval.

Continue only if all six complete sums meet2^-53 and the whole scalar work
ledger is finite and compared with a declared execution budget before any
large run. Otherwise preserve the specific precision or cost failure and
choose a different test. Width1e-4 full residual norms, C999 inverse-action
errors, signed S3, higher/mixed endpoints, C744q/H2, non-neutral and global
Xi assembly remain unresolved. This is local source coverage, not a new
sign theorem. Mathlib matching coverage and build availability were not
checked; neither is claimed absent. No new lemma or mathematical script.
