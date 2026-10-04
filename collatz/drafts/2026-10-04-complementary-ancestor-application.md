# Complementary-coordinate least-root application

The completed target is the first COVERED_TARGET in
drafts/literature/2026-10-04-complementary-valuation-three-ancestors.md.
Its prior IMPORT assessment was read before work and is reused unchanged.
The essential theorem and supporting guards were already inspected; this
application needs no new literature search or inverse-word reproof.

The main gap is universal convergence after arrival at residue 20. The
intermediate target is the necessary bound v_3(128n-157)<=16 for the
original least nonconvergent residue-20 root with v_3(4n+1)=3. This
narrows a domain left untouched by L016's ancestor rows and could feed
a later residual-class argument. Convergence or a root-relative descent
mechanism on the complement remains unresolved.

The discriminating test is whether the cited guard v_3(128n-157)>=17
supplies an integral positive residue-20 ancestor m<n with T^b(m)=n
for a finite nonnegative integer b, all compared against the original
root. If any positivity, map, membership or order guard fails, reject
the application. Retain the source threshold rather than lower it
from numerical examples or a slope alone.

L014 supplies the least root; L015 and L016 concern the old coordinate
and do not duplicate this bound. The threshold-17 source family is
inside valuation three for 4n+1. Attempts 009 and 010 stay parked/stopped;
this is neither the paired invariant search nor strict first-return
descent. The two fixed-cylinder applications are separately covered and
are reserved for the next step, outside this turn's mathematical work.

## Applicability argument saved before checks

For n>0 with n=20 modulo 27, write n=20+27k, k>=0. Thus 128n-157
is positive, and its ternary valuation is a finite nonnegative integer.
If the sought bound fails, that valuation is at least 17. The cited
theorem supplies a positive integral m=20 modulo 27, m<n, and T^b(m)=n.
Minimality makes m convergent. If its hit of 1 is at j>=b, then n
hits 1 at j-b; if j<b, then n=T^(b-j)(1) lies in the shortcut cycle
{1,2}. Either case contradicts nonconvergence of the same fixed n.

This is an imported partial restriction, not a complete candidate or a
claim beyond the checked source. The general ancestor conclusion is a
cited input; no new selector proof is needed.

## Completed application and comparison

[L017](../lemmas/L017-complementary-ancestor-least-root-depth-bound.md)
records the precise source statement and the complete applicability
argument. It retains integrality, positivity, target membership,
strict order and the finite shortcut identity. The convergence argument
handles both possible orders of the ancestor's hit of 1 and its specified
hit of n. Its only direct local mathematical input is L014, used for
existence of the fixed least root; the older valuation bounds are
comparisons, not premises for this restriction.

There is a nonempty infinite newly excluded guard within the previous
necessary conditions. Put q=3^17=129140163 and

\[
n=97864031+qs,\qquad s\in\mathbb Z_{\ge0}.
\]

Then n=20 modulo 27 and the exact identities are

\[
\begin{aligned}
128n-157&=q(97+128s),\\
4n+1&=27(14498375+19131876s),\\
n+7&=81(1208198+1594323s).
\end{aligned}
\]

The last two parenthesized factors are nonzero modulo 3 for every s.
Hence v_3(4n+1)=3 and v_3(n+7)=4, while the first identity gives
v_3(128n-157)>=17. Also t=2(14498375+19131876s)=1 modulo 9,
so these positive integers satisfy the older L014–L016 conditions.
They are excluded as least nonconvergent roots by the newly applied
source theorem. No member is asserted to be nonconvergent, and this
does not independently prove convergence of every member.

The achieved bound falls short of the main required conclusion:
termination of every remaining root. For instance, the prior family
n=47+243k, k>=0, still satisfies v_3(4n+1)=3, v_3(n+7)=3 and t=5.
Now

\[
128n-157=27(217+1152k)
\]

has valuation exactly 3, so all these positive candidate integers also
satisfy the new bound. The combined necessary conditions therefore
still admit an infinite class. No return transition theorem, eventual
descent estimate or complete candidate follows.

## Checks and continuation decision

Exact integer arithmetic confirmed 768*2^17=100663296<129140163=3^17,
with slope 33554432/43046721. At valuation 16 the same slope estimate
is 16777216/14348907>1; this does not exclude other certificates or
authorize lowering the source threshold. The computation obtained the
guard representative by 157*128^(-1) modulo 3^17, checked all displayed
family coefficients and unit residues, and evaluated three members
with new-coordinate valuations 17, 19 and 17. These checks protect
arithmetic transcription; the universal ancestor conclusion uses the
previously assessed proof by citation, not finite replay.

The target is complete with outcome ADVANCE and classification
KNOWN_IMPORTED: a relevant local necessary restriction, not a new
mathematical discovery beyond the checked literature. It spends no
mathematical EXPLORATION turn and resets no historical counter. Attempts
009 and 010 are unchanged. No source search, formal build, mathematical
script addition or unrelated notebook edit was needed.

The two fixed complementary cylinders are a distinct remaining part
of the same prior assessment. Their exact citation application is
already a COVERED_TARGET, so it supplies a ready mathematical next
step without another literature turn. No cylinder proof is applied
in this turn.
