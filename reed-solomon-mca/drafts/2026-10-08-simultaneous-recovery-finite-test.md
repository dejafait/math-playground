# Bounded simultaneous recovery test — completed exploration

The unchanged approved target is the uniform eleven bound for L043
(4)–(7). The main gap is arbitrary sixteen-error equality. L044 reduces
possible violations to rational normalized weights; its separate audit
is still outstanding. This step uses the already assessed recovery
equations, not new source coverage.

The discriminating test fixed h=1, d=96, {y_1,y_2}={8,89} and
{z_1,z_2}={12,85}. It enumerated all 120 three-subsets W of the other ten
labels for A_2={h} union W. For each labeling it classified all 1820
four-supports and counted distinct eligible mu for every gated rational
(p,q,r), retaining shared labels and dropping fourth-weight gates exactly
as in L044. This exhausts a specified finite family, not all labelings.
The paired opposite labels provide a different test from L016's stopped
fixed instance. No symmetry on arbitrary labels is assumed.

A maximum at least twelve would have triggered exact witness verification
to refute the intermediate threshold via L044's nonrational-rho construction.
A smaller maximum supplies only bounded exploration evidence, not a
uniform bound or a new lemma. Universal extraction, other patterns,
the global interval and ABF26 remain independent gaps.

## Exact computation and scope

Reproduce with `python3 scripts/simultaneous-recovery/finite_count.py`.
The complete certificate is
`scripts/simultaneous-recovery/finite-count-result.json`; it stores every
support classification, every case's weight-count histogram, and one
independently checked maximizer per case. Arithmetic is exact modulo 97.
No numerical tolerances, random sampling or external packages are used.

For each labeling the script computes c_x from L043's Q. For each
nonexcluded K it solves the four equations

    -mu F_K Y + sum_(x in {h,d} minus K) beta_x F_K v_x = -F_K Z.

L043's already proved quotient classification justifies this direct
RREF implementation: inconsistent systems are rejected; the only both-zero
system is the separately excluded K_*; mu=0 and mu=-1 are rejected.
Every remaining system has a unique mu and beta. The equations imposed
on the weights are precisely q=mu*p+beta_h/c_h when h is absent and
r=(1-beta_d/c_d)/(1+mu) when d is absent. Shared labels contained in K
impose no such equation. This uses the imported recurrence already
cited and specialized in L043, without reproving it or changing hypotheses.

For every r in F_97 minus {0,1} and p in F_97^*, the script groups rows
by their required q; a row imposing no q condition contributes to every
q. It takes the union of their mu sets for each q with q*(1-p-q)!=0.
Thus several supports with the same mu contribute once. Each labeling
checks exactly 95*(96+95*95)=866495 gated weight triples. The E=0
deletion is deliberately not applied: the object counted is M in L044,
with all of M realized by an allowed nonrational rho. No rationality of
the original chart, finite parameters or lambda is imposed.

Independent verification at the first maximizer of each labeling uses
neither the recurrence rows nor their recovered beta. For all 95 eligible
mu and all 1816 nonexcluded supports, it recovers omega directly from
the first four moments of L043's N_K and checks moments five through
eight. The resulting complete mu set must equal the counted set. All
120 comparisons pass. This is an independent check at one maximizing
weight triple per labeling, not at every maximizer or every weight triple.
The exhaustive weight histograms rely on the RREF and grouping code.

## Results and inspected evidence

The calculation classified 218400 supports across 120 labelings and
checked 103979400 gated weight cases. Its maximum is **3**, compared
with **12** needed for a counterexample and **11** sought uniformly.
The maxima by labeling are 1 in 48 cases, 2 in 32 cases, and 3 in 40
cases. The independent stage checks 20702400 support/mu memberships.
There are no reported failures. Certificate checks also confirm that
each case lists all 1820 distinct supports and that all 120 independently
recovered candidate sets agree. The complete `/summary` value was
inspected, not merely a preview.

For a concrete maximum, case index 6 has W={18,22,75}, (p,q,r)=(10,30,7)
and M={12,83,84}. The complete `/cases/6/count` and
`/cases/6/verification` values were inspected. Its full admitted records are:

| mu | K | omega in the displayed K order |
| --- | --- | --- |
| 12 | {22,47,50,75} | (61,46,72,23) |
| 83 | {18,27,70,96} | (62,13,75,65) |
| 84 | {1,18,47,50} | (30,51,62,38) |

All eight moments agree and all four weights are nonzero in each row.
This example exercises absence of both shared labels, inclusion of d,
and inclusion of h. Actual error weights still carry L043's nonzero
factor lambda/(gE); omega is not silently identified with those weights.
The universal K_* and original three supports are excluded throughout.

## Decision and limitations

Outcome: EXPLORATION. No counterexample was found, and no all-labeling
inequality was proved. The large count of weight cases must not be
mistaken for coverage of arbitrary labels. In particular neither a
symmetry reduction to these first two supports nor a uniform upper
bound follows. No lemma, DAG change, PROOF.md change, or claim of
mathematical novelty is warranted. Mathlib coverage was not checked.

L016's stopped fixed triple is not retested; the saved negative evidence
and positive-only sampling stops remain intact. This is one new bounded
test of simultaneous weight constraints under the existing EXPLORE
assessment. Repeating this same family would give no new evidence.
Continue the unchanged target by seeking a uniform argument on the
recovery equations; the finite rows can test such an argument, including
shared-label cases. L010, L041, audited L042–L043 and unaudited L044
remain the relevant inputs. The eleven count, L044 audit, arbitrary
triple extraction and challenge-level source identification remain open.
