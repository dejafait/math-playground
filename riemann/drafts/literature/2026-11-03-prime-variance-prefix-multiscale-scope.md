# Prime variance and the drift-removed prefix: completed source comparison

TARGET: Assess whether unconditional Selberg-integral estimates for prime counts in short intervals can control L732's drift-removed prefix energy through a multiscale decomposition, retaining cross-scale covariance and comparison with the October zero-free baseline.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Selberg integral unconditional short-interval psi mean square; Saffari–Vaughan Lemmas 5–6; current short-interval variance; cumulative/cross-scale and power-mode obstructions. Read L729/L732 statement and finite-prefix interface, four named ATTEMPTS stops, the Hardy screen, and the October assessment/register. Exact queries and exclusions below; no exhaustive absence claim.
SOURCE_EVIDENCE: Inspected Montgomery–Vaughan author-hosted MNT III Theorem 28.6/(28.36), its complete proof pp. 212–216 and RH exercises p. 217; Saffari–Vaughan 1977 Lemmas 5–6/(6.2)–(6.4),(6.19)–(6.21), including the additive/multiplicative transfer proof; Grenié–Molteni–Perelli 2017 proof (7) and its explicit correction to (6.20); Zaccagnini 2006 Theorem 3.1 and Section 3.1 only as a differently centered comparison.
COMPARISON: Unconditional source statements pay increment mean squares in their exact ranges; neither the inspected reconstruction proofs nor the pi-based stronger comparison supplies L732 cumulative prefix control or its cross-scale/coarse terms. The RH-sized source variant explicitly assumes RH. Thus importing that variant or dropping covariance cannot approve the proposed prefix upper bound.
GAP: No established upper estimate for J_N^*, no covariance-retaining prefix reconstruction, no bound for the actual scalar anchor or complementary physical tail, and no improvement on the registered October half-plane. A separate bounded power-profile diagnostic is nominated; it is not proved here.
REASON: The accessible primary hypotheses settle the source mismatch without a persistent access blocker. Park automatic interval-variance-to-prefix transfer and test the strength of the available variance envelope independently, before seeking a new arithmetic mechanism.
SCOPE: Literature-only completed step. Known interval statements may be cited within their stated scope; no new multiscale inequality, lemma or mathematical script was derived or written.

## Original nomination and exact comparison question

Keep the actual von Mangoldt function, psi(j)=sum_(n<=j)Lambda(n), and

    J_N^*=inf_(a in C) sum_(j<=N)|a j-psi(j)|²/[j(j+1)],

as defined in L732. A conventional short-interval statistic to search is

    S(X,h)=integral_X^(2X)|psi(x+h)-psi(x)-h|² dx,
    X>=2, 1<=h<=X,

along with precisely stated multiplicative-interval variants. This
formula only specifies the source observable; no bound or identity
relating it to J_N^* is asserted here. Source statements involving a
different centering, h-range, smoothing, averaging in X, or exceptional
set must retain those restrictions.

The proposed mechanism would reconstruct a cumulative discrepancy from
increments at several scales, with the scalar drift optimized only as
allowed by J_N^*. Its possible benefit is a quantitative arithmetic
input to upper control; no local interval variance can silently replace
the covariance of increments across scales or their long-range means.
This missing transfer is the independently testable issue, rather than
the exact full-norm Gram kernel already parked.

For calibration, L732's exponent shows why an N^(o(1)) upper estimate
would have RH strength, as already recorded in the prior source review.
That estimate is a threshold, not an assumption or an available bound.
The source review need not reach it: a rigorously quantified,
noncircular estimate for a specified term or a source obstruction to
reconstruction could justify a later bounded test. Comparison with
existing fixed-half-plane estimates is essential before calling a
weaker bound new progress. J_N^* also differs from J_N(ell alpha_N);
optimizing a drift does not estimate the actual triangular family's
scalar anchor or its complementary physical tail.

## Required inputs, duplicate boundary and decision test

