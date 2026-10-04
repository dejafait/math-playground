# Refined residue-20 ancestor application

The saved Next action is an IMPORT application covered explicitly by
drafts/literature/2026-10-03-residue20-residual-ancestor-selector.md.
That assessment was read before this calculation and is reused unchanged;
there is no essential unread source for this target and no new search.

The gap remains universal convergence after arrival at residue 20.
The proposed intermediate target is the conditional restriction
v_3(4n+1)<=12 for a least nonconvergent residue-20 root n. Its downstream
use is to remove the cited high-valuation family before addressing the
complementary roots. The discriminating test is whether the source gives
an actual forward identity from a positive residue-20 integer strictly
smaller than the original n. A mismatched map, missing integer guard,
or comparison only with a later return would invalidate the application.

The inspected statement is Sodelin's node
B-RESIDUE20-VALUATION13-ANCESTOR-2026-09-05, sections 1–3 and 5 of
[Residue20_Refined_Ancestor.md](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Residue20_Refined_Ancestor.md).
It uses the positive shortcut map of foundations/01-target-and-scope.md.
For r>0, r=20 modulo 27 and v_3(4r+1)>=13, it supplies positive m=20
modulo 27, m<r, and a finite identity T^b(m)=r. Import the theorem and
its integer guards by citation; do not rederive the selector. The saved
assessment records its full prose proof and essential retained-branch
reference as read on 2026-10-04. No independent Lean build is claimed.

If any positive start is nonconvergent, L014 gives a nonempty bad
residue-20 set and its least element n. Suppose v_3(4n+1)>=13. All source
hypotheses hold with r=n, so it gives m<n in the same starting class.
Minimality makes m convergent. Let T^j(m)=1 and T^b(m)=n. If j>=b,
then T^(j-b)(n)=1. If j<b, then n=T^(b-j)(1) belongs to {1,2}, whose
elements both converge. Thus n converges in either case, a contradiction.
This proves the bound and passes the original-root test.

The bound is not implied by L014's valuation condition alone. For
example, n_*=(3^14-1)/4 is a positive integer with n_*=20 modulo 27,
v_3(n_*+7)=3 and v_3(4n_*+1)=14: the identities are
4n_*+1=3^14 and 4(n_*+7)=27(3^11+1). This checks the independence of
the arithmetic predicates, without asserting that n_* is nonconvergent.
No finite orbit search or larger replay is needed.

L015 records the citation and complete applicability argument. This is
a local ADVANCE classified KNOWN_IMPORTED, not a discovery beyond the
checked literature. The achieved bound removes valuations at least 13;
the actual required conclusion is convergence or eventual descent for
every remaining root. No such conclusion, return rank, or complete
candidate is supplied. Attempts 009 and 010 remain unchanged.

The next direction is the exact lower-row target already preapproved
in the same assessment. It continues the guarded restriction mechanism
without extending its scope or reopening the stopped first-return route.
This successful application spends no mathematical EXPLORATION turn
and resets no counter.
