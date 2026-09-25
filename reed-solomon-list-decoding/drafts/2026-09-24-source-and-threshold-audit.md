# Source and threshold audit — 2026-09-24

This records one initial source/scope review. The notebook had no local modifications, lemma files, or failed approaches at entry; existing modifications elsewhere in the shared repository were preserved.

## Relevance and discriminating test

The immediate gap is the exact scope of the grand list-decoding challenge, including the field-size quantifier and interleaved list convention. The intermediate target is a cited specification together with an applicability check of the strongest directly located current bounds. This prevents selecting a route already covered by a theorem or replacing the required list threshold by polynomial-time decoding.

Continue a proposed theorem-transfer route only if its actual hypotheses cover the specified evaluation domain and field, and its explicit list bound implies at most epsilon times the base-field size for fixed interleaving. Abandon a claimed full transfer if the theorem requires prime fields, silently changes the distance convention, or leaves an uncontrolled field-size exponent. A restricted theorem can still motivate a later useful step; exact finite parameters and optimality remain separate requirements.

## Source record

Versions, definitions, precise theorem locations, and access limitations are recorded in [the foundations audit](../foundations/01-target-and-source-audit.md). Only primary mathematical sources were used for conclusions. The companion paper's full definitions could not be recovered, so no mathematical research route requiring a completed scope freeze was begun.

## Discriminating test and result

The tested inference was: a capacity decoder with a polynomial list bound in the field size automatically gives the prize list threshold when the field is sufficiently large. This fails already before interleaving.

Write the available bound abstractly as M <= K q^a, for an unspecified constant exponent a. For a >= 1 and K >= 1, the integer value M = q satisfies this bound for every q >= 1, but M > epsilon* q whenever 0 < epsilon* < 1. Thus the available estimate alone does not entail the target inequality. This is a logical witness to insufficiency of an upper bound, **not** an RS code with a large list. Increasing q does not repair that inference. Taking m = 1 is enough to expose it, so there is no need for an interleaved experiment.

The formal Corollary 5.1 of TR26-164 has precisely the unresolved field dependence relevant to this test. Its informal n-polynomial wording was not promoted to a uniform-in-q theorem: the displayed proof only retains the field-polynomial estimate. No conclusion that the true list is large, or that its decoding algorithm fails, follows from this audit.

By contrast, a bound M <= B(n,m,gamma) independent of q meets the prize inequality under the explicit condition q >= B/epsilon*. TR26-169 claims such an additional geometric bound and already states its fixed-interleaving consequence. Reproving that consequence alone would duplicate the located source. The geometric argument, its constants, and its characteristic restrictions remain unreviewed.

## Assessment

The direct transfer from a polynomial-in-q bound was rejected on new quantitative evidence. The result narrows route selection without resolving the main problem or producing a lemma. It also prevents treating either a decoder or a fixed positive slack as a determination of the largest radius.

The source freeze remains partial: the ABF PDF and version archive were unavailable, and the accessible website does not define smoothness or settle the ball boundary. Recovering those definitions is a specific remaining source task, rather than permission to select arbitrary substitutes. An independent review of the stronger preprint is a possible later mechanism, not an established input.

This step contains an informative negative result, with no open exploration streak. No complete informal proof or disproof candidate appeared.
