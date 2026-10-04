# Gaussian prime-log separation — completed source assessment

TARGET: Check a primary explicit linear-form-in-logarithms theorem against L364's condition (LF), to decide actual large-frequency negative signs for every fixed sufficiently small Gaussian regulator.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Twelve targeted queries found the original Matveev theorem, its readable full-text mirror, and author arXiv statements distinguishing additive and multiplicative forms. Exact queries and access failures are recorded below; the adequate 2026-10-03 Gaussian spectral assessment is reused.
SOURCE_EVIDENCE: Read Matveev, Izv. Math. 64:6 (2000), 1217–1269, (1.1)/(1.3)/(1.4), Theorems 2.1–2.2 and Corollary 2.3 (2.4)–(2.6), pp. 1217–1219, and the height definition p. 1226, in the full original-text mirror linked below; cross-check Sha, arXiv:1505.07147v6 (2018-10-02), section 2.4, (2.19), pp. 12–13; read Bugeaud–Mignotte–Siksek, arXiv:math/0403046v1 (2004-03-02), Theorem 9.4 and its proof, p. 16.
COMPARISON: Matveev's Corollary 2.3 bounds the additive logarithmic form itself; its 2^(6n+20) branch and product of logarithmic heights have adequate dimension growth for the deliberately weaker (LF). Distinct positive primes lie in the real degree-one field, with height log p and nonzero form; the actual regulated-sign conclusion is not a theorem in these sources.
GAP: In a later mathematical turn, write the prime specialization, absorb its displayed constants into the single universal constant required by (LF), handle one nonzero summand, and apply L364 with R fixed. No specialization proof, visit, negative sign, or regulator-uniform conclusion is derived in this literature turn.
REASON: The essential unread arithmetic source need is resolved and the exact later theorem application is approved. Import the known logarithmic-form theorem by citation; only its applicability and composition with the existing conditional return test need proof. No claim beyond the checked literature or RH claim follows from this assessment.
LITERATURE_REASON: The saved REVIEW_REQUIRED action specifically needed a primary theorem's number-of-logarithms dependence, algebraic-height normalization and coefficient norm; those had not been read in the adequate earlier spectral assessment and are now checked.
SCOPE: The unchanged L357 Gaussian family, with every sufficiently large R considered separately and ε=R^(−2); integer combinations of real logarithms of distinct primes through N_H. This approves the known theorem's specialization and L364 application, without a uniform onset in ε, a coupled endpoint return, an actual-theta sign, or an all-level assertion.
COVERED_TARGET: Specialize Matveev's Corollary 2.3 to L364's (LF) and apply its joint-window criterion to settle the Gaussian family's common global-first-sign threshold.

## Gap, relevance and threshold

The main gap remains global actual-theta mixed positivity, including the
low logarithmic and sublogarithmic Laguerre indices at unbounded heights.
This intermediate target tests one proposed first-sign approximation:
could L357's regulated functions have a nonnegative first sign at every
real frequency for all sufficiently small positive regulators? Negative
actual values at every fixed sufficiently small regulator would stop
that certificate. They would leave actual-theta signs and RH unresolved.

The already proved conditional test is
[L364](../../lemmas/L364-gaussian-joint-gamma-window-return-threshold.md).
Its discrepancy is at most 2/(H Delta_H)+24/sqrt(H), and it needs
H Delta_H beta_H >= 8 and sqrt(H) beta_H >= 96. The gamma requirement
is already adequate. The prime cutoff is O_R(sqrt(log log H)), while
log K_H is O_R(log log H). Its explicit condition (LF) admits the
dimension factor exp(C N log(N+2)), and its existing comparison (19)
explains why that factor would suffice. This review compares sources
with that recorded threshold; it does not repeat or extend the proof.

Retain the elementary separation failure in
[the attempt](../../ATTEMPTS/2026-10-04-gaussian-elementary-shrinking-return-obstruction.md),
the restricted-background stops, and the endpoint-return failures.
L336's cutoff and coupled-height quantifiers differ from this fixed-R,
freely growing-height test. Qualitative density from L362 has no required
rate. The six certificates still only constrain a possible common
threshold to ε_0 < 1/1000000. None settles the small-regulator quantifier.
The [existing spectral assessment](2026-10-03-gaussian-regulated-first-spectrum.md)
already covers Mellin, gamma and projected-sign tools and is reused.

