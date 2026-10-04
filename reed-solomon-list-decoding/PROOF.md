# Reed–Solomon grand list-decoding challenge: argument overview

No complete candidate resolution has been developed. The [source audit](foundations/01-target-and-source-audit.md) records the website target and current primary claims. The [pinned list model](foundations/02-pinned-list-model.md) fixes readable ArkLib definitions at an immutable commit; comparison with the unavailable July ABF26 PDF remains incomplete.

## Argument assembled

For closed column-Hamming balls, L001 counts the common k-subsets on which an entire polynomial tuple agrees with the center. Distinct tuples cannot share one, giving the field-independent bound

\[
 B_m(t/n)\le\left\lfloor\binom nk/\binom{n-t}k\right\rfloor\quad(0\le t\le n-k).
\]

L011 reproduces the known monic root-product construction on the prescribed domain: the center (x^k,0,...,0) has one candidate (X^k-product_{a in S}(X-a),0,...,0) for every k-subset S of L, with exactly S as its simultaneous agreement columns. Thus B_m((n-k)/n)=binomial(n,k) for every m>=1. At t=n-k+1, L001's scalar-multiple witness gives q^m nearby tuples. When epsilon* q>=1, the largest safe grid index is n-k if and only if q >= epsilon*^{-1} binomial(n,k), including threshold equality. This holds for all finite fields and the pinned smooth-domain subclass; the endpoint field condition is now necessary as well as sufficient.

L012 reproduces the next coefficient-fiber construction: the entire list at (x^(k+1)-b x^k,0,...,0) with k+1 agreements equals the (k+1)-subset sum fiber. On L=aH with H contained in F_Q, rescaling preserves counts and averaging gives B_m((n-k-1)/n)>=ceil(binomial(n,k+1)/Q), retaining ambient q in the threshold. Li-Wan's exact formula gives lists 673,257,33,8 on F_17^* inside F_{17^32}, with threshold between 1 and 8. C012a applies Zhu-Wan's estimate to the proper order-1024 subgroup of F_65537 inside F_{65537^28}: all four zero-sum lists exceed 2^322, whereas 2^320<epsilon* q<2^321. Both instances give t_star<=n-k-2 for every m.

L013 fixes two elementary symmetric coefficients at A=k+2: each entire list at (x^(k+2)-b x^(k+1)+c x^k,0,...,0) equals that joint subset fiber. Averaging over Q^2 pairs on the proper subgroup supplies ceil(binomial(1024,k+2)/65537^2), exceeding the ambient threshold at rates 1/2,1/4,1/8 and giving t_star<=509,765,893 for every m. At rate 1/16 that lower certificate is inconclusive. L014 applies the known monomial character estimate and weighted sieve to bound every assessed A=66 two-coefficient list by floor([binomial(1024,66)+(65537^2-1)binomial(579,66)]/65537^2)<2^317<epsilon* q, for every m. This stops that family as an unsafe witness at error index 958, without proving safety over arbitrary centers; the established t_star bound remains 958. These reproduce known constructions and counting tools; exact maximizing fibers and the smaller-radius boundary remain unresolved.

The largest grid radius under L011's endpoint condition is 1-k/n; the supremum of safe real radii is 1-k/n+1/n and is unsafe. More generally, whenever epsilon* q>=1, the safe set is [0,(t_star+1)/n) for a unique, possibly unknown, t_star<=n-k. The adjacent-grid convention is already explicit in ArkLib; no attained real maximum is inferred.

L002 checks a conditional geometric improvement. If every scalar candidate list with at least A>=k agreements has a cover over the algebraic closure of dimension at most s and total cumulative degree at most Delta, then

\[
 B_m((n-A)/n)\le\left\lfloor\Delta\sum_{a=0}^s n^a\right\rfloor^m.
\]

Agreement equations isolate each coefficient vector over that closure. Following proper hyperplane sections for at most s cuts and applying projective Bezout controls all candidate paths. Fixed s and polynomial Delta give a polynomial sufficient field-size condition at the covered radius. A suitable cover must still be supplied for each candidate list; support uniqueness alone does not construct it.

L003 checks the local degree input to a possible cover. For a differential polynomial of order s, total derivative-variable degree B, and parameter/X degrees at most D, let H be its highest-variable partial derivative at a fixed Taylor anchor. When H!=0 and the characteristic is zero or exceeds the message degree d, the coefficient at excess order t has a representation N_t/H^(2t-1) with degree(N_t)<=(D+B)(2t-1). Writing L=max(0,2(d-s)-1), every residual equation clears with H^(B L) to degree at most (D+B)(1+B L). These linear degree bounds strengthen the quadratic estimate in the reviewed local source passage.

