# Fixed outer-tail calculation plan and saved reasoning — step96

Approved target: Test the fixed increment-one Chernoff upper allowance for L938's negative-row tail beyond E=8 against the exact remaining margin m-B from L949.

Coverage: assessment94, SPECIALIZE, saved before invocation; completed work is REPRODUCTION. Main gap: actual-Xi all-degree mixed positivity. The intermediate target pays only the outer component of the fixed B_4 budget. Keep tilt1/10, increment1, split8, all34 rows, twelve factors, factorials and M_0^12. No parameter campaign follows this test.

Plan saved before computation: use precision200, theta terms1 through8 and4096 equal direct interval boxes on u in[0,4]. Include the weighted integrands u^(2k)exp(11u²/10)K(u)/(2k)! for all0<=k<=6. Import direct-box inclusion from Johansson (2018), Sections2,2.1,3.2 as inspected in assessment94; use L037's existing interval operations. Do not reuse L035's unheated tail.

For omitted theta terms n=9+j, n^4<=9^4*2^j and n²>=81+19j. Dropping the negative summand, using exp(2u)>=1 and u<=4, bounds their kernel sum by 8pi² exp(18)9^4 exp(-81pi)/(1-2exp(-19pi)). Multiply by4*4^(2k)exp(88/5)/(2k)! to pay its whole finite-interval contribution.

For the infinite u-tail use L058 with L=11/10,R=0,p=2k. The cutoff4 exceeds max(1,3*(33/5)/(2pi)). Its proof bounds the integrand by C(2k)!exp(-(pi/2)exp(2u)), with explicit C from L058. After factorial cancellation, convexity exp(2u)>=exp(8)*(1+2(u-4)) gives integrated tail <=C exp(-(pi/2)exp(8))/(pi exp(8)). This is a specialization of the assessed explicit majorant, not an assumed numerical onset.

Normalize each positive exp(E/10)h_alpha(E)dE measure; the cited Boyd–Vandenberghe Section7.4.2(7.20) with increment1 gives row tail <=exp(-8)product_k A_k(11/10)^alpha_k after its mass is restored. Since max(-v,0)<=sum_(c<0)|c|h_alpha, sum exactly these negative rows. No multinomial factor or removal of A_0 powers. Save all interval contributions and complete allowance. Compare with exact m-B, checking m and B identities.

Continuation test: full upper allowance<exact m-B passes. An upper allowance>=m-B stops only this fixed method; invalid moments are inconclusive. No lower bound on actual negative mass follows. Head/global variation, signs in other parameters/degrees, contacts, initialization and realization remain open.

State before execution: no moment or tail result yet. Original compact theta/polynomial/derivative-prefix/arithmetic contracts remain inherited. New integration keeps documented Decimal and Python exact-arithmetic contracts. Mathlib coverage unchecked.
