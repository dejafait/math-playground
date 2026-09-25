# Target and source audit

Initial audit: 2026-09-24; follow-up: 2026-09-25. **ABF26 source freeze
incomplete:** the current challenge page and paper metadata were read, but
the July paper's definitions remain inaccessible. A separate
[pinned upstream ArkLib model](02-pinned-affine-line-model.md) is now readable;
it is used for an endpoint comparison, not silently identified with the paper.

## Confirmed primary sources

The [official Proximity Prize statement](https://proximityprize.org/), under
“The grand MCA challenge”, gives the following target. For
\(C=\mathrm{RS}[\mathbb F,\mathcal L,k]\), with smooth
\(\mathcal L\subseteq\mathbb F\) and
\[
\rho(C)=k/|\mathcal L|\in\{1/2,1/4,1/8,1/16\},
\]
and a prescribed \(\varepsilon^*\) (the example is \(2^{-128}\)), determine
the largest \(\delta_C^*\in[0,1]\) satisfying
\[
\varepsilon_{\mathrm{mca}}(C,\delta_C^*)\le\varepsilon^*.
\]
The field is assumed sufficiently large for such a radius to exist. The page
still labels the statement preliminary. The threshold depends on the given
code; the page does not supply a radius formula or a numerical field-size
condition. An admissible radius alone would not establish maximality.

The [primary ePrint record](https://eprint.iacr.org/2026/680) identifies Gal
Arnon, Dan Boneh, and Giacomo Fenzi, *Open Problems in List Decoding and
Correlated Agreement*, IACR ePrint 2026/680, received 2026-04-07, last revised
2026-07-06, with three revisions reported. Its July note announces a changed KKH
comparison, changed concrete attack estimates, and an added MCA lower bound.
These are metadata, not an audited theorem statement. The record links to the
[paper](https://eprint.iacr.org/2026/680.pdf) and
[version history](https://eprint.iacr.org/archive/versions/2026/680).

The prize page describes a shared $1 million pool across the challenges and
permits split awards. Mathematical resolution and prize adjudication are
separate. Its companion protocol challenge is not the target of this notebook.

## Exact scope still unverified

The page does not define “smooth” or the MCA error. A complete ABF26 source
freeze still needs the current paper's domain definition, any additional parameter
restrictions, the family of lines or other objects being quantified over,
the sampling distribution, the error event, the order of support/codeword
quantifiers, and all endpoint conventions. In particular, no equivalence
between MCA, correlated agreement, and list size has been assumed.

The pinned ArkLib model supplies explicit support quantifiers, smoothness,
and an adjacent-grid boundary convention. Its definition agrees with the
support event in the primary WHIR Definition 4.8 excerpt recovered on September
25. This does not settle the current ABF26 correspondence. In particular, a
grid boundary cannot automatically replace the largest safe real radius:
the conditional endpoint analysis in L001 and the smooth-code witness C001a
show the distinction at the actual \(2^{-128}\) threshold. These are results
for the separately frozen model. ABF26's current positive and negative bounds
remain unaudited, and no maximal admissible radius for its target is claimed.

## Field-size qualification in the candidate review

The September 25 critical review reread the official page and ePrint metadata.
The primary definition remains unread. Indexed searches for its definition and
an additional Stanford author-publications lead supplied no readable primary
text; the failed direct PDF retrieval was not repeated.

The page's field-size assumption is a distinct unresolved qualification. It
does not specify whether existence means a nonempty safe set, an attained
maximum, or an eventual guarantee with a bound depending on length and rate.
The C001a witness proves the first property for one finite field. It cannot
be assumed to meet either of the latter readings. If existence of the maximum
is itself a hypothesis, a non-attainment example is excluded by that hypothesis.

This is not only a linguistic issue: L002 proves for the frozen length-16
constant-code model that every radius is safe whenever
\(q\ge120\cdot2^{128}\), and constructs a smooth example over
\(\mathbb F_{5^{60}}\). Thus the witness at \(q=5^{56}\) cannot refute
an unrestricted eventual field-size assertion at fixed length. This bound
does not identify the intended meaning of the source, which remains unresolved.
The candidate is therefore incomplete as a challenge-level disproof even if
the two support events are later identified. Its model-only endpoint conclusion
is preserved.

## Access and provenance

The official PDF returned HTTP 403 through the web tool; the version-history
page was unavailable. Local curl could not resolve the ePrint host. The
authors' [Arnon](https://galarnon42.github.io/) and
[Fenzi](https://gfenzi.io/) pages both direct readers to ePrint.

A [third-party reconstruction](https://raw.githubusercontent.com/przchojecki/rs-mca/main/open-proximity.tex)
was located. Its opening comment says it was reconstructed from an uploaded
PDF and is not the authors' original TeX; its displayed date is April 8, 2026.
It therefore cannot certify the July revision's exact statement. It is retained
as a retrieval lead only, and no mathematical premise is imported from it.
The accompanying mirrored PDF was not readable through the web tool either.

On September 25 the PDF and archive were still inaccessible; a search request
also reported a robots exclusion for the PDF. The author-page checks did not
recover another primary copy. Repeating direct PDF retrieval is not a useful
continuation mechanism. The successful new lead was the official companion
project's dependency manifest, which pins a readable upstream ArkLib revision.
The source and theorem names are retained in the separate model freeze.

The companion repository's
[`TargetLower.lean`](https://github.com/proximity-prize/proximity-prize/blob/main/ProximityPrize/Benchmark/TargetLower.lean)
explicitly describes an extractor error containing MCA and a list contribution;
it does not claim equality with pure MCA or with winning-set soundness. Its
protocol certificates therefore cannot certify this notebook's target without
additional theorems. Third-party claimed reductions found during retrieval were
not adopted as mathematical premises.

## Mathlib

Coverage: **not checked** for the full MCA definition or the grand challenge.
No supporting library theorem or formalization is being claimed as a match.
