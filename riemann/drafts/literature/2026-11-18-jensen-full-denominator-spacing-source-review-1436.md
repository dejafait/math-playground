# Full real-witness denominator: source review1436

Completed literature-only record, 18 November 2026. Target: exactly
nomination1435's full denominator bound, with its unchanged coefficients,
integer-d scales, four tapers, shifts and own heat times. No estimate is
derived here and no lemma or mathematical script is changed.

## Saved orientation

Read C019y hypotheses and (1),(3)--(5), including audit1421;
C019z hypotheses, (2)--(4) and audit1435's denominator paragraph;
source-notes1410 and assessment1409; stops1407/1408/1431. The
audited D0 scale is Bq^2, not a full-norm bound. The unique vs
representation groups exact equal frequencies but does not pay
unequal-frequency integrals. The signed completion mechanism remains
parked at its three-attempt stop. Those stops do not prohibit this
different positive-norm target.

## Search and source scope

Actual bounded queries included `Dirichlet polynomial mean square sparse
coefficients primes products short intervals Gallagher lemma mean value`,
`Montgomery Vaughan mean value theorem variable coefficients Dirichlet
polynomial local spacing primes products`, `"prime products" "mean square"
Dirichlet polynomial`, `Teravainen almost primes almost all short intervals
II Lemma 3.4 sparse mean value arxiv`, `Heath Brown differences consecutive
smooth numbers theorem 4 pdf 2018`, `Iwaniec Kowalski lemma 7.1 x_m Y
Dirichlet polynomials pdf`, and `"mean square" "Dirichlet polynomials"
"time-dependent" coefficients`. Search snippets served as discovery only.
No exact matching estimate was located; this does not establish novelty.

Reused source-notes1410's ordinary-moment exclusions, rather than repeating
their comparison. Reopened the Montgomery--Vaughan statement to fix the
spacing convention. Newly read Matomäki--Teräväinen Section 3 statements
and proofs through Lemma 3.4; followed its Heath-Brown reference. Read
Heath-Brown's Theorem 4, both directions of Lemma 4 and its proof, Lemma 7's
good/bad-pair cases, and Section 4's two length regimes for (iii) and closing
argument for (iv). This is a theorem comparison, not a source-proof audit.

The NSF and Turku copies failed (502/403); arXiv supplied the same titled
primary paper with a fixed version. The smooth-number haag010 publisher
lead failed to open and remains unread. Iwaniec--Kowalski Lemma 7.1 was
located as the cited origin, but its full book text was not inspected.
Neither unread item is an assumed premise: the available primary papers
state the inequalities used for the comparison explicitly. Matomäki--
Radziwiłł's Annals Section 4 was also inspected as a supporting lead; no
result from it is imported here. No essential source is blocked.

## Inspected results (source letters are not notebook DAG IDs)

**A. Montgomery--Vaughan.** Reuse [*Multiplicative Number Theory II*,
author-hosted draft](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf),
G.16, (G.25)--(G.28), printed pp. 426--427, PDF pp. 438--439;
accessed 18 November 2026, draft version date unidentified. Distinct real
frequencies have local separation delta_n=min_(m!=n)|lambda_m-lambda_n|.
The bilinear Hilbert bound has constant 3pi/2 and weighted norms
(sum |x_n|^2/delta_n)^(1/2)(sum |y_n|^2/delta_n)^(1/2).
This controls a fixed finite bilinear form. It does not specify the
separations or amplitude variation of this witness. The full matching
bound is not an import of G.16.

