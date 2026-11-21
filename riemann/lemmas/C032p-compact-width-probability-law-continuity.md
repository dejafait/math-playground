# Corollary C032p: compact-width probability-law continuity (imported tools)

## Hypotheses

Retain the actual-zero Gaussian half-variance convention and all the
fixed-v1 preprint, divisor, counting, finite-zero and heat-positivity
qualifications of C032j. For each sigma in W=[1,2], let nu_sigma be
precisely its Borel probability law on X=[0,infinity), with

    integral_X exp(-s*u) d nu_sigma(u)=exp(-B_sigma(s)), s>0.

Use C032k's identification B_sigma(w^2)=b_sigma(w) for real w>0,
its entire lift with b_sigma(0)=0, and C032m's joint continuity of
(sigma,w) -> b_sigma(w) on W times C, including the width endpoints.
The spaces W and X have their usual relative Euclidean topologies.

No density, absence of an atom at zero, finite positive exponential
moment, RH, or nonnegativity of the smoothed zero profile is assumed.
The probability laws and heat positivity are qualified source imports;
this result does not independently verify those preprints or their
finite-zero data.

## Conclusion

The map sigma -> nu_sigma is continuous for the weak topology of
probability measures on X: for every bounded continuous real f on X,

    sigma -> integral_X f(u) d nu_sigma(u)

is continuous on the closed interval W. For every Borel subset A of X,

    sigma -> nu_sigma(A)

is Borel measurable. The latter assertion is measurability, and does
not assert continuity of evaluations at arbitrary sets or atoms.

This establishes the probability-family interface only. No signed
width mixture is constructed here; its positivity, full odd-transform
cancellation, moment conclusions and unsmoothed actual-Xi transfer
remain separate questions. In particular no all-degree positivity
in L030-L032/C032a follows.

## Proof

### Imported theorems and their scope