Essential local IDs are L729 for the prescribed coefficients and finite
divisor identities, and L732 for the audited lower obstruction. Neither
L730/L731 nor neutrality/density/saturation supplies an upper estimate.
Before comparing any proposed zero-sensitive upper threshold, read
`2026-10-21-openai-quasi-rh-overlap.md` in this directory and
`foundations/2026-10-quasi-riemann-input.md` from the notebook root.
These were not needed for the completed Proposition 4 audit and have
not been refreshed by this nomination.

Retain these recorded stops under ATTEMPTS: the 2026-11-03 dyadic-energy
contraction, signed neutral tail Gram-dual, prime-representer saturation,
and triangular-prefix-growth source stops. They exclude treating an
exact kernel, a projection bound, or an RH-equivalent growth statement
as an arithmetic upper estimate. They are not bans on interval-variance
arguments. The local match
`2026-11-01-signed-short-interval-hardy-correlation-screen.md` concerns
Hardy derivatives and smooth height windows; its opening scope was
checked and does not cover this prime-counting observable.

Continue only if a primary unconditional theorem and its exact range
yield a concrete comparison for the proposed reconstruction, with all
unpaid terms displayed and an independently testable threshold. If the
needed variance/covariance bound assumes RH, averages away the required
N-quantifier, or leaves the cumulative term uncontrolled, record that
specific exclusion and stop this mechanism. Do not derive and approve
an uncovered multiscale inequality in the same source turn.

LITERATURE_REASON: This new interval-variance mechanism has essential
unread primary hypotheses and transfer cases; the completed causal
lower-bound assessment does not cover it. No additional literature on
the already-audited Proposition 4 is requested.

Creative priority remains pending source coverage and a concrete paid
term. This nomination neither labels routine specialization creative
nor renews an exhausted mathematical exploration budget. No mathematical
exploration has been performed on this proposed mechanism.

Mathlib: the proposed transfer has not been identified or checked;
availability is unknown.

## Inspected statements and source decisions (2026-11-03)