L004 turns that input into a bound on each nonsingular chart closure. Put A=D+B, E=A(1+B L), and T=A L+1. The total graph has dimension at most s+1 and cumulative degree at most A(E T)^(s+1). Closing a chart separately at a fixed parameter gives dimension at most s and cumulative degree at most B(E T)^s. Proper hypersurface intersections bound the base; a general section of the graph pulls back to degree-at-most-T equations in the initial variables. Components supported on H=0 are excluded before closure. Every resulting graph closure lies in the differential solution set, but these charts need not cover every singular solution.

L005 supplies the fixed scalar cover when the characteristic is zero or p>max(d,B). Starting with nonzero Q(X,Y_0,...,Y_r), 0<=r<=d, repeated highest-variable partial differentiation gives a chain of length at most B ending in a nonzero polynomial in X. Each solution of Q is nonsingular for some earlier equation in that chain. A common set of N=D+(B-1)d+1 anchors detects every such solution. There are at most BN chart closures, of dimension at most r, with summed degree at most

\[
 \Delta_*=B^2N(E_*T_*)^r,\quad
 L_*=\max(0,2d-1),\quad E_*=(D+B)(1+B L_*),\quad T_*=(D+B)L_*+1.
\]

For fixed r,B and D,d=O(n), this is O(n^(4r+1)). Anchors may lie outside the finite field. Derivative charts may contain extra solutions, as L002 permits.

L006 now supplies the interpolant over any field. At fixed gamma>0 and sufficiently large n, degree padding to K=ceil((1-gamma/2)A), where A=k+ceil(gamma n), allows a constant number of derivative variables and enough interpolation coefficients. A backward Hasse–Taylor substitution exhibits a large kernel in each local constraint map. With order r fixed only by gamma and multiplicity mu=r^3, the global rank is strictly below the coefficient-space dimension. The resulting nonzero Q contains every candidate and has total Y-degree at most the explicit constant B_gamma and X-degree below mu n. The proof checks this fixed-shape construction directly; it does not require the source's optimized order estimate or a differential root-enumeration theorem.

C006a combines this input with the scalar cover and agreement count. Put d=k-1, D=mu n, B=B_gamma, and use the displayed cover constants. Under p>max(k-1,B_gamma),

\[
 B_m(1-k/n-\gamma)\le\beta^m,\qquad
 \beta=\Delta_*\sum_{a=0}^r n^a\le C_\gamma n^{5r+1}.
\]

The closed ball is exactly the grid ball at (n-k-ceil(gamma n))/n. If d<r, the ambient coefficient space already has dimension k<=r and degree one, so no invalid application of L005 is needed. The sufficient field condition q>=epsilon*^(-1) beta^m is polynomial in n for fixed gamma,m, with explicit, potentially very large constants. It certifies this radius for instances satisfying that condition.

In small characteristic, L007 controls the agreement-filtered Frobenius obstruction inside one fixed derivative fiber. With h=floor((k-1)/p), that affine family becomes a degree-at-most-h RS code on the distinct points x_i^p. A direct count of simultaneous column agreements gives

\[
 M\le\left\lfloor\frac{n(A-h)}{A^2-nh}\right\rfloor\quad\text{if }A^2>nh,
\]

with no exponent m. At A=k, this bounds the family by 3, 15, 26, or 255 at rates 1/2, 1/4, 1/8, or 1/16, respectively, for prime characteristics p>=3,5,11,17. The other admissible primes have limiting sufficient slack sqrt(R/p)-R, with a linear bound at equality and a constant bound above it. Characteristic two is incompatible with the pinned even-order multiplicative domains. This controls one family; no bounded number of such families covering a general interpolant's candidates is established.

L008 extends the family description to aP'+bP=c, with a nonzero. A minimal monic homogeneous solution g generates the kernel over F[X^p], and rad(g) divides a. After deleting its e evaluation zeros, of which z match the center, the exact reduced parameters are N=n-e, h=floor((k-1-deg g)/p), and A_0=A-z. The list bound is floor(N(A_0-h)/(A_0^2-Nh)) when the denominator is positive; it counts interleaved rows with the same homogeneous operator directly.

For any such first-order equation, a sufficient slack is Gamma_p(R)=(1-R)(1-sqrt(1-1/p))/2. At gamma>=Gamma_p(R), integer rounding gives M<=pn, and strictly larger slack gives a constant independent of n,q,m. At the common slack Gamma_3(R), every odd characteristic has M<=3n, giving the sufficient field condition q>=3 epsilon*^(-1)n for this family. An attained fixed-zero example also gives the full-code lower bound B_m((n-k)/n)>=n-k+1, so safety at that grid radius requires epsilon* q>=n-k+1. Fixed zero columns can therefore destroy L007's zero-slack constant; this does not identify the general boundary.

