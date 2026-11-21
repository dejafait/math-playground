# Shifted sinc product: source comparison2244

21 November2026. Literature-only review of nomination2243. No new
model identity, convergence assertion, inverse sign, moment bound or
growth estimate is established here. The fixed target is preserved.

## Saved source extraction

Rick Durrett, *Probability: Theory and Examples*, version5,11 January2019,
[author PDF](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf),
Theorem2.5.6, printed pp84-85: independent centered variables with
summable variances have an almost surely convergent series. Read the
whole proof, including the maximal-inequality passage to the infinite
tail. Theorem3.3.14, printed p130: an integrable characteristic function
has the bounded continuous inverse density
`(2pi)^(-1) integral exp(-ity) phi(t)dt`. Read its Fubini and dominated
convergence proof. These inputs cover nonidentical variables and the
angular convention, but their hypotheses must be verified for the
proposed variables. Neither statement supplies strict positivity or
weighted derivative tails. The different theorem numbers in other
editions must not be substituted.

Byron Schmuland, *Random Harmonic Series*, *Amer. Math. Monthly*110(5)
(2003),407-416, DOI10.1080/00029890.2003.11919978,
[14-page manuscript](https://web.williams.edu/Mathematics/sjmiller/public_html/105Sp11/addcomments/Schmuland_RandomHarmonicSeries.pdf):
read section2, manuscript p2, and sections4-5, pp4-7. The paper treats
independent random signs with harmonic coefficients, regrouped into
independent uniforms on `[-2/(2j+1),2/(2j+1)]`. Its proof controls the
regrouping in mean square, not by arbitrary rearrangement. Section5
uses finite-head decay of the characteristic product and Fourier
inversion to establish a smooth density. This is substantial overlap
with the proposed smoothing method, but its widths differ, and it
does not state the nominated every-real-zero-prefix conclusion.

Section2 also proves full support by a finite prescribed-sign event
and an independent small tail. This is a support argument for that
law, not an automatic pointwise-positive-density theorem for G.

Wassily Hoeffding, *Probability Inequalities for Sums of Bounded Random
Variables*, UNC Institute of Statistics Mimeo Series326,May1962,
[repository manuscript](https://repository.lib.ncsu.edu/bitstreams/d0e6ed15-3e1c-432f-8419-e55ffb6f3171/download),
Theorem2, printed p6, formula(2.10): independent `a_i<=X_i<=b_i`
obey, for t>0,

    P(S-E S>=nt)<=exp(-2 n^2 t^2 / sum_i(b_i-a_i)^2).

Read Lemma1, p10, and the proof of Theorem2, pp12-13, formulas
(3.11)-(3.17). The bounded-variable exponential-moment input is
`E exp(h(X-E X))<=exp(h^2(b-a)^2/8)`; the proof uses convexity and
the logarithmic second-derivative bound1/4. Nonidentical ranges are
allowed. Nondegenerate intervals are understood; constant variables
can be omitted. The manuscript's formula(3.16) has damaged exponent
placement in the web extraction; (3.12),(3.15),(3.17) retain the needed
bound unambiguously. Cite this accessible version's numbering, not
the journal version's section4 numbering. The finite-sum result does
not justify an infinite-limit exponential-moment interchange. Fatou
or uniform integrability must be stated where needed later.

NIST DLMF [1.10(ix)](https://dlmf.nist.gov/1.10.ix), equations1.10.20-21
and the complete following conclusion: analytic factors `1+a_n(z)`
with a summable uniform majorant for `|a_n(z)|` have an analytic
product; it vanishes only at zeros of factors. The logarithmic
majorant version has the same conclusion. Apply on each compact
domain with its own majorant. Read the nonzero-tail convention
before the test and [1.10(x),1.10.23-24](https://dlmf.nist.gov/1.10.x).
The notes attribute the product section to Titchmarsh1962,pp13-19,
246-250; that book proof was not independently inspected. The DLMF
statement is the imported input. It gives no growth-order estimate
for the nominated product without an additional bound.

Alexandre Eremenko, *Zeros and coefficients*, author manuscript dated
28 October2015, [p2, item3](https://www.math.purdue.edu/~eremenko/dvi/legendre2new.pdf):
read the definitions of maximum modulus, order and finite normal
type. In particular order is `limsup log log M(r)/log r`. Only these
definitions are used; no later theorem or type bound is imported.
An order-one claim requires both upper and lower growth control,
and does not itself assert exponential type or Xi-scale asymptotics.

## Reused finite inputs and why specialization is still necessary

Source notes2239 already inspected DLMF5.12.5,5.12.1,5.5.1,5.5.3,
5.2(i),4.22.1,4.14.1-2 and Tao2009 Fourier convolution/inversion.
These unchanged assessments are reused. Read C919p through its
compact-inverse and tail sections this turn: (8)-(10) give the exact
normalized finite sinc-removal identity, including the nonzero
removable values. Its Gaussian argument for derivative tails depends
on a fixed compact convolution measure. It cannot be cited as an
infinite-convolution tail proof. The later application must justify
scaling, grouping of the globally ordered prefix into within-factor
initial segments, and reconstruction of one fixed function.

The C919p input contains no Xi or numerical backend premise. The
atomic cosine factor is already known, as documented in2239, and no
novelty for that factor or these probability/Fourier methods is claimed.

## Obligation-by-obligation comparison, not a derivation

1. Random-series existence and its real characteristic product:
   Durrett2.5.6 is the appropriate import after checking centering,
   independence and summable variances. The pointwise characteristic
   limit requires bounded convergence. L2 control and identification
   of moments must be justified rather than inferred from weak convergence.
2. Entire product, exhaustive real roots and retained nonreal zero:
   DLMF1.10(ix) supplies the no-extra-zeros principle after a local
   majorant is proved. The prescribed irrational shift must separately
   exclude coincident real roots. Local finiteness, ordering, simplicity
   and all removable values remain model-specific checks. No statement
   about these checks is proved by this review.
3. All-prefix nonnegative inverses: C919p's finite identity supplies
   the within-factor tool. A fixed finite prefix must affect only
   finitely many factors, and each affected factor's removed roots must
   form its own initial segment. Those assertions remain obligations.
   The infinite residual must represent a probability law; finite
   approximations with a changed G do not answer the question.
4. Smoothness and strict positivity: Schmuland section5 gives the
   finite-head smoothing method and its inversion proof. His widths
   differ and no deflation is included. For this candidate one must
   prove the requisite real-frequency decay for each derivative and
   strict positivity at every point, using a positive finite-head
   density together with support control of its independent remainder.
   Full support of a measure alone does not imply its density is
   strictly positive. Nor does uniform convergence of positive densities.
5. Exponential derivative weights and endpoint decay: Hoeffding covers
   the probability-tail tool after its hypotheses and limit step are
   checked. It does not control derivatives of a density. The later
   proof must combine a sufficiently smooth compact finite head with
   the tail law and bound each derivative; the head may depend on the
   derivative order and the fixed prefix. Weighted L1 integrability
   and weighted pointwise limits are separate required conclusions.
6. Prefix-uniform second moment: bounded supports and the cited finite
   identity provide possible tools; neither source states the desired
   uniform constant for this construction. A later proof must give
   a single explicit finite bound independent of the prefix, justifying
   its use at the infinite limit. Uniformity in all derivative constants
   is not part of the nomination.
7. Exact order one: the complex-product tool and elementary sine bounds
   permit a direct finite-head/infinite-tail growth comparison. A
   numerical fit or only an order upper bound cannot meet the target.
   Each finite quotient needs its own upper and lower bounds. No
   finite exponential type is required or approved; the distinction
   matters for interpreting any subsequent generic obstruction.

These are applicability and assembly tasks using ordinary imported
tools. They justify SPECIALIZE for a later REPRODUCTION attempt,
not importing a theorem already asserting the full countermodel.
No source inspected here contradicts a simultaneous requirement;
this is not a proof that they can all be met.

## Discovery, overlap and failures

Queries included: infinite product sinc harmonic probability; random
harmonic series uniform density; Kolmogorov convergence sum variances
Durrett; infinite product sinc random uniform series entire function
order; characteristic functions removing zeros sinc; characteristic
functions division real zeros positive definite; infinite sinc
j+sqrt; Hoeffding1963 bounded variables; and the exact two paper titles.
The exact-phrase searches did not locate a matching shifted-prefix
theorem; this does not establish novelty or nonexistence. Search
snippets and nonprimary summaries were used only as discovery leads.

Kent E. Morrison, *Cosine Products, Fourier Transforms, and Random Sums*,
*Amer. Math. Monthly*102(1995),716-724,
[arXiv:math/0411380v1](https://arxiv.org/html/math/0411380),17 November2004,
section5.2: read the random-harmonic-product discussion. It explicitly
leaves some limiting analysis informal and presents numerical
conjectures. It is historical overlap, not the needed rigorous import;
Schmuland's later proof and Durrett supply the limiting tools above.
No conjectured numerical equality is used.

The stronger Csordas1309.0055v2 Theorem3.7 comparison in2239 is reused:
positive definiteness of every weighted correlation kernel is a
different assertion from direct quotient inverses. No implication
between the two is imported. The optional Kwasnicki exponential-law
lead in2243 is unnecessary because independent uniform-series
coverage is now accessible; its primary text remains unread here.

Local duplicate searches used all-prefix/sinc/infinite-convolution
terms in the active literature and attempts directories, followed by
the exact source names and selected paths. Inspected the canonical
C919p finite-factor ranges and the recorded compact-spline and
approval-loop stops. The latter closes repeated work on the accepted
order-two model, not the new order-one question. The earlier finite
compact-spline result loses strictness and has multiplicity defects;
its stop does not establish impossibility of this different fixed
infinite product. No sibling notebook or cross-notebook input was used.

The RPI journal-PDF endpoint timed out twice. A shell download from
NCSU failed DNS resolution; the primary manuscript was nevertheless
accessible through the web tool, including Theorem2 and its relevant
proof. These are resolved access differences, not a source blocker.
No API key, paid service or changed infrastructure was used.

## Decision and limits

Essential ordinary-tool coverage is adequate for the fixed candidate;
the mathematical conclusions remain unproved. A source-covered
specialization should import the cited theorems and prove only the
listed differences. It should not reprove Kolmogorov convergence,
Hoeffding concentration or the cosine-power integral. Import a full
matching result if later identified, without claiming the bounded
search certifies originality. Full matching Mathlib coverage and
supporting theorem names remain unchecked.

The exact mathematical continuation is recorded in assessment2244.
Continue only if every listed property holds for every finite prefix
of this single G. A genuine contradiction abandons this fixed
candidate; a failed estimate alone is inconclusive and must be saved.
Even success only tests the order-one generic bridge. Actual-Xi
arithmetic structure, arbitrary iteration and mixed positivity remain
independent unresolved inputs. No RH candidate is asserted. No new
central creative mechanism is justified by these sources; this is
an ordinary-method specialization, not a creative label for scheduling.