## Search and actual reading

Queries used on 2026-10-04:

- `Matveev 2000 explicit lower bound homogeneous rational linear form logarithms algebraic numbers II theorem 2.1 pdf`
- `Baker Wustholz logarithmic forms group varieties 1993 18 (n+1) factorial theorem pdf`
- `prime logarithms linear form lower bound number logarithms exp n log n Baker Wustholz`
- `"Matveev" "1217" "pdf" -site:scribd.com -site:researchgate.net`
- `"Baker" "Wüstholz" "Logarithmic forms and group varieties" pdf`
- `"Matveev" "C(n)" "Theorem 2.1"`
- `"matveev" "im314" pdf`
- `Bugeaud Mignotte Siksek Fibonacci Lucas perfect powers theorem 9.4 Matveev pdf`
- `"Matveev" "Corollary 2.3" "2^{6"`
- `"Matveev" "Theorem 2.1" "linearly independent" "bn"`
- `"Effective results on the Skolem Problem for linear recurrence sequences" pdf`
- `"Matveev" "Corollary 2.3" "log(eB)" "6" arxiv`

Read the shared and local goals, checkpoint, whole PROOF overview,
DAG and saved assessment before selecting this review. Inspected the
uncommitted local documentation and L364, the prior return draft and
history, L362–L363's exact statements, and the reusable spectral coverage.
Preserved the pre-existing L364 work and all other notebooks' changes.

