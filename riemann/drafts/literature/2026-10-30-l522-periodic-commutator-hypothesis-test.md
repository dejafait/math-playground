# Periodic commutator: one necessary-hypothesis test

TARGET: Test whether [h(A_I),D_per], h(s)=s/(1+s^2), extends to a bounded form on L2(I) for L522's full signed killed operator, by proving a finite bound or an explicit boundary-sensitive unboundedness witness.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: The completed three-mechanism review in 2026-10-30-l522-collective-prime-sign-discovery.md records exact logarithmic/killed/periodic-commutator searches and the nodal, transport, localization, Abel and fixed-symbol failure comparison. No matching application theorem was inspected; no originality is claimed.
SOURCE_EVIDENCE: Moller--Westrich arXiv:1006.0410v2, https://arxiv.org/html/1006.0410v2 , Definition 1.1, Condition 1.4, Theorem 1.6 and Section 4; Teschl GSM 99, version 12 February 2009, https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf , Section 2.2 (2.35)--(2.39), printed pp.62--63 (PDF pages 74--75). Direct access and the load-bearing criterion/hypotheses/domain were rechecked in the URL-recovery review below; the prior proof-case review is reused.
COMPARISON: Known theory supplies the C1 criterion and self-adjoint periodic generator, but no bound for this killed signed operator. Endpoint-fixed transport stationarity and whole-line Fourier multipliers are different statements. No favorable commutator, H1 nullvector or local Mourre estimate is assumed.
GAP: Prove finiteness or divergence of the specified form norm, with the full perturbation retained. Finiteness would still leave C2, a local Mourre estimate, renewal-trace compatibility and transfer unresolved.
REASON: One independent operator-domain discriminator under the commutator mechanism survives; no direct sign mechanism does. Failure parks this fixed regularization/generator, while success justifies reviewing the next higher-regularity premise. No new mathematical result is derived here.
SCOPE: One necessary-hypothesis proof attempt after separate next-turn approval. Fixed 0<a<A, I=(0,ell), ell=2a>log(2), A_I exactly as in L522. No periodic replacement of A_I, full-Weil proof audit, nullvector existence, trace vanishing, sign or family estimate is included.

The main gap is actual-Xi all-degree positivity. This tests a
prerequisite for a possible eigenstate-regularity route to the
conditional trace obstruction. Theorem 1.6 additionally requires
higher regularity and Condition 1.4. Any subsequent compatibility
argument with the nonzero renewal trace also remains to be proved.

Use complex L2(I) and the canonical complexification of the
real-coefficient model; downstream nullvectors remain real. Put
B=h(A_I) by the self-adjoint spectral calculus. Choose

    D_per=-i d/dx,
    Dom(D_per)={g in H1(0,ell): g(0)=g(ell)}.

Use Teschl's closed periodic derivative, rescaled unitarily from
(0,2pi). This changes only the conjugate operator. A_I still uses
zero extension, its actual part domain, c=log(2pi), nu_rho, both
prime shifts, all equality atoms and the signed pole. Test the
source's commutator form on Dom(D_per), not undefined products.
The threshold is one finite C with

    |commutator_form_B_Dper(phi,psi)|<=C ||phi||_2 ||psi||_2

for every domain pair, or normalized pairs with exact form values
tending to infinity. Constructing a controlled Fourier or boundary
sequence is part of the attempt. Finite matrix previews prove neither
alternative. Import the C1 criterion rather than reprove its theory.

Do not substitute h(G_I) or a periodic Fourier multiplier for B.
A reference obstruction must survive the full signed perturbation.
As recorded in the pole-resolvent assessment, an L2 resolvent bound
alone supplies neither bounded forcing nor endpoint traces. Do not
differentiate renewal-trace errors or assume H1. The test itself
requires no nullvector existence; downstream use retains L516/L521/
L522's real normalization, nonzero left trace and exclusion
log(2)!=ell-d_n. No simplicity, positivity or gap is granted.

Continue only on a rigorous bound or divergence witness. If the
attempt yields only a formal derivative, stationarity identity or
uncontrolled trace, save the gap and park this implementation pending
materially new input. Failure of this fixed h/D_per pair is not a
ban on other generators or regularizations. Success supplies no C2,
local positive estimate, S<=P-H, family rate or RH conclusion.

This is development of a source-supported prerequisite, not an
approved creative sign mechanism. Full Mathlib matching is unchecked;
there is no cross-notebook input. The direct-source recovery review below completes the separate literature
approval of this unchanged target; it is not a completed proof.


## Direct-source recovery review, 2026-10-30

LITERATURE_REASON: Repair the supervisor-reported missing direct source URL;
reuse the existing search and proof-case assessment without broadening the target.

[Moller--Westrich v2](https://arxiv.org/html/1006.0410v2),
Definition 1.1 and the following paragraph, explicitly test the form
(B*phi,D psi)-(D phi,B psi) on Dom(D) pairs for bounded B. Its bounded
extension is equivalent to B in C1(D). This is the criterion to import,
not an application bound. Condition 1.4 requires self-adjoint H,D, a
regularization h_lambda, a smooth local cutoff f with f(lambda)=1 and
h_lambda'>0 on its support, and
i ad_D(h_lambda(H)) >= C0-C1(1-f(H))^2-K, with C0,C1>0 and K compact.
Theorem 1.6 additionally requires C(k+1) regularity to conclude
psi in Dom(D^k). Thus k=1 still needs C2 and the estimate. The prior
Section 4 proof-case review is reused; equations (4.1)--(4.2) and its
three-step organization were rechecked. No application of that theorem
to the notebook operator is approved by this source review.

[Teschl, GSM 99, February 12, 2009](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
Section 2.2, (2.35)--(2.37), printed p.62, was rechecked including
the integration-by-parts boundary calculation. The initial C1 periodic
domain is distinguished from its closed H1 periodic domain; the latter
is self-adjoint. Equations (2.38)--(2.39), pp.62--63, give the periodic
eigenfunctions. Interval rescaling changes only this generator, as
already specified above. It supplies no domain invariance or regularity
for the killed operator.

Decision remains EXPLORE for exactly TARGET. Direct source access is now
recorded here rather than only in a referenced assessment. This is a
process repair with no new mathematical evidence or novelty claim. The
existing nodal/transport/Abel/localization/resolvent/fixed-symbol stops
remain comparison evidence. There is no essential source blocker for
the bounded-form test; whether the actual form is bounded is precisely
the research question. Mathlib matching remains unchecked.