L009 tests the Riccati extension aP'+bP^2+cP+d=0 with ab nonzero in odd characteristic. Given two polynomial solutions and a nonzero homogeneous reciprocal kernel with minimal generator g, every further solution is encoded by a monic divisor T of W=(P_1-P_0)^2g. Its constant-field parameter is recovered by M=T'/((P_1-P_0)g)' and N=T-(P_1-P_0)gM, with explicit coprimality and degree tests. The unfiltered count is at most the divisor number of W, hence at most 2^(2(k-1)+(p-1)deg a); if the homogeneous kernel is zero there are at most two solutions.

This finite count cannot generally be replaced by a polynomial in n, even for fixed odd p. With Q=p^s, the equation (X^Q-X)P'+P^2+P=0 has at least p^(floor(s/2) ceil(s/2)) polynomial solutions of degree less than Q, obtained from vanishing polynomials of F_p-subspaces of F_Q. Their degrees fit the pinned rate and domain parameters over suitable extensions. No common received word with k agreements is supplied. The example blocks an unfiltered polynomial count, while leaving agreement filtering and geometric overcovers open.

L010 gives a filtered Riccati bound. A root of a pairwise difference away from zeros of a has multiplicity at least p. If e evaluation points are zeros of a, put V=n+(p-1)e and W_A=pA-(p-1)max(0,A-(n-e)). Weighted incidence counting gives M<=floor(V(W_A-k+1)/(pA^2-V(k-1))) when A^2>(k-1)(e+(n-e)/p), directly for simultaneous interleaved agreement. For e<=rho n, slack at least max(0,sqrt(R(rho+(1-rho)/p))-R) gives M<=pn, with a constant bound at strictly larger slack. Thus q>=epsilon*^(-1)pn suffices for this family's contribution. The e=n case is only the ordinary Johnson bound.

This filters an infinite part of L009's obstruction: take p=3, odd s>=3, k the least power of two at least 3^s, and a multiplicative domain of size n=2k. Exactly two domain points are roots of X^(3^s)-X. Every center then has at most four solution tuples at k agreements, despite the superpolynomial number of unfiltered scalar solutions. This is a bound within that equation, not for the full RS list.

## Unresolved gap

The target requires a sharp threshold for the given code, field, and interleaving width. L011 identifies the endpoint exactly: when 1<=epsilon* q<binomial(n,k), t_star<n-k. L012 and C012a exclude one further grid index at all four rates on the stated 16-point and proper 1024-point domains; L013 excludes another at rates 1/2,1/4,1/8 on the proper subgroup. L014 settles the rate-1/16 two-coefficient family below threshold at A=66, but the maximum over arbitrary centers at that grid radius and every sharper boundary remain unknown. At fixed prize rate the necessary and sufficient endpoint field condition grows exponentially in n. It cannot replace the source's weaker existence proviso or locate the general smaller-field boundary.

The formal q^{O(1)} bound in TR26-164 does not close that gap. The fixed-slack, field-independent conclusion separately claimed in TR26-169 now has a local scalar derivation through C006a, including the interpolation input. Its polynomial sufficient field condition is still stronger than the source's existence proviso. Its explicit constants have not been shown useful for any designated finite-field instance, and fixed positive slack does not determine the sharp boundary. Interpolation is characteristic-free, but the cover still requires p>max(k-1,B_gamma); a general small-characteristic extension remains uncovered. L007–L008 give counts for single families; L009's nonlinear classification gives an exponential bound and a superpolynomial obstruction before agreement filtering. L010 controls a Riccati family when its coefficient-zero count permits the weighted cutoff, but that count is uncontrolled for general interpolants. None supplies a controlled cover of a general nonlinear or higher-order interpolant. The parametric exceptional-set theorem is unnecessary for this list bound and remains outside this review. The exact relation between the pinned boundary formulation and ABF26 also remains qualified.

## Partial results

