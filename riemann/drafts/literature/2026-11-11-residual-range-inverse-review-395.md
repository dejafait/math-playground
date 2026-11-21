# Direct norm on the coupled residual range — nomination after audit395

TARGET: Assess source coverage for a direct bound on C997y's centered-moment functional over C997s's coupled complete-kernel span, using residual-specific Turan–Remez or derivative inequalities, with operator-norm rate strictly below 1/64.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step396 searched exponential-polynomial complex-exponent derivative/Remez inequalities, coupled coefficients and Laguerre observability; inspected Protasov arXiv:2209.12250v1, Erdelyi Sbornik208(2017) Theorems2.19/2.20/2.22 and Friedland arXiv:2606.24823v1; reused review312 and narrowly checked C997s/t/y and stops340/341. Exact queries and reading scope below.
SOURCE_EVIDENCE: Protasov https://arxiv.org/pdf/2209.12250v1 pp3–9, Theorem1/Conjecture1; Erdelyi https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=8670&what=fullteng pp442–443, Theorems2.19/2.20/2.22 and norm definition; Friedland https://arxiv.org/pdf/2606.24823v1 pp2–3,6–7, Theorems1.1/1.2 and Lemma3.2; reused primary contracts in review312 rather than retrieving Nazarov again.
COMPARISON: The inspected results control larger exponential-polynomial spaces, real-exponent half-line derivatives, or complex-exponent weighted half-line norms; none supplies this outside-interval germ functional on the coupled span at cost below exp(n/64). The new disk-growth preprint retains explicit growth assumptions and full exponential order. This is an import limit, not a lower bound on the actual norm.
GAP: No adequate match was established in the bounded search: the coupled-span interval-to-germ norm and its growing-order constants remain unproved; neither the claimed upper rate nor its negation follows. Source scope is assessed sufficiently for an EXPLORE attempt, without certifying originality or assuming additional coverage.
REASON: Park automatic Turan–Remez/Markov import and the real-exponent sharp-constant shortcut. A direct coupled-span representing-measure test is a distinct bounded continuation; its new nomination is saved in review396 for separate next-turn approval. No inequality was derived and no lemma or mathematical script was changed in this literature-only step.
LITERATURE_REASON: The hypothesis changes from arbitrary bounded analytic functions with a global scalar prior to the specific finite-dimensional complete-kernel span and a growing-order functional; review393 does not cover that change.
SCOPE: Source review only, retaining the original n, grid, complex cap, target and complete kernel. No generic-disk tuning, numerical fitting, new lemma or mathematical script until separate coverage is ready.

## Precise proposed discriminator

For integer n>=2 let S_n be the complex linear span of k_n(c,z_star)
and k_n(c,gamma_j), 0<=j<=n, with C997s's entire kernel,
z_star=1+i/8 and gamma_j=15/8+j/(4n). Define M_n(f) by the finite
germ expression on the right side of C997y(13), with
D(c)=-exp(nc/4)f(c)/2, m=ceil(sqrt(n)) and the same b_k,v_j,d.
No new inverse inequality or extension of C997y's theorem is proved here.

The quantitative target for a future, separately approved attempt is

    sup_{f in S_n, f != 0} |M_n(f)| / ||f||_{C([7/4,9/4])}
                  <= C exp((1/64-eta)n)

for fixed C<infinity, 0<eta<1/64 and all sufficiently large n.
Check well-definedness, the exact target direction, full multiplicities
and every constant needed for this bound. The norm is on the actual
span, not a larger space with independently variable endpoint
coefficients. If proved, it would combine with C997y's existing cap
gap to give a lower certificate at the required scale. This conditional
purpose is not a new bound for E_n. The original l1 cap cannot be
replaced by an l2 norm or prescribed jets without a new assessment.

## Three mechanisms compared for recovery

1. **Direct functional norm on the residual range — selected.**
   C997t(6) gives the complete endpoint representation, including both
   beta terms and the lower window. Its mandatory-root calculation (8)
   has degree 4(n+1)(n+2), so the free-coefficient count is not a justified
   Remez order. The new question is whether source theorems retain the
   coupled coefficients and control the specific germ functional.
   This can be tested by a precise theorem comparison or, after approval,
   a paid norm estimate/counterexample; no such estimate is assumed.
2. **Spectral cutoff of the continuum dual — retain its stop.**
   Stops340/341 identify the unpaid actual-target spectral tail.
   Algebraic regularization or sampled singular values do not pay it.
   This audit supplies no new tail estimate, so another Gram damping
   or cutoff attempt is not selected.
3. **Actual-Xi local signed margin — retain the independent gap.**
   The narrow L727 records show its conceptual audit already completed
   in step226, despite the older overview marker. Its tail bound does
   not establish a local signed margin. Repeating its normalization
   or audit is a duplicate; no new margin input is supplied here.

