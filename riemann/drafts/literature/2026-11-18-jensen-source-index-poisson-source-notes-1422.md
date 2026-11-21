# Source-index Poisson — source comparison1422

18 November 2026. Literature-only work for the unchanged TARGET in
assessment1421. The completed decision is SPECIALIZE, subject to separate
approval before research. No source-index transformation, new bound,
lemma or mathematical script has been produced.

## Findings retained during review

Read C020c's hypotheses, (1)--(8) and the exact reindexing in its proof;
C019's heat bounds, source-entry equivalence and four channel definitions;
source-notes1418/1420; and stops1417/1419. A targeted search of the
17--18 November Jensen assessments, stops and histories located the prior
progression-Poisson comparison, but no assessed source-index completion.
The audited analytic reduction is an input; no resonance estimate is
being newly certified. The direct additive stop and endpoint-deletion
stop retain their stated scopes.

Primary statement located and read: J.-H. Evertse, *The functional equation
for the Riemann zeta function*, lecture-notes Chapter 9, author-hosted
`ant13-9.pdf`, Section 9.1, Theorems 9.1--9.2,
printed pp. 125--128, https://pub.math.leidenuniv.nl/~evertsejh/ant13-9.pdf .
For integers a<b and f holomorphic on a neighborhood of [a,b], Theorem
9.2 states, writing e(t)=exp(2*pi*i*t),

\[
 \sum_{j=a}^{b} f(j)=\frac{f(a)+f(b)}2+
 \lim_{K\to\infty}\sum_{k=-K}^{K}\int_a^b f(t)e(-kt)\,dt.
\]

The endpoints in the full finite sum have weight one; the Fourier
limit has half weights, compensated by the explicit term. The proof
of 9.1 treats unequal endpoint values separately; 9.2 then sums unit
intervals. Its statement supplies no parameter-uniform truncation rate.

Primary stronger comparison read: Montgomery--Vaughan, *Multiplicative
Number Theory II: Primes and Sieves*, author-hosted Math 571 Spring 2025
PDF, Theorem 16.18/(16.32) and its complete proof, printed pp. 24--25,
https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf .
This is a draft copy with editing marks; cite these locators rather than
assuming the numbering of a later publication. For real f with continuous
increasing f', alpha=f'(a), beta=f'(b), its statement is

\[
 \sum_{a\le j\le b} e(f(j))=
 \sum_{\alpha-1\le k\le\beta+1}\int_a^b e(f(t)-kt)\,dt
       +O(\log(2+\beta-\alpha)).
\]

The proof uses a zero-extended bounded-variation function, half-weight
lattice endpoints, symmetric Fourier sums, integration by parts, and
paired endpoint sine sums. It does not state the present weighted bound.

NIST DLMF 1.8.14's globally C2, integrable f and |f''| hypothesis does
not directly cover a sharp zero extension; 1.8.15 assumes continuity on
the half-line. These are comparisons, not licenses to smooth the floors.
https://dlmf.nist.gov/1.8#iv .

## Bounded search and reuse

Queries, including unsuccessful narrowing queries, were:

- `finite interval Poisson summation formula half endpoints bounded variation symmetric limit`
- `DLMF 1.8 Poisson summation finite interval`
- `"Theorem 9.2" "Poisson" "complex analytic"`
- `"finite Poisson" "bounded variation" theorem proof math edu`
- `"Poisson's summation formula for finite sums" analytic`
- `Montgomery Vaughan appendix D Poisson theorem D.3 pdf math lsa umich`
- `finite Poisson summation formula theorem Titchmarsh Lemma 4.7 weighted endpoints`

Read the primary Evertse statement and complete proof of Theorems 9.1--9.2,
including the unequal-endpoint case, before the larger source comparison.
The chapter has no version date displayed in the inspected passage;
the file identifier and access date 2026-11-18 specify the inspected copy.
Read the MVII title, Theorem 16.18 and full proof through its endpoint
sine-sum argument, not the subsequent stationary-phase development. The
author's Math 571 Spring 2025 page links this PDF. No later-edition
numbering, draft-proof certification or version date is inferred.

Also inspected Pongsriiam--Vaughan, *The divisor function on residue
classes I*, Acta Arithmetica 168.4 (2015), 369--381, Lemma 2.2, p. 370,
https://www.impan.pl/shop/publication/transaction/download/product/82214 .
It states an unweighted finite transform for C2 real phase with monotone
derivative between integers H1,H2, retaining those modes with error
O(log(2+max(|H1|,|H2|))). It cites Vaughan Lemma 4.2 and Titchmarsh
Lemma 4.7 rather than proving the formula there. Those original proofs
were not newly read. MVII supplies the inspected stronger comparison
with derivative-range width in its error; neither statement includes
the present heat weight or pays repeated outer coefficients.

Search results also led to a homework formulation, secondary summaries,
and papers about BV or arithmetic Poisson variants. None is used as a
theorem input. No inaccessible essential source remains: Evertse's exact
analytic finite formula is enough for a bounded specialization test.
The search is not exhaustive and supports no novelty inference.