L001 supplies the unconditional support bound; L011 attains its endpoint, making the exponential field-size condition exact there. L012 supplies exact common-center coefficient-fiber lists at A=k+1 and a subfield/coset averaging bound. Its full-field application and C012a's proper-subgroup estimate give unsafe-grid certificates at the cryptographic threshold; L013 advances three proper-subgroup rate bounds by one further grid point. L014 supplies a uniform rate-1/16 upper bound for the assessed two-coefficient centers and stops that witness family at A=66. These are prescribed-domain and metric reproductions of known scalar mathematics, not novelty claims. C006a supplies a complete informal fixed-slack certificate under explicit large-characteristic and polynomial field-size conditions, using the local interpolation, scalar-cover, and agreement arguments. No novelty is claimed for this qualitative preprint result. L007–L008 show that growing geometric dimension alone need not prevent small agreement-filtered lists in Frobenius and first-order linear families, subject to their explicit thresholds. Their fixed-zero example remains a linear lower bound within one differential family, superseded for the full-code endpoint by L011. L009 supplies an exact Riccati pole-cancellation test and rules out polynomial unfiltered counts in fixed small characteristic. L010 supplies a conditional weighted nonlinear list bound and a four-candidate bound for an infinite smooth-domain subfamily of that raw obstruction. The earlier [quantitative transfer audit](drafts/2026-09-24-source-and-threshold-audit.md) continues to rule out inferring the threshold solely from q^{O(1)}. These partial results do not resolve the general challenge.

## Known traps checked

- The threshold scales with |F|, not |F|^m; simultaneous column agreement is distinct from separate row agreement.
- A polynomial in q need not be smaller than epsilon* q. L011's binomial endpoint condition is additional and exact: its failure gives an unsafe list at the explicit common center. This does not determine the smaller-radius boundary.
- A grid maximum, real supremum, and attained real maximum differ for closed balls. The pinned source uses a boundary; its distinction is not presented as a disproof of the unavailable ABF text.
- A fixed-slack certificate does not determine a sharp finite-code boundary; the source's informal n-bound cannot replace its formal q-bound without justification.
- The count uses simultaneous agreement and applies only through n-k errors. The next point has an explicit q^m list; zero is included and m must be positive.
- L001 works in arbitrary characteristic. Prime-field preprints, random-domain results, and folded codes are not silently substituted for all specified smooth codes.
- L011 cancels the leading term and checks distinct words at one common center. L012 and L013 retain coefficient signs and strict degree less than k; their entire lists remain fixed by root subsets even for ambient-extension messages. L013's Q^2-class partition assumes neither independence nor uniformity. L014 deletes zero from the monomial image, retains the A! divisor, and checks nontriviality for every sieve cycle since characteristic exceeds A; its family bound does not control arbitrary centers. The threshold retains ambient q. Full-field and subfield-domain formulas are not applied to a proper subgroup. Remaining zero rows preserve simultaneous agreement without an exponent m. A missed lower certificate establishes no safety; equality does not prove unsafety.
- L002 requires a cover with controlled cumulative degree as well as dimension. L005 supplies the cover for a given equation; L006 supplies that equation uniformly at fixed positive slack. Neither gives the sharp finite-code boundary.
- L003–L004 retain H!=0 and the base coefficient equation. Denominator clearing is equivalent only on that open set; naive closed graph equations can add spurious components. Closing after parameter specialization can differ from taking a fiber of the total closure. Small characteristic can destroy the triangular recursion, and bounded degree for one chart is not a global cover.
- L005 uses partial derivatives of the equation, not X-differentiation of a solution identity. Its charts may overcover the original solution set, and its anchors need not lie in the base field. The characteristic hypotheses remain essential to this proof; no small-characteristic or sharp-boundary conclusion follows.
- L006 uses Hasse identities without factorial division, strict degree/multiplicity inequalities, and padding with constants fixed before n. The auxiliary multiplicity mu differs from interleaving width m. In C006a the cover uses the actual message degree k-1; when r>k-1 the ambient-space case replaces it. A larger extension field does not repair a deficient characteristic.
- The Frobenius reduction lowers the message degree and applies only within a fixed affine family. Uncontrolled summation over fibers can restore a power of q. A nonpositive second-moment denominator is a limitation of that inequality, not an unsafe-list witness; rounding makes the limiting slack equality usable.
- First-order families require a minimal generator and deletion of its evaluation zeros before division. Only matching fixed columns count toward A. The direct interleaved bound assumes the same a,b in every row; the uniform slack is sufficient, not a sharp threshold for general interpolants.
- Riccati parameters must pass polynomial divisibility, coprimality, and degree tests; checking only evaluation points misses poles. Their finite unfiltered count need not be polynomial in n. The subspace example supplies many solutions, not many candidates around one received word, and does not reject agreement filtering or all geometric overcovers.
- L010 charges multiplicity p only away from zeros of a; its inverse-weight incidence count retains the exceptional-column cost. The four-candidate example bounds solutions of one equation, not the entire code list. A general interpolant need not be Riccati-shaped or have a controlled number of evaluation zeros of a.
- The ArkLib model is versioned, but the ABF definition comparison is incomplete. No complete candidate or verified result is claimed.
