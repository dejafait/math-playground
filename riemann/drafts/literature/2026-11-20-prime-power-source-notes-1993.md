# Prime-power signed-window source comparison1993

20 November 2026. Literature only. Outcome NEGATIVE concerns automatic
import from the inspected explicit formulas; it is not a mathematical
nonexistence theorem, an arithmetic cancellation estimate, or progress
beyond those sources. No lemma or mathematical script is changed.

## Target, relevance and test

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
This branch asks for C028b's H_d=o(d). Reuse C028d/e and C029i/j with
b_j=gamma_j/gamma_0, P_d(x)=sum binom(d,j)b_j*x^(d-j),
Q_d(y)=P_d(y-b_1), t_d(y)=log|Q_d(y)/y^d|/d. All roots retain
algebraic multiplicity. Degrees are all integers d>=3; A>=1,
q=1/(4d), L=2Ad, Z=L^(-1)*integral_[-Ad,Ad] exp(q*t_d).

The source-review target was an admissible arithmetic representation
of the signed window integral with every archimedean and boundary term.
Its possible downstream use was the still-unpaid ordered threshold
limsup_(A->infinity) limsup_(d->infinity) (L/q)*log Z<=0.
C029j's already audited comparison has error at most C/(8d);
C028e controls only the exterior. Neither bound is rederived here.

Continue automatic import only if a source identifies an actual
coefficient-defined observable and supplies the required signed transfer,
or isolates a concrete independently testable missing bound. A generic
zeta-zero formula, a missing sign renamed as a remainder, or an
RH-dependent real-ordinate representation fails this admission test.

## Inspected primary formula and reused coverage

