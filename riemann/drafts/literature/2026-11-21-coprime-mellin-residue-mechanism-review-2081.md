# Coprime Mellin residue mechanism: completed source comparison2082

TARGET: Assess whether the two-variable Mellin/Euler-product representation of GC12 at q=2 and the fixed pole-neutral bump cancels reciprocal-zeta pole residues through the coprime local factors and actual ratio kernel, sufficiently to support M_K<=C_epsilon K^epsilon while leaving the high primitive sector unpaid.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Step2082 searched exact coprime Mobius double-Dirichlet/Mellin, reciprocal-zeta and multivariable Euler-product terminology; reused source-notes2080/comparison2079. No adequate cancellation theorem was found in this bounded search. Queries and inspected ranges: drafts/literature/2026-11-21-coprime-mellin-source-notes-2082.md.
SOURCE_EVIDENCE: Bhowmik--Essouabri--Lichtin Lemma1 and complete extraction proof, Theorem1, author proof PDF pp4-8 https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/multieuler.pdf ; Delabarre2013 definitions and continuation/boundary statements pp226-230 https://www.numdam.org/article/BSMF_2013__141_2_225_0.pdf ; Ramare2016 Theorem1.1 and endpoint proof pp109-110,116 https://numdam.org/item/10.5802/ambp.356.pdf and October2021 addendum pp1-4 https://ramare-olivier.github.io/Maths/TruncatedPerron-5-Addendum-04.pdf ; Kowalski A.3.1-A.3.2 https://people.math.ethz.ch/~kowalski/number-theory.pdf ; Van Hemert v1.0.0 GC12-GC18 https://raw.githubusercontent.com/LeonardSEO/riemann-xi-zero-detection/refs/tags/v1.0.0/paper/paper.tex . Full citations, hypotheses, read boundaries and C034r interface: source-notes2082. Recovery2083 verified direct access to the extraction PDF, Perron PDF/addendum and tagged GC12-GC17 passage; other inspected coverage is reused.
COMPARISON: General meromorphic zeta-factor extraction is known; its hypotheses and conclusion do not supply cancellation of a reciprocal-zeta pole after the actual ratio integration or a sharp square cutoff. No inspected theorem gives the GC12 subpower upper. No application, new factorization or residue has been derived in this literature turn.
GAP: The exact GC12 local factors, valid continuation domain, integrated principal part and both cutoff boundary terms must still be proved in a mathematical attempt. Global contour/growth errors, high primitive control and actual-Xi mixed transfer remain independent gaps.
REASON: Accessible primary coverage now supports one bounded pole-removal test under EXPLORE; it supplies tools and qualifications, not the requested cancellation or upper. Missing a matching theorem is not a source-access blocker or evidence of novelty.
SCOPE: Exact TARGET unchanged: q=2, fixed bump, coprimality, rho, actual C_h and all square-cutoff terms retained. One future attempt may establish the exact representation and test one hypothetical zero's full integrated principal part; no unrestricted subpower contour shift or global upper is preapproved as a known fact. This updated ready assessment receives separate supervisor approval next turn.
LITERATURE_REASON: The new target asks about exact two-variable meromorphic factors and ratio-transform residues, which the ready detector assessment2080 and prior GC12 bound comparison2079 did not cover.

## Exact proposed object and purpose

The main gap remains L030-L032/C032a actual-Xi all-degree algebraic
mixed positivity. The detector C034r makes one possible downstream
contradiction threshold precise; it does not prove that an arithmetic
estimate will reach it. The upper-bound target is the same signed
GC12 sum reviewed in2079. Rename its primitive cutoff K here to keep
it distinct from the fixed Fourier projection band H in C034r:

\[
 M_K=\sum_{\substack{a,b\le K\\(a,b)=1}}
 \frac{\mu(a)\mu(b)\rho(ab)}{\sqrt{ab}}
 w_Q(\log(b/a))C_h(\log(b/a)),\quad Q=\log2,
\]
\[
 \rho(n)=\zeta(2)^{-1}\prod_{p\mid n}\frac p{p+1},\quad
 w_Q(r)=1_{|r|<Q}\int_{|r|/2}^{Q-|r|/2}
       e^{-s/2}(s^2-r^2/4)ds,
\]
with \(f=J(C_\Phi h)\),
\(C_h(r)=\int f(y)\overline{f(y+r)}dy\), and the exact fixed
\(h=-g''+g/4\), \(g(y)=e^{-1/(1-y^2)}\) on \(|y|<1\) and zero
otherwise, as in C034r. This is a transcription of the prior assessed
interface, not a new identity or estimate. The sought bound is one-sided
for every epsilon>0 and integer K>=2. A negative M_K is not a
counterexample to that bound.

## Bounded discriminator to assess before attempting it

The candidate is to preserve the common-prime restriction in an exact
two-variable Dirichlet/Mellin representation and ask whether its
arithmetic factors together with the actual ratio-kernel transform
annihilate the pole contributions that obstruct shifting toward the
subpower contour. Merely writing an Euler product is not an advance
on that obstruction. No product formula or cancellation has been
derived in this step.

