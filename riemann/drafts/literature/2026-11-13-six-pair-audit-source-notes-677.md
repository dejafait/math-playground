# Six-pair audit source coverage677

Literature-only comparison of the exact saved audit target in
assessment676. C998h was read in full to inventory its claimed uses of
standard tools; no identity was independently derived or certified.
C998a Section1 and C998g Section1 were read narrowly for source scope.
Assessment675, source-notes675, scope-stop675 and histories675/676 were
reused for duplicates, known stronger results and recorded failures.
No theorem or numerical data from another notebook was read.

## Essential primary tools and what was actually read

Folland, *Real Analysis: Modern Techniques and Their Applications*,
second edition, Wiley1999: Theorem2.24, printed pp54-55, statement and
proof; Theorem2.27, p56, both parts, proof and following local-interval
qualification, read in the [primary-book text mirror](https://djvu.online/file/NPF4BEtSuqdFA).
Theorem2.24 needs almost-everywhere convergence and one integrable
majorant for the sequence. Theorem2.27 requires integrability of each
parameter section; continuity uses a common integrable bound and
pointwise continuity, while differentiation requires an existing
parameter derivative with a common integrable bound. Bounds may be
local on compact parameter intervals. Its proof uses dominated
convergence on difference quotients. These tools permit checking the
claimed limits, not assuming them.

Rechecked Section2.5 Theorems2.37/2.39, pp67-68, including the proof
of2.37 and completion qualification of2.39, in the
[university-hosted primary extract](https://people.math.sc.edu/girardi/m7034/1617/hw/FollandRA2edProdMsr.pdf).
Tonelli requires nonnegative measurable data on sigma-finite products;
Fubini requires absolute integrability. The completion version allows
almost-everywhere sections. Neither supplies boundary traces or
parameter differentiation. Finite products and complex products retain
these hypotheses; the audit must check them at each use.

The targeted query was `Folland Real Analysis Theorem 2.27
differentiation under integral sign 2.24 dominated convergence pdf`.
The search result located the primary book, not an additional closure
result. A full PDF mirror at
https://buchholzmd.github.io/paying-in-attention/Assets/Folland---Real-Analysis--Modern-Techniques-and-Their-Applications.pdf
failed web opening because its content length exceeded the tool limit.
Its snippet was not the final evidence: the accessible primary-book
text supplied both complete theorem statements and proofs. OCR has
minor symbol damage; the hypotheses above and theorem numbering are
readable. No secondary discussion or search snippet is imported.

Blower, *Hankel operators that commute with second-order differential
operators*, [arXiv:0712.1013v1](https://arxiv.org/pdf/0712.1013v1),
6December2007, Theorem2.1 and proof(2.3)-(2.5), printed pp3-4,
rechecked. The coefficient condition a(0)=0, a'''=Aa', the
sum-variable quotient condition on b and the displayed ODE for phi
lead to commutation on compactly supported smooth functions on the
half-line. The proof displays its endpoint bracket. C998h's finite
cell and cosine domain are different; no commutation theorem is
imported. Ordinary integration by parts on a smooth positive-cutoff
compact interval is the standard named calculus tool to be applied
and checked directly, not a theorem about this singular compressed
operator. Its use needs the claimed regularity on that interval.

## Comparison and audit obligations

No new general theorem needs reproof. The new2.24/2.27 coverage makes
explicit a distinction absent from assessment676's original source
field: absolute Fubini coverage alone would not authorize differentiated
interchanges or singular endpoint limits. The specific majorants in
C998h must still be checked in the research audit. We do not endorse
their arithmetic, constants or applicability by approving the tools.

The audit must examine C998h(1)-(3)'s real-integral definitions and
claimed endpoint values, without substituting an unread dilogarithm
identity. It must check that H,P,T and dotted moments are independent
one-variable data. It must check regularization before removal of the
cutoff, both ends of the complete Wronskian brackets, and convergence
of the original K_tau integrals rather than only a differential equation.
The spectral derivatives use lambda=k^2 near positive lambda_1 and
lambda_2; their local domination and differentiation of endpoint
moments are separate obligations. A spatial-diagonal identity is not
frequency-diagonal data. Finally replay all six substitutions and the
C998a(4) unitary parity convention and square coefficient1/4.
These are proposed checks of existing mathematics, not completed
checks or new results in this source review.

Assessment675/source-notes675 already compared Arico--Rodriguez,
Sweet--Brent and Tracy--Widom at theorem/proof level. Their generator,
coincident-frequency, domain, stability and endpoint limitations are
unchanged. The inaccessible GKO leads remain nonessential and unread;
no repeated retrieval was attempted. Earlier652/657/660/662/672 stops,
673 hierarchy stop and675 turnkey-import stop remain intact.
A primary theorem resolving the whole six-case closure was not found
in that bounded search. Neither absence nor originality is established.

Decision: EXPLORE for exactly assessment676's audit. This is adequate
source coverage for an independent conceptual audit, not an IMPORT
of the six identities. Passing would preserve six-case analytic closure
only. Stop or repair on an invalid identity, missing convergent datum,
unjustified interchange or hidden integrated output product. New
hypotheses or general-mode/numerical claims need a separate assessment.
No new lemma, mathematical script, witness replay or PROOF/DAG edit is
appropriate in this literature-only turn. Mathlib full matching
coverage remains unchecked; no absence claim is made.
