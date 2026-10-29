# C101b — Literal d35 last-pair actual-word exclusion

## Hypotheses

Let T(n)=n/2 for even positive integers and T(n)=(3n+1)/2 for
odd positive integers. Letters O and E prescribe actual input parities
for this shortcut map. Use all 25 indexed pairs (J_i,H_i), in the
literal order of L055's table, changing only H_0=40 to 5 and
H_24=32670621 to 32670656. No other assertion of L055 is assumed.
Fix B=9250245 and an integer 0<=t<=B, and set

\[
a_i=2\ (0\le i\le22),\qquad
a_{23}=2+18t,\qquad a_{24}=2+18(B-t).
\]

Put W_i=(OOEO)^{J_i}O^{H_i}E^{a_i}, D_i=4J_i+H_i+a_i,
and N=sum_{i=0}^{24}D_i. Suppose W_0...W_24 is actual at a
positive odd integer n_0>1 and T^N(n_0)=n_0. Define its chronological
junctions by n_i=T^{sum_{j<i}D_j}(n_0), for 0<=i<=25.
Require each n_i for 0<=i<25 to be positive odd and congruent to
20 modulo 27, and every final even tail to be exact. Thus n_25=n_0.
Repeated periods and coincident junctions are allowed. No primitive
period, minimum, seed, ordering of heights or first-return hypothesis
is imposed. All logarithms below are natural.

## Conclusion

No actual closed concatenation satisfying these hypotheses exists,
for any integer 0<=t<=9250245.

This is a restricted actual-word exclusion, not an exclusion of all
cycles or divergent trajectories and not a complete Collatz candidate.
It is a RESEARCH/REPRODUCTION specialization under the prior SPECIALIZE
assessment `drafts/literature/2026-10-24-d35-literal-last-pair-actual-word-transfer.md`.
It adds a local application of existing results, without claiming
mathematical novelty beyond the sources checked. The separate step466
critical audit below found no defect within these hypotheses.

## Proof

Suppose such a concatenation exists. Keep its literal cut, indexed
pairs, parameter t and individual tails fixed. The full table gives
J_i>=2 and H_i>=3 after the two stated changes: the least J is 8,
the changed H_0 is 5, and all other H entries are at least 72.
Every a_i is an integer at least 2 and congruent to 2 modulo 18.
Thus this very representation meets L041's actual-word hypotheses
with r=25. We use only its occurrencewise necessity calculations,
not its length estimate, cycle estimates, cyclic minimum choice or seed.

Set kappa=23/11 and s_i=n_i+kappa for 0<=i<=25. A positive odd
integer congruent to 20 modulo 27 is at least 47: the nonnegative
residue representatives begin 20,47,74, and 20 is even. Hence at
each input

\[
s_i\ge47+23/11=540/11>0,\qquad s_{25}=s_0.
\tag{1}
\]

For each i=0,...,24, let y_i=T^{4J_i}(n_i) and
z_i=T^{4J_i+H_i}(n_i). L041's section "Each occurrence's own
prefix and the transfer to the next" supplies, at that same outgoing
input and with its own J_i,H_i,a_i,

\[
y_i+1=(27/16)^{J_i}s_i-12/11,
\qquad
z_i=(27/16)^{J_i}(3/2)^{H_i}s_i
          -(12/11)(3/2)^{H_i}-1,
\qquad n_{i+1}=z_i/2^{a_i}.
\tag{2}
\]

Adding kappa to the last identity gives exactly

\[
s_{i+1}=2^{-a_i}\left((27/16)^{J_i}(3/2)^{H_i}s_i
                    -(12/11)(3/2)^{H_i}-1\right)+\kappa.
\tag{3}
\]

Both subtractions are inside the tail division; the shift kappa is
outside. Equation (3) holds for every outgoing occurrence, including
i=24 with endpoint s_25=s_0. It uses the two changing tails
individually, rather than merely their total.

The same L041 passage gives

\[
4J_i\log2\le\log s_i+\log(11/4),\qquad
2^{H_i}\le y_i+1<(27/16)^{J_i}s_i.
\tag{4}
\]

These are finite actual-word necessities for arbitrary exact a_i>=2
and odd output, with H_i>=3; they do not require a_i=2. In particular
the first inequality is non-strict. All quantities in the second are
positive, so strict monotonicity of log gives

\[
H_i\log2<\log s_i+J_i\log(27/16).
\tag{5}
\]

The strictness comes from y_i+1<(27/16)^{J_i}s_i, not from
assuming a strict first inequality in the second part of (4).
Both guards concern s_i, the input of row i, rather than its output
or a rotated coordinate.

Equations (1), (3), (4)'s first inequality and (5), with this literal
table and integer t, match every hypothesis of C101a on the single
tuple (s_0,...,s_25). Its audited conclusion says that no such real
tuple exists on the entire integer interval 0<=t<=B, a contradiction.
No feasibility or converse realization inference is used.

At t=B the last two tails are (166504412,2). The last occurrence
still has odd output n_25=n_0, so the same L041 necessities and
closing equation apply. At t=0 the tails are (2,166504412).
Neither boundary is dropped. Repeated periods and coincident junctions
cause no loss: all 25 outgoing occurrences retain their indices, and
L041 and C101a impose no distinctness or primitive-period condition.
This proves the stated exclusion.

### Sources, overlap and qualifications

L041 supplies only the finite occurrencewise identities, lower domain
and necessary guards used above; L055 supplies only its table; C101a
supplies the audited real-system exclusion. The specialization checks
their hypotheses rather than reproving their general inputs. The
upstream affine reference is Halbeisen–Hungerbuehler, *Optimal bounds
for the length of rational Collatz cycles*, Acta Arithmetica 78 (1997),
227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Its finite-word affine use is imported through the existing proofs;
no parity-coding converse is used. C101a's analytic qualifications and
the completed L100/L101 audits remain unchanged; no certificate or
external formal verification is rerun here.

