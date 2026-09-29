# Counting law with a positive Fourier kernel: source assessment

TARGET: Construct a real even order-one F satisfying all conclusions of L354 that is also the Fourier transform F(z)=∫_R K(u)e^{izu}du of a smooth strictly positive even kernel K with ∫_R K(u)e^{c|u|}du<∞ for every c>0.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded searches on 2026-09-27 compared positive Fourier kernels, finite nonreal-zero insertion, Laguerre counterexamples, and imaginary-order Bessel zero theorems; the queries and inspected statements are recorded below. No inspected theorem states the full joint target.
SOURCE_EVIDENCE: Lagarias, arXiv:0712.3238v6, Theorem 4.1 and (4.7), pp. 16–18, https://arxiv.org/pdf/0712.3238v6; Gasper, arXiv:0801.2996v1, (1.5)–(1.7) and §2, https://arxiv.org/pdf/0801.2996v1; Paris, arXiv:2204.09306v1, Theorem 2, p. 5, https://arxiv.org/pdf/2204.09306v1; DLMF 10.32.9, https://dlmf.nist.gov/10.32.E9; Csordás, arXiv:1309.0055v2, Propositions 2.2–2.3 and Example 3.12, https://arxiv.org/pdf/1309.0055v2.
COMPARISON: Known theorems supply a positive-kernel Bessel background, its entire order and full zero classification, a two-term count with bounded remainder, and the local negative-pair mechanism. They do not establish positivity of the kernel after the required single-quartet modification or every exact L354 condition simultaneously.
GAP: Check the scaled background's precise counting convention, gap inequality and small-zero exclusion, and prove that the quartet multiplier retains a strictly positive whole-line kernel for parameters also giving D_1(F;A)/F(A)^2<−31. No such compatibility result is asserted here.
REASON: The missing zero-classification information is supplied by an independently inspected primary theorem. Reuse the covered background and sign results; test only their compatibility with the stronger kernel and exact model requirements in a later research turn.

## Scope and relevance

The saved target is unchanged. This completes its source assessment,
not its construction. The shared rules, local goal, whole overview,
DAG, checkpoint, pending assessment and existing changes were read.
No new mathematical result is derived in this literature-only step.

The immediate gap is whether the count and gap data tested in L354,
together with a positive Fourier kernel, still permit a negative
first Laguerre sign. This is a diagnostic for a proposed sufficient
condition, not an attempt to replace actual Ξ by a model.

The full target retains F(0)=1, the canonical-product conclusion,
order exactly one, N_F(T)=M(T)+O(1) counting positive real parts with
multiplicity, simple real zeros outside |z|≤4 apart from one simple
quartet ±(A±ib), A>40, 0<b<1/4, and the normalized sign below −31.
The new F need not be L354's inverse-counting product.

In particular, “all conclusions of L354” retains its displayed
bound t_(n+1)−t_n≤2π/log(t_n/(2π)), with the range required there.
An eventual O(1/log T) estimate alone is not a match for that
literal conclusion. The scaffold's shorter asymptotic description
must not silently weaken the saved action. A proposed background
must also handle its initial real zeros, not just its asymptotic tail.

The new kernel must be smooth and strictly positive at every real
point, with every exponential moment finite. Positivity only inside
compact support is insufficient. No theta modular identity, Euler
product or equality with Ξ is requested.

Plausible use: a successful model would stop this stronger generic
first-sign certificate. The actual first sign, the other low
Laguerre levels needed by L320, and the endpoint arithmetic margin
would remain open. L296's positive bands above coefficient 1/4
still do not cover L320's initial segment. No sign or zero-exclusion
range changes in this review.

## Search record and prior work

Representative queries actually used on 2026-09-27:

- Bagirova Khanmamedov zeros Macdonald function imaginary order simple real zeros 2020
- "On Zeros of the Modified Bessel Function of the Second Kind" pdf Bagirova
- "Fourier" "positive" "kernel" "Riemann-von Mangoldt"
- "Laguerre" "Bessel" "nonreal" zeros kernel
- "Pólya" "Fourier" "finitely many" "nonreal" zeros kernel
- "Fourier transform" "positive kernel" "prescribed" zeros
- "positive" "kernel" "polynomial" "cosh" "nonreal zeros"
- "Lagarias" "Morse" "zeros" Whittaker 2009
- "Fourier" "positive" "kernel" "single" "quartet"
- "Laguerre inequality" "positive kernel" counterexample
- "positive kernel" "order one" "zeros"
- "Fourier" "Riemann-von Mangoldt" "quartet"

