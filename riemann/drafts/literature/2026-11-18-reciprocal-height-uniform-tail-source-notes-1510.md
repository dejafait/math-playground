# Degree-uniform reciprocal-height tail source review1510

Literature-only work on the exact TARGET in assessment1509. Main gap:
L030--L032/C032a actual-Xi all-degree positivity. The intermediate target
is the saved C d/A bound for the actual centered signed-log tail at A d,
with C,A_0 independent of all integers d>=3. Its possible use is to
isolate the central signed-log payment in C028b/C028d; that independent
RH-equivalent payment remains unresolved.

## Working checkpoint

Read C028a's polynomial and normalization, complete C028b, and C028d's
definitions, conclusions, coefficient centering and exterior proof.
Reuse source-notes1507 and assessment1507 for finite-factor accounting,
and source-notes1500 for actual Jensen conventions and prior failures.
C028a/C028c positive-reference budget stops remain intact. No new lemma,
mathematical script, PROOF or DAG change is permitted or made.

New searches concern Jensen compact convergence/coefficient bounds,
Appell exterior asymptotics, and logarithmic tails. The directly reached
primary candidate is Craven--Csordas1989 Lemma2.2, pp244--245,
https://msp.org/pjm/1989/136-2/pjm-v136-n2-p03-s.pdf . O'Sullivan
arXiv:2007.13582v2 Section3.1 and Lemma3.4 are accessible at
https://arxiv.org/html/2007.13582v2 . Their compact convergence and
product formulas warrant a hypothesis comparison, not a proved tail
bound in this literature turn. Pending: inspect the complete essential
coefficient proof, compare the centering specialization, and record a
bounded continuation without deriving its estimate.

Boyer--Goh's author-hosted Appell PDF initially timed out; its arXiv v1
was subsequently accessible. The completed comparison is below. This
working checkpoint is retained as retrieval history, not a pending task.

## Primary coverage actually inspected