Reuse source-notes1418's inspected BCR progression-Poisson cases, including
the zero mode and smooth large-mode treatment; its hypotheses still do
not cover these sharp entries. Reuse source-notes1420's quadratic-integral
coverage only if later quadrature is used. The arithmetic and resonance
assessments are unchanged. Extra browsing of the same ready inputs would
not resolve the present local truncation obligation.

## Outstanding local obligations (not claims proved in this review)

For both terms of C020c (5), a later attempt must recover the finite
source sum from the exact domains, check analyticity in its positive
continuous source variable, retain full lattice endpoints, and quantify
the symmetric dual tail before integrating or summing outer parameters.
The second term's m-dependent exterior phases must be combined with
its negative phase explicitly. No equality of the translated domains
is licensed. Zero modes, all retained modes, and endpoint corrections
remain in the proposed expression. A symmetric-limit identity alone
does not meet the required total o(Bq^2) error.

The exact source domains to check are those already recorded in C020c
(4): on J0, m is present at Z and n at Z+h; on J1, m is present at Z
and n at Z-h. Thus the review must cover the two different band intervals,
the unshifted and shifted n entries, and every m entry. The four tapers
and alpha remain in the outer c_r,c_s, not a replacement source law.
There is no coprimality premise in the finite Poisson theorem, so the
gcd cases of C020d are not exceptions that may be deleted.

For an integer upper cutoff, Evertse's theorem requires full endpoint
corrections. Empty and singleton source sums require separate exact
treatment, not application of its a<b statement. A noninteger continuous
upper limit is not the stated theorem; a later choice of such a limit
needs a justified version or derivation under covered Fourier-convergence
tools. Do not treat endpoint corrections as errors already paid by C019.

The prospective smooth source functions must be checked on positive
intervals avoiding zero and the logarithm's branch cut. For the second
channel, a holomorphic function agreeing with the conjugated heat factor
on the real interval is needed; conjugation of the complex argument is
not a holomorphy argument. Exterior logarithmic phases remain part of
that check. The review does not supply the transformed source function
or assert its full quantitative derivative bounds.

A mathematical attempt may import the finite identity and use ordinary
integration by parts and finite-sum rearrangement to test its remaining
specialization. It must give an explicit finite dual cutoff and a bound
uniform in the full Z domains and all outer indices. If it integrates
a symmetric limit, it must supply domination or uniform convergence;
alternatively it may first control a finite symmetric truncation and
pay its error before integrating. Partitioning at source-entry values
must retain all pieces. A bound for Z derivatives of E_j such as C019
(6) is not automatically a bound for derivatives in the source variable.
No numerical value, power saving, endpoint cancellation or interchange
is proved in this literature turn. Reproof of Poisson's general theorem
is unnecessary; only these changed weights, parameters and error budget
need local work.

## Decision, relevance and test

SPECIALIZE: the exact finite source identity is known, and quantitative
endpoint treatment has an inspected standard model. The target also
asks for a complete parameter-dependent dual expression with total
discarded error o(Bq^2). That conclusion is not a quoted theorem here.
Its local weight, endpoint and uniform-summation verification is the
identified difference, not missing essential literature coverage.

Main gap: L030--L032/C032a actual-Xi all-degree positivity, with every-degree
Jensen hyperbolicity and the unbounded exceptional-root deficit unresolved.
This intermediate transformation could reorganize the complete mixed
channel for a later fixed-quotient cBq^2 versus O(B) test. It does not
evaluate that channel, show its sign or supply actual-P transfer.

Continue only with a complete explicit dual expression retaining zero
and nonzero modes and endpoints, and an outer-summed o(Bq^2) discarded
error, or isolate the first quantitatively unpaid tail, boundary term
or hypothesis mismatch. A formal conditionally summed identity is not
success. Do not infer a global obstruction if this implementation fails.
Stops1417/1419 remain the original endpoint-deletion and direct-additive
stops; the source-first ordering is the different test under review.

Essential local inputs for continuation are C019 (6),(7),(9)--(14),
C019y (1),(3)--(5), C020c (4)--(8), and C020d (5)--(10) as the preserved
alternative grouping and stop evidence. The exact original integer d,
alpha, four tapers, own heat times, phases, floors, and common factors
must remain. C019y's resonance estimates, C020a/b, O(G,J), UA, denominator
and E_P remain independent and unpaid. Later actual-P use still requires
C019t's C019j/k/l/s,L320,L018/L021 contracts, none assumed here.

This is standard-method development, not a justified new central creative
mechanism. The unresolved joint arithmetic weights and independent
actual-Xi transfer/sign gaps block a responsible creative nomination
within this exact review. Full matching Mathlib coverage is unchecked;
no absence or formal verification is claimed. PROOF.md and DAG.md need
no change because no argument or mathematical input use has changed.
