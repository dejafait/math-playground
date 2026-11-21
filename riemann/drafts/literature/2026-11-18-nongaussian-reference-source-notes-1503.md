# Positive reference-measure source review1503

Literature-only work on assessment1502's exact target. Main gap:
L030--L032/C032a actual-Xi all-degree positivity. C028b identifies
H_d=o(d) as an RH criterion; no payment is available. The intermediate
question is positive non-Gaussian reference feasibility and the full
Schmeisser cost for unchanged C028a R_d. No calculation or new lemma
is authorized in this turn.

## Saved working checkpoint (completed below)

Read canonical C028a/C028b and source-notes1500; compared L763/L764's
different Gaussian-product polynomials and the closed L827 six-moment
sequence via its ATTEMPTS record. Preserve their stops. New primary
coverage: Curto--Fialkow1991 Theorems3.1/3.9 and Simon's bounded
Favard theorem in his publisher-hosted Chapter1. Reuse Schmeisser's
height theorem/proof assessment; inspect its recurrence/norm interface
and real penultimate-coefficient absorption, not another full proof.

Pending: finish exact hypotheses and finite-reference comparison,
distinguish terminal-diagonal redundancy from a genuine reference
change, and nominate one bounded test with an independent next-turn
approval. No feasibility, cancellation or cost bound has been proved.

## Primary source coverage

Gerhard Schmeisser, *Estimates for the Imaginary Parts of the Zeros of
a Polynomial*, Mathematica Balkanica16(2002),203-217,
https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf .
Reuse C028a/review1497's Theorem1/Corollary1 and complete relevant proof
coverage. Newly inspected pp203-204,(1.1)/(1.5), and all of the
Corollary1 deduction pp206-207,(2.3)-(2.5). Its positive-real recurrence
has real diagonal parameters and strictly positive beta parameters;
beta_n=h_n/h_(n-1). The deduction changes only alpha_d to absorb
Re(a_(d-1)/a_d); lower polynomials and the norm ratios in the bound
are preserved. This is an explicit source construction, not a new
local invariance theorem. Merely freeing the last diagonal is therefore
a redundant candidate. Proposition1 pp207-208 varies both polynomial
and basis; its statement does not optimize a fixed actual polynomial.
The new proposal must change an earlier recurrence parameter.