1. Montgomery–Vaughan, *Multiplicative Number Theory III*, author-hosted
   working PDF, Theorem 28.6, (28.36), printed pp. 212–216 (PDF indices
   219–223), [source](https://personal.science.psu.edu/rcv4/Vol3/Vol3.pdf).
   For x>=2, h>=1 it states

       integral_0^x |psi(y+h)-psi(y)-h|² dy
       << x h² [(x^(1/6)/h)^(2/5)(log x)^c
                + exp(-(log x)^(1/3)/(c(log log x)^(1/3)))].

   Here c>0 is absolute; below we use only sufficiently large x and
   1<=h<=x. The proof treats small y dyadically, h>x/4 via the PNT,
   additive-to-multiplicative averaging, the full paired-zero sum,
   low/high ordinates, density bounds and the classical zero-free region.
   The h<=x^(1/6) case is explicitly trivial. Exercise 1(b), p. 217,
   explicitly assumes RH. This is a mutable working text with editorial
   placeholders, not a pinned published edition. No independent audit
   of its prerequisite density theorems is claimed.

2. Saffari–Vaughan, “On the fractional parts of x/n and related
   sequences. II,” *Ann. Inst. Fourier* 27(2) (1977), 1–30,
   [primary PDF](https://www.numdam.org/article/AIF_1977__27_2_1_0.pdf),
   Lemmas 5–6, pp. 19–25. Their (6.2) assumes
   N(sigma,T)<<T^(C(1-sigma))(log T)^B, C>=2. Lemma 6 gives
   the unconditional theta-increment estimate (6.19) for
   x^(1-2/C+epsilon)<h<=x, x>=3, with epsilon>0 fixed and a
   stretched-exponential saving over x h². It is a theta statement,
   not a silent psi substitution. Read the full (6.21) proof: it
   converts multiplicative increments to additive increments by
   averaging an auxiliary length. It does not reconstruct prefixes.
   The sharper (6.20) is RH-conditional and contains a printed h² typo.

   Grenié–Molteni–Perelli, “Primes and prime ideals in short intervals,”
   *Mathematika* 63(2) (2017), 364–371, proof of Proposition 1,
   [DOI](https://doi.org/10.1112/S0025579316000310), immediately before
   (7), explicitly corrects that h² to h. Their (7) also displays the
   additive/multiplicative averaging. Their prime-ideal result assumes
   the relevant RH and is not an unconditional substitute here.

3. Zaccagnini, “Primes in almost all short intervals and the distribution
   of the zeros of the Riemann zeta-function,” 2006 proceedings,
   [author PDF](https://people.dmi.unipr.it/alessandro.zaccagnini/psfiles/papers/Q429.pdf),
   Theorem 3.1, pp. 4–5: multiplicative pi variance, centered at
   theta*t/log t, for x^(-5/6-epsilon(x))<=theta<=1,
   0<=epsilon(x)<=1/6 tending to zero. Its bound is
   x³ theta²/(log x)² times (epsilon(x)+log log x/log x)².
   Section 3.1 explicitly labels its psi proof an outline and sends
   details to Saffari–Vaughan. It is not the 1998 Acta paper, whose
   direct and publisher downloads returned 403. No pi-to-psi transfer
   or theorem from the unread 1998 proof is imported.

## Why this does not yet supply a prefix estimate

This is a comparison of source conclusions, not a newly proved
impossibility theorem. The source statistic records differences across
one interval length, averaged over its starting point. A multiscale
prefix reconstruction must additionally handle products between its
chosen increments and the retained coarse/starting contribution. None
of the inspected statements estimates that proposed decomposition.
Within-statistic paired-zero correlations being paid does not pay those
different products. Even Cauchy–Schwarz would require a displayed
weighted reconstruction and a complete loss calculation; none is
asserted or approved by this review.

The source's strong RH-conditional variant must not be called
unconditional. Nor can an almost-all-prime conclusion replace a
weighted L² bound: exceptional contributions and the change from pi or
theta to psi remain part of any such application. The actual observable
is the discrete J_N^* with a *single* complex drift for each N, not a
separate freely centered value on every dyadic block. Fractional cells,
starting means, different weights and simultaneous ranges need explicit
accounting in any later theorem application.

The October register is reused with its stated trust qualifications,
not independently reverified. It records B_new=0.874957019420098946...
and the convenient boundary 34998281/40000000, with strict zero-free
half-plane and boundary retained. No exponent for J_N^* follows merely
from citing nonvanishing: that would require a justified quantitative
prime-error/contour application. In particular this source review
establishes no improvement over those imported conclusions, and no
RH-sized upper estimate. L732's lower obstruction remains intact.

The four earlier stops have different missing inputs (full update,
neutral tail, saturation, prefix upper growth) and remain recorded.
This review adds a specific source exclusion: interval reconstruction
in Lemma 6 is not reconstruction of a cumulative prefix. Park the latter
as an automatic import. It is not a general ban on multiscale methods.

## Bounded continuation selected, not executed

A coherent low-frequency profile is an independently testable way to
measure what the *available envelope alone* can exclude. The nominated
calculation uses F_b(x)=x+x^b (x>=0) and the exact L732 discrete drift
functional with psi replaced by F_b. It must check all 1<=h<=x in the
cited unconditional bound and optimize one drift, keeping b in (1/2,1).
No profile calculation, admissible b-range or asymptotic constant has
been obtained in this turn. A smooth model is not actual primes, a zeta
zero, a counterexample to RH, or a model satisfying the October analytic
input. Its purpose is only to falsify an inference from this variance
envelope alone, if possible. The exact scope/search is saved in
`2026-11-03-prime-variance-coherent-power-diagnostic.md` for separate
continuation approval. Creative actual-arithmetic work remains blocked
by absence of a concrete signed/covariance input; a routine diagnostic
must not be relabeled creative.

Searches also included “Selberg integral covariance primes multiscale,”
“Selberg integral prefix primes covariance,” “Selberg integral power
counterexample mean square,” and “Selberg integral psi(x)-x cumulative.”
No inspected primary result matched the requested prefix transfer or
this diagnostic. Search hits on pair correlation, generalized primes,
almost-prime existence and claimed RH proofs were not treated as
established inputs. This bounded search does not establish novelty.

Mathlib: full matching variance or prefix-transfer theorem not checked;
availability unknown. No Mathlib absence claim or formal verification.
