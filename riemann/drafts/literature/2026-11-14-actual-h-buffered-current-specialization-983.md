# Actual-h buffered current — nomination983, completed review984

TARGET: Assess source coverage for specializing C466y to H_x(z)=sum_{j=1}^3(log h(1+z_j)-x(1+z_j)), x=B'(1), on |z_j|<1/4, with explicit whole-box M_1/M_2 bounds and a nonzero buffered time.
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review984 read C466a/k conventions, C466y hypotheses, C466n completion/enclosure/audit939 passages, review935 and stop948; searched exact transformed-xi derivative and xi gradient-flow phrases plus complex logarithmic-derivative bounds and holomorphic-log terminology. No exact whole-chart theorem was located in this bounded search; primary tools and comparisons are detailed below.
SOURCE_EVIDENCE: Inspected DLMF 25.2.1/6/7/11 https://dlmf.nist.gov/25.2 and 25.10(i) https://dlmf.nist.gov/25.10; 5.2(i)/5.2.2 https://dlmf.nist.gov/5.2, 5.7.6 https://dlmf.nist.gov/5.7#E6 and 5.15.1 https://dlmf.nist.gov/5.15#E1; Stefan Adams, MA3B8 Complex Analysis, 18 March2020, Lemma10.12 pp102-103 and Corollary5.6 p45 https://warwick.ac.uk/fac/sci/maths/people/staff/stefan_adams/complexanalysis2020.pdf. Reuse C466y/audit983 and review935's completion/density coverage; no ODE, compound or density theorem is reproved or silently strengthened.
COMPARISON: C466y already supplies the entire generic current conclusion. C466n certifies values and a center derivative, not the requested full-polydisc bounds. Standard completion-factor identities and convergent derivative series cover the needed analytic tools; the quantitative chart assembly remains a routine specialization, not a new positivity mechanism or a ready imported chart theorem.
GAP: Still unproved: verify the completion-factor domains on the chosen chart, normalize its analytic logarithm, produce explicit uniform Hermitian M_1/M_2 and H_0, and exhibit 0<a<1/4 and T_0>0 satisfying the strict buffer. No constants or specialization were derived in review984.
REASON: Newly inspected primary inputs remove the essential source-coverage gap and support one bounded quantitative specialization; citation alone does not instantiate its constants. This changed ready assessment receives separate next-turn approval before the covered mathematical continuation.
SCOPE: One fixed three-particle chart centered at the Bromwich point 1; no larger domain, all-order claim, asymptotic height estimate, determinant sign, global contour or restart is covered.
COVERED_TARGET: Specialize C466y to the actual H_x on |z_j|<1/4 by proving the normalized logarithm branch, explicit whole-box Hermitian M_1/M_2 bounds and one positive buffered time.
LITERATURE_REASON: Nomination983 explicitly left the quantitative actual-h chart uncovered; generic-H audit coverage cannot supply uniform completion-factor bounds or an explicit buffer.

## Completed primary-source comparison984

### Exact imported tools and their hypotheses