Use Ante Mimica, *Laplace transform*, Dresden course notes,
27 April-1 May 2015, [author PDF](https://web.math.pmf.unizg.hr/~amimica/lt.pdf),
Corollary 2.2 and its proof, printed p.13. For probabilities on
[0,infinity), pointwise convergence of the Laplace transforms at all
s>0 to phi, with phi(0+)=1, supplies a probability law with transform
phi and convergence of distribution functions at its positive
continuity points. Proposition 1.8, printed p.9, gives uniqueness of
the law from its Laplace transform. No moment, density or separately
assumed tightness hypothesis is required. The standard probability
corollary is imported; apparent typographical errors in the more
general proof are recorded in source notes1539 and are not formulas
used here. In particular its mass identification uses the zero-limit
formula in Proposition 1.4(ii), printed pp.6-7.

Use also the standard Helly-Bray criterion, as stated in Joel A.
Tropp, *Probability Theory & Computational Mathematics*, Fall 2024,
typeset 23 January 2025, [author PDF](https://tropp.caltech.edu/notes/Tro24-Probability-Theory-LN.pdf),
Theorem 17.22, printed p.260; the quantile-coupling result is Theorem
17.39, printed p.268. For probability laws on R, convergence of
CDFs at every continuity point of the limiting CDF gives weak
convergence. The half-line/zero interface is checked below rather
than silently included in a citation about positive continuity points.

For the probability-space topology and evaluations use Tobias Fritz,
Paolo Perrone and Sharwin Rezagholi, *Probability, valuations,
hyperspace: Three monads on Top and the support as a morphism*,
[arXiv:1910.03752v3](https://arxiv.org/pdf/1910.03752v3),
16 September 2021 submission, PDF dated 17 September 2021:
Definitions 4.1/4.6 and Propositions 4.7/4.10, printed pp.39,41-43.
Their P X consists of tau-smooth Borel probabilities with the
A-topology. The Polish-space case is covered in Section 4, printed
p.39. Proposition 4.7 identifies that topology with integration of
bounded continuous real functions on completely regular Hausdorff X.
Proposition 4.10 states Borel measurability of evaluation at every
Borel subset of X, without continuity at arbitrary such subsets.
The source statements and essential proof cases were inspected in
review1539; its coverage and source qualifications are reused. These
are known general results, not theorems reproved here.

### Transform convergence, normalization and identification

Fix any sigma in W and any sequence sigma_n in W converging to sigma.
For each s>0, C032j/k and C032m give

    L_n(s):=integral_X exp(-s*u) d nu_sigma_n(u)
          =exp(-b_sigma_n(sqrt(s)))
          ->phi(s):=exp(-b_sigma(sqrt(s)))
          =integral_X exp(-s*u) d nu_sigma(u).

Here sqrt(s) is the positive real square root only. The limit is at
every positive s. C032k's entire b_sigma and b_sigma(0)=0 give
phi(s)->1 as s decreases to zero. Thus the limiting normalization is
one, not an unverified limit of masses inferred solely from positive
parameters. Each input law is a probability on X. Mimica Corollary
2.2 applies and supplies a limiting probability with transform phi;
Proposition 1.8 identifies it uniquely with nu_sigma. Consequently
its CDF convergence conclusion concerns this particular nu_sigma.
No additional choice of a law with the same transform is made.

### The half-line and zero endpoint

Regard these laws as probabilities on R supported on X, and write
D_n(x)=nu_sigma_n([0,x]) and D(x)=nu_sigma([0,x]) for x>=0, and
D_n(x)=D(x)=0 for x<0. The cited corollary gives D_n(x)->D(x)
for every positive continuity point of D. At negative points the
convergence is immediate. It remains to check zero only if D is
continuous there, which is equivalent to nu_sigma({0})=0.

In that case choose positive continuity points h_k decreasing to
zero. Such points exist because a probability CDF has at most
countably many jumps. Continuity from above of nu_sigma gives
D(h_k)->nu_sigma({0})=0. For each k,

    0<=liminf_n D_n(0)<=limsup_n D_n(0)
      <=lim_n D_n(h_k)=D(h_k).

Letting k increase proves D_n(0)->0=D(0). If nu_sigma has a zero
atom, zero is a discontinuity of the CDF on R and no convergence of
that atom is required by Helly-Bray. Hence all required continuity
points on R have been checked, in both cases. The criterion yields
weak convergence of the laws on R.

For a bounded continuous f on X, the extension

    f_tilde(x)=f(max(x,0)), x in R,

is bounded continuous on R. Since all laws are supported on X,
weak convergence on R gives convergence of their integrals of f.
This is precisely weak convergence on the relative half-line X;
it does not assume f vanishes at infinity or that X is open in R.

The argument applies to every sequence converging in W, including
sequences tending to 1 or 2. For each such f the real function
sigma -> integral f d nu_sigma is sequentially continuous on the
metric space W and hence continuous. The weak topology is the
initial topology of these integrals, so the map into probability
laws is continuous. No metrizability assertion about that law space
is needed for this sequential-to-continuous step.

### Borel evaluations

X is a closed subset of the complete separable metric space R,
so it is Polish. It is also completely regular Hausdorff, with its
usual metric topology. Its Borel probabilities therefore belong
to the P X of the cited Section 4. Proposition 4.7 identifies its
A-topology with precisely the weak topology just used. Thus the
map W -> P X proved continuous above is continuous in the topology
required by Proposition 4.10.

For each Borel A in X that proposition makes ev_A: P X -> [0,1],
ev_A(mu)=mu(A), Borel measurable. Its composition with the continuous
map sigma -> nu_sigma is Borel measurable on W. This holds for all
Borel A, including {0}, without upgrading any evaluation to a
continuous function. All probability, topology and normalization
hypotheses have been matched. This completes the applicability audit.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib theorem
is used. General weak-convergence, Laplace-transform and Borel-kernel
APIs are not asserted to cover this qualified family or these source
imports. The result is a local application of known probability and
topology theorems, not progress beyond the inspected general results.
