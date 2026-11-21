# Unbounded nonlocal metric discovery: source comparison, step158

TARGET: Compare at most three source constructions of unbounded nonlocal metrics for Hedenmalm's ODE-generated finite span and select one explicit form with an independent positivity and pair-symmetry diagnostic retaining possible complex zeros, or document why none qualifies.
CHECKED: 2026-11-09
DECISION: IMPORT
SEARCH_EVIDENCE: Step158 searched the exact Hedenmalm title/2606.17494, unbounded metric/quasi-Hermitian construction, resolvent symmetrizer, and imaginary-translation terminology; compared three construction families below and checked narrowly relevant local stops. Exact Hedenmalm plus imaginary-shift/Fourier-metric queries located no matching application; this is not evidence of novelty.
SOURCE_EVIDENCE: Mostafazadeh1203.6241v5 pp3-7 assumptions1-4/(1)-(2)/(6)-(10); Antoine-Trapani1307.5644v2 Section4.1 pp16-17/(4.1)-(4.2); Ahmed quant-ph/0108016v2 pp2-3/(2)-(7), pp5-6/(15)-(18); Teschl2009 Theorems3.2/7.5, (3.25)/(3.50)-(3.51), Section8.1/(8.4). Primary hypotheses and relevant domain/proof cases were inspected; precise links and limits below.
COMPARISON: General completion presupposes a metric and real spectrum; the graph-scale recipe presupposes a closed realization and leaves symmetry to prove. The explicit exponential-momentum family supplies independent positive spectral-multiplier data and a bounded domain diagnostic, but no theorem supplies Hedenmalm symmetry.
GAP: For the selected form at theta=1/4, membership of every retained complex-zero image in its form domain is unproved. All-zero pair symmetry, completion, multiplicities and actual-Xi positivity transfer remain separate; no new theta estimate is established here.
REASON: Import only the known constructions and their limitations; select the imaginary-translation form for a separately approved prerequisite test. This is source discovery, not a mathematical advance or a proof of RH.
LITERATURE_REASON: The startup REVIEW_REQUIRED target changed the metric class beyond the ready dt/t assessment; independent primary metric/domain data was essential and unread at invocation.
SCOPE: Completed literature comparison only. No lemma, mathematical script, transformed theta norm, or new symmetry claim was written. The continuation assessment is new and requires separate approval before research.

## Main gap and selection decision

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The downstream possibility here is an independently
specified positive form for Hedenmalm's differential pair. A useful
intermediate outcome would be one explicit form and a finite-span
test of its domain, positivity or symmetry, with the remaining
all-zero obligations stated. No implication from an arbitrary metric
construction to the main positivity gap is assumed.

The audited L909 excludes dt/t only. It proves neither that every
nonlocal form fails nor that unboundedness is necessary. We select
one explicit source family for a diagnostic, without testing it here.

## Three construction families compared

