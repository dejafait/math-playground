# Fixed complementary-cylinder least-root application

The completed target is the second COVERED_TARGET in
drafts/literature/2026-10-04-complementary-valuation-three-ancestors.md.
The prior IMPORT assessment is reused unchanged. Its two inspected
all-parameter certificates are mathematical inputs by citation; no
selector reconstruction or new literature search is needed.

The main gap is universal convergence on the infinite least-root domain
surviving L014–L017. The intermediate target excludes the cylinders
n=4529+19683s and n=17813+59049s, s>=0, as the original least
nonconvergent residue-20 root. A successful application could support a
later residual-class cover, but supplies no termination theorem there.

The discriminating test is whether each cited ancestor is an integer
m>0 with m=20 modulo 27, m<n, and an actual finite shortcut hit of n,
with every comparison made against the original root. Reject the
application if any map, parameter, positivity, residue or order guard
fails. Finite replay checks transcription only; it cannot replace the
inspected source's all-parameter proof.

## Applicability argument saved before checks

The cited note, Sodelin, *Complementary ancestor cylinders and a second
ternary-depth coordinate*, node B-SECOND-TERNARY-ANCESTOR-001,
[section “Two elementary infinite families missed by the original selector”](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Complementary_Ancestor_Cylinders.md#two-elementary-infinite-families-missed-by-the-original-selector),
gives, for every integer s>=0,

| Original root n | Ancestor m | Shortcut time b | n-m |
|---|---|---:|---|
| 4529+19683s | 3179+13824s | 9 | 1350+5859s |
| 17813+59049s | 16679+55296s | 11 | 1134+3753s |

The source includes T^b(m)=n with intermediate inverse guards. Positivity
and integrality follow from the positive integer coefficients and
s>=0. Both n and m have residue 20 modulo 27: the pairs are respectively
27(167+729s)+20, 27(117+512s)+20, and
27(659+2187s)+20, 27(617+2048s)+20. Each displayed difference is
strictly positive for every allowed s.

If n were the least nonconvergent residue-20 root supplied by L014,
minimality would make its m convergent. Choose j>=0 with T^j(m)=1.
For j>=b, the cited hit of n gives T^(j-b)(n)=1. For j<b,
n=T^(b-j)(1) belongs to the shortcut cycle {1,2}. Both cases contradict
nonconvergence of n. This applies the cited theorem to the fixed root,
without comparing an ancestor of a larger later return with that return.

The fixed cylinders are not already excluded by L014–L017. For the
first and second n, respectively,

\[
\begin{aligned}
n+7&=81(56+243s),&n+7&=81(220+729s),\\
4n+1&=27(671+2916s),&4n+1&=27(2639+8748s),\\
128n-157&=2187(265+1152s),&128n-157&=81(28147+93312s).
\end{aligned}
\]

All six parenthesized factors are nonzero modulo 3. Thus both have
v_3(n+7)=4 and v_3(4n+1)=3, while their complementary valuations
are 7 and 4, below L017's exclusion threshold 17. All L016 lower
exclusion thresholds are at least 4 in the old valuation, so neither
cylinder violates its conditions at valuation 3. This comparison is
an applicability and nonredundancy check, not an input to the
least-root contradiction.

Attempts 009 and 010 stay parked/stopped; this application uses neither
a paired invariant nor strict descent at the first return. The source
certificates are known imported results, not new discoveries.

## Completed result and limits

[L018](../lemmas/L018-fixed-complementary-cylinder-exclusions.md) records
the two precise cited inputs and the full least-root applicability
argument. Its direct local mathematical input is L014 for the least
root. L015–L017 are nonredundancy comparisons, not premises of the
contradiction.

The exact coefficient and unit checks passed. Replay at s=0,1,2 in
each cylinder reached its stated root at shortcut time 9 or 11, for
six transcription checks in total. No mathematical script was added
or changed; these finite checks do not supply the universal identities.

The achieved conclusion excludes two additional infinite families as
least roots, below the previously imported depth threshold. The
required conclusion remains convergence or eventual descent on every
remaining root. In particular, the already recorded family
n=47+243k, k>=0, still satisfies all older restrictions and avoids
the two new cylinders: their residues modulo 243 are 155 and 74,
whereas its residue is 47. This is an infinite admissible arithmetic
class, not a counterexample family.

The target is complete with outcome ADVANCE and classification
KNOWN_IMPORTED. No mathematical EXPLORATION turn was spent and no
historical counter was reset. No complete candidate or global rank
was produced. A bounded-cover test on the surviving class would test
coverage rather than merely import more isolated exclusions. That
stronger target has no ready assessment; its pending REVIEW_REQUIRED
record approves no new calculation in this turn.