The prior assessment checked duplicates and the relevant recorded
failures. Earlier different-table transfers are comparisons, not inputs.
Attempt032's failed fixed sufficient package and the two d0 rational
witnesses supply no premise and remain preserved. Early-support/order
exhaustion, universal entry into this language, other tables,
unrestricted cycles, divergence and universal eventual descent remain
unresolved. This proof establishes no additional reduction to the
literal language in the hypotheses.

### Independent critical audit — 2026-10-25, step466

This RESEARCH/REPRODUCTION audit uses the pre-invocation SPECIALIZE
assessment `drafts/literature/2026-10-24-c101b-actual-word-transfer-critical-audit.md`.
It checks the actual-word implication above. C101a and its completed
step462 audit are imported; L100/L101 certificates are not reaudited.
The ready source comparison and the precise affine citation above are
reused. No new coding theorem or realization converse is needed.

**Literal parameters and chronological cut.** Inspection of all 25
L055 pairs gives minimum J equal to 8. Replacing just the stated two
H entries leaves minimum H equal to 5; all other entries are at least
72. These are precisely C101a's pairs, not the original d0 table.
The integer interval makes both changing tails at least 2, and each
tail is 2 modulo 18. Thus r=25,J_i>=2,H_i>=3 meet the scope of
L041's finite occurrence calculations. L055 supplies no witness,
minimum, seed or additional count premise.

Write q_i=sum_{j<i}D_j. Since all D_j are positive, the intervals
[q_i,q_{i+1}) are the 25 successive word occurrences in [0,N).
Actualness of the full word restricts to W_i at n_i=T^(q_i)(n_0).
The states y_i,z_i in (2) are therefore precisely its prefix endpoints,
and q_i+D_i=q_{i+1} identifies its outgoing endpoint with n_{i+1}.
For i=24 the output is n_25=T^N(n_0)=n_0, which is positive odd.
State coincidences and repeated periods do not identify these time
intervals or remove any outgoing guard. L041's separate seed proof
does choose a minimum cut, but the occurrence passage and its audited
valuation argument use no such ordering. They apply at this original
cut; no rotation is made here.

**Domain and exact endpoints.** If n_i=20+27k is positive with k an
integer, then k>=0; oddness forces k odd, hence k>=1 and n_i>=47.
It follows that s_i=n_i+23/11>=540/11 at every input, with s_25=s_0.
All logarithms required by C101a are defined. L041's finite identities
give y_i+1=(27/16)^{J_i}s_i-12/11 and
z_i=(3/2)^{H_i}(y_i+1)-1. Substituting the former into the latter,
then using the actual E^{a_i} segment, yields (3) exactly. The
coefficient, both negative terms inside 2^{-a_i}, and the external
23/11 agree with C101a (1). This applies to all 25 rows, including
the closing equation, on the same tuple and individual tail list.

**Guard signs checked at arbitrary tails.** The inspected L041 proof,
supported by L031's arbitrary-tail necessity calculation, uses
2^{H_i}(2^{a_i}n_{i+1}+1)=3^{H_i}(y_i+1).
Since a_i>=2, the parenthesis on the left is odd. Thus
v_2(y_i+1)=H_i and y_i+1=2^{H_i}u_i with u_i positive odd.
For H_i>=3, the identity
11y_i+23=4(11*2^{H_i-2}u_i+3) has an odd parenthesis.
In 16^{J_i}(11y_i+23)=27^{J_i}(11n_i+23), taking dyadic
valuations therefore gives v_2(11n_i+23)=4J_i+2.
The positive integer 11n_i+23=11s_i is consequently at least
2^{4J_i+2}. Dividing by 4 and taking logarithms gives exactly
4J_i log2<=log s_i+log(11/4), with a non-strict sign.
Also u_i>=1 gives 2^{H_i}<=y_i+1, while the positive 12/11
subtraction gives y_i+1<(27/16)^{J_i}s_i. Taking logarithms of
this mixed chain gives the strict H guard at s_i. Neither guard
uses the next input's height, a seed, or an E^2-only transport law.
These calculations verify the imported local proof cases, rather than
reprove the general finite-word theorem.

**Endpoints and verdict.** Since 18B=166504410, the tails at t=0
are (a_23,a_24)=(2,166504412), and at t=B they are
(166504412,2). At the latter boundary, 2^2*n_25+1 is still odd;
the valuation argument, strict H comparison and row24 closing
equation are unchanged. The same checks apply at every intermediate
integer t. No interval endpoint or coordinate is omitted. Consequently
this single tuple satisfies every hypothesis of C101a, whose audited
exclusion is a contradiction. The actual-word transfer is valid as
stated; no correction or strengthening was obtained.

The direct inputs remain L041 (occurrencewise necessities), L055
(table only) and C101a (audited exclusion). L031 was checked only as
support for the imported L041 passage; it adds no new direct input.
Attempt032 and both d0 witnesses supply no premise. This audit secures
the existing restricted application, not entry into this language,
support/order exhaustion, an unrestricted cycle exclusion or descent.
No mathematical argument or DAG edge changed, so PROOF.md and DAG.md
are unchanged; this audit and the current checkpoint supersede the
overview's pending-audit wording. Source and Mathlib qualifications
remain as stated above and below.

## Mathlib

Full matching coverage for this actual-word specialization is unchecked.
Supporting affine, valuation and logarithm results would not alone
constitute a matching theorem. Unknown coverage is not absence; no
Lean verification or external Lean build is claimed.
