# Ordinary logarithm criterion: source review1343

17 November2026. Literature-only; no mathematical specialization is made.

The main gap is L030-L032/C032a's all-degree actual-Xi algebraic-square
positivity. The intermediate target was an independent sufficient
ordinary-series hypothesis from Zhu Proposition4.2. Its possible use
was a logarithmic Hankel sign input. The admission test required the
actual coefficients, logarithm normalization and shift to match, with
an independently checkable premise. That test is not met.

## Duplicate correction and inspected source

The supplied nomination correctly described the 6November assessment,
but omitted the later completed comparison785 in
[assessment784](literature/2026-11-13-post-countermodel-theta-bridge-discovery-784.md),
Section “2–3. Cumulant inputs and the newly read ordinary-logarithm proof”.
That comparison already read Proposition4.2's entire proof and parked
the actual-theta interface. Its
[stop785](../ATTEMPTS/2026-11-13-post-countermodel-three-input-source-stop-785.md)
is retained. Repeating that verdict is not an informative new negative.

Read Bao-Xuan Zhu, *Coefficientwise Hankel-total positivity from a
universal cumulant lifting*,
[arXiv:2611.01172v1](https://arxiv.org/html/2611.01172v1#S4.SS2),
31October2026, Section4.2, Proposition4.2, statement and full proof
(4.6)–(4.9). The exact input is a real Stieltjes sequence b_n with
b_0=1, used as **ordinary** coefficients B(t)=sum b_n t^n. The
conclusion concerns the once-shifted **exponential** coefficients
kappa_n of log B. This includes formal series of zero radius; no
determinacy or exponential-moment premise is imposed.

The proof chooses a probability measure for b_n and defines
L(s)=integral (1+sx)^(-1) dmu(x), h=1/L-1, phi=-log L. A possible
atom at x=0 becomes a constant Stieltjes term. It uses reciprocal
Stieltjes/Bernstein membership and composition, then differentiates
using the order-n majorant n!x^n. Each logarithm coefficient uses only
finitely many right derivatives. The Levy representation and monotone
convergence give the measure d delta_0+x rho(dx) for kappa_(n+1),
including drift and finite moments. These are the source's proof
steps, not a new proof or a theta application. The alternative Goldie
argument is mentioned by Zhu; its primary proof was not retrieved or
used as a separate input.

## Essential Bernstein coverage and its limits

R. L. Schilling, R. Song and Z. Vondracek, *Bernstein Functions:
Theory and Applications*, second revised and extended edition,
de Gruyter Studies in Mathematics37 (2012),
[publisher DOI](https://doi.org/10.1515/9783110269338).
The bibliographic edition/ISBN was checked against the publisher and
[author page](https://motapa.de/bernstein_functions/index.shtml).
Read primary book text reproduced in the
[second-edition transcription](https://dokumen.pub/bernstein-functions-theory-and-applications-2nd-rev-and-ext-ed-9783110269338-9783110252293.html):
Definition2.1 p16; Definition3.1/Theorem3.2 and its full proof pp21–22;
Corollary3.8(iii) and its proof pp28–29. The latter invokes
Theorem3.7 in both directions; that theorem's complete proof is not
claimed independently audited here. Theorem3.2 requires nonnegative
constant and drift and a positive Levy measure with integral
min(1,x) finite. Composition requires both functions to be Bernstein;
ordinary positive moments do not replace that membership hypothesis.

Theorem7.3 p93 asserts the reciprocal correspondence between nonzero
Stieltjes and complete Bernstein functions. Zhu states its use
explicitly, and Definition2.1's introductory passage confirms the
correspondence. However, the transcription jumps from the middle of
Proposition7.1 to p106, omitting the full theorem/proof passage.
A search-engine extraction of the primary PDF displayed the theorem
and short proof, but the PDF itself timed out on opening and a second
host spelling was inaccessible. A shell retrieval failed DNS. These
previews are not counted as inspected full source evidence. No access
campaign or dependent research is authorized from them.

Read the author's two-page second-edition
[errata, dated2December2022](https://motapa.de/bernstein_functions/misprints-ssv-2nd.pdf).
It lists no correction to Theorem3.2, Corollary3.8 or Theorem7.3.
This is an errata check, not verification of the omitted proof.

## Applicability and decision

Reused L021, L025 and L030's complete relevant proofs. L019 supplies
the actual positive K; L024 supplies the paired product used by L025.
L021's series uses M_(2n)/(2n)!, with alternating signs in the square
variable. L025's logarithm uses -S_k/k; L030 requires S_(i+j+2),
with algebraic rather than modulus squares. These are the already
established local conventions. Zhu instead assumes ordinary Stieltjes
coefficients and concludes a once-shifted exponential logarithmic
sequence. This review derives no conversion formula or sign claim.

Choosing the raw positive theta moments changes the series. Choosing
the factorial-divided coefficients requires an additional Stieltjes
premise. Neither the source nor the retained comparisons supplies that
premise and the required sign/factor/shift transfer. No claim is made
that a proposed actual sequence passes or fails a finite moment test.
The missing full book proof cannot repair this applicability failure.
Park this citation-only lead, consistently with785. Reopening needs
materially additional actual-law information, not another retrieval
or repetition of the normalization comparison.

Full matching and supporting Mathlib coverage remains unchecked; no
absence claim or cross-notebook input is made. No lemma, mathematical
script, PROOF or DAG changed. This step is STALLED relative to a new
research decision: it repairs duplicate/source-read bookkeeping and
adds limited Bernstein coverage, without mathematical or RH progress.

The next nomination focuses on an explicit signed-remainder estimate
at the nonsingular Schur gap, rather than another automatic positive
representation. It is uncovered and REVIEW_REQUIRED. No creative
mechanism or mathematical calculation is approved by this review.
