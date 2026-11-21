# Signed endpoint-support source comparison1535

18 November 2026. Literature only; no kernel asymptotic is derived.
The exact reviewed target is assessment1534's saved TARGET.

## Inspected primary theorems

**Signed scalar support recovery.** Maximillian Newman, *On rigidity
of infinite exchangeable sequences*, fixed
[arXiv:2610.18992v1, 13 October 2026](https://arxiv.org/html/2610.18992v1),
Proposition1.12, equation(5), and its complete proof in Section3.1
were read. For a finite real signed Borel measure mu on [0,infinity),
write L_mu(lambda)=integral exp(-lambda*y) dmu(y). If
0=lambda_0<lambda_1<... has a positive lower gap and divergent
sum_(n>=1)1/lambda_n, the proposition gives

    mu restricted to [0,b)=0
      iff sup_(n>=1) exp(b*lambda_n)*|L_mu(lambda_n)|<infinity

for every b>=0. For nonzero mu it also identifies inf supp|mu|
with -limsup log|L_mu(lambda_n)|/lambda_n, with log0=-infinity.
The proof uses the bounded right-continuous cumulative function,
explicitly recovers the atom at zero, and justifies Fubini by total
variation. No endpoint density or one-sign neighborhood is required.
Its analytic input is Arendt–Batty–Hieber–Neubrander, *Vector-valued
Laplace Transforms and Cauchy Problems*, second edition, 2011,
Theorem2.8.3(i)-(ii), p103. That book theorem was not independently
read; this is inspected primary preprint coverage, not an independent
audit of every external input.

**Compact distribution transforms.** Lars Hörmander, *Supports and
singular supports of convolutions*, Acta Mathematica110 (1963),
279–302, DOI10.1007/BF02391861,
[primary scan](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5966-11511_2006_Article_BF02391861.pdf),
Section2, Theorem2.1, equation(2.4), and its printed proof, pp281–282,
were read. For compact convex Q with support function H_Q, the
Fourier-Laplace transform of a distribution supported in Q is entire
and obeys

    |fhat(zeta)|<=C*(1+|zeta|)^N*exp(H_Q(Im zeta)).

Conversely that global bound yields a distribution supported in Q.
The transform convention is exp(-i<x,zeta>). For measures the proof
uses total variation, hence includes signed, atomic and singular
measures. The converse invokes established sphere/cube versions,
then intersects containing spheres/parallelepipeds; their proofs were
not newly inspected. For Q=[-A,A], H_Q(v)=A|v|. This necessary
bound is the new source input for the nominated growth screen.
The first scan retrieval supplied the statement and printed proof;
subsequent line/screenshot retrievals timed out or supplied no
inspectable image. The formula was also legible in indexed extraction.

## Reused coverage and duplicate checks

The relevant statements/proof ranges of C032j/k/m were consulted:
fixed actual divisor and source qualifications, normalized primitives,
and common compact bounds, including the removable spatial quotient.
C032n's equation and limitations were read; its later independent
audit remains pending. No completeness claim is extracted from it.
Ledger1532's unchanged Gaussian, Haslinger and signed scalar duality
coverage is reused. C032l and finite stop1302 do not cover arbitrary
signed width integrals. Direct recursion stop1534 stays in force.

Assessment1266 was consulted only at its transform comparison:
DLMF/Liehr require actual transforms; Ransford's already inspected
Theorem1.1/Lemma2.1 and Sections3–5 concern complex L1 convolutions.
No L1 density for eta is imported. The signed-measure source above
fills that particular scope issue, not the representation issue.
Stops1515/1525/1527 are preserved and not reopened or treated as global
bans. No sibling notebook was read.

## Exact target comparison

Here K_sigma(w)=exp(-E_sigma(w))*sinh(O_sigma(w)), and
J_eta(w)=integral_[1,2] K_sigma(w) deta(sigma), for arbitrary finite
real signed Borel eta. Neither inspected theorem identifies J_eta as
a Laplace transform of eta, an injective weighted image of eta, or a
convolution with nonzero compactly supported input. No such identity
is established in C032j/k/m/n.

A reduction must specify the transform variable, rate coordinate and
transformed input, including finiteness and interchanges. It must
also prove that a mass-one eta gives nonzero transformed input.
A transform of a different, possibly zero object supplies no
contradiction. An approximate reduction additionally needs control of
the integrated signed remainder strong enough for support recovery.
Individual-width asymptotic dominance or a density-only argument
supplies none of these hypotheses. This records a scope mismatch,
not a theorem that all reductions are impossible.

C032m's exp(K_M) compact-disk bound is not a proved Paley-Wiener
bound of fixed polynomial order and exponential type. Nor does its
size prove violation: a large upper envelope is not a lower bound.
Entire dependence and finite-family independence do not decide
compact signed cancellation. A global growth screen can test one
necessary condition of a direct uniform transform interface. Passing
it would leave identification, injectivity and signed transfer unpaid;
failing it would reject only that interface. Actual-Xi positivity,
positive mixtures and unsmoothed realization remain separate.

Conclusion: the signed endpoint theorem exists, but direct citation
does not settle the nonlinear target. Park immediate endpoint-support
import and nominate the bounded growth screen separately. No new
asymptotic, support lemma or mathematical script was produced.

## Search and access record

Queries included `Laplace transform compact signed measure support
endpoint limsup theorem`; `Paley Wiener theorem finite signed measure
support Laplace transform indicator`; `Laplace transform signed support
limsup measure compact`; `Laplace transform support complex measure
endpoint`; `exp(-E sinh smoothing Xi`; `Some positivity properties of
Riemann Xi under smoothing mixtures support`; `sinh Gaussian mixture
identifiability signed`; `difference of exponentials entire finite
order`; and `Gaussian signed mixture Paley-Wiener`.

No inspected matching nonlinear-kernel theorem was found; this does
not establish novelty. Finite-mixture results and *Partial Differential
Equation Barriers to Identifiability in Infinite Mixture Models* were
unread leads, not inputs or grounds to reopen the PDE route.
The Springer landing page confirmed book edition/chapter scope only;
no access was purchased. The original scan and Newman's primary
theorem/proof supply the stated coverage. Full matching Mathlib
coverage remains unknown. No theorem from this review is being applied
to K or imported into a new canonical lemma.