The local comparisons are [review312](2026-11-10-adaptive-slope-spectral-separation-review-312.md),
[stop340](../../ATTEMPTS/2026-11-11-scalar-gram-dual-residual-limit-340.md),
[stop341](../../ATTEMPTS/2026-11-11-response-spectral-cutoff-unpaid-tail-341.md)
and [L727 stop](../../ATTEMPTS/2026-11-03-l727-tail-only-signing-stop.md).
C997y's [scalar-prior stop](../../ATTEMPTS/2026-11-11-slope-origin-scalar-prior-stop-393.md)
remains in force on its exact scope. No historical stop becomes global.

## Source comparison boundary and test

Review312 inspected Friedland–Yomdin, *An observation on the
Turan–Nazarov inequality*, Studia Mathematica 218 (2013), 27–39,
Theorem1.1 p27 and Definition1.2/Theorem1.3 pp28–29 with the proof
and Lemma2.1 p30. Its displayed theorem covers finite sums of simple
exponentials on a real interval and a positive-measure subset. It does
not state the proposed confluent, coupled-span derivative bound.
Order and exponent-growth factors must remain explicit; a repeated-root
limit needs justification. Stronger results and obstructions need review.

Kovrijkine, *Some results related to the Logvinenko–Sereda theorem*,
math/0012186v1 (19 December 2000), Lemma1/proof pp4–6, uses a disk
analytic function and a paid growth maximum. Using C997y's stopped
scalar prior with it is not a new mechanism. It helps only if a new
residual-specific growth control is supplied. Aldaz–Kounchev–Render's
repeated-root basis supports C997t's representation, not this norm.
The original Nazarov PDF's formula extraction was damaged in review312;
do not repeat that retrieval. Use accessible primary statements or
identify a genuinely essential missing case. This nomination adds no
external search or new theorem claim; source scope is incomplete.

Continue only if the comparison supplies a concrete inequality or
technique respecting the coupled span that can be paid at the stated
rate, or a distinct bounded test of that norm. If the available theorem
only controls the larger free endpoint space, has uncharged derivative
hypotheses, or gives an insufficient rate, record the precise import
limit and park that application. Such a failure is not a lower bound
on the actual norm or a disproof of the upper target for E_n.

Essential prospective local inputs: C997c's kernel, C997s's objective,
C997t(6)'s endpoint representation and C997y(13)'s functional and
audited cap gap. C997w/x are contrasts, not all-coefficient stops.
Full matching Mathlib coverage is unknown and unchecked. There is no
cross-notebook input. C997a(8), selected/both-sign transfer,
assay/reconstruction, complements/regulators, L993, L984(H),
L966/L968 forcing and actual-Xi positivity remain open.

The preceding text is the preserved step395 nomination. The completed
step396 review and its qualifications follow; no mathematical attempt
was performed during this review.

## Completed source comparison — step396, 11 November 2026

### Exact local contract and duplicate checks

Read C997s's hypotheses/conclusion, C997t(4)–(6), and C997y's
hypotheses, conclusions and proof through (13). The proposed functional
is defined by the germ of the entire function f itself, with the gauge
D=-exp(nc/4)f/2. Its definition does not require choosing a unique
coefficient representation. The relevant orders and locations are
already explicit in C997y: positive coefficients through m+1 at c=0,
m=ceil(sqrt(n)), whereas the observed interval is [7/4,9/4].
No quantitative continuity estimate is inferred here. C997t's endpoint
polynomials and shared coefficients must be retained. Its band
annihilator degree 4(n+1)(n+2) is not a claim that this smaller coupled
span has that dimension.

Review312 already assessed generic Turan–Nazarov, analytic disk-growth
and Hahn–Banach/Riesz tools. Stops340/341 leave the actual target
spectral tail unpaid. C997y's scalar-prior stop leaves a data-specific
inverse open. This review does not repeat the completed L727 audit,
the finite paid-leakage experiments, or constant-coefficient annihilation.

### Primary derivative results: hypotheses matter

