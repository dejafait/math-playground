# Reed–Solomon grand list-decoding challenge: argument overview

No complete candidate resolution has been developed. The [source audit](foundations/01-target-and-source-audit.md) records the website target and current primary claims. The [pinned list model](foundations/02-pinned-list-model.md) fixes readable ArkLib definitions at an immutable commit; comparison with the unavailable July ABF26 PDF remains incomplete.

## Argument assembled

For closed column-Hamming balls, L001 counts the common k-subsets on which an entire polynomial tuple agrees with the center. Distinct tuples cannot share one, giving the field-independent bound

\[
 B_m(t/n)\le\left\lfloor\binom nk/\binom{n-t}k\right\rfloor
 \quad(0\le t\le n-k).
\]

At t=n-k+1, scalar multiples in each row of a polynomial vanishing on k-1 evaluation points give q^m distinct nearby tuples. Thus, when q >= epsilon*^{-1} binomial(n,k), the largest safe grid index is exactly n-k. This holds for all finite fields and interleaving widths m>=1, including the pinned smooth-domain subclass.

The largest grid radius is then 1-k/n; the supremum of safe real radii is 1-k/n+1/n and is unsafe. More generally, whenever epsilon* q>=1, the safe set is [0,(t_star+1)/n) for a unique, possibly unknown, t_star<=n-k. The adjacent-grid convention is already explicit in ArkLib; no attained real maximum is inferred.

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

## Unresolved gap

The target requires a sharp threshold for the given code, field, and interleaving width. L001 does not determine t_star when the field satisfies only the existence condition epsilon* q>=1 but lacks its additional sufficient binomial bound. At fixed prize rate the latter field condition grows exponentially in n. It cannot replace the source's weaker proviso.

The formal q^{O(1)} bound in TR26-164 does not close that gap. The fixed-slack, field-independent conclusion separately claimed in TR26-169 now has a local scalar derivation through C006a, including the interpolation input. Its polynomial sufficient field condition is still stronger than the source's existence proviso. Its explicit constants have not been shown useful for any designated finite-field instance, and fixed positive slack does not determine the sharp boundary. Interpolation is characteristic-free, but the cover still requires p>max(k-1,B_gamma); a general small-characteristic extension remains uncovered. L007–L008 give counts for single families, not a controlled cover of a general nonlinear or higher-order interpolant. The parametric exceptional-set theorem is unnecessary for this list bound and remains outside this review. The exact relation between the pinned boundary formulation and ABF26 also remains qualified.

## Partial results

L001 supplies an unconditional support bound and an exact boundary under an additional exponential field-size condition. C006a supplies a complete informal fixed-slack certificate under explicit large-characteristic and polynomial field-size conditions, using the local interpolation, scalar-cover, and agreement arguments. No novelty is claimed for this qualitative preprint result. L007–L008 show that growing geometric dimension alone need not prevent small agreement-filtered lists in Frobenius and first-order linear families, subject to their explicit thresholds. The fixed-zero example adds a linear full-code lower bound at k agreements. The earlier [quantitative transfer audit](drafts/2026-09-24-source-and-threshold-audit.md) continues to rule out inferring the threshold solely from q^{O(1)}. These partial results do not resolve the general challenge.

## Known traps checked

- The threshold scales with |F|, not |F|^m; simultaneous column agreement is distinct from separate row agreement.
- A polynomial in q need not be smaller than epsilon* q. The binomial field condition is additional, and failure of that sufficient condition is not itself an unsafe-list witness.
- A grid maximum, real supremum, and attained real maximum differ for closed balls. The pinned source uses a boundary; its distinction is not presented as a disproof of the unavailable ABF text.
- A fixed-slack certificate does not determine a sharp finite-code boundary; the source's informal n-bound cannot replace its formal q-bound without justification.
- The count uses simultaneous agreement and applies only through n-k errors. The next point has an explicit q^m list; zero is included and m must be positive.
- L001 works in arbitrary characteristic. Prime-field preprints, random-domain results, and folded codes are not silently substituted for all specified smooth codes.
- L002 requires a cover with controlled cumulative degree as well as dimension. L005 supplies the cover for a given equation; L006 supplies that equation uniformly at fixed positive slack. Neither gives the sharp finite-code boundary.
- L003–L004 retain H!=0 and the base coefficient equation. Denominator clearing is equivalent only on that open set; naive closed graph equations can add spurious components. Closing after parameter specialization can differ from taking a fiber of the total closure. Small characteristic can destroy the triangular recursion, and bounded degree for one chart is not a global cover.
- L005 uses partial derivatives of the equation, not X-differentiation of a solution identity. Its charts may overcover the original solution set, and its anchors need not lie in the base field. The characteristic hypotheses remain essential to this proof; no small-characteristic or sharp-boundary conclusion follows.
- L006 uses Hasse identities without factorial division, strict degree/multiplicity inequalities, and padding with constants fixed before n. The auxiliary multiplicity mu differs from interleaving width m. In C006a the cover uses the actual message degree k-1; when r>k-1 the ambient-space case replaces it. A larger extension field does not repair a deficient characteristic.
- The Frobenius reduction lowers the message degree and applies only within a fixed affine family. Uncontrolled summation over fibers can restore a power of q. A nonpositive second-moment denominator is a limitation of that inequality, not an unsafe-list witness; rounding makes the limiting slack equality usable.
- First-order families require a minimal generator and deletion of its evaluation zeros before division. Only matching fixed columns count toward A. The direct interleaved bound assumes the same a,b in every row; the uniform slack is sufficient, not a sharp threshold for general interpolants.
- The ArkLib model is versioned, but the ABF definition comparison is incomplete. No complete candidate or verified result is claimed.