**Craven and Csordas**, *Jensen polynomials and the Turan and Laguerre
inequalities*, Pacific J. Math. **136**(2) (1989), 241--260,
[Lemma 2.2, pp.244--245, (2.13)--(2.21)](https://msp.org/pjm/1989/136-2/pjm-v136-n2-p03-s.pdf).
For arbitrary entire h(z)=sum a_k z^k/k!, complex coefficients, and fixed
integer p>=0, the binomial polynomials g_(n,p)(z/n) converge to h^(p)(z)
uniformly on compact subsets of C. No real-zero premise. Read the
statement and complete proof text: scaled falling-factorial multipliers,
Cauchy coefficient inequalities, two geometric tails, and a finite
coefficient block. PDF extraction obscures several displays; screenshots
returned no inspectable images. No exact rate from those displays is
imported. The ordinary Cauchy coefficient estimate is the relevant
standard tool; its application to the centered family remains unproved.

**Cormac O'Sullivan**, *Zeros of Jensen polynomials and asymptotics for
the Riemann xi function*, arXiv:2007.13582v2, 9 December 2020,
[Section 3.1, Theorem 3.1 proof sketch; Section 3.2, Lemma 3.4/(3.3)--(3.4)](https://arxiv.org/html/2007.13582v2#S3.SS2).
The compact-limit formula is legible in the proof sketch. Read both
product identities and their stated formal-power-series scope; the
source leaves their proof as an exercise. They express reciprocal
Jensen polynomials of Phi*Omega by a finite binomial convolution. This
is relevant to the proposed exponential centering. No LP hypothesis is
needed for Lemma 3.4. Its short actual-coefficient applicability check
is reserved for research. Reuse source-notes1500/C028b for the actual
Theta normalization and order, rather than reprove their criterion.

**Robert P. Boyer and William M. Y. Goh**, *Appell Polynomials and Their
Zero Attractors*, [arXiv:0809.1266v1, Definition 1 p.1, Section 3,
Theorem 1 and proof, Corollary 1 p.4](https://arxiv.org/pdf/0809.1266v1).
This version assumes e^(xt)/g(t), with g entire, g(0)!=0 and at least
one zero. Its exterior asymptotic is uniform on compact subsets of
|x|>1/r_0, where r_0 is the least zero modulus. The proof uses a
Cauchy contour, deformation to the unit circle, and an invoked saddle
point estimate. Read that complete proof; its cited saddle theorem was
not audited. Neither the entire-denominator hypotheses for the actual
family nor domination on the entire unbounded tail are supplied by
this statement. It is a comparison only, not an imported input.

## Exact applicability and specialization boundary

C028a fixes F(u)=sum b_j u^j/j!, F(0)=1; C028b already checks that F
is the actual entire normalized Theta. C028d fixes the real translation,
the centered coefficients c_(d,k), c_(d,0)=1 and c_(d,1)=0. These are
existing inputs, not new conclusions of this review. The candidate
centered generating function for a subsequent application is
e^(-b_1 u)F(u). Its coefficient identification with the existing c_(d,k)
must be checked using the source product formula or a finite binomial
calculation. No additional actual-Xi moment or zero-location theorem
is needed for this identification.

The unrestricted entire-function theorem covers the proposed analytic
setting. It does not state the requested C d/A integral bound. Qualitative
compact convergence alone must not be called an integrable majorant.
The remaining difference is quantitative uniform control of the centered
normalized polynomial, its local logarithm and the unbounded real tail,
including every d>=3. The standard coefficient estimates cover the
method; only this finite-family specialization is approved. Do not
reprove Jensen convergence, Poisson--Jensen or a saddle point theorem.
If using an eventual bound, handle the finitely many smaller degrees
explicitly; no numerical root sweep is a substitute for that argument.

Assessment1509 is therefore SPECIALIZE, not IMPORT of the desired
estimate and not a claim of novelty. A subsequent proof may import
Jensen convergence and Cauchy's coefficient inequalities by citation,
then justify precisely the centering and uniformity required here.
No new estimate, centered generating-function identity, root bound or
tail lemma is derived in this literature turn. Full matching Mathlib
availability remains unchecked; absence is not claimed.

## Duplicate and failure comparison

Scoped checks covered C028a--d, source-notes1500/1507, assessment1507,
the named actual-Jensen height/Schmeisser assessments and stop1497,
and history1509. C028a's divergent Gaussian coefficient budget and
C028c's penultimate-Jacobi retained cost do not refute a signed exterior
estimate. C028d's fixed-d constants cannot supply the uniform constants
without further proof. C028b prevents promoting a later central o(d)
payment to an easy weakening of RH. No matching degree-uniform tail
proof was located in this scope; this is not an exhaustive novelty search.
No cross-notebook input or new zeta zero-free region is proposed.

## Bounded continuation and stopping test

Keep exactly assessment1509's original target: constants C,A_0>0,
independent of d, bounding the signed exterior integral by C d/A for
all integers d>=3 and real A>=A_0. Prove the uniform analytic estimates
and justify integration, or exhibit a rigorous obstruction in the actual
family. Constants may depend on its fixed normalized coefficients but
not on d or A. A proof of a stronger absolute-tail bound would suffice,
but is only a possible proof method, not a second task or an established
claim. Fixed-d constants and counterexamples from unrelated families
do not pass. Stop a proposed shortcut if it assumes hyperbolicity,
a global logarithm through zeros or unproved degree-limit domination.

Success could let A be chosen large before estimating the central
signed integral; it would not establish H_d=o(d), any central saving,
or RH. C028d's finite identity still lacks an independent proof audit;
the exterior target can be attempted directly from its polynomial and
coefficient definitions without relying on its full-line identity.
No justified creative central-payment mechanism was found during this
bounded review. Do not label the classical specialization creative or
extend this source step into unrelated discovery.

## Search and retrieval record

Queries: `Jensen polynomials uniform convergence compact sets entire
function zeros bounds coefficients`; `Appell polynomials logarithmic
potential scaled zeros exterior asymptotics entire generating function`;
`"Jensen polynomials" "logarithm" "uniform"`; `"Jensen polynomials"
"tail" "log"`; `"reciprocal Jensen" "uniform"`; `"Appell"
"logarithmic potential" "entire"`; `"Jensen polynomials" "log-modulus"
tail`; `"Jensen polynomials" "exterior" bound`; and a source-specific
Craven--Csordas/Cauchy/(2.17) query. Snippets, mirrors, recent claimed RH
solutions and secondary summaries supplied no theorem inputs. The
Appell HTML v2 URL returned404; the explicit PDF v1 was read. No larger
extracts or retries are needed for the approved Jensen specialization.

Outcome EXPLORATION: useful new theorem-to-target comparison and source
approval, with no mathematical estimate established. This literature
turn spends no mathematical exploration attempt and resets no budget.
