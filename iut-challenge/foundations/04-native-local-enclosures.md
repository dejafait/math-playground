# Native local enclosures — citation input

Use the April 2020 IUT IV formulation, printed pp. 9–14, retained in the [completed source assessment](../drafts/literature/2026-10-03-hull-transport-screening.md). The [author-hosted source](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf#page=10) and the [87-page reproduction read in that assessment](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf#page=10) are version-qualified there; byte identity was not checked.

## Hypotheses and named result

IUT IV, **Proposition 1.2(ii), “Differents and Logarithms”**, uses a finite family k_i/Q_p, their tensor order R, its normalization O_L, and J = tensor_i log(O_(k_i)^times). The Q_p-linear automorphism phi must preserve J. Let e_i be ramification indices, d_i different valuations, a_i = 2 for p = 2 and a_i = ceil(e_i/(p-2))/e_i for p > 2, and b_i = floor(log_p(p e_i/(p-1))) - 1/e_i. Write D,A_0,B_0 for their respective sums. For lambda in (1/e_i) Z, the cited inclusion is

phi(p^lambda O_L) subset p^floor(lambda-D-A_0) J subset p^(floor(lambda-D-A_0)-B_0) O_L.

Fractional powers denote the source's suitable elements/ideals with the prescribed component valuations, not arbitrary linear maps. **Proposition 1.4(iii), “Nonarchimedean Normalized Log-volume Estimates”**, imports these inclusions and bounds their normalized log-volumes. Its additional subset I* must contain every i with e_i > p-2. These statements are imported by citation; no reproof is supplied.

## Fixed-packet applicability and limit

For K = Q_2(sqrt(2)) in both factors, e_i = 2, d_i = 3/2, a_i = 2, b_i = 3/2 and lambda = 1/2 is allowed. Preserving the tensor log-shell I is equivalent to preserving J = 16 I. The native inclusion therefore applies to every g in the local test group G, on the input a O_L with a = 1 tensor sqrt(2). Take both indices in I* for Proposition 1.4(iii). This supplies a covered local enclosure without the auxiliary saturated rounding step.

The input is a O_L, not the potentially larger a beta^(-1) I. Thus a failure of a bound on the latter is no counterexample to the cited proposition. This import does not identify the original pilot, Ind3 envelope, complete image family, or the normalized A and B.

## Mathlib

The full native enclosure and its supporting local-field/library coverage are **not checked** in Mathlib. The named propositions and direct source links are precise primary citations, not claims of a matching formal theorem.