Andres Chirre and Felipe Goncalves, *Bounding the log-derivative of the
zeta-function*, Math. Z.300 (2022), 1041-1053,
[Proposition5](https://doi.org/10.1007/s00209-021-02820-9),
including its Fourier convention: for even h analytic on a strip of
half-width 1/2+epsilon and uniformly O((1+|z|)^(-1-delta)) there,
epsilon,delta>0, the unconditional identity is

    sum_rho h((rho-1/2)/i)
      =2*h(i/2)-log(pi)*hhat(0)/(2*pi)
       +integral_R h(u)*Re psi(1/4+i*u/2)du/(2*pi)
       -sum_(n>=2) Lambda(n)*hhat(log(n)/(2*pi))/(pi*sqrt(n)),
    hhat(v)=integral_R h(u)*exp(-2*pi*i*u*v)du.

Here rho are the nontrivial zeros, with the standard multiplicity
convention and potentially complex arguments. The polar terms combine
by evenness. The gamma term accounts for trivial zeros. The immediately
preceding Lemma4 and its partial-fraction proof assume RH; they are
excluded as unconditional inputs. Proposition5 references Lemma8
rather than supplying a new contour proof. Its real-axis approximation
lemmas do not remove that distinction.

Reuse the full non-even Guinand-Weil statement and complete citation
proofs already inspected in assessment1191 and source-notes1555:
Carneiro-Milinovich, *On Littlewood's Estimate for the Modulus of the
Zeta Function on the Critical Line*, published2024,
[Section2.2 Lemma2.2, p7](https://www.math.bas.bg/mathmod/Proceedings_CTF/CTF-2023/files_CTF-2023/05-Carneiro-Milinovich.pdf#page=7),
and Carneiro-Chirre-Milinovich,
[arXiv:1710.10362v1, Lemma8, pp9-10](https://arxiv.org/pdf/1710.10362v1).
They retain both Fourier frequencies and both pole evaluations.
Their generality addresses lack of evenness, not the missing
finite-polynomial identification. The unresolved Iwaniec-Kowalski
book-number/access issue in1191 is preserved; no new book-proof audit
or reproof is necessary for this scope comparison.

O'Sullivan, *Zeros of Jensen polynomials and asymptotics for the Riemann
xi function*, [arXiv:2007.13582v2](https://arxiv.org/html/2007.13582v2),
(1.2), Section3.1/Theorem3.1: reuse C028b's precise actual-family
identification and Jensen convergence scope. The introduction was
rechecked for the coefficient normalization. It concerns the finite
polynomial construction and its limit, not a prime-side formula for
the logarithm of that polynomial. No large-degree limit is imported
under an unverified signed integral.

## Applicability failure and boundary accounting

C029j's integration variable runs on a real interval and its polynomial
zeros are the finite Jensen zeros. Proposition5 instead evaluates an
analytic test at zeta zeros. Merely inserting a function on the right
does not identify its spectral left side with the desired integral.
Nonlinearity alone is not an impossibility argument: a specially
constructed coefficient-dependent test might work, but none is supplied.

The raw combined log has the real-root and origin singularities retained
in C029j. Multiplying it by a hard interval indicator does not provide
the analytic-strip hypothesis. Assigning finite values on a null set
solves neither analyticity nor the spectral identification. Evenness can
be handled by the more general cited formula; it is not the decisive
obstruction. No regularization, analytic approximation or associated
error bound has been constructed in this literature turn.

Any future transfer must preserve both poles, the archimedean integral
and all prime powers. It must separately pay interval-endpoint,
regularization and finite-polynomial transfer errors. The source's
infinite zero sum has no Jensen window endpoints to which one can
assign those terms automatically. Its fixed-test convergence does not
give uniform control as d and A vary. Either work directly with the
signed integral using C029j's established comparison, or retain the
entire L/q=8Ad^2 factor if estimating the normalized moment. Neither
the factor nor the order of limits may be dropped. No critical-line
Dirichlet-series expansion is used.

Consequently no independent signed arithmetic observable passed the
review test. This parks citation-only import, leaving open a future
explicit construction with the missing estimates. It does not rule
out all explicit-formula methods, prove RH, or refute it.

## Duplicate search, access and continuation

Read C029j's full proof/audit and C029i's norm contract/proof ranges;
C028b's normalization/reciprocal-zero argument and C028d/e's contracts
and centering/coefficient ranges. Reused notes1987/1991/1992, the
October31 direct-pair construction assessment and the recorded nonlocal
paired-tail signed-remainder stop. Those concern different missing
interfaces; none supplies the present identity. No stopped absolute
norm, fixed-q moment, positive-metric or co-Poisson route is reopened.

Queries actually submitted included `Guinand Weil explicit formula test
function analytic strip h i/2 log pi digamma prime powers theorem`,
`Riemann xi Jensen polynomial logarithmic integral prime powers explicit
formula`, `"Jensen polynomials" "explicit formula" prime`, and
`"Jensen" "signed" "logarithm" "zeta" polynomial integral`.
No matching inspected theorem resulted. Search absence does not certify
novelty. Unrelated model-polynomial and claimed-RH hits were not inputs.

Bombieri, *Remarks on Weil's quadratic functional in the theory of prime
numbers, I*,2000, Section2, was a search lead only. The bdim article/PDF
fetch timed out. Its theorem and residue proof were not read, and no
claim about them is used. This is not an essential-source blocker for
the comparison: accessible primary Guinand-Weil statements with ready
coverage already supply the required analytic interface. Do not schedule
another access retry merely to repeat it. Full matching Mathlib coverage
remains unchecked, not absent.

For a different possible prerequisite, nominate singular-value
regularization of the actual coefficient companion, with its own
REVIEW_REQUIRED assessment1993. Filename/field searches and the three
recorded companion stops1525/1588/1713 show that those results concern
trace-norm height majorants under specified similarities. They do not
assess a regularized log determinant. This distinction is a nomination,
not proof that the new target works or is original. The C034p audit
nomination was checked as an alternative and rejected as duplicate:
its record1902 already reports a first audit despite the older overview
label. No repeat audit is scheduled.

No justified creative mathematical target is ready: the arithmetic
identity remains absent, and the proposed regularization interface has
no essential source assessment yet. Its possible value is to replace
uncontrolled logarithmic singularities before a later signed estimate;
such an estimate, actual arithmetic cancellation, compact nonreal-mass
exclusion, higher signs and Xi transfer all remain independent gaps.