These queries found relevant background and partial constructions;
they do not certify originality or the nonexistence of a full match.

The ready
[preceding assessment](2026-09-27-count-preserving-laguerre-model.md)
is reused for canonical-product existence/order and the symmetric
local-sign qualification. Its optional Bessel classification gap
is resolved below without claiming to have read the unavailable
2020 paper. Its prescribed-zero method by itself has no positive
Fourier-kernel assertion.

L050–L057 were compared through their explicit constructions and
the overview. Their positive shifted kernels introduce infinitely
many nonreal zeros, whereas this target permits exactly one quartet.
L262's Gaussian construction has order two. L264 has a continuous
compactly supported kernel, positive only in its support interior,
and supplies no required counting law. L354 supplies the count and
sign without the kernel. These are distinct partial matches; their
separate conclusions cannot be combined as an established result.

The comparison-energy transfer audit remains applicable: the
auxiliary spectral argument for the comparison function does not
supply the required equation and boundary conditions for actual Ξ.
This review does not reopen that stopped transfer or L353's
unrelated Mellin-pole implementation.

## Inspected primary statements

### Full zero classification and counting background

Jeffrey C. Lagarias, The Schrödinger Operator with Morse Potential
on the Right Half Line,
[arXiv:0712.3238v6, 18 August 2009](https://arxiv.org/pdf/0712.3238v6).
Read Theorem 4.1 and proof, pp. 16–17, and (4.7), p. 18.
For fixed real κ,u₀, W_(κ,μ)(e^u₀) has order one, maximal type.
At κ=0 its zeros are simple, nonzero and purely imaginary; the
two-sided count is

\[
 \frac{2}{\pi}T\log T+
 \frac{2}{\pi}(2\log2-1-u_0)T+O(1).
\]

Equation (4.7) identifies K_μ(w) with this κ=0 case. Conversion
to N_F and calibration of both coefficients remain to be checked.
Neither the explicit gap inequality nor the modified-kernel target
is stated.

### Fourier representation and limits of zero-preservation results

[DLMF 10.32.9](https://dlmf.nist.gov/10.32.E9), inspected on
2026-09-27, gives

\[
 K_\nu(x)=\int_0^\infty e^{-x\cosh t}\cosh(\nu t)\,dt,
 \qquad |\arg x|<\pi/2.
\]

This is the representation to specialize, with positive real x
and imaginary order. It provides no positivity theorem for a
kernel changed by a differential operator.

George Gasper, Using integrals of squares … to prove … only real zeros,
[arXiv:0801.2996v1, 19 January 2008](https://arxiv.org/pdf/0801.2996v1).
Read pp. 2–4, (1.5)–(1.7), the unnumbered Pólya lemma, and §2
through (2.6). The paper proves zero reality for the Bessel
transform through an integral of squares and records the
real-zero-preserving symmetric imaginary shift under a
genus-zero-or-one hypothesis. This is useful background to import,
not a method that inserts the required quartet. Its conclusions
do not assert that an arbitrary polynomial multiplier preserves
positivity of the inverse Fourier kernel.

### Positive-zero asymptotics and the exact gap obligation

R. B. Paris, On the ν-zeros of the Bessel functions of purely
imaginary order,
[arXiv:2204.09306v1, 20 April 2022](https://arxiv.org/pdf/2204.09306v1).
Reused the preceding reading and inspected §2.1, especially the
phase equation preceding Theorem 2 and (2.17), pp. 4–5. For fixed
x>0, Theorem 2 gives a large-index expansion for the positive zeros
of K_(iν)(x), beginning with m₋/W(λm₋), where
m₋=(n−1/4)π and λ=2/(ex). The following terms are also specified.

This is stronger information than the leading ν_n∼πn/log n.
It is still not a stated bound for every consecutive gap of the
calibrated model. A later specialization must justify any use of
remainders in adjacent-zero comparisons and check the initial
range separately. Neither subtracting leading asymptotic
equivalences nor differentiating an unspecified error term supplies
the literal gap inequality.

### Local first-sign mechanism and a nearby kernel example

George Csordás, Fourier transforms of positive definite kernels
and the Riemann ξ-Function,
[arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/pdf/1309.0055v2).
Read Propositions 2.2–2.3, equation (2.3), pp. 3–4, and Example
3.12, p. 9. The propositions supply the reciprocal-square formula
and negativity from a sufficiently close conjugate pair against
a fixed nonvanishing remaining factor. The reflected factor in an
even quartet varies with b, so L354's uniform qualification must
be retained.

Example 3.12 gives a positive Gaussian-times-polynomial kernel
whose transform has four nonreal zeros and a positive first
associated spectrum. It has neither the required order/count nor
the desired negative first sign. Thus even this particularly close
four-zero example cannot be imported as the target. A reproof of
the general local sign identity would be redundant.

## Access resolution and unused leads

Bagirova–Khanmamedov, On Zeros of the Modified Bessel Function of
the Second Kind, Computational Mathematics and Mathematical
Physics 60 (2020), 817–820,
[publication record](https://doi.org/10.1134/S0965542520050048),
remains unread beyond its abstract. The MathNet DOI links and the
direct publisher PDF did not yield its full text; the ResearchGate
record requests an author copy. No request or message was sent.
Lagarias's independently read theorem and Gasper's proof supply
the relevant classification, so this inaccessible article is no
longer an essential unresolved dependency.

Mamedova–Khanmamedov,
[The zeros of modified Bessel functions as functions of their order,
41 (2021), 133–137](https://trans.imm.az/volumes/41-1/4101-13.pdf),
Theorems 1.1–1.2 and the boundary-value setup on pp. 134–135 were
inspected as a lead. The proposed test uses the Dirichlet Bessel
case already covered above; no general Robin or derivative
combination is imported.

Dimitrov–Rusev's
[Zeros of entire Fourier transforms](https://www.dcce.ibilce.unesp.br/~dimitrov/ProfRusev/EJA_Paper_24_02_11/Dim_Rus_main.pdf),
pp. 41–43, was used to locate the Pólya background; theorem support
here comes from the primary texts just described. The 2021
Krynytskyi–Rovenchak paper was opened as an asymptotic lead but
not needed or assessed at theorem level. Pólya's original papers
and journal revisions of the arXiv texts were not separately read.
Unrelated RH claims, automated research pages and search snippets
are not theorem evidence for this decision.

## Concrete compatibility test and decision

Retain the exact saved construction target, now screened as
SPECIALIZE. The selected mechanism to test is a scaled Bessel
background from the displayed integral, multiplied by the
single-quartet polynomial already used in L354. L262 illustrates
the Fourier polynomial-multiplier/differentiation method, but its
Gaussian positivity certificate does not cover this background.

Only the following compatibility work remains authorized for the
later research step:

1. Calibrate the background using the source count with the correct
   one-sided convention. Check the canonical normalization, exact
   order, simplicity, the |z|>4 condition and L354's gap inequality,
   including its initial range. Cite the general source theorems.
2. Identify the inverse Fourier kernel of the quartet modification
   and test its strict positivity on all R, with smoothness,
   exponential moments and boundary terms justified. Seek a
   parameter range, not positivity at sampled points.
3. Check that this range also permits A>40, 0<b<1/4, F(A)≠0 and
   the normalized first sign below −31, accounting for both pairs.

No scale selection, differential polynomial, positivity estimate
or modified product is calculated here. These are proof
obligations, not established conclusions of the reviewed sources.

Continue if the simultaneous compatibility test can be proved.
A full construction would settle the proposed generic implication
negatively; failure of this ansatz would stop this implementation
only. If the gap constant or kernel condition cannot be met,
record that limitation explicitly instead of relaxing the action.
An unresolved calculation must still finish its assessment and
continuation/stop decision within the remaining exploration budget.

Outcome: EXPLORATION; LITERATURE; NOVELTY_UNCHECKED. This is the
first consecutive unresolved exploration turn after L354's
informative negative result. The source gap is resolved and a
specific test is available, but the full target is neither imported
nor reproduced. The background/sign mechanisms are known; no
progress beyond the checked literature or novelty is claimed.
PROGRESS.md retains the sole current Next action. PROOF.md and
DAG.md need no change because the mathematical argument is unchanged.

## Mathlib

Full-target coverage: **not checked**. Supporting Bessel/Whittaker,
Fourier differentiation, canonical-product and first-sign coverage:
**not checked**. The named results and direct links above are
mathematical citations, not asserted Mathlib matches.