[DLMF 25.2](https://dlmf.nist.gov/25.2), equations 25.2.1,
25.2.6-7 and 25.2.11, gives zeta's Dirichlet series, its derivatives
of positive integral order, and the Euler product, all for Re(s)>1.
The sources are Apostol (1976), pp231,236. [25.10(i)](https://dlmf.nist.gov/25.10#i)
explicitly states nonvanishing there. These cover direct complex
estimation once a uniform real-part margin is checked. They do not
give that margin or numerical derivative bounds for the transformed
variable. Controlling reciprocal factors and all differentiated
series uniformly, including their tails, remains part of the
specialization. No new zero-free strip is proposed.

[DLMF 5.2(i), 5.2.2](https://dlmf.nist.gov/5.2)
states that Gamma has no zeros, has poles only at nonpositive
integers, and psi=Gamma'/Gamma off those poles.
[5.7.6](https://dlmf.nist.gov/5.7#E6) supplies
psi(v)=-EulerGamma-1/v+sum_(k>=1) v/[k(k+v)], for v outside
the nonpositive integers; [5.15.1](https://dlmf.nist.gov/5.15#E1)
supplies psi'(v)=sum_(k>=0)(k+v)^(-2) on that same domain.
The first series is used in its combined, convergent summand form.
These are exact identities, not asymptotic value remainders that
could be differentiated without error control. Uniform absolute
majorants on a chart separated from the poles must be supplied
later. No special-function algorithm or installed library is
needed to invoke these formulas.

Stefan Adams, *MA3B8 Complex Analysis*, 18 March2020,
[Lemma10.12, printed pp102-103; Corollary5.6, p45](https://warwick.ac.uk/fac/sci/maths/people/staff/stefan_adams/complexanalysis2020.pdf),
gives a holomorphic logarithm for a nowhere-zero holomorphic
function on an open simply connected domain, unique up to
2*pi*i times an integer, and the Cauchy coefficient estimate
|a_k|<=M/R^k for a holomorphic function bounded by M on a radius-R
disk. Read the logarithm proof's base-value choice and f'/f
integral, and the estimate's r<R limiting argument. Nonvanishing
must precede this invocation; selecting a principal logarithm of
computed h values is insufficient. Cauchy is an alternative
derivative tool requiring a genuinely larger bounded disk, not a
license to differentiate a center enclosure.

### Reuse, overlap and exact remaining specialization

The actual completion formula is already C466n(11), with its
normalization inherited from C466a/L018. Its factor arguments and
branch choices are the starting point. Verify them on the entire
w-disk |w-1|<1/4 (and on any larger disk actually used), for
q=sqrt(w), s=1/2+q and v=s/2. In particular the Euler-product
condition is on s, not w. Check each polynomial factor, the Gamma
poles, nonzero denominators and the normalization B(1)=log h(1)
on the positive axis. These are obligations for later mathematics;
no domain inequality or value enclosure is proved here.

C466n's inspected formulas (12)-(14) and audit939 cover rigorous
completion evaluation and x=B'(1) at the center. They do not claim
the needed whole-box M_1/M_2; evaluated vertical-line nodes cannot
replace such bounds. Its [review935](2026-11-14-third-marginal-effective-tail-nomination-934.md)
already covers explicit Gamma/Euler-Maclaurin remainder tools and
Cauchy control. Reuse it if needed, without rerunning its finite
density certificate. The newly inspected convergent Gamma/zeta
series offer simpler direct absolute estimates for this compact
chart, provided their exact domain margins and tails are checked.
No full matching Mathlib theorem was checked; unknown coverage is
not absence.

Retain C466a's original Hub-v1 one-sided density assertion and all
its external strip, symmetry, paired-product, counting and low-zero
qualifications. The Hub page initially loaded but two targeted
reopens timed out. Adequate inherited coverage in C466a/review935
is reused; density reconstruction is not a missing essential task.
For scope comparison only, inspected [Sra arXiv2611.02944v1](https://arxiv.org/pdf/2611.02944v1)
Theorem1.1 p2, Section2.1 pp3-4, Lemma2.4 p5 and Corollary2.5 p6.
The theorem supplies the alpha=1 smooth positive density, and the
section identifies the counting and low-zero inputs. This differs
from the Hub version; no entire-version equivalence, changed PF
assertion or extra verification claim is imported. The previously
reviewed density proof is not reaudited.

The later calculation should bound the one-variable logarithmic
derivatives uniformly, identify x and H_0 with the prescribed
normalization, translate to the three-variable Hermitian norms, and
exhibit finite a,T_0 meeting the exact strict inequality. Include
the equality of exp(-H_x) with the actual product of A_x factors.
Then apply C466y by citation, retaining its full beta/gamma,
zero-extension, unit-flat raw flow and first-lifetime conventions.
Reproducing the generic current proof would add no needed input.
No new lemma is required merely for a direct applicability record.

### Bounded search, stops and decision

Queries actually run included `"xi" "logarithmic derivative"
"digamma" bounds complex Euler product`, `"holomorphic logarithm"
"simply connected" theorem lecture notes`, `"xi" "derivative
bounds" "polydisc"`, `"Riemann xi" "logarithmic derivative" "Re"
"1" bounds`, `"xi(1/2+sqrt" "derivative" bounds`, and `"Riemann
xi" "gradient flow" holomorphic`. Exact transformed-chart searches
returned unrelated material. General logarithmic-derivative searches
returned positivity-region papers and unrelated proposed certificates;
their snippets are unread leads, not inputs or evidence against this
chart. Primary DLMF and Adams statements, rather than search snippets,
support the assessment. No novelty is inferred from a failed search.

Stop948 concerns the necessity of smooth phase extension and the
residual Jacobian phase. C466k's product obstruction and generic
coupled normalization concern signs. C466t's no-buffer comparison
is retained from nomination983. None supplies the present constants
or justifies repeating a completed current/phase audit. The local
chart has a plausible realization use, but no determinant sign,
global patch interface, outer/tail payment, all-order conclusion or
Xi transfer follows from these sources.

Continue only with explicit finite M_1,M_2,H_0, 0<a<1/4 and T_0>0,
with sqrt(3)*a+M_1*T_0<1/4 for this same H_x and whole box, or a
bounded attempt isolating the first failed estimate. A center-point
bound, existential compactness constant, numerical sample or
uncontrolled derivative is insufficient. Changed analytic hypotheses
need a separate review. This is SPECIALIZE, not a ready imported
chart and not creative sign research. Source coverage is ready for
the listed continuation, subject to its separate next-turn approval.

## Original nomination983 (historical; superseded by review984)

## Exact proposed use and qualifications

Use C466a/k's actual h(w)=xi(1/2+sqrt(w))/xi(1/2),
B(s)=log h(s) on the positive real axis and x=B'(1).
The proposed H_x and the branch of its logarithm must be justified
on the whole polydisc B={|z_j|<1/4}, not only on its initial
imaginary slice. The factor exp(-H_x) is intended to be the actual
product of A_x(1+z_j), A_x(w)=exp(xw)/h(w). This is the
definition to assess, not a completed applicability proof.

Essential local inputs are C466y with audit983 and C466x for its
already audited estimates, plus C466a/k for actual-function
normalizations. Inspect only the needed effective complex-completion
and derivative passages of C466n if they provide bounds for this
chart. Its formulas or certificates are leads until their exact
hypotheses and error bounds have been read. Retain the external
strip, symmetry, paired-product, counting and verified-low-zero
qualifications recorded in C466a; this review does not independently
certify them or import the source's other mixture assertions.

The prospective applicability test is explicit finite numbers
M_1,M_2 and 0<a<1/4, T_0>0 satisfying
sqrt(3)a+M_1 T_0<1/4 for the *same* actual H_x and whole-box
Hermitian norms in C466y. Do not replace the strict buffer by a
center-point estimate, silently discard a complex phase or assume
a global logarithm. Source results giving all needed bounds should
be imported with their exact locators and only the necessary
specialization. An existential compactness bound alone does not
meet the effective target. No numbers or new inequalities are
derived in this nomination.

The downstream use is one actual-weight local current chart, removing
one specified realization obligation before any proposed signed patch
assembly. It does not establish even one new density-minor sign:
known finite-order signs remain separate. Global patch interfaces,
outer/tail boundaries, the full Jacobian phase, all orders and
the density-to-Xi implication remain unresolved.

## Stop comparisons and review decision test

C466t rules out dropping the buffer. Stop948 distinguishes action
phase from residual Jacobian phase and rejects smooth collision
extension as an automatic necessary condition. C466k's product-contour
obstruction and its generic local normalization audit947 remain
intact. C466j/stop922 concern unrestricted chamber propagation and
are comparisons only, not theorem inputs for this chart.

Continue to a specialization only if existing primary/local results
cover the exact whole-box hypotheses and yield an explicit buffer,
or an assessed bounded gap remains. If this chart is already fully
covered, import it rather than manufacture a lemma; if the source
assumptions or proposed benefit fail, record the precise scope limit.
Persistent source blockage must park dependent work. No mathematical
derivation or approval of uncovered mathematics is authorized now.

This next turn is literature_comparison, standard/high. It is a
routine quantitative-specialization assessment, not a creative sign
mechanism. The audited current does not justify a new central creative
claim by itself: a phase-sensitive bridge with an independent global
test is still missing. Do not reopen its completed audit or fill a
creative quota by renaming this applicability check. Full matching
Mathlib coverage for the proposed specialization remains unchecked.