Raul E. Curto and Lawrence A. Fialkow, *Recursiveness, Positivity, and
Truncated Moment Problems*, Houston J.Math.17(4)(1991),603-635,
https://hjm.math.uzh.ch/v017n4/0603CURTO.pdf .
Read Theorem3.1 pp612-613, its invertible/singular proof cases p617,
and Theorem3.9 with complete proof pp619-620. For real truncated data
with m_0>0, the odd case requires Hankel positivity AND the next moment
column in its range; the even case requires a positive Hankel extension
(equivalently the source's rank/recursive consistency condition).
Both provide finite atomic representatives. Positivity alone in a
singular case cannot replace consistency. Their finite existence
statements do not supply nonzero orthogonal norms in all degrees or
an asymptotic Schmeisser cost. Thus the closed L827 finite pass cannot
be promoted to the present reference construction.

Barry Simon, *Szego's Theorem and Its Descendants: Spectral Theory for
L^2 Perturbations of Orthogonal Polynomials*, Princeton UP,2011,
Chapter1, https://assets.press.princeton.edu/chapters/s9377.pdf .
Read Proposition1.3.4 pp14-15 with its moment/Gram-Schmidt proof,
Proposition1.3.6 p16 and Theorem1.3.7 p17 with complete proof.
Strictly positive off-diagonals, real diagonals and bounded parameter
sequences yield a nontrivial bounded-support probability measure.
The proof uses finite Jacobi spectral measures, common moments and
weak convergence on a common compact interval. This supplies the
needed infinite-system admissibility interface for a bounded tail;
no uniform-in-d support bound is asserted. In Schmeisser's convention,
Simon's a_j is sqrt(beta_j), and b_j is alpha_j. Theorem1.3.9 p18
also states the unbounded Favard version, but its deferred proof in
Section3.8 is unnecessary and was not read. No reproof is proposed.
Book identity/year checked at the author's
https://math.caltech.edu/Szego.html and publisher listing.

PDF text was inspectable for these statements and proof cases.
Screenshot calls supplied no inspectable images (one timed out);
no visual or independent arithmetic verification is claimed.

## Comparison, exact scope and decision

Three possibilities were compared. A generic truncated moment search
does not yet control the full orthogonal system or the denominator.
A terminal-diagonal-only change is already absorbed by Schmeisser.
The selected candidate changes the penultimate diagonal and the last
positive beta, with a translated/scaled Hermite prefix and a bounded
positive tail. This is an explicit design to be tested, not a cited
optimal choice. It leaves the actual polynomial unchanged. All source
theorems are to be imported; only its specific coefficient equations
and residual cost would require new work.

The precise family and one bounded test are in assessment1503. It
asks for three leading residual cancellations, then the combined
fourth/fifth residual contribution divided by d^2. An infeasible
positive parameter system or a uniform positive lower limit stops
this family. A rigorously exhibited vanishing contribution passes
only this necessary test; the entire remaining sum still needs a
separate estimate. Arbitrarily small positive beta and unbounded
degree-dependent parameters must not be silently excluded from a
claimed obstruction. No equations were solved or asymptotic bounds
derived during this review.

C028a's fixed matched Gaussian stop remains intact. Its statement
does not optimize over all Gaussian choices or general measures.
L763/L764 alter the input entire function; L827's compensated
coefficient law is a different moment problem. The inverse-direction
and prescribed-primitive/grid stops retained in progress1502 are not
reopened. No new zero-free region or analytic continuation is proposed,
so the October baseline is not an essential source for this test.

## Search and evidence limits

Queries included `Schmeisser 2002 Estimates imaginary parts zeros
polynomial orthogonal polynomials measure optimal`; `truncated
Hamburger moment problem positive definite Hankel matrix representing
measure Curto Fialkow theorem`; `orthogonal polynomial prescribed
leading coefficients Jacobi matrix inverse eigenvalue positive measure`;
`Favard theorem Jacobi matrices measure all moments Teschl book
theorem 2.5 pdf`; `"Schmeisser" "orthogonal" "optimal" "imaginary"`;
`"Schmeisser" "imaginary" "orthogonality measure" optimization`;
`"Schmeisser" "imaginary" "minimize"`; `"Schmeisser" "imaginary
parts" "Jacobi" optimization`; `"prescribed leading coefficients"
"orthogonal polynomials" Jacobi`; `"Schmeisser" "Jacobi"
"penultimate"`; `"Jensen" "Schmeisser" "reference measure"`.
The bounded search found no theorem giving the proposed fixed-family
optimized cost. This is not evidence of novelty or impossibility.

Schmeisser's *Majorization of Zeros of Polynomials*, Varna2002
proceedings(2003),397-403, was opened at its abstract/intro: its stated
lead is Mahler-modulus majorization, not the required reference
optimization. Its proof was not used. Search leads on polynomial
measure modifications, connection coefficients, inverse spectra and
later moment-problem papers were not inspected as theorem inputs.
No essential source remains blocked for the narrowly nominated test.

Local duplicate checks were restricted to November18 Jensen/height
source notes, C028a/C028b, L763/L764 and the L827 closure record,
then named Jensen/Schmeisser assessments and attempts for penultimate,
terminal-Jacobi and reference-deformation terms. No exact same
reference-cost diagnostic was located in that scope. No global
novelty claim follows. Full matching Mathlib coverage is not checked;
absence is not claimed.

Outcome EXPLORATION: the needed admissibility sources are available
and a nonredundant finite diagnostic is nominated; whether it cancels
the cubic or pays even the retained cost remains unanswered. This
literature turn spends no mathematical exploration attempt. No lemma,
mathematical script, PROOF or DAG was changed. The newly saved EXPLORE
assessment must receive separate approval before its research test.