**Original primary theorem.** E. M. Matveev, *An explicit lower bound
for a homogeneous rational linear form in the logarithms of algebraic
numbers. II*, Izvestiya: Mathematics 64:6 (2000), 1217–1269;
[journal record and DOI](https://www.mathnet.ru/eng/im314),
[readable mirror of the original article](https://www.scribd.com/document/1000307340/An-Explicit-Lower-Bound-for-a-Homogeneous-Rational).
Read §1's parameter definitions, §2's statements and §5's height
normalization, at the pages specified above. The independent-logarithm
hypothesis belongs to Theorem 2.1; Corollary 2.3 allows a nonzero form
without that extra hypothesis. It explicitly permits the unweighted
maximum coefficient norm B* in place of the weighted B. The mirror is
the article's text, not its platform's AI-generated description.

Its OCR loses some inequality strokes, including ≠. Resolve the
essential nonzero hypothesis and the usable constant branch with the
author PDF below, rather than treating a corrupted `Lambda = 0` as
the theorem's hypothesis. The journal landing page verifies identity,
publication and DOI, but is not itself theorem evidence.

**Exact additive cross-check.** Min Sha, *Effective results on the
Skolem Problem for linear recurrence sequences*,
[arXiv:1505.07147v6](https://arxiv.org/pdf/1505.07147v6),
2 October 2018, §2.4, pp. 12–13, equation (2.19), explicitly attributed
to Matveev's Corollary 2.3. The author PDF states the following version.
For n >= 2, nonzero algebraic α_j in a field of degree D, integers b_j,
B=max_j |b_j|, fixed principal logarithms and
A_j >= max{D h(α_j), |log α_j|, 0.16}, a nonzero additive form
L=sum_j b_j log α_j satisfies

\[
 \log|L|>
 -2^{6n+20}D^2\left(\prod_{j=1}^n A_j\right)
       \log(eD)\log(eB).
\]

Read its height definitions (2.3)–(2.4), pp. 5–6, as a supporting
normalization check. This is a restatement in an author research paper,
not a new bound attributable to Sha or a match for the regulated sign.

**Multiplicative variant distinguished.** Yann Bugeaud, Maurice
Mignotte and Samir Siksek, *Classical and modular approaches to
exponential Diophantine equations. I. Fibonacci and Lucas perfect
powers*, [arXiv:math/0403046v1](https://arxiv.org/pdf/math/0403046v1),
submitted 2 March 2004, Theorem 9.4 and its proof, printed p. 16
(PDF page 16). Here Λ=prod_j α_j^(b_j)−1. For a real field the
displayed coefficient is 1.4·30^(n+3) n^4.5, with the same height
product and logarithmic coefficient dependence. Its proof derives the
estimate from Matveev's Corollary 2.3. This is useful corroboration,
but the multiplicative Λ must not be substituted for L in (LF).
The additive version above avoids any exponential-to-logarithm transfer.

## Applicability comparison and research boundary

Use one summand for each nonzero prime coefficient. The source's
algebraic numbers are the distinct positive primes themselves, all
in Q; thus D=1, the real case applies, and the chosen logarithms are
the usual real logarithms. For a prime p the logarithmic height is
log p, which also exceeds 0.16, so A_j=log p is admissible. The
coefficient maximum is at least one and at most L364's K. Unique
prime factorization supplies nonvanishing; it supplies independence
as well if using Theorem 2.1 instead. No complex branch, root of unity,
unknown field degree or conjectural zero-free region is involved.

The checked statement has exponential dimension factor 2^(6n+20),
and each height factor is at most max{1, log N}, with n <= N. Its
dependence on the coefficient maximum is log(eB), rather than B.
These displayed factors fit inside (LF)'s deliberately weaker
exp(C N log(N+2)) log(2+K) allowance after a universal enlargement
of C. This is the source-to-target comparison, not a separately
proved prime-log theorem. A later applicability proof must make that
enlargement explicit and cover a single nonzero summand without relying
on the n >= 2 restatement. Do not compress all primes into one large
rational number: doing so would replace the useful logarithmic
coefficient dependence with a large height.

**Decision: SPECIALIZE.** The essential source gap is resolved.
The known logarithmic-form theorem covers the arithmetic input with
adequate parameter dependence; the paper does not discuss the Gaussian
family, the gamma phase or its signs. Cite the theorem and prove only
the prime applicability and composition with L364. Reproving the
transcendence theorem or L364's gamma averaging is unnecessary.

The discriminating test is the exact (LF) dimension and coefficient
comparison, followed by L364's two inequalities with R held fixed.
Continue if the cited parameters give the claimed universal constant
and satisfy that existing return criterion. Stop this application if
an overlooked hypothesis or dimension loss prevents that comparison;
the inspected statements show no such mismatch. Constants and onset
may depend on the fixed regulator in the sign application. A common
global-sign threshold concerns every frequency for every sufficiently
small regulator; it does not require a regulator-independent onset.

No (LF) specialization, actual phase visit or new negative value is
proved in this turn. Even a later successful application would only
stop the proposed regulator certificate. L357's O(ε) absolute error
does not transfer negative signs at escaping frequencies to actual
theta, and the global mixed-form/all-level gap would remain.

## Access limits, reuse and classification

Math-Net's English download and two indexed PDF links redirected to
landing pages; the IOP PDF was denied by robots.txt. Local curl had
no DNS access. Baker–Wüstholz's 1993 publisher page failed, its
EuDML/DigiZeitschriften access did not expose the article, and a
monograph mirror timed out. Those originals remain unread, unused
leads and are parked; no further retry is required for this target.
Matveev's original full-text mirror and both arXiv statement PDFs
were readable. PDF screenshot requests provided no inspectable image
in this interface; the cited text statements and formulas were read.
The full Matveev proof and the earlier works it cites were not audited.
No essential source gap remains for the explicitly recorded bound.

This completed step is LITERATURE; EXPLORATION; REPRODUCTION: a new,
adequate theorem-level comparison, with the later application now
approved, and no new mathematical sign result. It spends or resets
no mathematical exploration turn. Its result is covered known input,
not progress beyond the sources checked; no originality or RH
candidate is claimed. Current status and the single next action live
only in PROGRESS.md.

## Mathlib

Full quantitative logarithmic-form theorem, (LF) specialization and
joint Gaussian sign application: **not checked**. Supporting height,
prime-factorization and finite-Fourier coverage is also **not checked**
in this review. No full matching library theorem or library absence
is asserted. The primary theorem is arithmetic support, not a match
for the entire sign statement; the DLMF support already recorded in
the preceding assessment is reused without a new lookup.
