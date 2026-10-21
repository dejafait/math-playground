# Lemma 385: empty response cells force conditional common-zero density

## Hypotheses

Use the fixed actual pair of L366, with real frequency t:

\[
 F_0(t)=2\xi_c(1/2+it),\qquad
 G(t)=-(t^2+1/4)\operatorname{Re}
             \frac{\xi_c(5/2+it)}{5/2+it}.
\]

For ordinary real derivatives define

\[
 \mathscr L(U)=U'^2-UU'',\qquad
 B(U,V)=2U'V'-UV''-U''V,\qquad
 D=B(F_0,G)^2-4\mathscr L(F_0)\mathscr L(G).
\]

Assume, additionally, that there is a finite H_D such that D(t)≤0
for every real t≥H_D. This eventual physical discriminant premise is
**unproved for the actual pair**. Use L368's unconditional eventual
strict \(\mathscr L(G)>0\), L372's consecutive simple response zeros
g_j, and L384's complete half-open cells with no full-strip nontrivial
zeta-zero ordinate. No common-zero upper bound, F_0 simplicity,
noncoincidence, common ODE or RH is assumed.

## Conclusion

Every complete empty cell (g_j,g_{j+1}] lying on the ray where all
these hypotheses hold has a common zero at its excluded left endpoint:

\[
                  F_0(g_j)=G(g_j)=0.                 \tag{1}
\]

Consequently there exist fixed c>0 and finite T_* such that every
real T≥T_* satisfies

\[
 N_{\rm common}([T,2T])\ge cT\log T,                \tag{2}
\]

where N_common counts distinct real common zeros, including both
endpoints. One may take exactly L384's existential empty-cell constant
c; T_* may also depend on the assumed H_D. No numerical onset is
asserted. This conditional density input is retained by the separate critical
audit below. It is not an unconditional common-zero theorem, actual-theta
sign extension, RH consequence or complete candidate resolution.

## Proof

The prior EXPLORE assessment is
`drafts/literature/2026-10-10-empty-cell-common-zero-charging.md`.
It covers precisely this endpoint/dependence and injective-count test.
We reuse the audited local Wronskian assertion of L378, rather than
reprove its pencil/Taylor argument or invoke L374's disjoint-ray
conclusion on a finite interval. L378 states that an independent,
nonzero real-analytic pair under these physical inequalities has
W=F_0G'−F_0'G nonzero at every noncommon point of the ray; its proof
and audit explicitly include counting endpoints, with the inequalities
available to their right. Its aggregate count bound alone is not a
count of empty cells and is not used here.

