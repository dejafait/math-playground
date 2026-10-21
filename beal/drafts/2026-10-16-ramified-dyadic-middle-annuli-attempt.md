# Ramified dyadic middle-annulus attempt

Approved target: the unchanged full local Kummer-image certificate in
`literature/2026-10-16-ramified-dyadic-two-descent-image.md` (SPECIALIZE).
Main gap is primitive integer emptiness. The intermediate target is
exhaustive coverage of original nonintegral x, especially -22<=v_H(x)<0,
with exact realizations and fixed L078 labels compared against L079.
Potential downstream use is global S-unit filtering; independence from
L077 and L074's localized class contribution remain unresolved.

Reuse L078's arithmetic and L079/L080's completed evidence; no duplicate
enumeration or reopening of ATTEMPTS/034–036. No new literature is needed
for this coordinate specialization of the already assessed Hensel and
square-neighborhood method. No claim beyond those sources is intended.

Use t=-x/y and u=1/x=t^2 v. The exact implicit equation is

    F_t(v)=v-1+t^2 v+(10t^4-t^3)v^2+20t^6 v^3=0.

For t in pi O_H its reduction is v-1 and its derivative is a unit.
The unique integral Hensel root gives x=1/(t^2 v), y=-1/(t^3 v).
The fixed Kummer evaluation, after multiplication by (tv/2)^2, is

    q(t)=v-(theta/4)t^2 v^2.

For k=v_H(t)>=1 it has J-valuation m=min(0,6k-22), always even.
For t,t' in one depth-N disk, N=15, 1<=k<N, put

    beta=min(N+11+k,2N), d=min(beta,N+2k).

Implicit-root differences have H-valuation at least d; squares of the
two unit roots differ to valuation at least d+11. Thus q differences
have J-valuation at least min(3d,3beta-22). After subtracting m this
exceeds 66 for every k=1,...,14. In the zero disk k>=15, q-1 has
valuation at least 68. These are analytical bounds, not sampling.

Bounded test: enumerate all 16384 t disks, compute each implicit root
in O_H/64 (H-error 66), normalize exactly before reduction modulo eight
in J, and save complete normal forms, collisions and L079 matches.
Replay every record, polynomial residual and class reconstruction.
Continue on complete arithmetic/coverage success; otherwise preserve
the precise failure and do not substitute cardinality for disk evidence.
No additional rank, global class value or integer conclusion is assumed.

## Completed attempt

Canonical [L081](../lemmas/L081-ramified-dyadic-nonintegral-parameter-disks.md)
proves the exact parameter coverage, realization, normalization and
constancy estimates. All 16384 disks are realized, including 16376
over the missing middle annuli. Odd negative x-valuations are empty.
All 2048 labels match the existing L079 list. Construction passes
13/13 checks; full-record replay passes 12/12; both have no failures.
Full bound tables, coverage and check objects were inspected, and all
stored root residuals and class identities were replayed. This is an
exhaustive implicit-parameter partition, not a literal cubic-X disk
tree. Historical L079/L080 evidence is preserved and was not rerun.

The local pointwise coverage gap is closed within the stated arithmetic
inputs. Independent audits of L078–L081 and all global contributions
remain unresolved. The next target is critical review, with its new
assessment explicitly REVIEW_REQUIRED for a separate source-approval
turn. This completed RESEARCH / REPRODUCTION step is ADVANCE, not a
new global restriction or a claim of progress beyond the checked methods.
It spends zero mathematical EXPLORATION attempts and resets no budget.
