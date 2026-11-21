# Complete even resolvent — one weak-pairing discriminator

TARGET: Test whether B=<v,(A_e+16I)^(-1)u><0 for the fixed even quartic bumps in assessment822, using a certified spectral floor and full L2 operator residual, with one trial space of dimension at most256.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the bounded exact-Weil, real-resolvent, positivity-improvement and residual search in completed assessment821/step822. Narrow local searches of Weil/resolvent assessments and stops found no certificate for this fixed pairing; no novelty or exhaustive absence is asserted.
SOURCE_EVIDENCE: Teschl GSM99 version12February2009 Theorem2.18 p77 and Lemma2.7 proof p66 supply the real resolvent norm estimate after a proved scalar floor; Section10.5 pp235-236 identifies positivity through nonnegative test pairings. C759a Sections1,3 and L741(13)-(17) supply the complete form, supported Fourier domain, bounded prime shifts and exact multiplier. Precise URLs/read limits are in assessment821's completed comparison.
COMPARISON: The resolvent norm bound and a posteriori residual comparison are standard operator theory. Only the actual-form/domain specialization and one certified mixed pairing remain. The test does not require an ordinary Green kernel, background positivity, a ground-state sign, or a full source positivity certificate.
GAP: No bound below-16, operator-domain verification, approximate response, full residual norm or sign of B is established by this nomination. A nonnegative B does not imply positivity improvement. Even sign/simplicity, parity, other windows and Xi realization remain independent.
REASON: The pointwise-kernel proposal lacked an independently available kernel estimate. A single full-resolvent weak sign certificate is independently evaluable without that missing representation and can refute the fixed-parameter positivity implementation if negative. It is routine specialization/reproduction, not a creative central-RH mechanism.
SCOPE: One research attempt only after separate supervisor approval of this newly written assessment; C759a's unchanged complete even real form on [-1,1], parameter-16, exactly the forcing pair and trial ceiling below. No pointwise-kernel claim, spectral-parameter sweep, forcing sweep, eventual positivity or source-certificate import.

## Exact fixed test and its relevance

Let A_e denote the self-adjoint operator represented by C759a's closed
form restricted to the real even subspace. Complexification may be used
for the standard spectral theorem, with its real structure retained.
Write

    h(s) = (max(1-s^2,0))^2,
    u(x) = h(40(x-1/5)) + h(40(x+1/5)),
    v(x) = h(40(x-4/5)) + h(40(x+4/5)).

These specify the proposed forcing and testing functions on [-1,1],
not an assertion about their resolvent responses. First verify all
needed function-space properties. The tests are chosen to be
nonnegative and even without imposing the unknown ground-state sign.
No neutrality or prime deletion is permitted.

The unresolved main gap is L030-L032/C032a's actual-Xi all-degree mixed
positivity. The intermediate discriminator asks whether this ONE
complete even resolvent has a negative pairing on the specified tests.
Such a certificate would park the positivity-improving implementation
at -16. A positive or unresolved answer cannot establish ground-state
sign/simplicity. Neither answer settles parity or RH.

## Known input, needed specialization and bounded test

Use [Teschl, Theorem2.18](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf)
for the real inverse bound only after proving A_e>=E I with E>-16.
C759a's m_* and full prime cost C provide existing lower-bound inputs;
verify the even pole sign and the full arithmetic comparison on the
closed form domain. Do not assume the positive complete energy of
any external certificate, or confuse this Friedrichs operator with
L741's causal nonsymmetric generator. No spectral comparison is
claimed in this literature-only nomination.

For one approximate response w, the future standard specialization
must justify a full L2 residual certificate. The sought sufficient
negative test has the form

    <v,w> + ||v||_2 ||u-(A_e+16I)w||_2 / delta < 0,
    delta = E+16 > 0.

This is a proposed a posteriori certificate to justify and evaluate
next turn using the cited inverse bound and Cauchy-Schwarz; it is not
a new inequality derived or accepted here. Its strict zero threshold
must include every numerical and analytic error. The residual is on
the whole physical interval, not just the trial coordinates.

Use a single space

    (1-x^2) span{P_0(x),P_2(x),...,P_510(x)},

with P_j the Legendre polynomial, of dimension256; a subspace is
allowed. Establish the zero-extended trial functions' operator-domain
membership and identify the actual form operator action before using
an L2 residual. If a candidate fails this condition, stop and record
that failure; do not use an unexplained form residual as an L2 norm.
The known Fourier multiplier and all shifts/poles can be used to
bound the complete residual, including Fourier tails if evaluated
there. A finite matrix inverse or sampled kernel alone is insufficient.
No new numerical method needs to be presented as a theorem.

Continue only to the strict certified sign decision for this fixed
pair. If the floor/domain fails, the full error cannot be bounded,
or the enclosure contains zero at this trial ceiling, preserve the
partial result and stop this implementation as inconclusive. A
certified negative pairing refutes positivity at-16 only. A certified
nonnegative pairing ends this witness test without promoting it to a
positive-operator claim. No forcing/parameter/basis-size sweep beyond
the single stated ceiling is approved.

## Coverage limits and next approval

The exact operator formula is already canonical in C759a; source
normalization and weighted-domain evidence are reused, not rederived.
The cited norm estimate covers the generic error machinery; the
remaining floor, domain action and full residual are its necessary
specialization. This is why a future result is REPRODUCTION, not a
claim of progress beyond those sources. Any successful specialization
belongs in a canonical lemma with the required sections and precise
citations, after this newly written ready assessment receives its
separate approval. This literature step has produced no such lemma.
Mathlib full-result and supporting-theorem coverage is unchecked.