The empty-cell input is L384's audited variable-phase specialization
of T. Trudgian, *On the success and failure of Gram's Law and the
Rosser Rule*, Acta Arith. 148(3) (2011), DOI
[10.4064/aa148-3-2](https://doi.org/10.4064/aa148-3-2),
Theorems 5.1–5.3, pp. 242–244. The variable grid and right-continuous
endpoint count are justified in L384, not asserted as a verbatim
theorem of that paper. We import no stronger occupancy statement or
ordinary-grid sign transfer. L378's source comparisons require a
common regular ODE or global polynomial-pencil hypotheses absent here;
they are not imported. Only the cellwise consequence missing from the
ready local inputs is derived below. Classification POTENTIALLY_NEW
reflects this bounded assessment, not established historical novelty.

**Analytic domain and zero interpretation.** L366's exact formulas
make F_0 and G real analytic on the connected real line: xi_c is
entire, and the denominator 5/2+it has no real zero. F_0 is real
on that line by the critical-line completion identity in L366.
For real t>0, a zero of F_0 is a zero of xi_c at 1/2+it and hence
a nontrivial zeta zero. At these points the defining completion factor
\(s(s-1)\pi^{-s/2}\Gamma(s/2)/2\) is finite and nonzero.
Thus absence of every full-strip zero ordinate on (a,b] implies

\[
                F_0(t)\ne0\quad(a<t\le b).         \tag{3}
\]

There is no assumption on F_0(a) or its multiplicity. For the use
of L378, G is not identically zero since L372 supplies simple zeros
on its eventual ray. F_0 is not identically zero since L384 supplies
empty cells, and (3) gives a nonzero value at their right endpoints.
These facts are unconditional; the assumed D sign is not used to
establish them.

**Single-cell endpoint implication.** Set a=g_j and b=g_{j+1} for
a complete empty cell on the common eventual ray. Then a<b,
G(a)=G(b)=0, both zeros are simple, and G has no zero in (a,b),
by L372. Equation (3) includes F_0(b)≠0.

First handle dependence. If F_0 and G are dependent over the real
constants on their connected analytic domain, their nonzero assumptions
give F_0=dG with a nonzero real constant d. This would give F_0(b)=0,
contrary to (3). Therefore any such empty cell rules out this case;
no independent-case Wronskian claim is applied to a dependent pair.

For an independent pair suppose, for contradiction, that F_0(a)≠0.
Then neither endpoint is common. By (3), no interior point is common
either. L378 therefore makes W nowhere zero on the entire closed
interval [a,b]. Its continuity gives a fixed nonzero sign there.
This uses the inequalities on the whole eventual ray, including to
the right of b, as required by L378's local endpoint argument.

Since G has one constant nonzero sign on (a,b) and its two endpoint
zeros are simple, its Taylor expansions from the interior sides give

\[
             \operatorname{sgn}G'(a)=-\operatorname{sgn}G'(b).
\]

At the endpoints W(a)=F_0(a)G'(a) and
W(b)=F_0(b)G'(b). These have the same nonzero sign, so F_0(a) and
F_0(b) have opposite signs. The intermediate value theorem places
an F_0 zero strictly inside (a,b), contradicting (3). Hence F_0(a)=0,
which together with G(a)=0 proves (1). This argument permits every
finite F_0 multiplicity at a and makes no assertion that W retains
its sign across a common zero.

**Injective dyadic count and quantifiers.** Let H_G be an eventual
onset for L368's strict sign and L372's consecutive simple-zero grid,
and let T_0,c_0 be the fixed onset and positive constant in L384.
Take a single

\[
                 T_*\ge\max(1,H_D,H_G,T_0).
\]

For every real T≥T_*, L384 supplies at least c_0T log T complete
empty cells (g_j,g_{j+1}] with T≤g_j<g_{j+1}≤2T.
Apply (1) to each and assign its left endpoint g_j. Different cells
have different indices j and therefore different left endpoints,
since the grid is strictly increasing. This map is injective without
counting multiplicities or making a separation assumption between
different cells. Every charge lies in [T,2T]. A cell starting at T
charges the included endpoint T; a cell ending at 2T charges its
left endpoint, still inside [T,2T]. No point in an incomplete boundary
cell is needed. A point that is also a neighboring right endpoint
does not duplicate a charge, since each cell is charged only at its
own left endpoint.

All counted common points have positive finite F_0 multiplicity,
but each is counted exactly once. Analyticity and nonzero functions
make their number finite on [T,2T], including its endpoints.
Thus (2) follows with c=c_0. Its quantifier is one constant and one
onset valid for every sufficiently large T, not a selected sequence.
Only the onset is enlarged for the additional assumed D premise. ∎

**Qualifications and remaining gaps.** L371/L373's common-zero resets
are allowed, and no fixed W sign across common zeros is used. L375/L376's
generic disjointness obstructions, L379/L383's stopped diagnostics and
the stopped two-cell large-gap import remain intact. An independently
proved common-zero upper count below (2) could exclude eventual D≤0;
that upper count is not established here. Both D≤0 itself and every
global actual-theta mixed-positivity, total L367 margin, common-free
Wronskian localization, low-index, above-forty and endpoint arithmetic
gap remain unresolved. The proof is exact and needs no numerical or
mathematical script. The separate critical audit below retains the claim.

### Separate critical audit, 2026-10-10

The prior EXPLORE assessment is
`drafts/literature/2026-10-10-empty-cell-common-zero-density-audit.md`.
This audit retains (1)–(2) with exactly their existing hypotheses,
constant and direct inputs. No new theorem, repaired mathematical error
or stronger conclusion is claimed. POTENTIALLY_NEW records only the
prior bounded comparison, not verified historical originality.

**Domain and input applicability.** L366 (1) identifies the exact fixed
pair and ordinary real-frequency convention used here. Restricting the
entire completion to either vertical line is real analytic in t; taking
the real part preserves real analyticity, and 5/2+it never vanishes
on the real line. Thus one connected open analytic domain is R.
The critical-line completion is real by L366. At s=1/2+it, t>0,
none of s, s-1, the exponential pi factor or Gamma(s/2) vanishes
or has a pole. Consequently an F_0 zero gives an actual nontrivial
zeta-zero ordinate in the full-strip count. L384's empty cell gives
F_0 nonzero on (a,b], not merely away from its right endpoint.
There is at least one such cell for all sufficiently large T because
c T log T>0. Its right endpoint proves F_0 is not identically zero
without using the conditional D premise. L372 supplies simple G zeros,
and L368's strict L(G)>0 also excludes identically zero G. All of
L378's domain and nonzero-function hypotheses are therefore met.

**Dependence and the local test.** Dependence over real constants on R
would give F_0=dG, d nonzero, and hence F_0(b)=0. This contradicts
emptiness. A relation on an open subinterval would extend to R by
real analytic identity, so no local dependent exception is concealed.
For the resulting independent pair, L378's already audited assertion
applies at every noncommon point of the eventual ray. Under the
contradictory assumption F_0(a) nonzero, emptiness rules out common
points throughout [a,b], including both endpoints. Its Wronskian is
therefore nowhere zero on that entire compact interval. The physical
inequalities hold to the right of b as well; an upper counting endpoint
is not an upper endpoint of their domain. No common ODE or division
by a vanishing function is used.

Let sigma be the sign of G on (a,b). Consecutiveness excludes interior
G zeros. Simplicity and one-sided Taylor expansions give sign G'(a)
= sigma and sign G'(b) = -sigma. Continuity and nonvanishing of W
make sign W(a) = sign W(b). Since W equals F_0 G' at both endpoints,
sign F_0(a) = -sign F_0(b). Both values are nonzero in this case,
so IVT gives a zero strictly in (a,b), contradicting the full-strip
emptiness. This checks the excluded-left/included-right distinction
and proves the charge. If a is common, the contradiction argument is
not applied across it: every positive finite multiplicity of F_0 at a
is allowed, and W is allowed to vanish or change sign there. No F_0
simplicity assumption has entered.

**Counting and uniformity.** L384 supplies complete cells with
T<=a<b<=2T for every real T above one fixed onset; its c is independent
of T. Strictly increasing consecutive zero levels make their left
endpoints distinct. Thus the assignment is an injection into distinct
common zeros in [T,2T], and no multiplicity factor or endpoint loss is
required. For a=T the charge is included; for b=2T it is still a<2T.
An adjacent cell's right endpoint cannot create a second charge, since
only left endpoints are assigned. Incomplete boundary cells are unused.
Nonzero analyticity on R makes every compact zero set finite, even
when an endpoint is a zero, so this is ordinary finite counting.

L368 and L372 concern the same fixed actual G and provide fixed eventual
onsets; L384 provides another fixed onset and a fixed positive c.
The additional hypothesis supplies fixed H_D. Their maximum, increased
to be at least one, is a single T_* for which all preceding arguments
hold for every real T>=T_*. At a=T_* the right-neighborhood version
of L378 is valid, and at b=2T the assumptions continue beyond b.
There is no dependence of c on H_D and no subtraction that would
shrink c. This validates precisely (2), not only a subsequence result.

The conditional density survives all covered cases without repair.
It still supplies neither eventual D<=0 nor an unconditional smaller
common-zero upper count. L371/L373's resets and the recorded diagnostic
stops are compatible with this proof. Mathlib coverage remains as below.

## Mathlib

Full matching conditional actual-response common-zero density theorem:
**not checked**. No Mathlib theorem is imported. Supporting analytic
identity/zero finiteness, connected-sign and intermediate value results
have not been checked in Mathlib; unknown coverage is not evidence of
absence.