1. **Completion from a supplied unbounded metric.** Mostafazadeh,
   *Pseudo-Hermitian Quantum Mechanics with Unbounded Metric Operators*,
   [arXiv:1203.6241v5](https://arxiv.org/pdf/1203.6241v5), assumptions
   1-4 and (1)-(2), printed p3: a closed densely defined Hamiltonian
   with real discrete spectrum, a positive self-adjoint eta satisfying
   the intertwining identity with equal product domains, and every
   eigenvector in Dom(eta). The completion and square-root isometry
   do not construct eta. The oscillator example (6)-(10), pp6-7,
   uses multiplication by exp(2a x), not a nonlocal form for this pair.
   Reject automatic import; real spectrum and intertwining are unpaid.

2. **Intrinsic graph scale.** Antoine and Trapani, *Some remarks on
   quasi-Hermitian operators*,
   [arXiv:1307.5644v2](https://arxiv.org/pdf/1307.5644v2), Section4.1,
   printed pp16-17: for closed unbounded B use
   G=1+(B*B)^(1/2) and the powers-of-G Hilbert scale (4.2).
   The bounded T=G^(-1/2) makes B quasi-Hermitian only if TB is
   symmetric. The preceding (4.1) requires the stated product-domain
   conditions. This supplies a scale, not automatic symmetrization;
   the actual pair has no supplied closed B. Reject as a ready
   diagnostic here; constructing a realization would be a new target.

3. **Exponential momentum / imaginary translation.** Ahmed,
   *Pseudo-Hermiticity of Hamiltonians under imaginary shift of the
   co-ordinate: real spectrum of complex potentials*,
   [arXiv:quant-ph/0108016v2](https://arxiv.org/pdf/quant-ph/0108016v2),
   (4)-(6), pp2-3, explicitly proposes eta=exp(-theta p),
   p=-i d/dx, theta real. The formal power-series argument and the
   shifted-potential case (18), pp5-6, do not establish a maximal
   operator domain or apply to Hedenmalm's pair. In particular no
   contour shift through singularities is licensed. Select this
   formula, using the spectral definition below instead of treating
   its formal “automorphism” as everywhere defined. The orthogonality
   argument (15) is conditional on intertwining; (14)'s numerical
   check is not imported as a proof.

These are three mechanisms, not three claimed applicable theorems.
Antoine-Trapani is also the domain caution for family1. Bagarello,
[arXiv:1309.5065v1](https://arxiv.org/pdf/1309.5065v1), SectionIV
(4.1)-(4.3), pp11-12, was inspected as supporting exponential-family
evidence: its oscillator quasi-basis and invariant-domain assumptions
are not transferred to theta images. Its printed Schwartz/exponential
domain is not used to justify imaginary translations of arbitrary
smooth functions. No extra construction is selected from it.

## Precise positive data and proposed diagnostic

Use the unitary Fourier convention

    Ff(k)=(2pi)^(-1/2) integral_R f(x) exp(-ikx) dx.

The imported general input is Teschl, *Mathematical Methods in Quantum
Mechanics*, GSM99, online edition dated 12February2009,
[Theorem3.2 and (3.25), pp91-92; (3.50)-(3.51), p97;
Theorem7.5, p164; Section8.1/(8.4), pp173-174](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).
For real Borel multipliers these specify the self-adjoint maximal
domain, form domain and unitary Fourier realization of momentum.
Specialize only the multiplier to exp(-theta k), theta=1/4:

    M_theta = F^(-1) multiplication_by_exp(-theta k) F,
    Dom(M_theta) = {f in L2: integral exp(-2theta k)|Ff(k)|^2 dk < infinity},
    Q_theta = {f in L2: integral exp(-theta k)|Ff(k)|^2 dk < infinity},
    b_theta(f,g) = integral exp(-theta k) Ff(k) conjugate(Fg(k)) dk,
                  f,g in Q_theta.

This is the standard multiplication-form specialization, not a new
theta lemma or a reproof of spectral calculus. Strict positivity on
nonzero domain vectors uses the everywhere positive multiplier.
No positive lower bound in the original L2 norm is asserted. The
operator and its inverse are unbounded. Membership of the actual
G_alpha=(Lu_alpha)(exp x) is deliberately unproved. The rational
theta fixes a bounded experiment; it is not an optimized parameter.

Hedenmalm's already assessed Definition4.2.1/Theorem4.2.2 supplies the
pair diagnostic: after domain membership is established, symmetry
requires

    (conjugate(beta)-alpha) b_theta(G_alpha,G_beta)=0

for all retained zeros, with the first argument linear. This merely
states the source's eigenvector test in its original convention;
it is not a symmetry identity proved for the proposed form. Even a
single nonzero distinct-real-pair entry would reject this theta.
No entry, transformed norm or contour identity is evaluated here.

## Search, duplicate and source limits

Queries included the exact Hedenmalm title and identifier;
`unbounded metric operator quasi Hermitian Hamiltonian construction
positive resolvent integral symmetrizer`; `resolvent integral metric
operator unbounded quasi Hermitian square function`; `Mostafazadeh
imaginary translation metric`; `Ahmed imaginary shift Pseudo-Hermiticity`;
and Hedenmalm with imaginary-shift/Fourier-metric terminology.
No resolvent-vector recipe with verified relevant hypotheses was
identified by these searches; no resolvent theorem is imported.

The operator-pair source assessment and the positive-import and dt/t
ATTEMPTS were read. L906/L907 proofs locate W,L and the finite domain;
L908/L909 statements locate available real tails and the existing
metric stop. A scoped local terminology search found no earlier
imaginary-shift application in these route records. Broader searches
had unrelated hits and cannot establish absence or originality.
Source snippets and secondary summaries were leads only.

The 0810.5643v4 review's translation discussion was inspected as a
lead; its quartic-specific metric is not an additional candidate or
input. Primary Ahmed statements resolved the exponential formula.
Screenshot calls supplied no displayed image; no visual verification
is claimed. The theorem/domain conclusions above use textual primary
statements and the independently specified spectral multiplier.

Full matching and supporting Mathlib coverage for this metric
application is unchecked. No Mathlib absence claim follows.

## Continuation and preserved limitations

The selected construction meets the source-discovery test only:
formula, independent positivity data and an explicit domain/symmetry
diagnostic exist. Test Q_theta membership first, for theta=1/4 and
every retained complex zero. Continue only with a rigorous weighted
Fourier bound; abandon this fixed metric if one retained generator
is excluded. An unresolved estimate is unfinished, not an exclusion.
Changing theta, deleting nonreal generators or simply repeating
source discovery is not the same target. If domain inclusion passes,
all-zero symmetry still needs an independent test.

Essential local inputs for later applicability are L906 (W and L),
L907 (finite complex-zero span, exact ODE and injectivity), L908(1)-(3)
(normalization and real-zero tails) and L909 (audited dt/t obstruction).
L908 step154 is not an input. There is no cross-notebook input.
Unresolved assumptions include convergence for possible complex-zero
images, nondegeneracy, all-zero pair symmetry, completion, multiplicity
issues and transfer to actual-Xi positivity. Do not supply any of these
by assuming RH or by deleting nonreal generators.

The new continuation assessment is
`2026-11-09-hedenmalm-exponential-momentum-domain-test.md`.
It requires separate approval next turn. No domain claim is derived
and approved together here. This is known-construction development,
not a protected creative attempt: a structural reason for all-zero
symmetry, beyond trying an independent positive form, is still missing.
The original nomination's dt/t, inverse-domain and positive-import
stops remain in their canonical files. None is a ban on other metrics.