First compare precise primary statements for this weighted coprime
Möbius series and its finite square cutoff. Reuse earlier known-result
comparisons unless a statement specifically covers the changed target.
Retrieve only needed hypotheses and essential residue/contour cases.
If an adequate known theorem applies, import it with the necessary
specialization. Otherwise a later bounded mathematical test should
track one arbitrary hypothetical off-line zero through the exact
integrated numerator and cutoff terms. Continue only with a paid
cancellation identity or another concrete signed estimate reaching
the subpower threshold; an explicit surviving residue rejects this
particular pole-removal contour mechanism, not RH or every GC12 route.
An unexplained unsigned replacement or an assumption of zero-free
continuation also rejects the proposed mechanism.

Essential local inputs are C034r for the detection threshold and
L030-L032/C032a for the main gap. C034q and stops2076/2077/2079 remain
contrasts and exclusions, not premises. The GC12/GC13/GC18 arithmetic
decomposition is source-inspected but not locally audited; even a
successful low-sector bound would leave its error/scale choices,
the high primitive complement, full source-energy control and any
mixed-form transfer unresolved. No cross-notebook input is requested.
Full matching Mathlib coverage is unchecked.

## Direct-source recovery2083

The ready assessment's SOURCE_EVIDENCE now carries direct primary URLs,
repairing the reported missing-URL issue without changing TARGET, scope,
or EXPLORE. On 21 November2026 direct retrieval confirmed the identities
and inspected locators of the author extraction PDF (Lemma1 and Theorem1),
published Perron PDF (Theorem1.1), dated addendum (Theorem1.1 and Note1),
and tagged source (GC12-GC17, lines11613-11687). The earlier complete
essential-case readings in source-notes2082 are reused, not replaced by
these smaller access checks. Delabarre and Kowalski coverage is also
reused; neither is newly audited here. No new search for an unchanged
theorem, factorization, specialization, residue calculation or lemma.

The source comparison remains unchanged: the extraction and inversion
tools do not establish integrated pole cancellation. In particular the
fixed-height Perron statement requires a line strictly above absolute
convergence, retains absolute errors, and the addendum does not license
an unqualified simultaneous good-height choice. The prior signed-upper
and inverse stops2076/2077/2079 keep their stated scope. No new theorem
or mathematical obstruction is claimed. This recovery is STALLED as a
mathematical outcome: it repairs source traceability, not the main gap.
The repaired ready assessment is submitted for separate supervisor
approval before the unchanged bounded mathematical attempt.

## Completion2082 and bounded next invocation

The preceding nomination is retained as the historical proposal.
Comparison2082 performed source review only. The complete theorem-level
comparison and access record are in
[source-notes2082](2026-11-21-coprime-mellin-source-notes-2082.md).
EXPLORE approves investigation of the unchanged question after separate
next-turn approval; it asserts neither an exact factorization nor
cancellation. No original mathematics was derived and approved here.

The proposed attempt must distinguish three levels: a candidate pole of
the arithmetic Dirichlet series; a nonzero principal part after the
actual ratio-transform integration; and a contribution to the finite
square-cutoff quantity. Evidence at the first level alone does not
settle either later level. Likewise a surviving oscillatory contribution
does not by itself disprove the one-sided upper. The original statement
that a surviving residue rejects the mechanism means a justified
surviving principal part of the complete representation required by
that pole-removal mechanism, with endpoint/cutoff contributions retained.

Work with one arbitrary hypothetical zero rho=1/2+delta+i gamma,
0<delta<1/2, of finite order m>=1. Neither a rightmost zero nor
simplicity nor RH may be assumed. First obtain a representation in a
proved region of absolute convergence. A local Laurent test must state
its neighborhood and every nonvanishing/domain condition. Do not shift
an infinite contour or commute an integral through a singularity using
meromorphic continuation alone. Keep finite-height horizontal and
truncation errors visible, or explicitly leave the global shift open.

Continue this mechanism only with a paid cancellation identity for the
complete relevant principal part or another concrete estimate toward
the subpower threshold. A proved surviving part rejects automatic
pole removal; failure to justify the representation is an unfinished
attempt, not noncancellation. Routine Euler extraction alone is no
substantive advance. Save partial reasoning and do not repeat an
unsuccessful test without a refined mechanism or new input.

The creative purpose, if approved, is the integrated cancellation test
in the signed covariance, not routine Euler-product algebra. Its payoff
is a possible low-sector payment in a later complete energy argument.
GC13/GC18 remain source-inspected and unaudited locally; both primitive
uppers, scale/error payment, the full energy estimate and mixed transfer
are unresolved. No complete candidate, cross-notebook input or matching
Mathlib theorem is claimed. No extra literature is needed for this
unchanged bounded test; a genuinely enlarged scope needs review.
