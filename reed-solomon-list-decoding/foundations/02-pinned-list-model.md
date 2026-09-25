# Pinned interleaved list model

Audit date: 2026-09-25. This is a readable, versioned model for the present
scope-and-threshold audit. It does **not** assert that the unavailable July 6
ABF26 PDF has been recovered or that every convention below matches that PDF.

## Sources and version

The [prize website](https://proximityprize.org/) still states the grand list
threshold as epsilon* times the base-field size. Its linked
[ABF26 record](https://eprint.iacr.org/2026/680) still identifies July 6, 2026 as
the latest revision. PDF and archive access failed again; local HTTP retrieval
also failed at DNS resolution. The authors' pages supplied no readable mirror.

The [proximity-prize repository](https://github.com/proximity-prize/proximity-prize)
hosts the separate IRS reduction benchmark. Its
[manifest](https://raw.githubusercontent.com/proximity-prize/proximity-prize/main/lake-manifest.json)
pins ArkLib commit `e65197892890b8fd9b0dc05b8980273cf1d595cc`. All ArkLib links
below use that immutable commit. This dependency contains grand-challenge
definitions as well as the separate benchmark machinery; the benchmark's
single fixed profile is not substituted for the website's general challenge.

## Code, domain, and interleaving

For a finite field F with q elements, let L be a set of n distinct elements,
with 1 <= k <= n. The code is

\[
 C=\{(f(x))_{x\in L}: f\in F[X],\ \deg f<k\}.
\]

This is
[`ReedSolomon.code`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ReedSolomon.lean#L55).
[`ReedSolomon.Smooth`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ReedSolomon.lean#L737)
requires L = aH for a multiplicative subgroup H of F's units and a nonzero a,
with n a power of two. For all four prize rates together, the pinned
specialization requires n >= 16 and k = n/2, n/4, n/8, or n/16. The bounds
investigated here require only distinct evaluation points, so they also cover
this smooth subclass without a prime-field assumption.

Fix an integer m >= 1. An interleaved codeword P is a function L -> F^m whose
m coordinate functions belong to C. This is
[`Code.interleavedCodeSet`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/InterleavedCode.lean#L127),
used by the notation `C ^⋈ (Fin m)`. Set

\[
 d_{\rm col}(Y,P)=n^{-1}|\{x\in L:Y(x)\ne P(x)\}|,
 \quad B_m(\delta)=\max_{Y:L\to F^m}
 |\{P\in C^{\equiv m}:d_{\rm col}(Y,P)\le\delta\}|.
\]

A position agrees only if all m entries agree. The closed inequality is fixed
by [`Code.mem_closeCodewordsRel_iff`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ListDecodability.lean#L83).
[`Code.Lambda`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ListDecodability.lean#L124)
is this maximized cardinality, not a union of lists from different centers.
Finiteness makes the maximum well defined. The target is B_m(delta) <= epsilon* q,
not epsilon* q^m, with 0 < epsilon* < 1 (the designated example is 2^-128).

## Radius and field quantifiers

The pinned [`grandListDecodingChallenge`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/GrandChallenges.lean#L75)
uses adjacent error grid points t/n and (t+1)/n, or safety through radius one.
`GrandListResolution` records both inequalities. This is a boundary problem;
it is not a definition of an attained largest safe real radius.
The source's `lambda_eq_of_floor_eq` and
[`GrandListResolution.sublevel_iff`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/GrandChallenges.lean#L427)
already describe constant floor cells and the open right endpoint. These facts
are existing inputs, not a new discovery of this notebook.

Keep q, L, k, m, and epsilon* fixed when locating a boundary. The website gives
no explicit q-versus-n growth condition. Any sufficient inequality on q proved
in this model is an additional hypothesis on an instance, not permission to
enlarge the given field. Matching this pinned model to the July ABF text remains
an unresolved source qualification.

## Mathlib

Full challenge and full support-counting bound: **not checked** in Mathlib.
The cited definitions and floor-cell/boundary results are **present** in the
pinned ArkLib source, which is a separate library. They support the model;
they do not establish a sharp list bound for a specified Reed-Solomon code.
No local Lean build or check of ArkLib's entire dependency closure was performed.