V. Yu. Protasov, *Generalized Markov-Bernstein inequalities and stability
of dynamical systems*, [arXiv:2209.12250v1](https://arxiv.org/pdf/2209.12250v1)
(25 September 2022), explicitly includes repeated exponents as
t^r exp(-h t) on pp3–4. Theorem1, p6, compares derivative extrema for
positive **real** exponent vectors and a monotone norm on C_0(R_+).
Its proof, pp6–8, uses real Chebyshev zero/sign structure. The uniform
bounds in Theorems2–3, pp9–10, retain the real-exponent restriction;
Conjecture1, p5, asks for equality with the complex-exponent extremum.
The discussion on p3 explicitly identifies the complex comparison as
unproved there. This is not a claim about its present global status.

Thus repeated roots alone do not supply coverage: our endpoint
exponents are complex, the supplied norm is on a finite interval, and
the desired derivative germ is outside that interval. A half-line
bound is not supplied by our data. No real-exponent reduction,
conjugate-pair positivity, or use of the conjecture is authorized.
Only the stated contracts and the relevant real-sign proof mechanism
were inspected; no theorem from this paper is imported into a lemma.

T. Erdelyi, *Inequalities for exponential sums*, Sbornik: Mathematics
208(3) (2017), 433–464, [DOI10.1070/SM8670, published English PDF](https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=8670&what=fullteng).
On p442, Theorem2.20 bounds the interval derivative norm by
(1+epsilon_N)(108N^5+sum lambda_j^2)^(1/2) times the interval norm
for sums sum a_j exp(i lambda_j t) with **real**, ordered lambda_j.
Theorem2.19 is an interior derivative estimate for the same class.
Neither statement covers our general complex endpoint spectrum.
Theorem2.22, p443, does allow complex lambda_j with Re(lambda_j)<1/2,
but both norms are L2([0,infinity), exp(-t)dt), as defined immediately
before it. Its derivative constant is max|lambda_j| plus the square
root of sum_(j<k)(1-2Re(lambda_j))(1-2Re(lambda_k)).

The complex result therefore requires a weighted half-line norm we
have not paid; it is not an interval-to-origin estimate. Confluent
passage and restriction to coupled coefficients are additional tasks,
not stated improvements of these constants. Statements and norm
definitions were read, not their full proofs; no application requiring
those missing proofs is made. A different norm or exponent class
cannot silently replace the target.

### Remez and disk growth: no missing automatic improvement

O. Friedland, *A Disk-Growth Remez Principle and a Modular Proof of
the Measurable Turan-Nazarov Inequality*,
[arXiv:2606.24823v1](https://arxiv.org/pdf/2606.24823v1)
(23 June 2026), Theorem1.1 pp2–3 requires f nonzero holomorphic on
D(0,5), d>=1, H0>=1, H1>=d, and BOTH growth assumptions
sup_D(0,4)|f|<=exp(H0)sup_D(0,1)|f| and
sup_D(x,4)|f|<=exp(H1)r^(-d)sup_D(x,r)|f| for every
x in [-1/2,1/2], 0<r<=1. Its cost is
exp(C(H0+H1))(C/|E|)^d for measurable E in that interval.
Theorem1.2 p3 gives the classical exponential-sum order cost.
Lemma3.2 and its complete ray-restriction proof, pp6–7, obtain disk
growth with spectral-radius and order factors from interval Turan.

This is an inspected **preprint statement**, not an independently
audited new input. It does not pay residual-specific growth constants
or reduce order to the number of coupled free coefficients. Its
disk theorem is conditional on precisely quantified growth; using it
without those bounds would recreate an unpaid input. The accessible
statement adds no adequate improvement over review312 for our target.
No confluent specialization or new rate calculation is made here.

### Search record, access and nonclaims

Queries on 11 November 2026:

- `exponential polynomials Markov inequality complex exponents derivatives norm interval confluent Turan Remez`
- `exponential sums coupled coefficients inverse Laplace moment functional norm inequality derivative`
- `"exponential polynomials" "coupled" "Remez"`
- `"exponential sums" derivative inequalities "complex exponents" finite interval`
- `"Laguerre" "observability" "moment" finite dimensional inverse inequality`

The first searches located the derivative papers; the coupled query
did not establish an exact match. The observability search also
returned arXiv:2610.31876 (parabolic systems), and a model-reduction
paper DOI10.1080/13873954.2018.1488742. These remain **unread leads**,
not inspected theorems, coverage, or evidence of a norm estimate.
No PDE realization or quantitative control constant connecting them
to this complete kernel was supplied. Search snippets were not used
as theorem evidence. Failed searches do not establish novelty.

Web PDF text supplied the primary hypotheses above. A local curl
download failed DNS resolution; this did not block reading through
the web tool. The damaged Nazarov PDF was not retrieved again.
Full matching Mathlib coverage remains unknown and unchecked; the
standard functional-analysis inputs are reused from review312.

### Decision, downstream use and next-turn boundary

The source comparison rules out these **automatic imports**, not the
proposed upper bound. In particular an inadequate upper estimate
on a larger space is not a lower estimate on S_n. No asymptotic norm,
counterexample, cap contradiction or RH assertion has been proved.

The distinct bounded mathematical test is to seek an exact complex
measure on I representing the specified M_n on every complete kernel
column, and to pay its total variation at the required exponential
rate. Hahn–Banach and the Riesz–Markov–Kakutani theorem, whose contracts
were already inspected in review312, are standard justification for
this way to study a bounded functional on a subspace of C(I); they
supply no numerical or asymptotic bound. No new duality specialization
is proved in this turn. Representation equations must use the actual
coupled columns, not independently adjustable endpoint jets.

The intended use remains C997y's existing centered-moment cap gap:
an adequate functional bound would give a lower certificate for
C997s's selected E_n at a rate strictly stronger than exp(-n/64).
All later selected-response/both-sign, reconstruction and actual-Xi
gaps remain independent and open. Continue only on an exact
representing-measure estimate with paid total variation, or an actual
violating family in S_n; stop the proposed construction if it needs
free endpoint coefficients, a half-line/global norm, or only an
insufficient generic order cost. Such a stop is local to that
construction. The precise new research nomination is in
[review396](2026-11-11-residual-range-measure-test-review-396.md),
and receives separate next-turn approval. No further literature is
needed merely to repeat the contracts inspected here.