**B. Matomäki--Teräväinen.** [*Almost primes in almost all short intervals
II*, arXiv:2207.05038v2](https://arxiv.org/html/2207.05038v2), 1 February
2023, Lemmas 3.2--3.4 and proofs, PDF pp. 12--13. For N,U>=1 and fixed
complex b_n, zero outside 1<=n<=N, Lemma 3.3 states

\[
 \int_{-U}^{U}\left|\sum_{n\le N}b_n n^{-it}\right|^2dt
 \ll U\sum_{n\le N}|b_n|^2+
 U\sum_{0<|j|\le N/U}\sum_{n\le N}|b_n b_{n+j}|.
\]

Its proof cites Iwaniec--Kowalski, *Analytic Number Theory* (2004),
Lemma 7.1, with Y=10U and x_m=log(m)/(2pi). Lemma 3.4 instead assumes
a product of fixed polynomials, one supported on integers in [M,U]
with coefficients of modulus <=1, the other on n~N with real coefficients.
It retains a maximum-coefficient square and an (NU)^eta factor;
the third term is removable only if N>=U^(2/3) or the sparse support
has size <=U^(1/3). Its proof normalizes coefficients, splits real signs,
changes the vertical line and invokes Heath-Brown 4(iii). It supplies
no moving-coefficient assertion. Lemma 3.3 is the more direct tool here;
its neighboring-coefficient sum remains to be estimated, not omitted.

**C. Heath-Brown.** [*The Differences Between Consecutive Smooth Numbers*,
arXiv:1808.02947v1](https://arxiv.org/html/1808.02947v1), 8 August 2018,
Theorem 4; Lemma 4 (pp. 10--11), Lemma 7 (pp. 14--15), Section 4
(pp. 15--17). Let U>=20, Mset subset (0,U] distinct integers, r=|Mset|,
|epsilon_m|<=1, and Q(s)=sum_(n<=N)q_n n^(-s), 0<=q_n<=1 real,
N a positive integer. Write I=int_0^U |(sum_Mset epsilon_m m^(-it))Q(it)|^2dt.
The unconditional 4(iii) gives

\[
 I\ll_\eta N^2r^2+(NU)^\eta(NrU+Nr^{7/4}U^{3/4}).
\]

The last term drops if N>=U^(2/3) or r<=U^(1/3). Part (ii) assumes
Lindelöf and is excluded. Part (iv), for the prescribed prime power
Q=(sum_(N^(1/k)/2<p<=N^(1/k))p^(-s))^k/k!, gives
I<<_k N^2r^2+r^2U+NrU. Lemma 4's real-coefficient upper bound counts
|log(m/n)|<=2pi/U with absolute weights; its reverse requires
nonnegative coefficients. Its triangular-kernel proof keeps nearby
unequal products. Lemma 7 retains good pairs and both bad-pair branches;
Section 4 retains their costs. These results do not erase them.

## Exact local comparison and bounded continuation

The local quantities below come from C019y/z, not from an application of
any source theorem. J_(vs)(Y)=a_v(Y)c_s is indexed by the original
unordered distinct witness-prime pairs and s<=R. Its coefficient norm
is paid at Bq^2 only after integration in D0. C019y (5) still contains
O(J,J) and the nonconjugate integral in the full denominator.

The following are obligations for research, **not established reductions**:

1. For A, pay separations for the complete set of vs, including different
   v and different s. Injectivity of vs only handles equality; the nearest
   unequal products are not bounded by a prime-counting assertion. Keep
   weighted amplitudes and their variation; the unweighted budget stopped
   in1407 is not a substitute.
2. For B, retain the full neighboring-product correlation, with the
   actual factors c_s and a_v, in the range prescribed by the source's
   length/time ratio. Decide how to use a fixed-coefficient theorem on
   the moving a_v(Y), without paying for freezing them by an uncontrolled
   absolute coefficient sum. A uniform pointwise small heat error alone
   is not an L2 error estimate at the required scale.
3. C(iv) has a relevant quadratic prime skeleton, but its prescribed
   prime square includes repeated primes and has fixed coefficients.
   Our original witness excludes repetitions and has two own-time heat
   factors; c_s has four tapers and complex shifts. No deletion,
   coefficient majorization, sign split or dyadic subdivision has been
   paid at an absolute constant. The N^2r^2 and r^2U costs remain even
   in the part with no eta loss. C(iii)'s eta factor cannot simply be
   called a constant or tuned with d while ignoring its implicit constant.
4. Any dominating complex-norm argument must justify its relation to
   S=W(A+conjugate A), retaining W; H^2 and W have different phases.
   Either pay the real norm directly or rigorously dominate it. No
   implication D>=D0, diagonal dominance, random phase model or actual-P
   estimate is available. These points are not derivations in this review.

The strongest directly useful inspected framework is B's full weighted
near-neighbor sum, with A as a possible separation alternative; neither
evaluates that sum for this array. C is a stronger product theorem worth
comparing, but not a direct bound at the required local scale. A future
specialization must explicitly compare **all** costs with Bq^2, not with
an unweighted source norm. A proof of failure of one sufficient spacing
budget would stop that budget only. An oversized upper envelope does
not refute D<=CBq^2.

Decision: EXPLORE for the unchanged target. This completes missing source
comparison and provides a concrete weighted-spacing attempt; it supplies
no new norm estimate, mathematical obstruction or beyond-source result.
No theorem reproof is needed: cite B/A/C precisely if used and prove only
the missing applicability and quantitative specialization. Full matching
Mathlib coverage is unchecked; no absence claim is made.

Continue only if one complete weighted-spacing/amplitude budget reaches
an absolute multiple of Bq^2, or a proved obstruction explains why that
specific budget cannot. Unbounded power/logarithmic losses fail the test.
Other numerator channels, E_P and actual-Xi transfer remain independent.
This review spends no mathematical exploration turn and does not reopen
or reset signed-completion1431. A new central creative mechanism is not
justified by the available resonant sign alone; source tools here concern
an independent norm obstacle. The next attempt develops these established
tools, rather than being labeled creative to satisfy a scheduling target.
